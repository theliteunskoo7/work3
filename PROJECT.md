# LLM-Integrated Reinforcement Learning on LunarLander

## Overview

This project integrates LLM-based AI agents into a reinforcement learning training loop on the LunarLander-v3 (Gymnasium) environment. The core idea is to use language model reasoning to provide a higher-level understanding of the environment and to identify harmful actions during training, which then feeds back into the RL agent's learning signal.

The system has three distinct components that work together:

1. **AI Agent** — explores the environment, builds and maintains a living 10-point summary of environment dynamics
2. **PPO Agent** — the RL agent that learns to land via clipped-surrogate policy gradient + GAE
3. **LLM Trajectory Analyzer** — analyzes completed trajectories, identifies the top-K bad actions per trajectory, which are then used to suppress those actions in the actor network

Two copies of the RL agent exist side by side: `ppo.py` is the **untouched PPO baseline** (no LLM involvement at all), kept around purely so its training curve can be compared against the LLM-integrated version. `ppo_llm.py` is the actual integration — same PPO core, plus the AI Agent and LLM Trajectory Analyzer wired in.

---

## Motivation

Standard RL agents learn purely from numerical reward signals with no semantic understanding of what is happening. This project explores whether injecting LLM-based reasoning into the training loop can:
- Accelerate convergence by penalizing structurally bad decisions
- Provide a richer, interpretable signal beyond just scalar rewards
- Ground the LLM's analysis in actual environment dynamics via the evolving summary

---

## System Architecture

```
WARM START PHASE  (ai_agent.py, run standalone before training)
─────────────────────────────────────────────────────────────
  AI Agent (GPT-4o mini)
    → explores LunarLander with action chunking (20 steps/call)
    → collects full episodes
    → generates initial 10-point summary → saved to summary.md
    → updates summary every 2 episodes (each update builds on prior summary)

TRAINING PHASE  (ppo_llm.py — single process, interleaved, not multi-threaded)
─────────────────────────────────────────────────────────────
  PPO Agent
    → collects a fixed-size rollout (n_steps env steps, default 2048),
      resetting at episode boundaries; bootstraps the value of a partial
      trailing episode rather than waiting for it to finish
    → computes GAE advantages + returns
    → runs n_epochs (default 4) of clipped-surrogate minibatch updates
      on actor + baseline jointly (one optimizer)
    → completed episodes from the rollout are buffered (raw, unnormalized
      state/action/reward) for the two LLM-driven steps below; a rollout's
      unfinished trailing episode is dropped from these buffers

  LLM Trajectory Analyzer + unlikelihood update (every `analyzer_every`
  completed episodes, hyperparam, default 5)
    → reads the latest summary.md as system context
    → sends that batch of full episode trajectories to GPT-4o mini
    → receives top `analyzer_topk` (default 2) bad (state, action) pairs
      PER episode
    → runs ONE separate gradient step on the actor only (its own optimizer,
      its own lr) minimizing -log(1 - π(bad_action|bad_state)) averaged
      over all flagged pairs in the batch — this is interleaved with, not
      fused into, the PPO update above

  AI Agent summary refresh (every `summary_every` completed episodes,
  hyperparam, default 10)
    → takes the most recent `summary_n_traj` (default 2) episodes of that
      window
    → sends them + the current summary to GPT-4o mini to produce an updated
      10-point summary → overwrites summary.md
    → there is no separate, continuously-running AI Agent environment
      during training — the AI Agent and the LLM Trajectory Analyzer both
      consume the SAME trajectories the PPO agent already collected
```

---

## Module 1: AI Agent (`ai_agent.py`)

### Role
The AI agent's purpose is to build a semantic understanding of the LunarLander environment — how physics work, what actions do, and what patterns lead to success or failure. This understanding is distilled into a 10-point summary that grounds the LLM Trajectory Analyzer's reasoning.

### Action Mechanism: Chunking
The AI agent uses GPT-4o mini to select actions. Rather than calling the LLM at every step (which would cost ~500 API calls per episode), it uses **action chunking**: the current state is sent to GPT-4o mini, which returns the next 20 actions at once. This reduces API calls to ~25 per episode while preserving the agent's genuine decision-making nature.

- Chunk size: **20 steps per API call**
- State is passed as a **raw numerical array** — no text conversion
- The system prompt defines what each state index means once, so every call stays minimal

### State Format
```
[x_pos, y_pos, x_vel, y_vel, angle, ang_vel, left_leg_contact, right_leg_contact]
```
- x_pos: horizontal position (negative = left of pad, positive = right)
- y_pos: height above ground (starts ~1.4)
- x_vel: horizontal velocity
- y_vel: vertical velocity (negative = falling)
- angle: tilt in radians (0 = upright)
- ang_vel: angular velocity
- left_leg_contact, right_leg_contact: 1.0 if touching ground, else 0.0

### Actions
- 0 = Do nothing
- 1 = Fire left orientation engine
- 2 = Fire main engine (upward thrust)
- 3 = Fire right orientation engine

### Summary Generation and Updates
After every `summary_update_every` episodes, the agent generates or updates the 10-point summary:
- **Initial summary**: generated from the first batch of episodes
- **Subsequent updates**: the previous summary is passed as context alongside new trajectory data, so insights accumulate rather than restart
- The summary is always written to `summary.md` after each update

### Trajectory Format for Summary
Full trajectories are passed (no sampling), in compact format:
```
step | state                     | action | reward
   0 | [0.12, 1.4, ...]          |   2    | -0.234
   1 | [0.11, 1.38, ...]         |   2    | -0.198
...
```

### Warm Start
Before PPO training begins, the AI agent runs **5 episodes** to build an initial summary. This ensures the LLM Trajectory Analyzer has meaningful environment context from episode 1 of training.

### Logging
Every API call the AI Agent makes — action chunks during warm start, plus summary generation/updates whether triggered during warm start or during PPO training (`ppo_llm.py`'s `update_summary_from_episodes` also writes here) — is logged to `logs/interaction_log.md` with full prompt and response, timestamped. The LLM Trajectory Analyzer logs separately (see Module 3).

---

## Module 2: PPO Agent (`ppo.py` baseline / `ppo_llm.py` LLM-integrated)

### Algorithm
PPO (clipped surrogate objective) with Generalized Advantage Estimation (GAE), replacing an earlier REINFORCE-with-baseline design.

This project originally used REINFORCE + full-episode Monte Carlo returns (no bootstrapping) specifically because that aligns cleanly with the LLM seeing complete episodes. Switching to PPO trades that clean alignment for faster, more stable training (PPO reuses each rollout for multiple epochs, and the clipped objective tolerates larger updates without collapsing). The cost: PPO collects a fixed-size **step** buffer rather than a fixed number of **episodes**, so rollouts now routinely end mid-episode. The LLM Trajectory Analyzer and AI Agent summarizer need complete episodes, so `ppo_llm.py` buffers completed episodes separately and drops any rollout's unfinished trailing episode before handing data to either of them.

### Actor Network
```
Input:  8   (state dim)
Hidden: 128 (Tanh)
Hidden: 128 (Tanh)
Output: 4   (action logits → softmax via Categorical)
```
Orthogonal weight init (gain √2 on hidden layers, gain 0.01 on the output layer so the initial policy starts close to uniform).

### Baseline (Value) Network
```
Input:  8   (state dim)
Hidden: 128 (Tanh)
Hidden: 128 (Tanh)
Output: 1   (estimated state value V(s))
```
Actor and baseline share a single Adam optimizer (one learning rate, annealed linearly across training) — there is no separate baseline learning rate.

### PPO Loss
```
advantage  At, return Gt = GAE(rewards, V(s), gamma, gae_lambda)   # bootstraps V(s) at episode/rollout cutoffs
ratio      = exp(log π_new(at|st) - log π_old(at|st))
policy_loss  = -min(ratio * At, clip(ratio, 1-eps, 1+eps) * At)
value_loss   = max(SmoothL1(V(st), Gt), SmoothL1(V_clipped(st), Gt))
loss = policy_loss + value_coef * value_loss - entropy_coef * entropy
```
Run for `n_epochs` minibatch passes over each `n_steps`-sized rollout. Advantages are normalized (zero mean, unit std) once per rollout before the epochs begin. Entropy bonus maintains exploration.

### Unlikelihood Update (LLM-driven bad-action suppression)
Once the LLM Trajectory Analyzer flags `(bad_state, bad_action)` pairs, **`ppo_llm.py` only** (not the baseline) runs one additional, separate gradient step on the actor:
```
p_bad = π(bad_action | bad_state)     # bad_state normalized with the SAME running normalizer the actor was trained on
loss  = -log(1 - clamp(p_bad, max=0.999))   averaged over all flagged pairs in the batch
```
This is deliberately **not** the originally-planned `mean(π(bad|s))` term fused into the PPO loss with a coefficient λ. Two design changes made during integration:
1. **Loss shape**: `-log(1-p)` (unlikelihood loss) instead of raw `mean(p)`. Gradient is self-limiting — large when p is near 1 (urgent), vanishing as p→0 (job done) — versus a flat, constant-magnitude gradient for raw probability minimization.
2. **Separate optimizer step, no λ**: rather than tuning a coefficient to balance two competing loss terms in one backward pass, the unlikelihood update runs as its own Adam step (own lr: `unlikelihood_lr`) on its own cadence, interleaved with — not fused into — the PPO update. This sidesteps λ-tuning, at the cost of having no trust-region protection (PPO's clipping only protects PPO's own update).

The core mechanism is unchanged from the original design: the actor is π(a|s); feed `bad_state` through it, index into `bad_action`, minimize that probability. This stays **state-conditioned** — softmax normalization automatically redistributes the suppressed probability mass to the other actions, so nearby/unrelated states are only affected via ordinary neural-net generalization, not by direct construction of a target distribution.

### Hyperparameters (`ppo_llm.py`, all CLI flags)
- Gamma (discount): 0.99, GAE lambda: 0.95
- Learning rate: 3e-4 (linearly annealed to 0), shared by actor+baseline
- Clip epsilon: 0.2, entropy coefficient: 0.01, value coefficient: 0.5
- Gradient clipping: max norm 0.5 (both PPO and unlikelihood updates)
- Rollout size: `n_steps`=2048, `n_epochs`=4, `batch_size`=64
- `analyzer_every`=5, `analyzer_topk`=2 — LLM Trajectory Analyzer cadence/yield
- `unlikelihood_lr`=1e-4 — separate actor-only optimizer for the unlikelihood step
- `summary_every`=10, `summary_n_traj`=2 — AI Agent summary-refresh cadence
- `llm_model`="gpt-4o-mini" — single model used everywhere (warm start, analyzer, summarizer)
- `api_key` — resolved the same way in `ai_agent.py` and `ppo_llm.py`: `--api-key` CLI flag, else `OPENAI_API_KEY` env var
- `seed`=1 (`seeding.py`'s `DEFAULT_SEED`) — same default across `ai_agent.py`, `ppo.py`, `ppo_llm.py`; seeds Python `random`, NumPy, PyTorch (CPU+CUDA, deterministic cuDNN), the Gymnasium env's `reset(seed=...)`, and is passed as OpenAI's best-effort `seed` parameter on every API call. Makes a run reproducible across machines/GPUs, not just re-runs on one machine (exact bit-for-bit equality across different GPU hardware still isn't 100% guaranteed by PyTorch, and the LLM-side `seed` is best-effort only — but everything local is exactly reproducible)

### Convergence Tracking
- Episode rewards logged each episode
- Running mean over last 100 episodes tracked
- Plot saved every `plot_every` episodes (raw rewards + running mean + solved threshold at 200) — `logs/rewards.png` for the baseline, `logs/rewards_llm.png` for the LLM-integrated run
- Best model saved whenever a new best mean-100 is achieved — `actor_best.pt` (baseline) vs `actor_best_llm.pt` (LLM-integrated), kept separate so the two can be compared
- Training stops early if mean-100 ≥ 200 (environment considered solved)

---

## Module 3: LLM Trajectory Analyzer (`llm_trajectory_analyzer.py`)

### Role
Every `analyzer_every` completed PPO episodes (default 5), the LLM Trajectory Analyzer receives that batch of full trajectories and identifies the **top `analyzer_topk` bad (state, action) pairs** (default 2) per trajectory. These pairs feed the unlikelihood update described in Module 2.

### Definition of "Bad Action"
A bad action is not simply the step with the lowest immediate reward. It is the action that:
- Caused the most **trajectory divergence** (pushed the lander away from a recoverable path)
- Had the greatest **negative impact on reaching the goal** (landing safely on the pad)

This holistic judgment requires reasoning about the full trajectory arc, which is why an LLM is well-suited for it and why full trajectories (not samples) are passed.

### Context: summary.md
The current 10-point environment summary is read from `summary.md` and placed in the system prompt. This gives the LLM the grounding to reason about *why* an action was bad — e.g., "firing the main engine while angle was high worsened angular momentum and made recovery impossible."

The LLM always reads the **latest version** of `summary.md`, so as the AI agent updates the summary during training, the analyzer's reasoning automatically improves.

### Input Format
Each trajectory is passed as:
```
Episode N | Total Return: -412.3 | Steps: 98
step | state                                      | action | reward
   0 | [0.08, 1.41, 0.02, -0.12, 0.01, 0.0, 0, 0] |   0   | 1.234
   1 | ...
```

### Output Format
Structured JSON, one entry per episode in the batch, each carrying its own top-K bad actions:
```json
{
  "episodes": [
    {
      "episode_index": 0,
      "bad_actions": [
        {"step": 14, "state": [...], "action": 2, "reason": "..."},
        {"step": 47, "state": [...], "action": 1, "reason": "..."}
      ]
    }
  ]
}
```
`episode_index` lines up positionally with the order episodes were sent in. Pairs that fail to parse (missing/malformed state or an out-of-range action) are dropped rather than crashing the run; if the whole API call fails, that round's analysis is skipped and the unlikelihood update is simply not run that cycle.

### Batching
All `analyzer_every` episodes are sent in a single GPT-4o mini call (one call analyzes the whole batch and returns bad actions for every episode in it). Logged to its own `logs/analyzer_log.md` — kept separate from the AI Agent's `logs/interaction_log.md` so the two roles' logs are never interleaved.

---

## Data Flow Summary

```
summary.md
    ↑ written by AI Agent (warm start, then every summary_every episodes during training)
    ↓ read by LLM Trajectory Analyzer before each batch analysis

Episode trajectory (state, action, reward per step)
    → produced by the PPO Agent's own rollout collection (collect_rollout)
    → buffered, then sent to the LLM Trajectory Analyzer (every analyzer_every episodes)
    → ALSO buffered and sent to the AI Agent for summary updates (every summary_every episodes)
    → there is no separate trajectory source — both LLM consumers read the
      exact same completed episodes the PPO agent already collected

(bad_state, bad_action) pairs
    → produced by the LLM Trajectory Analyzer
    → consumed by ppo_llm.py's separate unlikelihood update (actor only)

actor_best.pt / actor_best_llm.pt
    → saved whenever a new best mean-100 reward is achieved (baseline vs LLM-integrated, kept separate)
```

---

## File Structure

```
llm_rl_project/
├── ai_agent.py                # AI Agent: action chunking, summary generation + updates
├── ppo.py                     # PPO baseline: actor, baseline, training loop — NO LLM involvement, kept for comparison
├── ppo_llm.py                 # PPO + LLM Trajectory Analyzer + AI Agent integration
├── llm_trajectory_analyzer.py # LLM Trajectory Analyzer: batch episode analysis -> top-K bad (state,action) pairs
├── seeding.py                  # set_global_seed(): shared reproducibility helper used by all three runnable scripts
├── summary.md                 # Living 10-point environment summary (auto-updated)
├── actor_best.pt               # Best baseline (ppo.py) actor checkpoint
├── actor_best_llm.pt           # Best LLM-integrated (ppo_llm.py) actor checkpoint
├── PROJECT.md                  # This file
└── logs/
    ├── interaction_log.md     # AI Agent API prompts/responses: warm start action chunks + all summary generation/updates
    ├── analyzer_log.md        # LLM Trajectory Analyzer API prompts/responses
    ├── rewards.png            # ppo.py baseline training reward curve
    └── rewards_llm.png        # ppo_llm.py training reward curve
```

---

## Key Design Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| RL algorithm | PPO + GAE (was REINFORCE + MC baseline) | Faster, more stable training; trade-off is a step-buffer/episode-buffer mismatch the LLM modules now need bridging (see Module 2) |
| Baseline kept | `ppo.py` left untouched, `ppo_llm.py` is a separate copy | Lets the LLM-integrated run be compared against a clean PPO baseline |
| Action chunking size | 20 steps | Balances LLM decision quality vs API cost |
| State representation | Raw numerical array | Consistent format across all modules; LLM handles numbers directly |
| Bad action definition | Trajectory divergence / goal prevention | More meaningful than lowest immediate reward |
| Bad action penalty | Unlikelihood loss `-log(1-π(bad_action\|bad_state))`, separate actor-only optimizer step (was: `mean(π(bad\|s))` fused into actor loss with λ) | Self-limiting gradient (strong when p is high, vanishes as p→0); avoids tuning a λ to balance two competing loss terms in one backward pass |
| Trajectory source for LLM modules | Reuse the PPO agent's own collected episodes (was: a separate, continuously-running AI Agent environment) | One source of truth, no redundant live agent/API usage during training |
| Analyzer/summarizer scheduling | Interleaved into the single training loop, triggered by completed-episode counters (was: implied background/async) | No real concurrency needed on shared actor weights; only the OpenAI calls are "slow," and they just run inline between rollouts |
| Summary persistence | summary.md file | Shared across modules; human-readable |
| LLM interaction logging | Separate files per role: `logs/interaction_log.md` (AI Agent) vs `logs/analyzer_log.md` (LLM Trajectory Analyzer) | Two different roles/concerns; keeping them apart makes each log readable on its own instead of interleaving unrelated calls |
| Reproducibility | Shared `seeding.py`, default seed = 1 everywhere (`ai_agent.py`, `ppo.py`, `ppo_llm.py`) | One run config should reproduce the same result on any machine/GPU, not just on the one it was first run on; verified bit-identical across independent fresh processes |
| LLM model | GPT-4o mini, passed as a `model`/`llm_model` parameter everywhere (CLI-overridable) | Cost-efficient; never hardcoded, so it's a true hyperparameter consistent across `ai_agent.py` and `ppo_llm.py` |
| API key | `--api-key` CLI flag, else `OPENAI_API_KEY` env var — same resolution in `ai_agent.py` and `ppo_llm.py` | Guarantees warm start and main training use the same key without duplicating logic |
| Summary update strategy | Previous summary + most recent `summary_n_traj` episodes of each `summary_every`-sized window | Knowledge accumulates rather than restarting each time |
| Trajectory format for LLM | Full trajectory, compact (state, action, reward) | Complete picture without doubling tokens with next_state |

---

## Environment: LunarLander-v3

- **State space**: 8 continuous values (position, velocity, angle, leg contacts)
- **Action space**: 4 discrete actions (nothing, left engine, main engine, right engine)
- **Reward**: shaped reward for moving toward pad, penalty for crash (-100), bonus for safe landing (+100 to +140)
- **Solved**: mean reward ≥ 200 over 100 consecutive episodes
- **Max steps**: 500 per episode
