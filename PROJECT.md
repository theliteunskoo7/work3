# LLM-Integrated Reinforcement Learning on LunarLander

## Overview

This project integrates LLM-based AI agents into a reinforcement learning training loop on the LunarLander-v3 (Gymnasium) environment. The core idea is to use language model reasoning to provide a higher-level understanding of the environment and to identify harmful actions during training, which then feeds back into the RL agent's learning signal.

The system has three distinct components that work together:

1. **AI Agent** — explores the environment, builds and maintains a living 10-point summary of environment dynamics
2. **REINFORCE Agent** — the RL agent that learns to land using policy gradient with a baseline
3. **LLM Trajectory Analyzer** — analyzes completed trajectories, identifies the top 2 bad actions per trajectory, which are then used to penalize the actor network

---

## Motivation

Standard RL agents learn purely from numerical reward signals with no semantic understanding of what is happening. This project explores whether injecting LLM-based reasoning into the training loop can:
- Accelerate convergence by penalizing structurally bad decisions
- Provide a richer, interpretable signal beyond just scalar rewards
- Ground the LLM's analysis in actual environment dynamics via the evolving summary

---

## System Architecture

```
WARM START PHASE
─────────────────────────────────────────────────────────────
  AI Agent (GPT-4o mini)
    → explores LunarLander with action chunking (20 steps/call)
    → collects full episodes
    → generates initial 10-point summary → saved to summary.md
    → updates summary every 2 episodes (each update builds on prior summary)

TRAINING PHASE (runs concurrently)
─────────────────────────────────────────────────────────────
  REINFORCE Agent
    → collects full episodes (state, action, reward, next_state, done)
    → computes Monte Carlo returns Gt
    → sends trajectory batch to LLM Trajectory Analyzer
    → receives top 2 (bad_state, bad_action) pairs per trajectory
    → computes modified actor loss
    → updates actor and baseline networks

  AI Agent (async)
    → continues exploring environment in parallel
    → updates summary.md periodically with new observations
    → LLM Trajectory Analyzer always reads the latest summary.md

  LLM Trajectory Analyzer (GPT-4o mini)
    → reads current summary from summary.md as system context
    → receives batch of trajectories (state, action, reward per step)
    → identifies top 2 bad (state, action) pairs per trajectory
    → returns structured output: [(state, action_index), (state, action_index)]
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
Before REINFORCE training begins, the AI agent runs **5 episodes** to build an initial summary. This ensures the LLM Trajectory Analyzer has meaningful environment context from episode 1 of training.

### Logging
Every API call (action chunks + summary calls) is logged to `logs/interaction_log.md` with full prompt and response, timestamped.

---

## Module 2: REINFORCE Agent (`reinforce.py`)

### Algorithm
REINFORCE with a learned baseline (value network). Full-episode Monte Carlo returns are used — no bootstrapping.

REINFORCE is chosen because:
- It collects **complete episodes**, which aligns perfectly with LLM trajectory analysis (the LLM sees the full arc of what happened)
- Simpler than actor-critic; no TD error or bootstrapping complexity
- The LLM's "bad action" judgment of "action that prevented reaching the goal" maps naturally to full-episode reasoning

### Actor Network
```
Input:  8  (state dim)
Hidden: 256 (ReLU)
Hidden: 256 (ReLU)
Output: 4  (action logits → softmax)
```
The actor outputs a probability distribution over the 4 discrete actions given the current state.

### Baseline (Value) Network
```
Input:  8  (state dim)
Hidden: 256 (ReLU)
Hidden: 256 (ReLU)
Output: 1  (estimated state value V(s))
```
The baseline reduces variance in the policy gradient update without introducing bias.

### Standard REINFORCE Loss
```
returns    Gt = Σ γᵗ rₜ  (Monte Carlo, computed backwards)
advantage  At = Gt - V(st)   (normalized across episode)
actor_loss = -Σ log π(at | st) * At
baseline_loss = MSE(V(st), Gt)
```

Advantage normalization (zero mean, unit std) stabilizes training. An entropy bonus (coefficient 0.01) is added to the actor loss to maintain exploration and prevent premature convergence.

### Modified Actor Loss (with LLM penalty)
Once the LLM Trajectory Analyzer is integrated:
```
bad_penalty = mean(π(bad_action | bad_state))   for each (bad_state, bad_action) from LLM
total_actor_loss = actor_loss + λ * bad_penalty
```

The key insight: the actor network is the function π(a|s). To penalize a specific (state, action) pair:
1. Feed `bad_state` through the actor → get full probability distribution
2. Index into it at `bad_action` → get π(bad_action | bad_state)
3. Minimize this probability

This is naturally **state-conditioned** — the same action is only penalized in the specific state where the LLM identified it as harmful. Different states produce different distributions, so the penalty is automatically localized.

### Hyperparameters
- Gamma (discount): 0.99
- Actor learning rate: 3e-4
- Baseline learning rate: 1e-3
- Entropy coefficient: 0.01
- Gradient clipping: max norm 0.5
- LLM penalty coefficient λ: to be tuned during integration

### Convergence Tracking
- Episode rewards logged each episode
- Running mean over last 100 episodes tracked
- Plot saved to `logs/rewards.png` every 100 episodes (raw rewards + running mean + solved threshold at 200)
- Best model saved to `actor_best.pt` whenever a new best mean-100 is achieved
- Training stops early if mean-100 ≥ 200 (environment considered solved)

---

## Module 3: LLM Trajectory Analyzer

### Role
After each batch of REINFORCE episodes, the LLM Trajectory Analyzer receives the full trajectory data and identifies the **top 2 bad (state, action) pairs** per trajectory. These pairs are fed back into the modified actor loss.

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
Structured JSON identifying the top 2 bad actions:
```json
{
  "bad_actions": [
    {"step": 14, "state": [...], "action": 2, "reason": "..."},
    {"step": 47, "state": [...], "action": 1, "reason": "..."}
  ]
}
```

### Batching
Trajectories are batched before each LLM call to reduce API costs. One GPT-4o mini call analyzes a full batch of episodes and returns bad actions for each.

---

## Data Flow Summary

```
summary.md
    ↑ written by AI Agent after every update
    ↓ read by LLM Trajectory Analyzer before each batch analysis

Episode trajectory (state, action, reward per step)
    → produced by REINFORCE Agent
    → sent to LLM Trajectory Analyzer
    → also sent to AI Agent (async) for summary updates

(bad_state, bad_action) pairs
    → produced by LLM Trajectory Analyzer
    → consumed by REINFORCE Agent modified actor loss

actor_best.pt
    → saved whenever a new best mean-100 reward is achieved
```

---

## File Structure

```
llm_rl_project/
├── ai_agent.py          # AI Agent: action chunking, summary generation + updates
├── reinforce.py         # REINFORCE agent: actor, baseline, training loop
├── summary.md           # Living 10-point environment summary (auto-updated)
├── actor_best.pt        # Best actor network checkpoint
├── PROJECT.md           # This file
└── logs/
    ├── interaction_log.md   # All AI Agent API prompts and responses
    └── rewards.png          # Training reward curve (updated every 100 episodes)
```

---

## Key Design Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| RL algorithm | REINFORCE + baseline | Full episodes align with LLM trajectory analysis |
| Action chunking size | 20 steps | Balances LLM decision quality vs API cost |
| State representation | Raw numerical array | Consistent format across all modules; LLM handles numbers directly |
| Bad action definition | Trajectory divergence / goal prevention | More meaningful than lowest immediate reward |
| Bad action penalty | π(bad_action \| bad_state) minimized | Naturally state-conditioned; same action only penalized in specific context |
| Summary persistence | summary.md file | Shared across modules; async-safe; human-readable |
| LLM model | GPT-4o mini | Cost-efficient; capable enough for numerical reasoning and trajectory analysis |
| Summary update strategy | Previous summary + new trajectories | Knowledge accumulates rather than restarting each time |
| Trajectory format for LLM | Full trajectory, compact (state, action, reward) | Complete picture without doubling tokens with next_state |

---

## Environment: LunarLander-v3

- **State space**: 8 continuous values (position, velocity, angle, leg contacts)
- **Action space**: 4 discrete actions (nothing, left engine, main engine, right engine)
- **Reward**: shaped reward for moving toward pad, penalty for crash (-100), bonus for safe landing (+100 to +140)
- **Solved**: mean reward ≥ 200 over 100 consecutive episodes
- **Max steps**: 500 per episode
