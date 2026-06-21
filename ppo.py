import os
import sys
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import gymnasium as gym
import matplotlib.pyplot as plt
from collections import deque
from torch.distributions import Categorical

from seeding import set_global_seed, DEFAULT_SEED


class _Tee:
    """Mirror writes to multiple streams (e.g. stdout + a log file)."""
    def __init__(self, *streams):
        self.streams = streams

    def write(self, text):
        for s in self.streams:
            s.write(text)

    def flush(self):
        for s in self.streams:
            s.flush()


def init_layer(layer, gain=np.sqrt(2), bias=0.0):
    nn.init.orthogonal_(layer.weight, gain)
    nn.init.constant_(layer.bias, bias)
    return layer


class ActorNetwork(nn.Module):
    def __init__(self, state_dim=8, action_dim=4, hidden_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            init_layer(nn.Linear(state_dim, hidden_dim)),
            nn.Tanh(),
            init_layer(nn.Linear(hidden_dim, hidden_dim)),
            nn.Tanh(),
            init_layer(nn.Linear(hidden_dim, action_dim), gain=0.01),
        )

    def forward(self, x):
        return self.net(x)


class BaselineNetwork(nn.Module):
    def __init__(self, state_dim=8, hidden_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            init_layer(nn.Linear(state_dim, hidden_dim)),
            nn.Tanh(),
            init_layer(nn.Linear(hidden_dim, hidden_dim)),
            nn.Tanh(),
            init_layer(nn.Linear(hidden_dim, 1), gain=1.0),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


class RunningStateNormalizer:
    def __init__(self, shape, clip=5.0, eps=1e-8):
        self.mean  = np.zeros(shape, dtype=np.float64)
        self.var   = np.ones(shape,  dtype=np.float64)
        self.count = eps
        self.clip  = clip

    def update(self, x):
        x = np.asarray(x, dtype=np.float64)
        self.count += 1.0
        delta       = x - self.mean
        self.mean  += delta / self.count
        self.var   += delta * (x - self.mean)   # Welford M2

    def normalize(self, x):
        std = np.sqrt(self.var / self.count)
        return np.clip(
            (np.asarray(x, dtype=np.float64) - self.mean) / (std + 1e-8),
            -self.clip, self.clip,
        ).astype(np.float32)


def collect_rollout(env, actor, baseline, state_normalizer,
                    n_steps, gamma, gae_lambda):
    """
    Collect exactly n_steps transitions from a single env, resetting at episode
    boundaries.  Returns flat arrays suitable for minibatch PPO training, plus
    a list of completed-episode total rewards for logging.
    """
    obs_buf  = np.zeros((n_steps, 8), dtype=np.float32)
    act_buf  = np.zeros(n_steps,      dtype=np.int64)
    lp_buf   = np.zeros(n_steps,      dtype=np.float32)   # log π_old(a|s)
    rew_buf  = np.zeros(n_steps,      dtype=np.float32)
    val_buf  = np.zeros(n_steps,      dtype=np.float32)
    done_buf = np.zeros(n_steps,      dtype=np.float32)

    ep_rewards = []
    cur_ep_rew = 0.0
    state, _   = env.reset()

    for t in range(n_steps):
        state_normalizer.update(state)
        norm_s = state_normalizer.normalize(state)
        s_t    = torch.FloatTensor(norm_s)

        with torch.no_grad():
            val   = baseline(s_t).item()
            dist  = Categorical(logits=actor(s_t))
            act   = dist.sample()
            lp    = dist.log_prob(act).item()

        obs_buf[t] = norm_s
        act_buf[t] = act.item()
        lp_buf[t]  = lp
        val_buf[t] = val

        next_state, reward, terminated, truncated, _ = env.step(act.item())
        done = terminated or truncated
        rew_buf[t]  = reward
        done_buf[t] = float(done)
        cur_ep_rew += reward

        if done:
            ep_rewards.append(cur_ep_rew)
            cur_ep_rew = 0.0
            state, _ = env.reset()
        else:
            state = next_state

    # Bootstrap value for a rollout that ends mid-episode
    if done_buf[-1] == 0.0:
        state_normalizer.update(state)
        last_t = torch.FloatTensor(state_normalizer.normalize(state))
        with torch.no_grad():
            last_val = baseline(last_t).item()
    else:
        last_val = 0.0

    # GAE with episode-boundary masking: (1 - done) zeros out V(s') and
    # the carry-over term at every episode end, so advantages never bleed
    # across episode boundaries.
    adv_buf = np.zeros(n_steps, dtype=np.float32)
    gae = 0.0
    for t in reversed(range(n_steps)):
        next_val = val_buf[t + 1] if t < n_steps - 1 else last_val
        mask  = 1.0 - done_buf[t]
        delta = rew_buf[t] + gamma * next_val * mask - val_buf[t]
        gae   = delta + gamma * gae_lambda * mask * gae
        adv_buf[t] = gae

    ret_buf = adv_buf + val_buf
    return obs_buf, act_buf, lp_buf, adv_buf, ret_buf, val_buf, ep_rewards


def ppo_update(obs, actions, old_log_probs, advantages, returns, old_values,
               actor, baseline, optimizer,
               clip_eps=0.2, n_epochs=4, batch_size=64,
               entropy_coef=0.01, value_coef=0.5, max_grad_norm=0.5):
    """
    K epochs of minibatch PPO updates on a fixed collected rollout.

    Policy loss: clipped surrogate -min(r·A, clip(r,1-ε,1+ε)·A)
    Value loss:  clipped to prevent value function from jumping too far from
                 the rollout estimates, mirroring the policy clip constraint.
    """
    n = len(obs)
    obs_t     = torch.FloatTensor(obs)
    acts_t    = torch.LongTensor(actions)
    old_lp_t  = torch.FloatTensor(old_log_probs)
    adv_t     = torch.FloatTensor(advantages)
    ret_t     = torch.FloatTensor(returns)
    old_val_t = torch.FloatTensor(old_values)

    # Normalize advantages across the full rollout once before epochs
    adv_t = (adv_t - adv_t.mean()) / (adv_t.std() + 1e-8)

    total_aloss = total_vloss = 0.0
    n_updates = 0

    for _ in range(n_epochs):
        perm = np.random.permutation(n)
        for start in range(0, n, batch_size):
            idx       = perm[start:start + batch_size]
            b_obs     = obs_t[idx]
            b_act     = acts_t[idx]
            b_old     = old_lp_t[idx]
            b_adv     = adv_t[idx]
            b_ret     = ret_t[idx]
            b_old_val = old_val_t[idx]

            dist    = Categorical(logits=actor(b_obs))
            new_lp  = dist.log_prob(b_act)
            entropy = dist.entropy().mean()

            # Clipped policy loss
            ratio = torch.exp(new_lp - b_old)
            surr1 = ratio * b_adv
            surr2 = torch.clamp(ratio, 1 - clip_eps, 1 + clip_eps) * b_adv
            aloss = -torch.min(surr1, surr2).mean()

            # Clipped value loss — prevents large value jumps from corrupting
            # advantage estimates on subsequent rollouts
            v_pred         = baseline(b_obs)
            v_pred_clipped = b_old_val + torch.clamp(
                v_pred - b_old_val, -clip_eps, clip_eps
            )
            vloss = torch.max(
                F.smooth_l1_loss(v_pred, b_ret),
                F.smooth_l1_loss(v_pred_clipped, b_ret),
            )

            loss = aloss + value_coef * vloss - entropy_coef * entropy
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(
                list(actor.parameters()) + list(baseline.parameters()),
                max_grad_norm,
            )
            optimizer.step()

            total_aloss += aloss.item()
            total_vloss += vloss.item()
            n_updates   += 1

    return total_aloss / n_updates, total_vloss / n_updates


def plot_rewards(episode_rewards, save_path, window=50):
    fig, ax = plt.subplots(figsize=(10, 5))
    eps = np.arange(1, len(episode_rewards) + 1)
    ax.plot(eps, episode_rewards, alpha=0.3, color="steelblue",
            linewidth=0.8, label="Episode reward")
    if len(episode_rewards) >= window:
        rm = np.convolve(episode_rewards, np.ones(window) / window, mode="valid")
        ax.plot(np.arange(window, len(episode_rewards) + 1), rm,
                color="steelblue", linewidth=2, label=f"Running mean (w={window})")
    ax.axhline(y=200, color="green", linestyle="--", linewidth=1.5, label="Solved (200)")
    ax.axhline(y=0,   color="gray",  linestyle=":",  linewidth=1)
    ax.set_xlabel("Episode")
    ax.set_ylabel("Total Reward")
    ax.set_title("PPO — LunarLander-v3")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Plot saved to: {save_path}")


def train(n_steps=2048, n_epochs=4, batch_size=64,
          gamma=0.99, gae_lambda=0.95, clip_eps=0.2,
          lr=3e-4, entropy_coef=0.01, value_coef=0.5,
          max_episodes=2000, max_grad_norm=0.5,
          print_every=10, plot_every=50, seed=DEFAULT_SEED):

    set_global_seed(seed)
    env = gym.make("LunarLander-v3")
    env.reset(seed=seed)

    actor    = ActorNetwork()
    baseline = BaselineNetwork()
    # Single optimizer — PPO updates both networks jointly each minibatch
    optimizer = optim.Adam(
        list(actor.parameters()) + list(baseline.parameters()),
        lr=lr, eps=1e-5,
    )

    all_ep_rewards   = []
    recent           = deque(maxlen=100)
    best_mean        = -float("inf")
    state_normalizer = RunningStateNormalizer(shape=8)
    save_dir         = os.path.dirname(os.path.abspath(__file__))

    print(f"Training PPO on LunarLander-v3 (up to {max_episodes} episodes)")
    print(f"  n_steps={n_steps}  n_epochs={n_epochs}  batch_size={batch_size}")
    print(f"  clip_eps={clip_eps}  lr={lr}  gae_lambda={gae_lambda}")
    print(f"  entropy_coef={entropy_coef}  value_coef={value_coef}\n")

    ep_count   = 0
    update_num = 0

    while ep_count < max_episodes:
        # Linear LR annealing: full lr at ep 0, approaches 0 at max_episodes.
        # Prevents overshooting a good policy in later training.
        lr_now = lr * max(0.0, 1.0 - ep_count / max_episodes)
        for pg in optimizer.param_groups:
            pg['lr'] = lr_now

        obs, acts, old_lp, advs, rets, old_vals, ep_rewards = collect_rollout(
            env, actor, baseline, state_normalizer,
            n_steps=n_steps, gamma=gamma, gae_lambda=gae_lambda,
        )

        for r in ep_rewards:
            all_ep_rewards.append(r)
            recent.append(r)
            ep_count += 1

        mean_100 = np.mean(recent) if recent else float("nan")
        if mean_100 > best_mean:
            best_mean = mean_100
            torch.save(actor.state_dict(), os.path.join(save_dir, "actor_best.pt"))

        al, vl = ppo_update(
            obs, acts, old_lp, advs, rets, old_vals,
            actor, baseline, optimizer,
            clip_eps=clip_eps, n_epochs=n_epochs, batch_size=batch_size,
            entropy_coef=entropy_coef, value_coef=value_coef,
            max_grad_norm=max_grad_norm,
        )
        update_num += 1

        if update_num % print_every == 0 or ep_count >= max_episodes:
            last_r = all_ep_rewards[-1] if all_ep_rewards else float("nan")
            print(f"  Update {update_num:4d} | Ep {ep_count:5d} | "
                  f"reward: {last_r:8.1f} | mean(100): {mean_100:8.1f} | "
                  f"actor_loss: {al:.4f} | value_loss: {vl:.4f} | "
                  f"lr: {lr_now:.2e}")

        if ep_count % plot_every == 0 and all_ep_rewards:
            plot_rewards(all_ep_rewards,
                         save_path=os.path.join(save_dir, "logs", "rewards.png"))

        if mean_100 >= 200 and ep_count >= 100:
            print(f"\nSolved at episode {ep_count} (update {update_num}) "
                  f"with mean {mean_100:.1f}!")
            break

    plot_rewards(all_ep_rewards,
                 save_path=os.path.join(save_dir, "logs", "rewards.png"))
    env.close()
    return actor, baseline, all_ep_rewards


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PPO on LunarLander-v3.")
    parser.add_argument("--episodes",   type=int,   default=2000)
    parser.add_argument("--n-steps",    type=int,   default=2048,
                        help="Env steps per rollout before each PPO update.")
    parser.add_argument("--n-epochs",   type=int,   default=4,
                        help="Number of PPO update epochs per rollout.")
    parser.add_argument("--batch-size", type=int,   default=64)
    parser.add_argument("--clip-eps",   type=float, default=0.2)
    parser.add_argument("--lr",         type=float, default=3e-4)
    parser.add_argument("--gae-lambda", type=float, default=0.95)
    parser.add_argument("--seed",       type=int,   default=DEFAULT_SEED)
    args = parser.parse_args()

    save_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(save_dir, "logs"), exist_ok=True)

    log_path = os.path.join(save_dir, "terminal_output.md")
    log_file = open(log_path, "w")
    sys.stdout = _Tee(sys.__stdout__, log_file)

    try:
        actor, baseline, rewards = train(
            n_steps=args.n_steps,
            n_epochs=args.n_epochs,
            batch_size=args.batch_size,
            clip_eps=args.clip_eps,
            lr=args.lr,
            gae_lambda=args.gae_lambda,
            max_episodes=args.episodes,
            seed=args.seed,
        )
    finally:
        sys.stdout = sys.__stdout__
        log_file.close()
        print(f"Terminal output saved to: {log_path}")
