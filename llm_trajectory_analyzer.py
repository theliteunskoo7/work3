import json
import os
from datetime import datetime

# Own log file — kept separate from ai_agent.py's logs/interaction_log.md so
# the AI Agent's logs (warm start + summary refresh) and the LLM Trajectory
# Analyzer's logs are never interleaved in one file.
LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "analyzer_log.md")


def log_interaction(call_type, prompt_messages, response_text):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"---\n\n## [{timestamp}] {call_type}\n\n")
        f.write("### Prompt\n\n")
        for msg in prompt_messages:
            f.write(f"**{msg['role'].upper()}:**\n```\n{msg['content']}\n```\n\n")
        f.write("### Response\n\n")
        f.write(f"```\n{response_text}\n```\n\n")

ANALYZER_SYSTEM_PROMPT_TEMPLATE = """You are an expert reinforcement learning trajectory analyst studying a lunar lander simulation.

STATE: A list of 8 values — [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]
ACTIONS: 0=nothing, 1=left engine, 2=main engine, 3=right engine

Current environment understanding (10-point summary built from prior observed trajectories):
{summary}

You will be given a batch of full episode trajectories (state, action, reward per step). For each
trajectory, identify the top {top_k} "bad actions" in it.

A bad action is NOT simply the step with the lowest immediate reward. It is the action that most
likely CAUSED the trajectory to end up in a bad state — i.e. the action that pushed the lander away
from a recoverable path, or had the greatest negative impact on eventually reaching a safe landing.
Reason about the full arc of the trajectory: ask "which action here was the reason this trajectory
ended up bad?", using the environment summary above to judge whether an action was structurally
harmful given the state it was taken in.

Always respond with valid JSON in this exact format:
{{
  "episodes": [
    {{
      "episode_index": 0,
      "bad_actions": [
        {{"step": 0, "state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "action": 0, "reason": "short reason"}}
      ]
    }}
  ]
}}
Return exactly one "episodes" entry per trajectory given, in the same order, indexed from 0.
Return exactly {top_k} bad_actions entries per episode (fewer only if the episode has fewer steps
than that)."""


def format_trajectories_for_analysis(episodes):
    lines = []
    for i, traj in enumerate(episodes):
        total_reward = sum(step["reward"] for step in traj)
        lines.append(f"\nEpisode {i} | Total Reward: {total_reward:.1f} | Steps: {len(traj)}")
        lines.append("step | state                                                              | action | reward")
        lines.append("-----|--------------------------------------------------------------------|--------|-------")
        for step, s in enumerate(traj):
            lines.append(f"{step:4d} | {s['state']} | {s['action']}      | {s['reward']:.3f}")
    return "\n".join(lines)


def analyze_trajectories(client, episodes, summary_text, top_k=2, model="gpt-4o-mini", seed=None):
    """
    episodes: list of episode trajectories, each a list of {"state","action","reward"} dicts
              with RAW (unnormalized) physical states.
    summary_text: latest summary.md body, or None if not available yet.

    Returns a list, same length and order as `episodes`, where each entry is a list of up to
    `top_k` (state, action) tuples — state is a raw list of 8 floats, action is an int 0-3.
    Returns [] for an episode if parsing/the API call failed for it.
    """
    if not episodes:
        return []

    summary_text = summary_text or "No environment summary available yet — use general physical reasoning."
    system_prompt = ANALYZER_SYSTEM_PROMPT_TEMPLATE.format(summary=summary_text, top_k=top_k)
    traj_text = format_trajectories_for_analysis(episodes)

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": (
                f"Trajectories:\n{traj_text}\n\n"
                f"Identify the top {top_k} bad actions per episode, per the JSON format described."
            ),
        },
    ]

    results = [[] for _ in episodes]
    try:
        # `seed` is OpenAI's best-effort determinism knob (not a hard
        # guarantee), threaded through from the same seed used locally.
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
            seed=seed,
        )
        response_text = response.choices[0].message.content
        log_interaction(f"Trajectory Analysis | {len(episodes)} episodes", messages, response_text)
        data = json.loads(response_text)
    except Exception as e:
        log_interaction(f"Trajectory Analysis ERROR | {len(episodes)} episodes", messages, str(e))
        print(f"  [Analyzer failed: {e}] — skipping unlikelihood update this round")
        return results

    for ep_entry in data.get("episodes", []):
        idx = ep_entry.get("episode_index")
        if not isinstance(idx, int) or not (0 <= idx < len(episodes)):
            continue
        pairs = []
        for bad in ep_entry.get("bad_actions", [])[:top_k]:
            try:
                state = [float(v) for v in bad["state"]]
                action = int(bad["action"])
                if len(state) == 8 and action in (0, 1, 2, 3):
                    pairs.append((state, action))
            except (KeyError, TypeError, ValueError):
                continue
        results[idx] = pairs
    return results
