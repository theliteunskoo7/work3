import os
import sys
import argparse
import faulthandler
import threading
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import gymnasium as gym
import matplotlib
matplotlib.use("Agg")  # headless training script — only ever saves PNGs, never shows a window;
                        # the default GUI backend (TkAgg) repeatedly creating/destroying figures
                        # in a long-running background process is what caused the segfaults.
import matplotlib.pyplot as plt
from collections import deque
from torch.distributions import Categorical
from openai import OpenAI

import ai_agent
from llm_trajectory_analyzer import analyze_trajectories
from seeding import set_global_seed, DEFAULT_SEED


class _Tee:
    """Mirror writes to multiple streams (e.g. stdout + a log file)."""
    def __init__(self, *streams):
        self.streams = streams

    def write(self, text):
        for s in self.streams:
            s.write(text)
            s.flush()

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
                    n_steps, gamma, gae_lambda, device):
    """
    Collect exactly n_steps transitions from a single env, resetting at episode
    boundaries.  Returns flat arrays suitable for minibatch PPO training, plus
    a list of completed-episode total rewards for logging, plus the completed
    episodes themselves as RAW (unnormalized) state/action/reward trajectories
    for the LLM trajectory analyzer and AI agent summarizer. A trailing
    episode that hasn't finished by the time the rollout ends is dropped (the
    analyzer/summarizer only ever see complete episodes).
    """
    obs_buf  = np.zeros((n_steps, 8), dtype=np.float32)
    act_buf  = np.zeros(n_steps,      dtype=np.int64)
    lp_buf   = np.zeros(n_steps,      dtype=np.float32)   # log π_old(a|s)
    rew_buf  = np.zeros(n_steps,      dtype=np.float32)
    val_buf  = np.zeros(n_steps,      dtype=np.float32)
    done_buf = np.zeros(n_steps,      dtype=np.float32)

    ep_rewards = []
    completed_episodes = []
    cur_ep_rew  = 0.0
    cur_ep_traj = []
    state, _    = env.reset()

    for t in range(n_steps):
        state_normalizer.update(state)
        norm_s = state_normalizer.normalize(state)
        s_t    = torch.FloatTensor(norm_s).to(device)

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
        cur_ep_traj.append({
            "state":   [round(float(v), 4) for v in state],
            "action":  act.item(),
            "reward":  round(float(reward), 4),
            "step":    t,
        })

        if done:
            ep_rewards.append(cur_ep_rew)
            completed_episodes.append((cur_ep_traj, cur_ep_rew))
            cur_ep_rew  = 0.0
            cur_ep_traj = []
            state, _ = env.reset()
        else:
            state = next_state

    # Bootstrap value for a rollout that ends mid-episode
    if done_buf[-1] == 0.0:
        state_normalizer.update(state)
        last_t = torch.FloatTensor(state_normalizer.normalize(state)).to(device)
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

    # Stamp each trajectory step with its GAE advantage so the training loop
    # can look it up by (state, action) when filtering unlikelihood pairs.
    for traj, _ in completed_episodes:
        for step_data in traj:
            step_data["advantage"] = float(adv_buf[step_data["step"]])

    return obs_buf, act_buf, lp_buf, adv_buf, ret_buf, val_buf, ep_rewards, completed_episodes


def ppo_update(obs, actions, old_log_probs, advantages, returns, old_values,
               actor, baseline, optimizer, device,
               clip_eps=0.2, n_epochs=4, batch_size=64,
               entropy_coef=0.01, value_coef=0.5, max_grad_norm=0.5):
    """
    K epochs of minibatch PPO updates on a fixed collected rollout.

    Policy loss: clipped surrogate -min(r·A, clip(r,1-ε,1+ε)·A)
    Value loss:  clipped to prevent value function from jumping too far from
                 the rollout estimates, mirroring the policy clip constraint.
    """
    n = len(obs)
    obs_t     = torch.FloatTensor(obs).to(device)
    acts_t    = torch.LongTensor(actions).to(device)
    old_lp_t  = torch.FloatTensor(old_log_probs).to(device)
    adv_t     = torch.FloatTensor(advantages).to(device)
    ret_t     = torch.FloatTensor(returns).to(device)
    old_val_t = torch.FloatTensor(old_values).to(device)

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


def unlikelihood_update(actor, optimizer, state_normalizer, bad_pairs, device, max_grad_norm=0.5):
    """
    One gradient step pushing pi(bad_action | bad_state) down, for every
    (state, action) pair the LLM Trajectory Analyzer flagged.

    loss = -log(1 - pi(a|s))   averaged over all flagged pairs this round.

    This is intentionally a SEPARATE optimizer/step from ppo_update — it is
    interleaved with the normal PPO update, not fused into it (see PROJECT
    discussion: avoids having to balance two loss terms with a single lambda,
    and keeps PPO's own clipped objective untouched).

    bad_pairs: list of (raw_state, action) — raw_state is the un-normalized
    8-float state as seen by the LLM. It's normalized here with the SAME
    running normalizer PPO uses, since that's the input distribution the
    actor was actually trained on.
    """
    if not bad_pairs:
        return None

    raw_states = np.array([p[0] for p in bad_pairs], dtype=np.float32)
    norm_states = np.stack([state_normalizer.normalize(s) for s in raw_states])
    states_t  = torch.FloatTensor(norm_states).to(device)
    actions_t = torch.LongTensor([p[1] for p in bad_pairs]).to(device)

    dist  = Categorical(logits=actor(states_t))
    p_bad = dist.probs.gather(1, actions_t.unsqueeze(1)).squeeze(1)
    p_bad_pre = p_bad.mean().item()

    # Clamp away from 1.0 so -log(1-p) can't blow up to inf on a confident
    # bad action; no lower clamp needed since log(1-p)->0 as p->0 is fine.
    loss = -torch.log(1.0 - p_bad.clamp(max=0.999)).mean()

    optimizer.zero_grad()
    loss.backward()
    nn.utils.clip_grad_norm_(actor.parameters(), max_grad_norm)
    optimizer.step()

    return {"loss": loss.item(), "p_bad_pre": p_bad_pre, "n_pairs": len(bad_pairs)}


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


def update_summary_from_episodes(client, current_summary, episodes, rewards, model="unsloth/gemma-4-26B-A4B-it-GGUF", seed=None):
    """
    Refresh summary.md from PPO-collected episodes, reusing the exact prompts
    ai_agent.py uses during warm start so the summary's voice/format stays
    consistent whether it was written during warm start or during training.

    `current_summary` may be None (e.g. warm start was skipped) — in that case
    this generates a fresh initial summary instead of updating one.
    """
    traj_text = ai_agent.format_trajectories_for_summary(episodes, rewards)

    if current_summary is None:
        print("\n[AI Agent] No prior summary found — generating initial summary from PPO episodes...")
        user_content = (
            f"State format: [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]\n"
            f"Actions: 0=nothing, 1=left engine, 2=main engine, 3=right engine\n\n"
            f"Trajectories:\n{traj_text}\n\n"
            f"Generate exactly 10 concise numbered key points summarizing:\n"
            f"- Environment physics and dynamics\n"
            f"- How each action affects state\n"
            f"- What action patterns lead to success vs failure\n"
            f"- Critical moments in a trajectory"
        )
        log_label = "Initial Summary Generation (from PPO episodes)"
    else:
        print("\n[AI Agent] Updating 10-point summary with new PPO episodes...")
        user_content = (
            f"State format: [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]\n"
            f"Actions: 0=nothing, 1=left engine, 2=main engine, 3=right engine\n\n"
            f"Your current 10-point understanding of the environment:\n{current_summary}\n\n"
            f"New trajectories observed:\n{traj_text}\n\n"
            f"Update and refine your 10-point summary of environment physics and action effects. "
            f"Keep points that are still valid, update points where new trajectory data reveals "
            f"more about how the environment behaves, and add new physics insights. "
            f"Do not comment on agent performance, training progress, or learning trends. "
            f"Output exactly 10 numbered points."
        )
        log_label = "Summary Update (from PPO episodes)"

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert analyst studying a lunar lander simulation. "
                "Your summaries will be used by an LLM to analyze RL training trajectories "
                "and identify bad actions."
            ),
        },
        {"role": "user", "content": user_content},
    ]

    try:
        # `seed` is OpenAI's best-effort determinism knob — not a hard
        # guarantee like the local torch/numpy/random seeding, but it's the
        # closest the API offers.
        response = client.chat.completions.create(model=model, messages=messages, seed=seed)
        response_text = response.choices[0].message.content
        ai_agent.log_interaction(log_label, messages, response_text)
        ai_agent.save_summary(response_text)
        return response_text
    except Exception as e:
        ai_agent.log_interaction(log_label + " ERROR", messages, str(e))
        print(f"  [Summary update failed: {e}] — keeping previous summary")
        return current_summary


def train(n_steps=2048, n_epochs=4, batch_size=64,
          gamma=0.99, gae_lambda=0.95, clip_eps=0.2,
          lr=3e-4, entropy_coef=0.01, value_coef=0.5,
          max_episodes=2000, max_grad_norm=0.5,
          print_every=1, plot_every=50, seed=DEFAULT_SEED,
          api_key=None, base_url="http://172.16.180.19:8001/v1",
          analyzer_base_url="http://172.16.180.19:8002/v1",
          llm_model="unsloth/gemma-4-26B-A4B-it-GGUF",
          analyzer_every=10, analyzer_topk=2, analyzer_n_traj=2,
          analyzer_threshold=200,
          unlikelihood_lr=1e-4,
          summary_n_traj=2):
    """
    Same PPO loop as ppo.py, interleaved with two LLM-driven side updates,
    both triggered on completed-episode counts (not on the PPO n_steps
    rollout boundary, since they need whole episodes):

      - every `analyzer_every` completed episodes: send them + the latest
        summary.md to the LLM Trajectory Analyzer, get back `analyzer_topk`
        bad (state,action) pairs per episode, and take ONE separate
        unlikelihood gradient step on the actor with all of them.
      - every `summary_every` completed episodes: hand the most recent
        `summary_n_traj` of that window to the AI agent's summarizer, which
        refreshes summary.md (building on the prior summary).

    Both are plain interleaved steps in this single loop — not background
    threads — per the agreed design (see PROJECT discussion).

    Both start from the very first PPO update — no warmup gate. The analyzer
    fires every `analyzer_every` completed episodes and sends only the most
    recent `analyzer_n_traj` of that window to the LLM; the summary refreshes
    once per update in a background thread (not on a fixed episode cadence).
    """
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY", "sk-no-key-required")
    client          = OpenAI(base_url=base_url,          api_key=api_key, timeout=None)  # summary updates
    analyzer_client = OpenAI(base_url=analyzer_base_url, api_key=api_key, timeout=None)  # trajectory analysis

    set_global_seed(seed)
    env = gym.make("LunarLander-v3")
    env.reset(seed=seed)

    # Hybrid device placement: the batched PPO minibatch update (and the
    # small-batch unlikelihood update) genuinely benefit from the GPU, but
    # collect_rollout does single-sample inference sequentially ~n_steps
    # times per rollout — thousands of tiny CUDA kernel launches in a tight
    # loop, which proved to reliably segfault on this driver (faulthandler
    # pinned the crash to Categorical.log_prob's internal validation kernel
    # during rollout collection). So rollout collection always runs on CPU;
    # the actor/baseline are shuttled to the GPU only for batched updates.
    cpu_device = torch.device("cpu")
    device     = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device} (rollout collection stays on CPU; batched updates use {device})")

    actor    = ActorNetwork().to(cpu_device)
    baseline = BaselineNetwork().to(cpu_device)
    # Single optimizer — PPO updates both networks jointly each minibatch
    optimizer = optim.Adam(
        list(actor.parameters()) + list(baseline.parameters()),
        lr=lr, eps=1e-5,
    )
    # Separate, actor-only optimizer for the unlikelihood update — kept
    # independent of PPO's optimizer/lr-schedule on purpose (see PROJECT
    # discussion: PPO's clipping protects its own update, nothing protects
    # this one, so it gets its own smaller, fixed lr).
    unlikelihood_optimizer = optim.Adam(actor.parameters(), lr=unlikelihood_lr)

    all_ep_rewards   = []
    recent           = deque(maxlen=100)
    best_mean        = -float("inf")
    last_plot_ep     = 0
    state_normalizer = RunningStateNormalizer(shape=8)
    save_dir         = os.path.dirname(os.path.abspath(__file__))

    # Seed from whatever summary.md already has (e.g. from ai_agent.py warm
    # start). None is fine — update_summary_from_episodes will bootstrap one.
    summary_text = ai_agent.load_summary()

    # summary_text is shared between the main loop (reads it for the analyzer)
    # and the background summary thread (writes a new value after the API call).
    # summary_lock protects all reads/writes; summary_ref is a mutable
    # container so the thread can write back without a closure-cell race.
    summary_lock    = threading.Lock()
    summary_ref     = [summary_text]
    summary_thread: threading.Thread | None = None
    analyzer_buffer = []

    print(f"Training PPO+LLM on LunarLander-v3 (up to {max_episodes} episodes)")
    print(f"  n_steps={n_steps}  n_epochs={n_epochs}  batch_size={batch_size}")
    print(f"  clip_eps={clip_eps}  lr={lr}  gae_lambda={gae_lambda}")
    print(f"  entropy_coef={entropy_coef}  value_coef={value_coef}")
    print(f"  analyzer_every={analyzer_every}  analyzer_n_traj={analyzer_n_traj}  analyzer_topk={analyzer_topk}  analyzer_threshold={analyzer_threshold}  unlikelihood_lr={unlikelihood_lr}")
    print(f"  summary_n_traj={summary_n_traj} (AI agent updates summary every PPO update using the last N episodes)  llm_model={llm_model}\n")

    ep_count   = 0
    update_num = 0

    while ep_count < max_episodes:
        # Linear LR annealing: full lr at ep 0, approaches 0 at max_episodes.
        # Prevents overshooting a good policy in later training.
        lr_now = lr * max(0.0, 1.0 - ep_count / max_episodes)
        for pg in optimizer.param_groups:
            pg['lr'] = lr_now

        obs, acts, old_lp, advs, rets, old_vals, ep_rewards, completed_episodes = collect_rollout(
            env, actor, baseline, state_normalizer,
            n_steps=n_steps, gamma=gamma, gae_lambda=gae_lambda, device=cpu_device,
        )

        for traj, r in completed_episodes:
            all_ep_rewards.append(r)
            recent.append(r)
            ep_count += 1
            analyzer_buffer.append((traj, r))

        mean_100 = np.mean(recent) if recent else float("nan")
        if mean_100 > best_mean:
            best_mean = mean_100
            # actor is on cpu_device here (rollout just finished, not yet
            # moved to GPU for the updates below) — .cpu() kept anyway as a
            # cheap safety net.
            torch.save({k: v.cpu() for k, v in actor.state_dict().items()},
                       os.path.join(save_dir, "actor_best_llm.pt"))

        # OpenSSL (used by the summary thread's HTTPS call) and CUDA both
        # install SIGSEGV handlers. Running them concurrently crashes the CUDA
        # autograd worker thread. Fix: join the summary thread here — before
        # any CUDA op — so SSL and CUDA are never active at the same time.
        # The thread was launched AFTER the previous iteration's CUDA work and
        # runs during collect_rollout (CPU-only), so in the common case it has
        # already finished by the time we reach this join.
        if summary_thread is not None and summary_thread.is_alive():
            summary_thread.join()

        # Batched updates: move params to the GPU only for these steps,
        # where there's an actual batch to parallelize. baseline is only
        # needed for ppo_update, so it goes back to CPU right after; actor
        # stays on GPU a bit longer for the unlikelihood update below.
        actor.to(device)
        baseline.to(device)
        al, vl = ppo_update(
            obs, acts, old_lp, advs, rets, old_vals,
            actor, baseline, optimizer, device,
            clip_eps=clip_eps, n_epochs=n_epochs, batch_size=batch_size,
            entropy_coef=entropy_coef, value_coef=value_coef,
            max_grad_norm=max_grad_norm,
        )
        baseline.to(cpu_device)
        update_num += 1

        # --- LLM Trajectory Analyzer + unlikelihood actor update ---
        # Reward-adaptive annealing: full lr when mean_100 <= 0, zero at analyzer_threshold.
        _mean_for_scale = mean_100 if not np.isnan(mean_100) else 0.0
        reward_scale = max(0.0, 1.0 - max(0.0, _mean_for_scale) / analyzer_threshold)
        ul_lr_now = unlikelihood_lr * reward_scale
        for pg in unlikelihood_optimizer.param_groups:
            pg['lr'] = ul_lr_now

        while len(analyzer_buffer) >= analyzer_every:
            batch = analyzer_buffer[:analyzer_every]
            analyzer_buffer = analyzer_buffer[analyzer_every:]
            # Only send the most recent analyzer_n_traj episodes to the LLM —
            # the rest of the window were just the cadence trigger.
            recent_batch = batch[-analyzer_n_traj:]
            filtered = [(traj, r) for traj, r in recent_batch if r < analyzer_threshold]
            if not filtered:
                continue
            episodes = [traj for traj, _ in filtered]

            # Snapshot summary under the lock so the background summary thread
            # can't write a new value mid-call.
            with summary_lock:
                current_summary = summary_ref[0]
            bad_pairs_per_ep = analyze_trajectories(
                analyzer_client, episodes, current_summary, top_k=analyzer_topk, model=llm_model, seed=seed,
            )
            bad_pairs = [pair for pairs in bad_pairs_per_ep for pair in pairs]

            # Advantage filter: drop pairs where the policy is already confident
            # (prob > 0.5) AND PPO found the action above average (advantage > 0).
            # Applying unlikelihood against PPO's own positive signal is what caused
            # the catastrophic regression at ep 748.
            n_raw = len(bad_pairs)
            if bad_pairs:
                raw_states  = np.array([p[0] for p in bad_pairs], dtype=np.float32)
                norm_states = np.stack([state_normalizer.normalize(s) for s in raw_states])
                states_t    = torch.FloatTensor(norm_states).to(device)
                actions_t   = torch.LongTensor([p[1] for p in bad_pairs]).to(device)
                with torch.no_grad():
                    dist  = Categorical(logits=actor(states_t))
                    probs = dist.probs.gather(1, actions_t.unsqueeze(1)).squeeze(1)

                filtered_pairs = []
                for i, (state, action) in enumerate(bad_pairs):
                    prob = probs[i].item()
                    if prob > 0.5:
                        adv = None
                        for ep in episodes:
                            for step_data in ep:
                                if (step_data["action"] == action and
                                        all(abs(a - b) < 1e-4
                                            for a, b in zip(step_data["state"], state))):
                                    adv = step_data.get("advantage")
                                    break
                            if adv is not None:
                                break
                        if adv is not None and adv > 0.0:
                            continue  # drop: policy confident + PPO agrees it's good
                    filtered_pairs.append((state, action))
                bad_pairs = filtered_pairs

            n_dropped = n_raw - len(bad_pairs)
            stats = unlikelihood_update(actor, unlikelihood_optimizer, state_normalizer, bad_pairs, device,
                                        max_grad_norm=max_grad_norm)
            if stats:
                print(f"  [Analyzer] {len(episodes)} episodes -> {n_raw} bad pairs "
                      f"({n_dropped} dropped by adv filter) | "
                      f"unlikelihood_loss={stats['loss']:.4f} | "
                      f"mean p(bad) before update={stats['p_bad_pre']:.4f} | "
                      f"ul_lr={ul_lr_now:.2e} (scale={reward_scale:.2f})")
            else:
                print(f"  [Analyzer] {len(episodes)} episodes -> {n_raw} bad pairs "
                      f"({n_dropped} dropped by adv filter, 0 applied)")

        # Back to CPU before launching the summary thread — all CUDA ops for
        # this update are now done. The thread will run during the NEXT
        # collect_rollout (CPU-only), safely separated from CUDA.
        actor.to(cpu_device)

        # --- AI agent summary refresh: background thread, reward-adaptive rate ---
        # Launched AFTER all CUDA work for this update. Runs concurrently with
        # the next collect_rollout. Joined at the top of the next iteration
        # before CUDA resumes, so SSL and CUDA never overlap.
        # Gap scales from 1 (every rollout, when policy is bad) up to 5 (every
        # 5th rollout, when mean_100 approaches the solve threshold) — summaries
        # converge early so high-frequency updates add no value at late training.
        _summary_gap = max(1, int(5 * _mean_for_scale / analyzer_threshold))
        if completed_episodes and update_num % _summary_gap == 0:
            recent_eps = completed_episodes[-summary_n_traj:]
            ep_trajs   = [traj for traj, _ in recent_eps]
            ep_rews    = [r for _, r in recent_eps]

            def _run_summary(trajs, rews):
                with summary_lock:
                    base = summary_ref[0]
                new_text = update_summary_from_episodes(
                    client, base, trajs, rews, model=llm_model, seed=seed,
                )
                with summary_lock:
                    summary_ref[0] = new_text

            summary_thread = threading.Thread(
                target=_run_summary, args=(ep_trajs, ep_rews), daemon=True,
            )
            summary_thread.start()

        if update_num % print_every == 0 or ep_count >= max_episodes:
            last_r = all_ep_rewards[-1] if all_ep_rewards else float("nan")
            print(f"  Update {update_num:4d} | Ep {ep_count:5d} | "
                  f"reward: {last_r:8.1f} | mean(100): {mean_100:8.1f} | "
                  f"actor_loss: {al:.4f} | value_loss: {vl:.4f} | "
                  f"lr: {lr_now:.2e}")

        # A rollout can complete several episodes at once, so ep_count can
        # jump past an exact multiple of plot_every — track episodes since
        # the last plot instead of testing for exact equality.
        if ep_count - last_plot_ep >= plot_every and all_ep_rewards:
            last_plot_ep = ep_count
            plot_rewards(all_ep_rewards,
                         save_path=os.path.join(save_dir, "logs", "rewards_llm.png"))

        if mean_100 >= 200 and ep_count >= 100:
            print(f"\nSolved at episode {ep_count} (update {update_num}) "
                  f"with mean {mean_100:.1f}!")
            break

    plot_rewards(all_ep_rewards,
                 save_path=os.path.join(save_dir, "logs", "rewards_llm.png"))
    env.close()
    return actor, baseline, all_ep_rewards


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PPO + LLM Trajectory Analyzer on LunarLander-v3.")
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
    parser.add_argument("--api-key",          type=str,   default=None,
                        help="API key for the model server. Defaults to OPENAI_API_KEY env var, or 'sk-no-key-required'.")
    parser.add_argument("--base-url",          type=str,   default="http://172.16.180.19:8001/v1",
                        help="Base URL for summary update LLM calls (port 8001).")
    parser.add_argument("--analyzer-base-url", type=str,   default="http://172.16.180.19:8002/v1",
                        help="Base URL for trajectory analysis LLM calls (port 8002).")
    parser.add_argument("--llm-model",        type=str,   default="unsloth/gemma-4-26B-A4B-it-GGUF")
    parser.add_argument("--analyzer-every",   type=int,   default=10,
                        help="Run the LLM Trajectory Analyzer + unlikelihood update every N completed episodes.")
    parser.add_argument("--analyzer-n-traj",  type=int,   default=2,
                        help="Of each analyzer window, send only the most recent N episodes to the LLM.")
    parser.add_argument("--analyzer-topk",      type=int,   default=2,
                        help="Top-K bad (state,action) pairs the analyzer extracts per episode.")
    parser.add_argument("--analyzer-threshold", type=float, default=200,
                        help="Only send episodes with return below this threshold to the analyzer.")
    parser.add_argument("--unlikelihood-lr",  type=float, default=1e-4,
                        help="LR for the separate actor-only unlikelihood optimizer.")
    parser.add_argument("--summary-n-traj",   type=int,   default=2,
                        help="Number of most recent episodes sent to the AI agent summary update each PPO update.")
    args = parser.parse_args()

    save_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(save_dir, "logs"), exist_ok=True)

    # Diagnostic instrumentation for the recurring segfault: faulthandler
    # installs a low-level handler for SIGSEGV that dumps every thread's
    # Python-level stack the instant the fault happens, bypassing normal
    # exception handling (which a segfault skips entirely). This is what
    # will tell us which line of Python code (and which thread — e.g. a
    # background CUDA/autograd thread vs the main loop) was executing when
    # the crash hit, instead of just inferring it from training logs.
    crash_log = open(os.path.join(save_dir, "crash_trace_llm.log"), "w")
    faulthandler.enable(file=crash_log, all_threads=True)

    log_path = os.path.join(save_dir, "terminal_output_llm.md")
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
            api_key=args.api_key,
            base_url=args.base_url,
            analyzer_base_url=args.analyzer_base_url,
            llm_model=args.llm_model,
            analyzer_every=args.analyzer_every,
            analyzer_n_traj=args.analyzer_n_traj,
            analyzer_topk=args.analyzer_topk,
            analyzer_threshold=args.analyzer_threshold,
            unlikelihood_lr=args.unlikelihood_lr,
            summary_n_traj=args.summary_n_traj,
        )
    finally:
        sys.stdout = sys.__stdout__
        log_file.close()
        print(f"Terminal output saved to: {log_path}")
