Using device: cuda (rollout collection stays on CPU; batched updates use cuda)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  analyzer_threshold=200  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=unsloth/gemma-4-26B-A4B-it-GGUF
  llm_cutoff_mean=0.0 (analyzer + summary permanently stop once mean(100) first reaches this)

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2982 | mean p(bad) before update=0.2571 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2563 | mean p(bad) before update=0.2259 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    1 | Ep    22 | reward:    -85.4 | mean(100):   -191.1 | actor_loss: -0.0100 | value_loss: 72.8860 | lr: 3.00e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.3003 | mean p(bad) before update=0.2541 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2355 | mean p(bad) before update=0.2095 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    2 | Ep    43 | reward:   -102.8 | mean(100):   -171.1 | actor_loss: -0.0098 | value_loss: 57.4671 | lr: 2.97e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2739 | mean p(bad) before update=0.2343 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1917 | mean p(bad) before update=0.1738 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    3 | Ep    66 | reward:   -185.9 | mean(100):   -152.5 | actor_loss: -0.0044 | value_loss: 46.8841 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3057 | mean p(bad) before update=0.2615 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2414 | mean p(bad) before update=0.2120 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2526 | mean p(bad) before update=0.2199 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    4 | Ep    90 | reward:   -125.3 | mean(100):   -141.7 | actor_loss: -0.0086 | value_loss: 47.2269 | lr: 2.90e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2991 | mean p(bad) before update=0.2584 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2623 | mean p(bad) before update=0.2293 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    5 | Ep   112 | reward:    -79.7 | mean(100):   -127.7 | actor_loss: -0.0089 | value_loss: 41.6255 | lr: 2.86e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2143 | mean p(bad) before update=0.1862 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3408 | mean p(bad) before update=0.2847 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    6 | Ep   134 | reward:    -26.5 | mean(100):   -114.7 | actor_loss: -0.0042 | value_loss: 39.8408 | lr: 2.83e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4377 | mean p(bad) before update=0.3373 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2063 | mean p(bad) before update=0.1861 | ul_lr=1.00e-04 (scale=1.00)
  Update    7 | Ep   155 | reward:    -76.5 | mean(100):   -105.8 | actor_loss: -0.0085 | value_loss: 36.0380 | lr: 2.80e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2610 | mean p(bad) before update=0.2239 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2701 | mean p(bad) before update=0.2344 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   176 | reward:   -101.4 | mean(100):   -104.8 | actor_loss: -0.0078 | value_loss: 40.6520 | lr: 2.77e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2008 | mean p(bad) before update=0.1810 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2277 | mean p(bad) before update=0.1871 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    9 | Ep   195 | reward:    -57.4 | mean(100):   -101.9 | actor_loss: -0.0082 | value_loss: 33.6300 | lr: 2.74e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.1732 | mean p(bad) before update=0.1571 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer failed: Expecting value: line 1 column 1 (char 0)] — skipping unlikelihood update this round
  [Analyzer] 2 episodes -> 0 bad pairs (0 dropped by adv filter, 0 state-echo mismatches, 0 applied)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   10 | Ep   218 | reward:    -81.2 | mean(100):    -97.7 | actor_loss: -0.0109 | value_loss: 27.6594 | lr: 2.71e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3186 | mean p(bad) before update=0.2625 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2538 | mean p(bad) before update=0.2210 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   237 | reward:    -70.1 | mean(100):    -89.4 | actor_loss: -0.0069 | value_loss: 22.5130 | lr: 2.67e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2152 | mean p(bad) before update=0.1929 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3913 | mean p(bad) before update=0.3066 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   258 | reward:   -133.6 | mean(100):    -84.1 | actor_loss: -0.0069 | value_loss: 27.1400 | lr: 2.64e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3605 | mean p(bad) before update=0.2834 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2482 | mean p(bad) before update=0.2158 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   277 | reward:    -49.1 | mean(100):    -71.1 | actor_loss: -0.0087 | value_loss: 20.0412 | lr: 2.61e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2481 | mean p(bad) before update=0.2197 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5520 | mean p(bad) before update=0.3828 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   296 | reward:    -41.8 | mean(100):    -62.9 | actor_loss: -0.0091 | value_loss: 23.1904 | lr: 2.58e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5485 | mean p(bad) before update=0.4022 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3742 | mean p(bad) before update=0.2668 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   315 | reward:    -50.7 | mean(100):    -56.8 | actor_loss: -0.0062 | value_loss: 21.2455 | lr: 2.56e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.5815 | mean p(bad) before update=0.4164 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4593 | mean p(bad) before update=0.3533 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   331 | reward:    -28.3 | mean(100):    -54.2 | actor_loss: -0.0022 | value_loss: 26.6010 | lr: 2.53e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.4857 | mean p(bad) before update=0.3344 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   348 | reward:     -0.2 | mean(100):    -46.0 | actor_loss: -0.0093 | value_loss: 21.0193 | lr: 2.50e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2634 | mean p(bad) before update=0.2132 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.5729 | mean p(bad) before update=0.4079 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   18 | Ep   365 | reward:    -72.1 | mean(100):    -39.1 | actor_loss: -0.0065 | value_loss: 22.5440 | lr: 2.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5235 | mean p(bad) before update=0.3618 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4002 | mean p(bad) before update=0.3200 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   19 | Ep   381 | reward:    -63.5 | mean(100):    -37.4 | actor_loss: -0.0068 | value_loss: 21.7512 | lr: 2.45e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2460 | mean p(bad) before update=0.2052 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   20 | Ep   397 | reward:    -35.0 | mean(100):    -32.8 | actor_loss: -0.0085 | value_loss: 17.5873 | lr: 2.43e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5017 | mean p(bad) before update=0.3922 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   403 | reward:     62.6 | mean(100):    -31.3 | actor_loss: -0.0064 | value_loss: 23.6921 | lr: 2.40e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   22 | Ep   407 | reward:    -15.5 | mean(100):    -30.7 | actor_loss: -0.0061 | value_loss: 13.9795 | lr: 2.40e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2962 | mean p(bad) before update=0.2345 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1795 | mean p(bad) before update=0.1572 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   23 | Ep   422 | reward:     20.9 | mean(100):    -26.8 | actor_loss: -0.0041 | value_loss: 21.1714 | lr: 2.39e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4828 | mean p(bad) before update=0.3480 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   24 | Ep   430 | reward:      1.5 | mean(100):    -24.6 | actor_loss: -0.0062 | value_loss: 14.6247 | lr: 2.37e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4734 | mean p(bad) before update=0.3497 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   25 | Ep   440 | reward:   -138.7 | mean(100):    -25.6 | actor_loss: -0.0068 | value_loss: 19.4113 | lr: 2.35e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   26 | Ep   445 | reward:     35.8 | mean(100):    -26.0 | actor_loss: -0.0069 | value_loss: 17.4084 | lr: 2.34e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   27 | Ep   448 | reward:    103.6 | mean(100):    -23.5 | actor_loss: -0.0042 | value_loss: 13.4679 | lr: 2.33e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3506 | mean p(bad) before update=0.2833 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   28 | Ep   453 | reward:    -39.2 | mean(100):    -22.0 | actor_loss: -0.0057 | value_loss: 13.9584 | lr: 2.33e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   29 | Ep   455 | reward:     42.4 | mean(100):    -20.7 | actor_loss: -0.0055 | value_loss: 8.9738 | lr: 2.32e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3077 | mean p(bad) before update=0.2596 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   30 | Ep   460 | reward:    -26.9 | mean(100):    -20.4 | actor_loss: -0.0063 | value_loss: 14.0651 | lr: 2.32e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   31 | Ep   463 | reward:     84.5 | mean(100):    -19.4 | actor_loss: -0.0064 | value_loss: 10.6079 | lr: 2.31e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   32 | Ep   465 | reward:     13.1 | mean(100):    -17.6 | actor_loss: -0.0066 | value_loss: 8.0396 | lr: 2.31e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   33 | Ep   467 | reward:      9.0 | mean(100):    -16.4 | actor_loss: -0.0079 | value_loss: 7.3201 | lr: 2.30e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   34 | Ep   469 | reward:     25.6 | mean(100):    -14.1 | actor_loss: -0.0052 | value_loss: 8.4096 | lr: 2.30e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.1586 | mean p(bad) before update=0.1464 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   35 | Ep   471 | reward:     17.0 | mean(100):    -12.6 | actor_loss: -0.0095 | value_loss: 7.3446 | lr: 2.30e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   36 | Ep   473 | reward:     60.8 | mean(100):     -9.9 | actor_loss: -0.0053 | value_loss: 7.2105 | lr: 2.29e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   37 | Ep   475 | reward:     94.6 | mean(100):     -7.6 | actor_loss: -0.0086 | value_loss: 4.6077 | lr: 2.29e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   38 | Ep   477 | reward:     83.9 | mean(100):     -5.0 | actor_loss: -0.0050 | value_loss: 5.4587 | lr: 2.29e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2006 | mean p(bad) before update=0.1738 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   39 | Ep   481 | reward:     29.8 | mean(100):     -2.0 | actor_loss: -0.0080 | value_loss: 12.5470 | lr: 2.28e-04
  [LLM] mean(100)=0.4 reached cutoff 0.0 -- permanently disabling the analyzer and summary refresh for the rest of this run.
  Update   40 | Ep   484 | reward:     35.4 | mean(100):      0.4 | actor_loss: -0.0035 | value_loss: 10.0241 | lr: 2.28e-04
  Update   41 | Ep   487 | reward:    -19.4 | mean(100):      2.5 | actor_loss: -0.0043 | value_loss: 11.2426 | lr: 2.27e-04
  Update   42 | Ep   489 | reward:    114.3 | mean(100):      5.5 | actor_loss: -0.0021 | value_loss: 4.7898 | lr: 2.27e-04
  Update   43 | Ep   491 | reward:     18.7 | mean(100):      6.6 | actor_loss: -0.0025 | value_loss: 7.8523 | lr: 2.27e-04
  Update   44 | Ep   493 | reward:    131.5 | mean(100):      9.5 | actor_loss: -0.0041 | value_loss: 5.3692 | lr: 2.26e-04
  Update   45 | Ep   495 | reward:     95.3 | mean(100):     12.5 | actor_loss: -0.0051 | value_loss: 5.0347 | lr: 2.26e-04
  Update   46 | Ep   497 | reward:     82.2 | mean(100):     13.8 | actor_loss: -0.0019 | value_loss: 6.2385 | lr: 2.26e-04
  Update   47 | Ep   499 | reward:    112.6 | mean(100):     18.3 | actor_loss: -0.0049 | value_loss: 5.5019 | lr: 2.25e-04
  Update   48 | Ep   501 | reward:    137.0 | mean(100):     21.4 | actor_loss: -0.0036 | value_loss: 4.6680 | lr: 2.25e-04
  Update   49 | Ep   503 | reward:    115.8 | mean(100):     22.9 | actor_loss: -0.0028 | value_loss: 4.9690 | lr: 2.25e-04
  Update   50 | Ep   505 | reward:   -149.2 | mean(100):     23.4 | actor_loss: -0.0043 | value_loss: 10.6506 | lr: 2.25e-04
  Update   51 | Ep   507 | reward:    101.4 | mean(100):     25.5 | actor_loss: -0.0040 | value_loss: 4.9497 | lr: 2.24e-04
  Update   52 | Ep   509 | reward:    128.1 | mean(100):     29.3 | actor_loss: -0.0050 | value_loss: 4.1605 | lr: 2.24e-04
  Update   53 | Ep   511 | reward:    -67.2 | mean(100):     30.3 | actor_loss: -0.0028 | value_loss: 8.2481 | lr: 2.24e-04
  Update   54 | Ep   513 | reward:     36.2 | mean(100):     30.4 | actor_loss: -0.0021 | value_loss: 6.3961 | lr: 2.23e-04
  Update   55 | Ep   515 | reward:   -101.4 | mean(100):     29.7 | actor_loss: -0.0046 | value_loss: 7.9885 | lr: 2.23e-04
  Update   56 | Ep   517 | reward:     26.0 | mean(100):     29.5 | actor_loss: -0.0021 | value_loss: 4.8359 | lr: 2.23e-04
  Update   57 | Ep   519 | reward:     67.6 | mean(100):     31.1 | actor_loss: -0.0047 | value_loss: 8.4077 | lr: 2.22e-04
  Update   58 | Ep   521 | reward:    -78.4 | mean(100):     33.3 | actor_loss: -0.0073 | value_loss: 10.4515 | lr: 2.22e-04
  Update   59 | Ep   523 | reward:    220.2 | mean(100):     36.8 | actor_loss: -0.0032 | value_loss: 11.1461 | lr: 2.22e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  Update   60 | Ep   526 | reward:    254.8 | mean(100):     42.7 | actor_loss: -0.0034 | value_loss: 15.8202 | lr: 2.22e-04
  Update   61 | Ep   529 | reward:    163.8 | mean(100):     49.3 | actor_loss: -0.0017 | value_loss: 14.7722 | lr: 2.21e-04
  Update   62 | Ep   532 | reward:    203.8 | mean(100):     53.7 | actor_loss: -0.0039 | value_loss: 9.7750 | lr: 2.21e-04
  Update   63 | Ep   535 | reward:    -75.1 | mean(100):     54.4 | actor_loss: -0.0059 | value_loss: 17.2331 | lr: 2.20e-04
  Update   64 | Ep   539 | reward:    268.8 | mean(100):     64.3 | actor_loss: -0.0021 | value_loss: 17.3018 | lr: 2.20e-04
  Update   65 | Ep   542 | reward:    233.9 | mean(100):     72.8 | actor_loss: -0.0036 | value_loss: 14.9311 | lr: 2.19e-04
  Update   66 | Ep   546 | reward:    268.3 | mean(100):     80.1 | actor_loss: -0.0032 | value_loss: 15.2990 | lr: 2.19e-04
  Update   67 | Ep   550 | reward:    209.1 | mean(100):     87.7 | actor_loss: -0.0024 | value_loss: 17.9285 | lr: 2.18e-04
  Update   68 | Ep   554 | reward:    186.4 | mean(100):     94.1 | actor_loss: -0.0015 | value_loss: 16.2183 | lr: 2.17e-04
  Update   69 | Ep   559 | reward:    -97.0 | mean(100):    100.5 | actor_loss: -0.0033 | value_loss: 18.5561 | lr: 2.17e-04
  Update   70 | Ep   562 | reward:    234.8 | mean(100):    107.1 | actor_loss: -0.0034 | value_loss: 16.2424 | lr: 2.16e-04
  Update   71 | Ep   566 | reward:    228.2 | mean(100):    113.9 | actor_loss: -0.0019 | value_loss: 18.8686 | lr: 2.16e-04
  Update   72 | Ep   570 | reward:    215.7 | mean(100):    122.5 | actor_loss: -0.0032 | value_loss: 19.3139 | lr: 2.15e-04
  Update   73 | Ep   575 | reward:    254.3 | mean(100):    128.8 | actor_loss: -0.0002 | value_loss: 18.5343 | lr: 2.15e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  Update   74 | Ep   580 | reward:    210.9 | mean(100):    137.4 | actor_loss: -0.0010 | value_loss: 19.5589 | lr: 2.14e-04
  Update   75 | Ep   584 | reward:    252.5 | mean(100):    144.1 | actor_loss: -0.0031 | value_loss: 17.2586 | lr: 2.13e-04
  Update   76 | Ep   587 | reward:    193.7 | mean(100):    149.7 | actor_loss: -0.0015 | value_loss: 14.3597 | lr: 2.12e-04
  Update   77 | Ep   592 | reward:    256.9 | mean(100):    157.8 | actor_loss: -0.0018 | value_loss: 20.4798 | lr: 2.12e-04
  Update   78 | Ep   596 | reward:    194.8 | mean(100):    162.5 | actor_loss: -0.0050 | value_loss: 17.2484 | lr: 2.11e-04
  Update   79 | Ep   600 | reward:    225.8 | mean(100):    167.8 | actor_loss: -0.0026 | value_loss: 15.6129 | lr: 2.11e-04
  Update   80 | Ep   605 | reward:    195.6 | mean(100):    174.8 | actor_loss: -0.0026 | value_loss: 19.4265 | lr: 2.10e-04
  Update   81 | Ep   609 | reward:    273.0 | mean(100):    180.0 | actor_loss: -0.0013 | value_loss: 20.1927 | lr: 2.09e-04
  Update   82 | Ep   614 | reward:    255.1 | mean(100):    192.6 | actor_loss: -0.0025 | value_loss: 20.8749 | lr: 2.09e-04
  Update   83 | Ep   619 | reward:      2.3 | mean(100):    202.6 | actor_loss: -0.0021 | value_loss: 19.5116 | lr: 2.08e-04

Solved at episode 619 (update 83) with mean 202.6!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
