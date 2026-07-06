import json
import os
import re
from datetime import datetime

from seeding import DEFAULT_SEED

# Own log file — kept separate from ai_agent.py's logs/agent_interaction_log.md
# so the AI Agent's logs (warm start + summary refresh) and the LLM Trajectory
# Analyzer's logs are never interleaved in one file. Seed-suffixed so runs
# with different seeds never clobber each other's log.
def _log_file(seed):
    return os.path.join(os.path.dirname(__file__), "logs", f"analyzer_log_{seed}.md")


def log_interaction(call_type, prompt_messages, response_text, seed):
    log_file = _log_file(seed)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
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


ANALYZER_SYSTEM_PROMPT_TEMPLATE = """You are an expert reinforcement learning trajectory analyst studying a lunar lander simulation.

STATE: A list of 8 values — [x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]
ACTIONS: 0=nothing, 1=left engine, 2=main engine, 3=right engine

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
likely CAUSED the trajectory to end up in a bad state — i.e. the action that pushed the lander away
from a recoverable path, or had the greatest negative impact on eventually reaching a safe landing.
Reason about the full arc of the trajectory: ask "which action here was the reason this trajectory
ended up bad?", using the environment summary above to judge whether an action was structurally
harmful given the state it was taken in.

Always respond with valid JSON in this exact format. The "reason" field must be plain English only — no backslashes, LaTeX, math notation, or special characters:
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


def analyze_trajectories(client, episodes, summary_text, top_k=2, model="unsloth/gemma-4-26B-A4B-it-GGUF", seed=None):
    """
    episodes: list of episode trajectories, each a list of {"state","action","reward"} dicts
              with RAW (unnormalized) physical states.
    summary_text: latest summary.md body, or None if not available yet.

    Returns a list, same length and order as `episodes`, where each entry is a list of up to
    `top_k` (state, action, step) tuples — state is the raw list of 8 floats the LLM echoed
    back (kept only for logging/verification, no longer used as a lookup key), action is an
    int 0-3, step is the 0-based index into that episode's trajectory list (matches the row
    number the LLM was shown in format_trajectories_for_analysis, which enumerates from 0 --
    NOT the rollout-global "step" field stored on each trajectory dict, which is a different,
    larger number). Callers should index the real trajectory as episodes[ep_idx][step] rather
    than re-matching the echoed state, since the state is retyped by the LLM and can silently
    drift (rounding, digit swaps, sign flips) in a way a step index cannot.
    Returns [] for an episode if parsing/the API call failed for it.
    """
    if not episodes:
        return []

    log_seed = seed if seed is not None else DEFAULT_SEED
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
        log_interaction(f"Trajectory Analysis | {len(episodes)} episodes", messages, response_text, log_seed)
        json_text = strip_markdown_json(response_text)
        # Escape any backslash not part of a valid JSON escape sequence
        json_text = re.sub(r'\\(?!["\\/bfnrtu]|u[0-9a-fA-F]{4})', r'\\\\', json_text)
        data = json.loads(json_text)
    except Exception as e:
        log_interaction(f"Trajectory Analysis ERROR | {len(episodes)} episodes", messages, str(e), log_seed)
        print(f"  [Analyzer failed: {e}] — skipping unlikelihood update this round")
        return results

    for ep_entry in data.get("episodes", []):
        idx = ep_entry.get("episode_index")
        if not isinstance(idx, int) or not (0 <= idx < len(episodes)):
            continue
        pairs = []
        ep_len = len(episodes[idx])
        for bad in ep_entry.get("bad_actions", [])[:top_k]:
            try:
                state = [float(v) for v in bad["state"]]
                action = int(bad["action"])
                step = int(bad["step"])
                if len(state) == 8 and action in (0, 1, 2, 3) and 0 <= step < ep_len:
                    pairs.append((state, action, step))
            except (KeyError, TypeError, ValueError):
                continue
        results[idx] = pairs
    return results
