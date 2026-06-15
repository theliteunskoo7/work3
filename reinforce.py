import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import gymnasium as gym
import matplotlib.pyplot as plt
from collections import deque


class ActorNetwork(nn.Module):
    def __init__(self, state_dim=8, action_dim=4, hidden_dim=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, x):
        return F.softmax(self.net(x), dim=-1)


class BaselineNetwork(nn.Module):
    def __init__(self, state_dim=8, hidden_dim=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


def compute_returns(rewards, gamma=0.99):
    returns = []
    G = 0.0
    for r in reversed(rewards):
        G = r + gamma * G
        returns.insert(0, G)
    return returns


def run_episode(env, actor, baseline):
    state, _ = env.reset()
    log_probs, values, rewards = [], [], []
    done = False

    while not done:
        state_t = torch.FloatTensor(state)
        probs = actor(state_t)
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()

        log_probs.append(dist.log_prob(action))
        values.append(baseline(state_t))

        next_state, reward, terminated, truncated, _ = env.step(action.item())
        rewards.append(reward)
        done = terminated or truncated
        state = next_state

    return log_probs, values, rewards


def update(log_probs, values, rewards, actor_optimizer, baseline_optimizer,
           gamma=0.99, entropy_coef=0.01):
    returns = torch.FloatTensor(compute_returns(rewards, gamma))
    log_probs = torch.stack(log_probs)
    values = torch.stack(values)

    advantages = returns - values.detach()
    # Normalize advantages for stable training
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

    # Entropy bonus — keeps exploration alive
    probs = log_probs.exp()
    entropy = -(probs * log_probs).sum()

    actor_loss = -(log_probs * advantages).mean() - entropy_coef * entropy
    baseline_loss = F.mse_loss(values, returns)

    actor_optimizer.zero_grad()
    actor_loss.backward()
    torch.nn.utils.clip_grad_norm_(actor_optimizer.param_groups[0]['params'], max_norm=0.5)
    actor_optimizer.step()

    baseline_optimizer.zero_grad()
    baseline_loss.backward()
    baseline_optimizer.step()

    return actor_loss.item(), baseline_loss.item()


def plot_rewards(episode_rewards, save_path, window=50):
    fig, ax = plt.subplots(figsize=(10, 5))
    episodes = np.arange(1, len(episode_rewards) + 1)

    ax.plot(episodes, episode_rewards, alpha=0.3, color="steelblue", linewidth=0.8, label="Episode reward")

    if len(episode_rewards) >= window:
        running_mean = np.convolve(episode_rewards, np.ones(window) / window, mode="valid")
        ax.plot(np.arange(window, len(episode_rewards) + 1), running_mean,
                color="steelblue", linewidth=2, label=f"Running mean (window={window})")

    ax.axhline(y=200, color="green", linestyle="--", linewidth=1.5, label="Solved threshold (200)")
    ax.axhline(y=0, color="gray", linestyle=":", linewidth=1)
    ax.set_xlabel("Episode")
    ax.set_ylabel("Total Reward")
    ax.set_title("REINFORCE with Baseline — LunarLander-v3")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Plot saved to: {save_path}")


def train(n_episodes=1000, gamma=0.99, lr_actor=3e-4, lr_baseline=1e-3,
          entropy_coef=0.01, print_every=50, plot_every=100):

    env = gym.make("LunarLander-v3")
    actor    = ActorNetwork()
    baseline = BaselineNetwork()
    actor_optimizer    = optim.Adam(actor.parameters(),    lr=lr_actor)
    baseline_optimizer = optim.Adam(baseline.parameters(), lr=lr_baseline)

    episode_rewards = []
    recent = deque(maxlen=100)
    best_mean = -float("inf")
    save_dir = os.path.dirname(__file__)

    print(f"Training REINFORCE on LunarLander-v3 for {n_episodes} episodes\n")

    for ep in range(1, n_episodes + 1):
        log_probs, values, rewards = run_episode(env, actor, baseline)
        actor_loss, baseline_loss = update(
            log_probs, values, rewards,
            actor_optimizer, baseline_optimizer,
            gamma=gamma, entropy_coef=entropy_coef
        )

        total_reward = sum(rewards)
        episode_rewards.append(total_reward)
        recent.append(total_reward)
        mean_100 = np.mean(recent)

        if mean_100 > best_mean:
            best_mean = mean_100
            torch.save(actor.state_dict(), os.path.join(save_dir, "actor_best.pt"))

        if ep % print_every == 0:
            print(f"  Ep {ep:4d} | reward: {total_reward:8.1f} | "
                  f"mean(100): {mean_100:8.1f} | "
                  f"actor_loss: {actor_loss:.4f} | baseline_loss: {baseline_loss:.4f}")

        if ep % plot_every == 0:
            plot_rewards(episode_rewards,
                         save_path=os.path.join(save_dir, "logs", "rewards.png"))

        if mean_100 >= 200 and ep >= 100:
            print(f"\nSolved at episode {ep} with mean reward {mean_100:.1f}!")
            break

    plot_rewards(episode_rewards, save_path=os.path.join(save_dir, "logs", "rewards.png"))
    env.close()
    return actor, baseline, episode_rewards


if __name__ == "__main__":
    os.makedirs(os.path.join(os.path.dirname(__file__), "logs"), exist_ok=True)
    actor, baseline, rewards = train(n_episodes=1000)
