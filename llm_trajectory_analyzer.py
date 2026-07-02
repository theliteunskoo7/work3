import json
import os
import re
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

def strip_markdown_json(text):
    """Extract the first JSON object from text, stripping markdown code fences."""
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group() if match else text


ANALYZER_SYSTEM_PROMPT_TEMPLATE = """You are an expert reinforcement learning trajectory analyst studying a cart-pole balancing simulation.

STATE: A list of 4 values — [cart_pos, cart_vel, pole_angle, pole_ang_vel]
  - cart_pos    : position of cart (fails if |cart_pos| > 2.4)
  - cart_vel    : velocity of cart (negative=moving left, positive=moving right)
  - pole_angle  : angle of pole in radians (fails if |angle| > 0.2095; 0=upright)
  - pole_ang_vel: angular velocity of pole (negative=falling left, positive=falling right)
ACTIONS: 0=push left, 1=push right

Current environment understanding (10-point summary built from prior observed trajectories):
{summary}

You will be given a batch of full episode trajectories (state, action, reward per step). For each
trajectory, identify the top {top_k} "bad actions" in it.

TRAJECTORY FORMAT: The state at step N is the state BEFORE the action at step N is taken.
The state at step N+1 is the direct result of that action. To evaluate whether an action
was harmful, compare the state at step N with the state at step N+1 — that difference shows
what the action actually caused. Use the reward as corroborating evidence alongside this
state transition, not as the primary criterion.

A bad action is NOT simply the step with the lowest immediate reward. It is the action that most
likely CAUSED the trajectory to end up in a bad state — i.e. the action that failed to counter
the pole's fall or moved the cart dangerously close to the track edge.
Reason about the full arc of the trajectory: ask "which action here was the reason this trajectory
ended up bad?", using the environment summary above to judge whether an action was structurally
harmful given the state it was taken in.

Always respond with valid JSON in this exact format. The "reason" field must be plain English only — no backslashes, LaTeX, math notation, or special characters:
{{
  "episodes": [
    {{
      "episode_index": 0,
      "bad_actions": [
        {{"step": 0, "state": [0.0, 0.0, 0.0, 0.0], "action": 0, "reason": "short reason"}}
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


def analyze_trajectories(client, episodes, summary_text, top_k=2, model="unsloth/gemma-4-26B-A4B-it-GGUF", seed=None):
    """
    episodes: list of episode trajectories, each a list of {"state","action","reward"} dicts
              with RAW (unnormalized) physical states.
    summary_text: latest summary.md body, or None if not available yet.

    Returns a list, same length and order as `episodes`, where each entry is a list of up to
    `top_k` (state, action) tuples — state is a raw list of 4 floats, action is an int 0-1.
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
            seed=seed,
        )
        response_text = response.choices[0].message.content
        log_interaction(f"Trajectory Analysis | {len(episodes)} episodes", messages, response_text)
        json_text = strip_markdown_json(response_text)
        # Escape any backslash not part of a valid JSON escape sequence
        json_text = re.sub(r'\\(?!["\\/bfnrtu]|u[0-9a-fA-F]{4})', r'\\\\', json_text)
        data = json.loads(json_text)
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
                if len(state) == 4 and action in (0, 1):
                    pairs.append((state, action))
            except (KeyError, TypeError, ValueError):
                continue
        results[idx] = pairs
    return results
