import json
import os
import re
import numpy as np
import gymnasium as gym
from datetime import datetime
from openai import OpenAI

from seeding import set_global_seed, DEFAULT_SEED

SYSTEM_PROMPT = """You are an intelligent agent controlling a cart-pole balancing system.

GOAL: Keep the pole balanced upright as long as possible by moving the cart left or right.

STATE: A list of 4 values — [cart_pos, cart_vel, pole_angle, pole_ang_vel]
  - cart_pos    : position of the cart on the track (0 = center; fails if |cart_pos| > 2.4)
  - cart_vel    : velocity of the cart (negative=moving left, positive=moving right)
  - pole_angle  : angle of the pole in radians (0 = upright; fails if |angle| > 0.2095 rad ≈ 12°)
  - pole_ang_vel: angular velocity of the pole (negative=falling left, positive=falling right)

ACTIONS:
  0 = Push cart LEFT
  1 = Push cart RIGHT

REWARD STRUCTURE:
  - +1 for every timestep the pole remains upright
  - Episode ends when pole falls beyond ±12° or cart goes beyond ±2.4
  - Maximum episode length: 500 steps (reward = 500 = perfect episode)

STRATEGY: Counter the direction the pole is falling. If pole_angle > 0 (falling right), push right
(action 1) to move the cart under the pole. If pole_angle < 0 (falling left), push left (action 0).
Also account for cart_vel to avoid driving the cart off the track edge.

Always respond with valid JSON: {"actions": [a1, a2, ..., a20]} where each value is 0 or 1."""


LOG_FILE              = os.path.join(os.path.dirname(__file__), "logs", "agent_interaction_log.md")
SUMMARY_FILE          = os.path.join(os.path.dirname(__file__), "summary.md")
SUMMARY_HISTORY_FILE  = os.path.join(os.path.dirname(__file__), "summary_history.md")


def strip_markdown_json(text):
    """Extract the first JSON object from text, stripping markdown code fences."""
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group() if match else text


def init_log():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write(f"# AI Agent Interaction Log\nStarted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")


def save_summary(summary_text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(SUMMARY_FILE, "w") as f:
        f.write(f"# Environment Summary\nLast updated: {timestamp}\n\n")
        f.write(summary_text)
    with open(SUMMARY_HISTORY_FILE, "a") as f:
        f.write(f"\n---\n\n## {timestamp}\n\n")
        f.write(summary_text)
        f.write("\n")


def load_summary():
    if not os.path.exists(SUMMARY_FILE):
        return None
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    # Strip the header (first 2 lines) and return body
    return "".join(lines[2:]).strip()


def log_interaction(call_type, prompt_messages, response_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"---\n\n## [{timestamp}] {call_type}\n\n")
        f.write("### Prompt\n\n")
        for msg in prompt_messages:
            f.write(f"**{msg['role'].upper()}:**\n```\n{msg['content']}\n```\n\n")
        f.write("### Response\n\n")
        f.write(f"```\n{response_text}\n```\n\n")


def format_trajectories_for_summary(trajectories, episode_rewards):
    lines = []
    for i, (traj, reward) in enumerate(zip(trajectories, episode_rewards)):
        outcome = "SUCCESS" if reward >= 475 else ("PARTIAL" if reward > 100 else "FAILURE")
        lines.append(f"\nEpisode {i+1} | Total Reward: {reward:.1f} | Outcome: {outcome} | Steps: {len(traj)}")
        lines.append("step | state                                                              | action | reward")
        lines.append("-----|-------------------------------------------------------------------|--------|-------")
        for step, step_data in enumerate(traj):
            lines.append(f"{step:4d} | {step_data['state']} | {step_data['action']}      | {step_data['reward']:.3f}")
    return "\n".join(lines)


class CartPoleAIAgent:
    def __init__(self, api_key, base_url, chunk_size=20, model="unsloth/gemma-4-26B-A4B-it-GGUF", seed=DEFAULT_SEED):
        self.seed = seed
        set_global_seed(seed)
        self.env = gym.make("CartPole-v1")
        self.env.reset(seed=seed)
        self.client = OpenAI(base_url=base_url, api_key=api_key, timeout=None)
        self.chunk_size = chunk_size
        self.model = model
        self.summary = None
        init_log()

    def get_chunk_actions(self, state, episode_num, chunk_num):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Current state: {[round(float(v), 4) for v in state]}\n\n"
                    f"Provide the next {self.chunk_size} actions as JSON: "
                    f"{{\"actions\": [list of {self.chunk_size} integers, each 0-3]}}"
                ),
            },
        ]
        try:
            # `seed` is OpenAI's best-effort determinism knob (not a hard
            # guarantee), threaded through from the same seed used locally.
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                seed=self.seed,
            )
            response_text = response.choices[0].message.content
            log_interaction(f"Action Chunk | Episode {episode_num} Chunk {chunk_num}", messages, response_text)

            data = json.loads(strip_markdown_json(response_text))
            actions = [int(a) for a in data.get("actions", []) if int(a) in (0, 1)]
            while len(actions) < self.chunk_size:
                actions.append(0)
            return actions[: self.chunk_size]

        except Exception as e:
            log_interaction(f"Action Chunk ERROR | Episode {episode_num} Chunk {chunk_num}", messages, str(e))
            print(f"  [Chunk failed: {e}] — defaulting to do-nothing")
            return [0] * self.chunk_size

    def run_episode(self, episode_num):
        state, _ = self.env.reset()
        trajectory = []
        total_reward = 0.0
        done = False
        chunk_num = 0

        while not done:
            chunk_num += 1
            actions = self.get_chunk_actions(state, episode_num, chunk_num)

            for action in actions:
                if done:
                    break
                next_state, reward, terminated, truncated, _ = self.env.step(action)
                done = terminated or truncated
                trajectory.append({
                    "state": [round(float(v), 4) for v in state],
                    "action": action,
                    "reward": round(float(reward), 4),
                    "next_state": [round(float(v), 4) for v in next_state],
                    "done": done,
                })
                total_reward += reward
                state = next_state

        outcome = "SUCCESS" if total_reward >= 475 else ("PARTIAL" if total_reward > 100 else "FAILURE")
        print(f"  Episode {episode_num}: steps={len(trajectory)}, reward={total_reward:.1f}, "
              f"outcome={outcome}, api_calls={chunk_num}")
        return trajectory, total_reward

    def generate_initial_summary(self, trajectories, episode_rewards):
        print("\nGenerating initial 10-point summary...")
        traj_text = format_trajectories_for_summary(trajectories, episode_rewards)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert analyst studying a cart-pole balancing simulation. "
                    "Your summaries will be used by an LLM to analyze RL training trajectories "
                    "and identify bad actions."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"State format: [cart_pos, cart_vel, pole_angle, pole_ang_vel]\n"
                    f"Actions: 0=push left, 1=push right\n\n"
                    f"Trajectories:\n{traj_text}\n\n"
                    f"Generate exactly 10 concise numbered key points summarizing:\n"
                    f"- Environment physics and dynamics\n"
                    f"- How each action affects state\n"
                    f"- What action patterns lead to success vs failure\n"
                    f"- Critical moments in a trajectory"
                ),
            },
        ]

        response = self.client.chat.completions.create(model=self.model, messages=messages, seed=self.seed)
        response_text = response.choices[0].message.content
        log_interaction("Initial Summary Generation", messages, response_text)
        self.summary = response_text
        save_summary(self.summary)
        return self.summary

    def update_summary(self, new_trajectories, episode_rewards):
        print("\nUpdating 10-point summary with new trajectories...")
        traj_text = format_trajectories_for_summary(new_trajectories, episode_rewards)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert analyst studying a cart-pole balancing simulation. "
                    "Your summaries will be used by an LLM to analyze RL training trajectories "
                    "and identify bad actions."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"State format: [cart_pos, cart_vel, pole_angle, pole_ang_vel]\n"
                    f"Actions: 0=push left, 1=push right\n\n"
                    f"Your current 10-point understanding of the environment:\n{self.summary}\n\n"
                    f"New trajectories observed:\n{traj_text}\n\n"
                    f"Update and refine your 10-point summary of environment physics and action effects. "
                    f"Keep points that are still valid, update points where new trajectory data reveals "
                    f"more about how the environment behaves, and add new physics insights. "
                    f"Do not comment on agent performance, training progress, or learning trends. "
                    f"Output exactly 10 numbered points."
                ),
            },
        ]

        response = self.client.chat.completions.create(model=self.model, messages=messages, seed=self.seed)
        response_text = response.choices[0].message.content
        log_interaction("Summary Update", messages, response_text)
        self.summary = response_text
        save_summary(self.summary)
        return self.summary

    def run_warm_start(self, n_episodes=5, summary_update_every=2):
        print(f"=== AI Agent Warm Start ({n_episodes} episodes, chunk_size={self.chunk_size}) ===\n")
        all_trajectories = []
        all_rewards = []

        for ep in range(1, n_episodes + 1):
            traj, reward = self.run_episode(episode_num=ep)
            all_trajectories.append(traj)
            all_rewards.append(reward)

            # Generate initial summary after first batch, then update periodically
            if ep == summary_update_every:
                self.generate_initial_summary(all_trajectories[:ep], all_rewards[:ep])
                print(f"\n--- Initial Summary (after episode {ep}) ---\n{self.summary}\n")
            elif ep > summary_update_every and ep % summary_update_every == 0:
                self.update_summary(all_trajectories[ep - summary_update_every:ep],
                                    all_rewards[ep - summary_update_every:ep])
                print(f"\n--- Updated Summary (after episode {ep}) ---\n{self.summary}\n")

        # Final update if last batch wasn't covered
        if n_episodes % summary_update_every != 0 and self.summary is not None:
            remaining_start = (n_episodes // summary_update_every) * summary_update_every
            self.update_summary(all_trajectories[remaining_start:], all_rewards[remaining_start:])
            print(f"\n--- Final Summary ---\n{self.summary}\n")

        print(f"\n=== Warm Start Complete ===")
        print(f"  Mean reward : {np.mean(all_rewards):.1f}")
        print(f"  Best reward : {np.max(all_rewards):.1f}")
        print(f"  Worst reward: {np.min(all_rewards):.1f}")
        print(f"  Log saved to    : {LOG_FILE}")
        print(f"  Summary saved to: {SUMMARY_FILE}")

        return all_trajectories, all_rewards, self.summary

    def close(self):
        self.env.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Agent warm start on CartPole-v1.")
    parser.add_argument("--api-key", type=str, default=None,
                        help="API key for the model server. Defaults to OPENAI_API_KEY env var, or 'sk-no-key-required'.")
    parser.add_argument("--base-url", type=str, default="http://172.16.180.19:8001/v1",
                        help="Base URL of the OpenAI-compatible model server.")
    parser.add_argument("--model", type=str, default="unsloth/gemma-4-26B-A4B-it-GGUF",
                        help="Model name served by the local inference server.")
    parser.add_argument("--chunk-size", type=int, default=20)
    parser.add_argument("--episodes", type=int, default=5)
    parser.add_argument("--summary-update-every", type=int, default=2)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("OPENAI_API_KEY", "sk-no-key-required")

    agent = CartPoleAIAgent(api_key=api_key, base_url=args.base_url, chunk_size=args.chunk_size, model=args.model, seed=args.seed)
    try:
        trajectories, rewards, summary = agent.run_warm_start(
            n_episodes=args.episodes, summary_update_every=args.summary_update_every,
        )
    finally:
        agent.close()
