import json
import os
import numpy as np
import gymnasium as gym
from datetime import datetime
from openai import OpenAI

SYSTEM_PROMPT = """You are an intelligent agent controlling a lunar lander in a physics simulation.

GOAL: Land the spacecraft safely on the landing pad at coordinates (0, 0).

STATE: A list of 8 values — [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]
  - x_pos      : horizontal position (negative=left of pad, positive=right of pad)
  - y_pos      : height above ground (starts ~1.4, ground=0)
  - x_vel      : horizontal velocity (negative=moving left, positive=moving right)
  - y_vel      : vertical velocity (negative=falling, positive=rising)
  - angle      : tilt in radians (negative=tilted left, positive=tilted right, 0=upright)
  - ang_vel    : angular velocity
  - left_leg_contact  : 1.0 if left leg touches ground, else 0.0
  - right_leg_contact : 1.0 if right leg touches ground, else 0.0

ACTIONS:
  0 = Do nothing
  1 = Fire left orientation engine  (tilts lander clockwise)
  2 = Fire main engine              (upward thrust, slows descent)
  3 = Fire right orientation engine (tilts lander counter-clockwise)

REWARD STRUCTURE:
  - Moving toward pad and reducing speed: positive reward
  - Moving away or crashing: negative reward
  - Crash: -100 penalty
  - Safe landing (both legs, low speed): +100 to +140 bonus
  - Main engine fire cost: ~0.3 per step
  - Orientation engine fire cost: ~0.03 per step

STRATEGY: Navigate toward the pad, keep angle near 0, reduce velocity as you approach,
touch down gently with both legs simultaneously.

Always respond with valid JSON: {"actions": [a1, a2, ..., a20]} where each value is 0, 1, 2, or 3."""


LOG_FILE     = os.path.join(os.path.dirname(__file__), "logs", "interaction_log.md")
SUMMARY_FILE = os.path.join(os.path.dirname(__file__), "summary.md")


def init_log():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write(f"# AI Agent Interaction Log\nStarted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")


def save_summary(summary_text):
    with open(SUMMARY_FILE, "w") as f:
        f.write(f"# Environment Summary\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(summary_text)


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
        outcome = "SUCCESS" if reward > 200 else ("PARTIAL" if reward > 0 else "FAILURE")
        lines.append(f"\nEpisode {i+1} | Total Reward: {reward:.1f} | Outcome: {outcome} | Steps: {len(traj)}")
        lines.append("step | state                                                              | action | reward")
        lines.append("-----|-------------------------------------------------------------------|--------|-------")
        for step, step_data in enumerate(traj):
            lines.append(f"{step:4d} | {step_data['state']} | {step_data['action']}      | {step_data['reward']:.3f}")
    return "\n".join(lines)


class LunarLanderAIAgent:
    def __init__(self, api_key, chunk_size=20):
        self.env = gym.make("LunarLander-v3")
        self.client = OpenAI(api_key=api_key)
        self.chunk_size = chunk_size
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
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                response_format={"type": "json_object"},
            )
            response_text = response.choices[0].message.content
            log_interaction(f"Action Chunk | Episode {episode_num} Chunk {chunk_num}", messages, response_text)

            data = json.loads(response_text)
            actions = [int(a) for a in data.get("actions", []) if int(a) in (0, 1, 2, 3)]
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

        outcome = "SUCCESS" if total_reward > 200 else ("PARTIAL" if total_reward > 0 else "FAILURE")
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
                    "You are an expert analyst studying a lunar lander simulation. "
                    "Your summaries will be used by an LLM to analyze RL training trajectories "
                    "and identify bad actions."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"State format: [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]\n"
                    f"Actions: 0=nothing, 1=left engine, 2=main engine, 3=right engine\n\n"
                    f"Trajectories:\n{traj_text}\n\n"
                    f"Generate exactly 10 concise numbered key points summarizing:\n"
                    f"- Environment physics and dynamics\n"
                    f"- How each action affects state\n"
                    f"- What action patterns lead to success vs failure\n"
                    f"- Critical moments in a trajectory"
                ),
            },
        ]

        response = self.client.chat.completions.create(model="gpt-4o-mini", messages=messages)
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
                    "You are an expert analyst studying a lunar lander simulation. "
                    "Your summaries will be used by an LLM to analyze RL training trajectories "
                    "and identify bad actions."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"State format: [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]\n"
                    f"Actions: 0=nothing, 1=left engine, 2=main engine, 3=right engine\n\n"
                    f"Your current 10-point understanding of the environment:\n{self.summary}\n\n"
                    f"New trajectories observed:\n{traj_text}\n\n"
                    f"Update and refine your 10-point summary. Keep points that are still valid, "
                    f"update points where you have learned more, and add new insights. "
                    f"Output exactly 10 numbered points."
                ),
            },
        ]

        response = self.client.chat.completions.create(model="gpt-4o-mini", messages=messages)
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
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Set OPENAI_API_KEY environment variable")

    agent = LunarLanderAIAgent(api_key=api_key, chunk_size=20)
    try:
        trajectories, rewards, summary = agent.run_warm_start(n_episodes=5, summary_update_every=2)
    finally:
        agent.close()
