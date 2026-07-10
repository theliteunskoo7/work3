Using device: cuda (rollout collection stays on CPU; batched updates use cuda)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  analyzer_threshold=200  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=unsloth/gemma-4-26B-A4B-it-GGUF
  llm_cutoff_mean=0.0 (analyzer + summary permanently stop once mean(100) first reaches this)

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.3115 | mean p(bad) before update=0.2669 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2836 | mean p(bad) before update=0.2462 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    1 | Ep    22 | reward:   -112.3 | mean(100):   -162.2 | actor_loss: -0.0062 | value_loss: 61.3195 | lr: 3.00e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2158 | mean p(bad) before update=0.1941 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3011 | mean p(bad) before update=0.2591 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    2 | Ep    42 | reward:    -75.1 | mean(100):   -169.5 | actor_loss: -0.0080 | value_loss: 61.4513 | lr: 2.97e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1870 | mean p(bad) before update=0.1703 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3328 | mean p(bad) before update=0.2806 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    3 | Ep    64 | reward:    -72.1 | mean(100):   -157.5 | actor_loss: -0.0076 | value_loss: 51.7527 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2731 | mean p(bad) before update=0.2314 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4167 | mean p(bad) before update=0.3329 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    4 | Ep    86 | reward:   -151.4 | mean(100):   -150.4 | actor_loss: -0.0085 | value_loss: 51.2501 | lr: 2.90e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2862 | mean p(bad) before update=0.2343 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2392 | mean p(bad) before update=0.2081 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    5 | Ep   109 | reward:      7.0 | mean(100):   -138.5 | actor_loss: -0.0099 | value_loss: 46.5349 | lr: 2.87e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5688 | mean p(bad) before update=0.4327 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2796 | mean p(bad) before update=0.2275 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2071 | mean p(bad) before update=0.1825 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    6 | Ep   132 | reward:    -69.7 | mean(100):   -123.3 | actor_loss: -0.0056 | value_loss: 40.1129 | lr: 2.84e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.4708 | mean p(bad) before update=0.3682 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3511 | mean p(bad) before update=0.2937 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    7 | Ep   153 | reward:    -77.1 | mean(100):   -105.9 | actor_loss: -0.0083 | value_loss: 31.2801 | lr: 2.80e-04
  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2007 | mean p(bad) before update=0.1792 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2594 | mean p(bad) before update=0.2230 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   175 | reward:   -156.3 | mean(100):    -95.3 | actor_loss: -0.0052 | value_loss: 29.2028 | lr: 2.77e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5784 | mean p(bad) before update=0.4101 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4683 | mean p(bad) before update=0.3700 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    9 | Ep   198 | reward:    -72.8 | mean(100):    -79.9 | actor_loss: -0.0052 | value_loss: 25.0583 | lr: 2.74e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2710 | mean p(bad) before update=0.2130 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.6784 | mean p(bad) before update=0.4779 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4721 | mean p(bad) before update=0.3630 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   10 | Ep   220 | reward:    -76.0 | mean(100):    -78.1 | actor_loss: -0.0088 | value_loss: 28.7056 | lr: 2.70e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.6144 | mean p(bad) before update=0.4460 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2799 | mean p(bad) before update=0.2352 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   242 | reward:    -52.3 | mean(100):    -70.5 | actor_loss: -0.0048 | value_loss: 23.7587 | lr: 2.67e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5252 | mean p(bad) before update=0.3922 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4168 | mean p(bad) before update=0.3238 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   264 | reward:    -58.2 | mean(100):    -69.0 | actor_loss: -0.0095 | value_loss: 26.1765 | lr: 2.64e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.4856 | mean p(bad) before update=0.3692 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3837 | mean p(bad) before update=0.2996 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   286 | reward:    -55.7 | mean(100):    -67.5 | actor_loss: -0.0074 | value_loss: 23.7663 | lr: 2.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.3023 | mean p(bad) before update=0.2507 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1252 | mean p(bad) before update=0.1163 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   309 | reward:    -37.5 | mean(100):    -64.8 | actor_loss: -0.0062 | value_loss: 24.1595 | lr: 2.57e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2904 | mean p(bad) before update=0.2447 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.3217 | mean p(bad) before update=0.2717 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.4609 | mean p(bad) before update=0.3384 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   332 | reward:    -86.5 | mean(100):    -60.1 | actor_loss: -0.0070 | value_loss: 22.3480 | lr: 2.54e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5722 | mean p(bad) before update=0.4050 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5567 | mean p(bad) before update=0.3530 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   352 | reward:      0.3 | mean(100):    -53.0 | actor_loss: -0.0093 | value_loss: 20.9320 | lr: 2.50e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4848 | mean p(bad) before update=0.3239 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.7758 | mean p(bad) before update=0.5248 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   371 | reward:    -65.1 | mean(100):    -43.8 | actor_loss: -0.0062 | value_loss: 20.4291 | lr: 2.47e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4735 | mean p(bad) before update=0.3738 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   18 | Ep   389 | reward:    -30.1 | mean(100):    -36.8 | actor_loss: -0.0075 | value_loss: 20.2557 | lr: 2.44e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2398 | mean p(bad) before update=0.1877 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4810 | mean p(bad) before update=0.3671 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   19 | Ep   408 | reward:     15.5 | mean(100):    -30.4 | actor_loss: -0.0092 | value_loss: 20.6773 | lr: 2.42e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3849 | mean p(bad) before update=0.3029 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 4 state-echo mismatches) | unlikelihood_loss=0.3583 | mean p(bad) before update=0.2971 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   20 | Ep   426 | reward:     21.8 | mean(100):    -24.3 | actor_loss: -0.0077 | value_loss: 18.5623 | lr: 2.39e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5253 | mean p(bad) before update=0.3966 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2276 | mean p(bad) before update=0.2012 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   445 | reward:     36.8 | mean(100):    -19.9 | actor_loss: -0.0055 | value_loss: 19.1420 | lr: 2.36e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2394 | mean p(bad) before update=0.1867 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.3994 | mean p(bad) before update=0.2909 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   22 | Ep   464 | reward:    -43.5 | mean(100):    -17.6 | actor_loss: -0.0066 | value_loss: 16.7930 | lr: 2.33e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3074 | mean p(bad) before update=0.2569 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   23 | Ep   477 | reward:      1.3 | mean(100):    -17.1 | actor_loss: -0.0069 | value_loss: 17.9038 | lr: 2.30e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4660 | mean p(bad) before update=0.3575 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   24 | Ep   488 | reward:    -27.2 | mean(100):    -16.0 | actor_loss: -0.0038 | value_loss: 16.2311 | lr: 2.28e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3299 | mean p(bad) before update=0.2671 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5346 | mean p(bad) before update=0.4021 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   25 | Ep   506 | reward:    -34.1 | mean(100):    -12.0 | actor_loss: -0.0067 | value_loss: 17.9358 | lr: 2.27e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5820 | mean p(bad) before update=0.4296 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   26 | Ep   518 | reward:      9.3 | mean(100):    -11.4 | actor_loss: -0.0049 | value_loss: 17.4191 | lr: 2.24e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2185 | mean p(bad) before update=0.1917 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   27 | Ep   527 | reward:     -9.9 | mean(100):     -6.8 | actor_loss: -0.0068 | value_loss: 14.7963 | lr: 2.22e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1988 | mean p(bad) before update=0.1778 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   28 | Ep   537 | reward:    -15.8 | mean(100):     -4.0 | actor_loss: -0.0052 | value_loss: 13.3614 | lr: 2.21e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3712 | mean p(bad) before update=0.3074 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.2772 | mean p(bad) before update=0.2383 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   29 | Ep   552 | reward:     13.6 | mean(100):     -2.2 | actor_loss: -0.0085 | value_loss: 19.1044 | lr: 2.19e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   30 | Ep   559 | reward:      8.7 | mean(100):     -3.8 | actor_loss: -0.0045 | value_loss: 19.8964 | lr: 2.17e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2981 | mean p(bad) before update=0.2495 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   31 | Ep   564 | reward:    117.9 | mean(100):     -4.3 | actor_loss: -0.0044 | value_loss: 17.8601 | lr: 2.16e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4194 | mean p(bad) before update=0.3409 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   32 | Ep   570 | reward:      3.3 | mean(100):     -2.5 | actor_loss: -0.0034 | value_loss: 13.2961 | lr: 2.15e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   33 | Ep   573 | reward:     69.1 | mean(100):     -0.3 | actor_loss: -0.0055 | value_loss: 9.5921 | lr: 2.15e-04

  [LLM] mean(100)=1.3 reached cutoff 0.0 -- permanently disabling the analyzer and summary refresh for the rest of this run.
  Update   34 | Ep   578 | reward:      0.8 | mean(100):      1.3 | actor_loss: -0.0048 | value_loss: 13.1995 | lr: 2.14e-04
  Update   35 | Ep   587 | reward:     18.6 | mean(100):      3.9 | actor_loss: -0.0069 | value_loss: 11.1047 | lr: 2.13e-04
  Update   36 | Ep   593 | reward:     11.2 | mean(100):      6.4 | actor_loss: -0.0053 | value_loss: 14.0381 | lr: 2.12e-04
  Update   37 | Ep   599 | reward:    -31.2 | mean(100):      6.2 | actor_loss: -0.0027 | value_loss: 14.6165 | lr: 2.11e-04
  Update   38 | Ep   602 | reward:     51.2 | mean(100):      7.3 | actor_loss: -0.0020 | value_loss: 12.0113 | lr: 2.10e-04
  Update   39 | Ep   604 | reward:     60.8 | mean(100):      9.6 | actor_loss: -0.0030 | value_loss: 7.8985 | lr: 2.10e-04
  Update   40 | Ep   608 | reward:    -39.2 | mean(100):     11.1 | actor_loss: -0.0048 | value_loss: 11.8284 | lr: 2.09e-04
  Update   41 | Ep   610 | reward:    122.1 | mean(100):     13.4 | actor_loss: -0.0067 | value_loss: 6.6268 | lr: 2.09e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update   42 | Ep   612 | reward:     71.8 | mean(100):     15.7 | actor_loss: -0.0034 | value_loss: 6.3436 | lr: 2.08e-04
  Update   43 | Ep   614 | reward:    158.3 | mean(100):     18.0 | actor_loss: -0.0047 | value_loss: 6.5436 | lr: 2.08e-04
  Update   44 | Ep   616 | reward:    167.6 | mean(100):     20.4 | actor_loss: -0.0035 | value_loss: 5.5661 | lr: 2.08e-04
  Update   45 | Ep   618 | reward:    140.3 | mean(100):     21.9 | actor_loss: -0.0095 | value_loss: 8.0614 | lr: 2.08e-04
  Update   46 | Ep   620 | reward:     83.9 | mean(100):     22.7 | actor_loss: -0.0027 | value_loss: 5.0578 | lr: 2.07e-04
  Update   47 | Ep   622 | reward:    -40.6 | mean(100):     23.5 | actor_loss: -0.0023 | value_loss: 7.7463 | lr: 2.07e-04
  Update   48 | Ep   624 | reward:     86.0 | mean(100):     25.8 | actor_loss: -0.0042 | value_loss: 5.5538 | lr: 2.07e-04
  Update   49 | Ep   626 | reward:    132.0 | mean(100):     28.5 | actor_loss: -0.0041 | value_loss: 5.0589 | lr: 2.06e-04
  Update   50 | Ep   628 | reward:    143.3 | mean(100):     31.6 | actor_loss: -0.0047 | value_loss: 7.3754 | lr: 2.06e-04
  Update   51 | Ep   630 | reward:    -40.4 | mean(100):     32.1 | actor_loss: -0.0036 | value_loss: 11.7131 | lr: 2.06e-04
  Update   52 | Ep   632 | reward:     95.6 | mean(100):     34.8 | actor_loss: -0.0050 | value_loss: 5.4409 | lr: 2.06e-04
  Update   53 | Ep   634 | reward:     87.3 | mean(100):     33.9 | actor_loss: -0.0010 | value_loss: 8.5087 | lr: 2.05e-04
  Update   54 | Ep   636 | reward:    124.5 | mean(100):     35.4 | actor_loss: -0.0035 | value_loss: 6.4112 | lr: 2.05e-04
  Update   55 | Ep   638 | reward:    106.6 | mean(100):     37.0 | actor_loss: -0.0051 | value_loss: 6.3118 | lr: 2.05e-04
  Update   56 | Ep   640 | reward:    118.0 | mean(100):     40.1 | actor_loss: -0.0056 | value_loss: 4.8644 | lr: 2.04e-04
  Update   57 | Ep   642 | reward:     -3.6 | mean(100):     42.0 | actor_loss: -0.0045 | value_loss: 7.0868 | lr: 2.04e-04
  Update   58 | Ep   645 | reward:     70.7 | mean(100):     46.1 | actor_loss: -0.0029 | value_loss: 13.9635 | lr: 2.04e-04
  Update   59 | Ep   647 | reward:    105.6 | mean(100):     48.6 | actor_loss: -0.0049 | value_loss: 4.8298 | lr: 2.03e-04
  Update   60 | Ep   649 | reward:    126.8 | mean(100):     49.0 | actor_loss: -0.0049 | value_loss: 7.8205 | lr: 2.03e-04
  Update   61 | Ep   651 | reward:    108.6 | mean(100):     50.6 | actor_loss: 0.0000 | value_loss: 5.1315 | lr: 2.03e-04
  Update   62 | Ep   653 | reward:    128.0 | mean(100):     52.5 | actor_loss: -0.0060 | value_loss: 4.2813 | lr: 2.02e-04
  Update   63 | Ep   656 | reward:     60.4 | mean(100):     57.9 | actor_loss: -0.0021 | value_loss: 10.8101 | lr: 2.02e-04
  Update   64 | Ep   658 | reward:    -97.2 | mean(100):     58.7 | actor_loss: -0.0043 | value_loss: 7.1539 | lr: 2.02e-04
  Update   65 | Ep   660 | reward:     82.7 | mean(100):     60.7 | actor_loss: -0.0038 | value_loss: 4.9749 | lr: 2.01e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update   66 | Ep   662 | reward:     40.0 | mean(100):     64.5 | actor_loss: -0.0037 | value_loss: 7.7187 | lr: 2.01e-04
  Update   67 | Ep   664 | reward:     82.0 | mean(100):     65.6 | actor_loss: -0.0044 | value_loss: 5.2345 | lr: 2.01e-04
  Update   68 | Ep   666 | reward:    144.4 | mean(100):     67.1 | actor_loss: -0.0025 | value_loss: 4.4874 | lr: 2.00e-04
  Update   69 | Ep   668 | reward:    105.2 | mean(100):     68.7 | actor_loss: -0.0036 | value_loss: 3.4342 | lr: 2.00e-04
  Update   70 | Ep   671 | reward:    122.2 | mean(100):     73.6 | actor_loss: -0.0047 | value_loss: 10.4735 | lr: 2.00e-04
  Update   71 | Ep   673 | reward:    131.3 | mean(100):     76.4 | actor_loss: -0.0016 | value_loss: 8.9196 | lr: 1.99e-04
  Update   72 | Ep   675 | reward:    190.9 | mean(100):     77.6 | actor_loss: -0.0007 | value_loss: 12.6838 | lr: 1.99e-04
  Update   73 | Ep   677 | reward:    106.4 | mean(100):     77.9 | actor_loss: -0.0024 | value_loss: 9.5129 | lr: 1.99e-04
  Update   74 | Ep   679 | reward:    151.5 | mean(100):     79.9 | actor_loss: -0.0019 | value_loss: 4.4840 | lr: 1.98e-04
  Update   75 | Ep   681 | reward:    134.8 | mean(100):     82.4 | actor_loss: -0.0020 | value_loss: 4.8402 | lr: 1.98e-04
  Update   76 | Ep   683 | reward:     74.9 | mean(100):     82.5 | actor_loss: -0.0031 | value_loss: 7.1602 | lr: 1.98e-04
  Update   77 | Ep   685 | reward:    118.0 | mean(100):     83.5 | actor_loss: -0.0058 | value_loss: 4.4730 | lr: 1.98e-04
  Update   78 | Ep   687 | reward:    126.0 | mean(100):     85.9 | actor_loss: -0.0031 | value_loss: 4.7288 | lr: 1.97e-04
  Update   79 | Ep   689 | reward:    130.5 | mean(100):     82.8 | actor_loss: -0.0048 | value_loss: 12.5489 | lr: 1.97e-04
  Update   80 | Ep   691 | reward:     99.9 | mean(100):     85.2 | actor_loss: -0.0043 | value_loss: 5.6255 | lr: 1.97e-04
  Update   81 | Ep   693 | reward:    125.2 | mean(100):     87.5 | actor_loss: -0.0039 | value_loss: 3.0037 | lr: 1.96e-04
  Update   82 | Ep   695 | reward:    134.4 | mean(100):     88.7 | actor_loss: -0.0043 | value_loss: 3.5433 | lr: 1.96e-04
  Update   83 | Ep   697 | reward:    144.6 | mean(100):     93.0 | actor_loss: -0.0069 | value_loss: 9.5155 | lr: 1.96e-04
  Update   84 | Ep   699 | reward:    121.9 | mean(100):     95.3 | actor_loss: -0.0049 | value_loss: 2.7934 | lr: 1.95e-04
  Update   85 | Ep   701 | reward:    109.7 | mean(100):     97.1 | actor_loss: -0.0013 | value_loss: 3.4996 | lr: 1.95e-04
  Update   86 | Ep   703 | reward:    113.2 | mean(100):     97.7 | actor_loss: -0.0056 | value_loss: 3.4286 | lr: 1.95e-04
  Update   87 | Ep   705 | reward:     92.2 | mean(100):     98.5 | actor_loss: -0.0051 | value_loss: 4.3904 | lr: 1.95e-04
  Update   88 | Ep   707 | reward:    123.3 | mean(100):     99.9 | actor_loss: -0.0034 | value_loss: 2.8136 | lr: 1.94e-04
  Update   89 | Ep   709 | reward:     22.0 | mean(100):    100.7 | actor_loss: -0.0014 | value_loss: 5.7298 | lr: 1.94e-04
  Update   90 | Ep   711 | reward:    111.9 | mean(100):    101.3 | actor_loss: -0.0040 | value_loss: 6.4408 | lr: 1.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update   91 | Ep   713 | reward:    132.5 | mean(100):    102.2 | actor_loss: -0.0021 | value_loss: 3.4886 | lr: 1.93e-04
  Update   92 | Ep   715 | reward:     84.1 | mean(100):    101.0 | actor_loss: -0.0035 | value_loss: 6.0235 | lr: 1.93e-04
  Update   93 | Ep   717 | reward:     76.8 | mean(100):     99.7 | actor_loss: -0.0017 | value_loss: 7.2305 | lr: 1.93e-04
  Update   94 | Ep   719 | reward:    124.9 | mean(100):     99.2 | actor_loss: -0.0047 | value_loss: 2.8688 | lr: 1.92e-04
  Update   95 | Ep   721 | reward:    122.8 | mean(100):     99.6 | actor_loss: -0.0005 | value_loss: 2.7290 | lr: 1.92e-04
  Update   96 | Ep   723 | reward:    123.6 | mean(100):    100.8 | actor_loss: -0.0011 | value_loss: 2.9491 | lr: 1.92e-04
  Update   97 | Ep   725 | reward:     17.0 | mean(100):    100.1 | actor_loss: -0.0036 | value_loss: 5.3308 | lr: 1.92e-04
  Update   98 | Ep   727 | reward:     97.9 | mean(100):     99.8 | actor_loss: -0.0023 | value_loss: 2.8189 | lr: 1.91e-04
  Update   99 | Ep   729 | reward:     30.4 | mean(100):     97.4 | actor_loss: -0.0069 | value_loss: 6.4569 | lr: 1.91e-04
  Update  100 | Ep   731 | reward:    136.7 | mean(100):     98.9 | actor_loss: -0.0008 | value_loss: 9.6415 | lr: 1.91e-04
  Update  101 | Ep   733 | reward:    104.3 | mean(100):    100.9 | actor_loss: -0.0044 | value_loss: 2.7025 | lr: 1.90e-04
  Update  102 | Ep   735 | reward:    197.7 | mean(100):    103.0 | actor_loss: -0.0041 | value_loss: 6.5835 | lr: 1.90e-04
  Update  103 | Ep   737 | reward:     60.2 | mean(100):    102.8 | actor_loss: -0.0022 | value_loss: 4.1467 | lr: 1.90e-04
  Update  104 | Ep   740 | reward:    -95.2 | mean(100):     99.3 | actor_loss: -0.0042 | value_loss: 11.7771 | lr: 1.89e-04
  Update  105 | Ep   742 | reward:    112.6 | mean(100):    101.3 | actor_loss: -0.0023 | value_loss: 6.0860 | lr: 1.89e-04
  Update  106 | Ep   744 | reward:    104.5 | mean(100):    100.3 | actor_loss: -0.0018 | value_loss: 5.9544 | lr: 1.89e-04
  Update  107 | Ep   746 | reward:     93.6 | mean(100):    100.6 | actor_loss: -0.0018 | value_loss: 2.7124 | lr: 1.88e-04
  Update  108 | Ep   748 | reward:    117.3 | mean(100):    102.2 | actor_loss: -0.0023 | value_loss: 2.3133 | lr: 1.88e-04
  Update  109 | Ep   750 | reward:    199.9 | mean(100):    103.5 | actor_loss: -0.0020 | value_loss: 6.5481 | lr: 1.88e-04
  Update  110 | Ep   753 | reward:     -4.0 | mean(100):    100.7 | actor_loss: -0.0022 | value_loss: 7.9259 | lr: 1.87e-04
  Update  111 | Ep   755 | reward:    115.8 | mean(100):    101.2 | actor_loss: -0.0028 | value_loss: 1.7218 | lr: 1.87e-04
  Update  112 | Ep   757 | reward:     99.5 | mean(100):    101.2 | actor_loss: -0.0050 | value_loss: 1.9341 | lr: 1.87e-04
  Update  113 | Ep   761 | reward:    204.5 | mean(100):     99.7 | actor_loss: -0.0035 | value_loss: 13.8853 | lr: 1.86e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  114 | Ep   764 | reward:     -3.2 | mean(100):     98.4 | actor_loss: -0.0010 | value_loss: 6.8793 | lr: 1.86e-04
  Update  115 | Ep   766 | reward:     48.0 | mean(100):     96.9 | actor_loss: -0.0058 | value_loss: 3.4082 | lr: 1.85e-04
  Update  116 | Ep   770 | reward:    230.7 | mean(100):     91.1 | actor_loss: -0.0026 | value_loss: 16.2307 | lr: 1.85e-04
  Update  117 | Ep   772 | reward:    114.5 | mean(100):     90.0 | actor_loss: -0.0029 | value_loss: 1.9958 | lr: 1.84e-04
  Update  118 | Ep   774 | reward:     57.8 | mean(100):     89.3 | actor_loss: -0.0020 | value_loss: 5.6900 | lr: 1.84e-04
  Update  119 | Ep   777 | reward:    102.4 | mean(100):     92.1 | actor_loss: -0.0027 | value_loss: 7.1669 | lr: 1.84e-04
  Update  120 | Ep   779 | reward:    113.1 | mean(100):     91.9 | actor_loss: -0.0021 | value_loss: 2.0772 | lr: 1.83e-04
  Update  121 | Ep   781 | reward:     -5.0 | mean(100):     90.4 | actor_loss: -0.0038 | value_loss: 10.9995 | lr: 1.83e-04
  Update  122 | Ep   783 | reward:    127.9 | mean(100):     92.2 | actor_loss: -0.0027 | value_loss: 3.5245 | lr: 1.83e-04
  Update  123 | Ep   785 | reward:     68.5 | mean(100):     91.3 | actor_loss: -0.0036 | value_loss: 5.4426 | lr: 1.83e-04
  Update  124 | Ep   787 | reward:     53.4 | mean(100):     90.5 | actor_loss: -0.0038 | value_loss: 3.6817 | lr: 1.82e-04
  Update  125 | Ep   789 | reward:     73.3 | mean(100):     93.0 | actor_loss: -0.0017 | value_loss: 2.6657 | lr: 1.82e-04
  Update  126 | Ep   791 | reward:     57.3 | mean(100):     90.2 | actor_loss: -0.0055 | value_loss: 6.4944 | lr: 1.82e-04
  Update  127 | Ep   793 | reward:    113.5 | mean(100):     90.4 | actor_loss: -0.0037 | value_loss: 1.7893 | lr: 1.81e-04
  Update  128 | Ep   797 | reward:    -53.5 | mean(100):     85.4 | actor_loss: -0.0082 | value_loss: 14.1789 | lr: 1.81e-04
  Update  129 | Ep   799 | reward:    106.4 | mean(100):     85.4 | actor_loss: -0.0020 | value_loss: 4.0021 | lr: 1.80e-04
  Update  130 | Ep   801 | reward:    107.4 | mean(100):     85.1 | actor_loss: -0.0037 | value_loss: 3.2259 | lr: 1.80e-04
  Update  131 | Ep   803 | reward:    122.3 | mean(100):     84.7 | actor_loss: -0.0025 | value_loss: 3.7859 | lr: 1.80e-04
  Update  132 | Ep   805 | reward:     94.4 | mean(100):     85.0 | actor_loss: -0.0006 | value_loss: 2.4663 | lr: 1.80e-04
  Update  133 | Ep   807 | reward:    131.9 | mean(100):     84.7 | actor_loss: -0.0052 | value_loss: 2.1090 | lr: 1.79e-04
  Update  134 | Ep   810 | reward:    -84.7 | mean(100):     79.8 | actor_loss: -0.0066 | value_loss: 13.6718 | lr: 1.79e-04
  Update  135 | Ep   814 | reward:    -20.9 | mean(100):     75.9 | actor_loss: -0.0063 | value_loss: 16.5174 | lr: 1.78e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  136 | Ep   816 | reward:     87.7 | mean(100):     76.2 | actor_loss: -0.0025 | value_loss: 6.7858 | lr: 1.78e-04
  Update  137 | Ep   818 | reward:    184.0 | mean(100):     77.4 | actor_loss: -0.0038 | value_loss: 5.3077 | lr: 1.78e-04
  Update  138 | Ep   820 | reward:    236.3 | mean(100):     78.4 | actor_loss: -0.0019 | value_loss: 4.8525 | lr: 1.77e-04
  Update  139 | Ep   822 | reward:    191.1 | mean(100):     79.1 | actor_loss: -0.0014 | value_loss: 5.9514 | lr: 1.77e-04
  Update  140 | Ep   824 | reward:    202.7 | mean(100):     80.5 | actor_loss: -0.0076 | value_loss: 7.4703 | lr: 1.77e-04
  Update  141 | Ep   826 | reward:    131.9 | mean(100):     81.4 | actor_loss: -0.0035 | value_loss: 3.5227 | lr: 1.76e-04
  Update  142 | Ep   828 | reward:    106.9 | mean(100):     80.6 | actor_loss: -0.0053 | value_loss: 6.3626 | lr: 1.76e-04
  Update  143 | Ep   830 | reward:     97.8 | mean(100):     80.0 | actor_loss: -0.0008 | value_loss: 5.7630 | lr: 1.76e-04
  Update  144 | Ep   832 | reward:     98.7 | mean(100):     78.9 | actor_loss: -0.0041 | value_loss: 2.3674 | lr: 1.75e-04
  Update  145 | Ep   834 | reward:    -16.9 | mean(100):     77.1 | actor_loss: -0.0034 | value_loss: 6.1224 | lr: 1.75e-04
  Update  146 | Ep   836 | reward:    139.7 | mean(100):     76.4 | actor_loss: -0.0026 | value_loss: 2.3546 | lr: 1.75e-04
  Update  147 | Ep   838 | reward:    116.4 | mean(100):     77.0 | actor_loss: -0.0008 | value_loss: 1.9322 | lr: 1.75e-04
  Update  148 | Ep   840 | reward:     88.2 | mean(100):     80.1 | actor_loss: -0.0022 | value_loss: 2.4154 | lr: 1.74e-04
  Update  149 | Ep   842 | reward:     69.1 | mean(100):     79.5 | actor_loss: -0.0012 | value_loss: 7.0718 | lr: 1.74e-04
  Update  150 | Ep   844 | reward:     75.1 | mean(100):     78.4 | actor_loss: -0.0046 | value_loss: 1.9305 | lr: 1.74e-04
  Update  151 | Ep   846 | reward:    112.0 | mean(100):     79.7 | actor_loss: -0.0035 | value_loss: 5.1475 | lr: 1.73e-04
  Update  152 | Ep   848 | reward:    141.2 | mean(100):     80.2 | actor_loss: -0.0017 | value_loss: 4.8893 | lr: 1.73e-04
  Update  153 | Ep   850 | reward:     80.1 | mean(100):     78.7 | actor_loss: -0.0017 | value_loss: 2.0082 | lr: 1.73e-04
  Update  154 | Ep   852 | reward:    101.6 | mean(100):     80.3 | actor_loss: -0.0031 | value_loss: 2.2602 | lr: 1.72e-04
  Update  155 | Ep   854 | reward:    223.8 | mean(100):     82.6 | actor_loss: -0.0010 | value_loss: 4.6812 | lr: 1.72e-04
  Update  156 | Ep   857 | reward:    131.6 | mean(100):     85.3 | actor_loss: -0.0023 | value_loss: 8.4908 | lr: 1.72e-04
  Update  157 | Ep   859 | reward:    146.5 | mean(100):     88.4 | actor_loss: -0.0043 | value_loss: 3.1197 | lr: 1.71e-04
  Update  158 | Ep   861 | reward:     93.9 | mean(100):     88.0 | actor_loss: -0.0015 | value_loss: 1.6499 | lr: 1.71e-04
  Update  159 | Ep   865 | reward:     26.6 | mean(100):     85.8 | actor_loss: -0.0051 | value_loss: 18.0112 | lr: 1.71e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  160 | Ep   867 | reward:     80.0 | mean(100):     88.0 | actor_loss: -0.0032 | value_loss: 1.9308 | lr: 1.70e-04
  Update  161 | Ep   869 | reward:     92.2 | mean(100):     91.8 | actor_loss: -0.0023 | value_loss: 2.6118 | lr: 1.70e-04
  Update  162 | Ep   871 | reward:    103.6 | mean(100):     90.8 | actor_loss: -0.0021 | value_loss: 1.8717 | lr: 1.70e-04
  Update  163 | Ep   873 | reward:    137.6 | mean(100):     92.7 | actor_loss: -0.0039 | value_loss: 3.3195 | lr: 1.69e-04
  Update  164 | Ep   875 | reward:    113.7 | mean(100):     92.0 | actor_loss: -0.0008 | value_loss: 1.6941 | lr: 1.69e-04
  Update  165 | Ep   877 | reward:    118.2 | mean(100):     91.2 | actor_loss: -0.0003 | value_loss: 2.5654 | lr: 1.69e-04
  Update  166 | Ep   879 | reward:     99.7 | mean(100):     91.2 | actor_loss: -0.0003 | value_loss: 1.8952 | lr: 1.68e-04
  Update  167 | Ep   881 | reward:    103.5 | mean(100):     91.6 | actor_loss: -0.0038 | value_loss: 3.6099 | lr: 1.68e-04
  Update  168 | Ep   884 | reward:     89.6 | mean(100):     93.0 | actor_loss: -0.0032 | value_loss: 7.3558 | lr: 1.68e-04
  Update  169 | Ep   886 | reward:     54.8 | mean(100):     93.1 | actor_loss: -0.0012 | value_loss: 3.9238 | lr: 1.67e-04
  Update  170 | Ep   888 | reward:    107.4 | mean(100):     93.9 | actor_loss: -0.0028 | value_loss: 2.5619 | lr: 1.67e-04
  Update  171 | Ep   890 | reward:    210.9 | mean(100):     97.1 | actor_loss: -0.0026 | value_loss: 3.8027 | lr: 1.67e-04
  Update  172 | Ep   892 | reward:    232.3 | mean(100):     98.8 | actor_loss: -0.0013 | value_loss: 5.0013 | lr: 1.66e-04
  Update  173 | Ep   894 | reward:    126.6 | mean(100):    100.5 | actor_loss: -0.0016 | value_loss: 2.7641 | lr: 1.66e-04
  Update  174 | Ep   896 | reward:    236.7 | mean(100):    102.3 | actor_loss: -0.0015 | value_loss: 4.8860 | lr: 1.66e-04
  Update  175 | Ep   898 | reward:    120.2 | mean(100):    104.1 | actor_loss: -0.0016 | value_loss: 1.5497 | lr: 1.66e-04
  Update  176 | Ep   900 | reward:    115.0 | mean(100):    104.6 | actor_loss: -0.0018 | value_loss: 2.4875 | lr: 1.65e-04
  Update  177 | Ep   902 | reward:    218.7 | mean(100):    106.1 | actor_loss: -0.0019 | value_loss: 5.3398 | lr: 1.65e-04
  Update  178 | Ep   904 | reward:    100.0 | mean(100):    105.9 | actor_loss: -0.0019 | value_loss: 1.7362 | lr: 1.65e-04
  Update  179 | Ep   906 | reward:    111.9 | mean(100):    106.3 | actor_loss: -0.0012 | value_loss: 2.1497 | lr: 1.64e-04
  Update  180 | Ep   908 | reward:    114.2 | mean(100):    109.1 | actor_loss: -0.0005 | value_loss: 4.5949 | lr: 1.64e-04
  Update  181 | Ep   910 | reward:    160.8 | mean(100):    112.5 | actor_loss: -0.0042 | value_loss: 3.9011 | lr: 1.64e-04
  Update  182 | Ep   912 | reward:     63.7 | mean(100):    114.4 | actor_loss: -0.0016 | value_loss: 6.8294 | lr: 1.63e-04
  Update  183 | Ep   914 | reward:    128.4 | mean(100):    117.4 | actor_loss: -0.0036 | value_loss: 2.5202 | lr: 1.63e-04
  Update  184 | Ep   916 | reward:    129.3 | mean(100):    119.0 | actor_loss: -0.0004 | value_loss: 3.0695 | lr: 1.63e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  185 | Ep   918 | reward:    158.1 | mean(100):    118.9 | actor_loss: -0.0051 | value_loss: 5.0117 | lr: 1.63e-04
  Update  186 | Ep   921 | reward:    118.6 | mean(100):    116.9 | actor_loss: -0.0023 | value_loss: 9.1718 | lr: 1.62e-04
  Update  187 | Ep   923 | reward:    100.3 | mean(100):    115.1 | actor_loss: -0.0028 | value_loss: 1.8873 | lr: 1.62e-04
  Update  188 | Ep   925 | reward:    131.6 | mean(100):    114.3 | actor_loss: -0.0024 | value_loss: 4.2015 | lr: 1.62e-04
  Update  189 | Ep   927 | reward:    107.1 | mean(100):    116.0 | actor_loss: -0.0028 | value_loss: 2.7287 | lr: 1.61e-04
  Update  190 | Ep   929 | reward:     86.0 | mean(100):    116.9 | actor_loss: -0.0024 | value_loss: 2.0951 | lr: 1.61e-04
  Update  191 | Ep   932 | reward:    -17.6 | mean(100):    116.6 | actor_loss: -0.0011 | value_loss: 8.8873 | lr: 1.61e-04
  Update  192 | Ep   935 | reward:    226.6 | mean(100):    120.8 | actor_loss: -0.0019 | value_loss: 7.7007 | lr: 1.60e-04
  Update  193 | Ep   937 | reward:    113.6 | mean(100):    120.9 | actor_loss: -0.0010 | value_loss: 1.5870 | lr: 1.60e-04
  Update  194 | Ep   939 | reward:     97.9 | mean(100):    121.2 | actor_loss: -0.0042 | value_loss: 3.7529 | lr: 1.59e-04
  Update  195 | Ep   941 | reward:    121.1 | mean(100):    120.7 | actor_loss: -0.0033 | value_loss: 1.9553 | lr: 1.59e-04
  Update  196 | Ep   944 | reward:    -43.4 | mean(100):    121.1 | actor_loss: -0.0022 | value_loss: 9.0830 | lr: 1.59e-04
  Update  197 | Ep   947 | reward:     27.6 | mean(100):    116.8 | actor_loss: -0.0049 | value_loss: 12.7947 | lr: 1.58e-04
  Update  198 | Ep   949 | reward:     64.9 | mean(100):    115.8 | actor_loss: -0.0026 | value_loss: 3.1304 | lr: 1.58e-04
  Update  199 | Ep   951 | reward:    100.3 | mean(100):    116.0 | actor_loss: -0.0045 | value_loss: 3.0320 | lr: 1.58e-04
  Update  200 | Ep   953 | reward:     53.3 | mean(100):    115.3 | actor_loss: -0.0015 | value_loss: 3.1273 | lr: 1.57e-04
  Update  201 | Ep   955 | reward:    112.5 | mean(100):    112.7 | actor_loss: -0.0023 | value_loss: 3.0911 | lr: 1.57e-04
  Update  202 | Ep   957 | reward:    116.3 | mean(100):    111.1 | actor_loss: -0.0045 | value_loss: 2.2869 | lr: 1.57e-04
  Update  203 | Ep   959 | reward:    112.7 | mean(100):    111.2 | actor_loss: -0.0017 | value_loss: 1.2470 | lr: 1.56e-04
  Update  204 | Ep   961 | reward:    123.1 | mean(100):    111.7 | actor_loss: -0.0023 | value_loss: 1.4043 | lr: 1.56e-04
  Update  205 | Ep   964 | reward:     85.8 | mean(100):    113.4 | actor_loss: -0.0024 | value_loss: 7.7148 | lr: 1.56e-04
  Update  206 | Ep   966 | reward:    146.4 | mean(100):    114.4 | actor_loss: -0.0032 | value_loss: 2.5915 | lr: 1.55e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  207 | Ep   969 | reward:    213.2 | mean(100):    116.3 | actor_loss: -0.0022 | value_loss: 7.9201 | lr: 1.55e-04
  Update  208 | Ep   971 | reward:    134.6 | mean(100):    116.3 | actor_loss: -0.0024 | value_loss: 1.4147 | lr: 1.55e-04
  Update  209 | Ep   974 | reward:    106.3 | mean(100):    115.6 | actor_loss: -0.0030 | value_loss: 7.7425 | lr: 1.54e-04
  Update  210 | Ep   976 | reward:    118.8 | mean(100):    115.7 | actor_loss: -0.0002 | value_loss: 1.1038 | lr: 1.54e-04
  Update  211 | Ep   978 | reward:    149.2 | mean(100):    116.0 | actor_loss: -0.0034 | value_loss: 1.8166 | lr: 1.54e-04
  Update  212 | Ep   980 | reward:     95.8 | mean(100):    117.6 | actor_loss: -0.0001 | value_loss: 3.6429 | lr: 1.53e-04
  Update  213 | Ep   982 | reward:    108.8 | mean(100):    117.1 | actor_loss: -0.0008 | value_loss: 2.1343 | lr: 1.53e-04
  Update  214 | Ep   984 | reward:     89.4 | mean(100):    116.3 | actor_loss: -0.0012 | value_loss: 2.2322 | lr: 1.53e-04
  Update  215 | Ep   987 | reward:    182.3 | mean(100):    116.1 | actor_loss: -0.0013 | value_loss: 7.7732 | lr: 1.52e-04
  Update  216 | Ep   990 | reward:    208.8 | mean(100):    117.8 | actor_loss: -0.0037 | value_loss: 6.8331 | lr: 1.52e-04
  Update  217 | Ep   992 | reward:    133.3 | mean(100):    117.0 | actor_loss: -0.0040 | value_loss: 2.4747 | lr: 1.51e-04
  Update  218 | Ep   995 | reward:    118.7 | mean(100):    119.3 | actor_loss: -0.0009 | value_loss: 5.6362 | lr: 1.51e-04
  Update  219 | Ep   997 | reward:    156.9 | mean(100):    118.4 | actor_loss: -0.0018 | value_loss: 1.6444 | lr: 1.51e-04
  Update  220 | Ep   999 | reward:    246.0 | mean(100):    120.0 | actor_loss: -0.0024 | value_loss: 5.7493 | lr: 1.50e-04
  Update  221 | Ep  1001 | reward:    112.3 | mean(100):    120.1 | actor_loss: -0.0030 | value_loss: 1.5584 | lr: 1.50e-04
  Update  222 | Ep  1004 | reward:   -296.7 | mean(100):    116.4 | actor_loss: -0.0009 | value_loss: 15.5331 | lr: 1.50e-04
  Update  223 | Ep  1006 | reward:    133.6 | mean(100):    117.7 | actor_loss: -0.0013 | value_loss: 5.0654 | lr: 1.49e-04
  Update  224 | Ep  1010 | reward:    110.0 | mean(100):    117.2 | actor_loss: -0.0064 | value_loss: 10.2917 | lr: 1.49e-04
  Update  225 | Ep  1012 | reward:    123.7 | mean(100):    117.0 | actor_loss: -0.0019 | value_loss: 1.7217 | lr: 1.48e-04
  Update  226 | Ep  1015 | reward:     96.1 | mean(100):    113.2 | actor_loss: -0.0087 | value_loss: 15.3198 | lr: 1.48e-04
  Update  227 | Ep  1018 | reward:    176.0 | mean(100):    114.7 | actor_loss: 0.0001 | value_loss: 10.3897 | lr: 1.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  228 | Ep  1020 | reward:     89.1 | mean(100):    115.8 | actor_loss: -0.0042 | value_loss: 2.4416 | lr: 1.47e-04
  Update  229 | Ep  1022 | reward:    111.9 | mean(100):    115.6 | actor_loss: -0.0022 | value_loss: 1.7108 | lr: 1.47e-04
  Update  230 | Ep  1026 | reward:    203.1 | mean(100):    114.0 | actor_loss: -0.0028 | value_loss: 12.7637 | lr: 1.47e-04
  Update  231 | Ep  1029 | reward:    -14.8 | mean(100):    114.8 | actor_loss: -0.0032 | value_loss: 8.9813 | lr: 1.46e-04
  Update  232 | Ep  1032 | reward:      7.6 | mean(100):    115.5 | actor_loss: -0.0050 | value_loss: 6.9482 | lr: 1.46e-04
  Update  233 | Ep  1035 | reward:      3.4 | mean(100):    113.0 | actor_loss: -0.0020 | value_loss: 9.9740 | lr: 1.45e-04
  Update  234 | Ep  1039 | reward:    232.4 | mean(100):    116.6 | actor_loss: -0.0025 | value_loss: 11.3357 | lr: 1.45e-04
  Update  235 | Ep  1042 | reward:      5.5 | mean(100):    115.7 | actor_loss: -0.0041 | value_loss: 7.1067 | lr: 1.44e-04
  Update  236 | Ep  1044 | reward:     25.4 | mean(100):    116.2 | actor_loss: -0.0012 | value_loss: 4.1795 | lr: 1.44e-04
  Update  237 | Ep  1046 | reward:    165.4 | mean(100):    119.6 | actor_loss: -0.0028 | value_loss: 4.2258 | lr: 1.43e-04
  Update  238 | Ep  1048 | reward:    101.6 | mean(100):    120.9 | actor_loss: -0.0034 | value_loss: 1.5537 | lr: 1.43e-04
  Update  239 | Ep  1051 | reward:    237.9 | mean(100):    123.7 | actor_loss: 0.0002 | value_loss: 6.7510 | lr: 1.43e-04
  Update  240 | Ep  1053 | reward:    118.3 | mean(100):    124.8 | actor_loss: -0.0026 | value_loss: 1.6262 | lr: 1.42e-04
  Update  241 | Ep  1057 | reward:    235.3 | mean(100):    126.5 | actor_loss: -0.0018 | value_loss: 14.5812 | lr: 1.42e-04
  Update  242 | Ep  1060 | reward:    186.2 | mean(100):    128.6 | actor_loss: -0.0015 | value_loss: 5.9849 | lr: 1.41e-04
  Update  243 | Ep  1062 | reward:    150.4 | mean(100):    130.0 | actor_loss: -0.0020 | value_loss: 1.9067 | lr: 1.41e-04
  Update  244 | Ep  1064 | reward:    242.4 | mean(100):    132.6 | actor_loss: -0.0069 | value_loss: 4.8276 | lr: 1.41e-04
  Update  245 | Ep  1066 | reward:     80.0 | mean(100):    132.3 | actor_loss: -0.0032 | value_loss: 1.9389 | lr: 1.40e-04
  Update  246 | Ep  1070 | reward:    -22.7 | mean(100):    131.4 | actor_loss: -0.0014 | value_loss: 10.0742 | lr: 1.40e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  247 | Ep  1072 | reward:    132.7 | mean(100):    130.5 | actor_loss: -0.0009 | value_loss: 1.8720 | lr: 1.39e-04
  Update  248 | Ep  1074 | reward:    119.8 | mean(100):    132.9 | actor_loss: -0.0019 | value_loss: 3.0240 | lr: 1.39e-04
  Update  249 | Ep  1078 | reward:     -4.8 | mean(100):    134.1 | actor_loss: -0.0059 | value_loss: 10.4751 | lr: 1.39e-04
  Update  250 | Ep  1080 | reward:    110.7 | mean(100):    133.2 | actor_loss: -0.0028 | value_loss: 1.2026 | lr: 1.38e-04
  Update  251 | Ep  1082 | reward:    139.3 | mean(100):    133.3 | actor_loss: -0.0024 | value_loss: 1.9608 | lr: 1.38e-04
  Update  252 | Ep  1086 | reward:    216.0 | mean(100):    135.6 | actor_loss: -0.0023 | value_loss: 10.2568 | lr: 1.38e-04
  Update  253 | Ep  1088 | reward:    164.7 | mean(100):    131.7 | actor_loss: -0.0018 | value_loss: 7.8230 | lr: 1.37e-04
  Update  254 | Ep  1090 | reward:    121.2 | mean(100):    130.7 | actor_loss: -0.0030 | value_loss: 1.4379 | lr: 1.37e-04
  Update  255 | Ep  1092 | reward:    115.2 | mean(100):    130.5 | actor_loss: -0.0023 | value_loss: 1.4337 | lr: 1.36e-04
  Update  256 | Ep  1094 | reward:    127.5 | mean(100):    129.5 | actor_loss: -0.0004 | value_loss: 3.3052 | lr: 1.36e-04
  Update  257 | Ep  1096 | reward:    133.9 | mean(100):    129.7 | actor_loss: -0.0013 | value_loss: 1.8502 | lr: 1.36e-04
  Update  258 | Ep  1100 | reward:    209.7 | mean(100):    127.7 | actor_loss: -0.0017 | value_loss: 8.1785 | lr: 1.36e-04
  Update  259 | Ep  1105 | reward:     -1.3 | mean(100):    124.4 | actor_loss: -0.0022 | value_loss: 16.0357 | lr: 1.35e-04
  Update  260 | Ep  1107 | reward:    132.6 | mean(100):    123.6 | actor_loss: -0.0030 | value_loss: 1.4773 | lr: 1.34e-04
  Update  261 | Ep  1109 | reward:    156.6 | mean(100):    124.1 | actor_loss: -0.0040 | value_loss: 2.5003 | lr: 1.34e-04
  Update  262 | Ep  1111 | reward:    141.7 | mean(100):    124.3 | actor_loss: -0.0018 | value_loss: 1.8930 | lr: 1.34e-04
  Update  263 | Ep  1113 | reward:    145.9 | mean(100):    129.0 | actor_loss: -0.0036 | value_loss: 1.3762 | lr: 1.33e-04
  Update  264 | Ep  1115 | reward:    154.2 | mean(100):    128.7 | actor_loss: -0.0048 | value_loss: 2.3413 | lr: 1.33e-04
  Update  265 | Ep  1117 | reward:     -7.2 | mean(100):    126.6 | actor_loss: -0.0026 | value_loss: 5.0485 | lr: 1.33e-04
  Update  266 | Ep  1119 | reward:    140.1 | mean(100):    126.0 | actor_loss: -0.0028 | value_loss: 1.8984 | lr: 1.32e-04
  Update  267 | Ep  1121 | reward:    113.3 | mean(100):    126.8 | actor_loss: -0.0032 | value_loss: 1.6494 | lr: 1.32e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  268 | Ep  1123 | reward:    155.4 | mean(100):    128.8 | actor_loss: -0.0036 | value_loss: 1.7923 | lr: 1.32e-04
  Update  269 | Ep  1126 | reward:    129.9 | mean(100):    130.7 | actor_loss: -0.0029 | value_loss: 7.4698 | lr: 1.32e-04
  Update  270 | Ep  1129 | reward:    -26.3 | mean(100):    130.1 | actor_loss: -0.0018 | value_loss: 7.0918 | lr: 1.31e-04
  Update  271 | Ep  1132 | reward:     38.5 | mean(100):    130.4 | actor_loss: -0.0045 | value_loss: 6.6795 | lr: 1.31e-04
  Update  272 | Ep  1134 | reward:    140.0 | mean(100):    130.4 | actor_loss: -0.0023 | value_loss: 2.1474 | lr: 1.30e-04
  Update  273 | Ep  1136 | reward:    170.7 | mean(100):    131.5 | actor_loss: -0.0016 | value_loss: 4.6303 | lr: 1.30e-04
  Update  274 | Ep  1138 | reward:    138.4 | mean(100):    129.6 | actor_loss: -0.0033 | value_loss: 0.9509 | lr: 1.30e-04
  Update  275 | Ep  1144 | reward:     37.6 | mean(100):    125.6 | actor_loss: -0.0021 | value_loss: 19.5299 | lr: 1.29e-04
  Update  276 | Ep  1148 | reward:     62.4 | mean(100):    126.2 | actor_loss: -0.0017 | value_loss: 8.6015 | lr: 1.28e-04
  Update  277 | Ep  1152 | reward:    136.1 | mean(100):    123.7 | actor_loss: -0.0018 | value_loss: 8.4489 | lr: 1.28e-04
  Update  278 | Ep  1158 | reward:     21.1 | mean(100):    121.8 | actor_loss: -0.0045 | value_loss: 17.8178 | lr: 1.27e-04
  Update  279 | Ep  1161 | reward:    228.2 | mean(100):    122.3 | actor_loss: -0.0022 | value_loss: 5.6335 | lr: 1.26e-04
  Update  280 | Ep  1163 | reward:    139.2 | mean(100):    123.8 | actor_loss: -0.0049 | value_loss: 4.3980 | lr: 1.26e-04
  Update  281 | Ep  1165 | reward:    156.5 | mean(100):    123.3 | actor_loss: -0.0010 | value_loss: 3.9467 | lr: 1.26e-04
  Update  282 | Ep  1168 | reward:    167.2 | mean(100):    124.5 | actor_loss: -0.0009 | value_loss: 6.0920 | lr: 1.25e-04
  Update  283 | Ep  1170 | reward:     98.9 | mean(100):    125.9 | actor_loss: -0.0015 | value_loss: 3.5457 | lr: 1.25e-04
  Update  284 | Ep  1172 | reward:    176.4 | mean(100):    126.4 | actor_loss: -0.0019 | value_loss: 2.9334 | lr: 1.24e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  285 | Ep  1176 | reward:     -0.1 | mean(100):    125.4 | actor_loss: -0.0011 | value_loss: 9.4249 | lr: 1.24e-04
  Update  286 | Ep  1178 | reward:    138.0 | mean(100):    126.4 | actor_loss: -0.0034 | value_loss: 2.0566 | lr: 1.24e-04
  Update  287 | Ep  1181 | reward:    232.9 | mean(100):    129.3 | actor_loss: -0.0013 | value_loss: 6.8325 | lr: 1.23e-04
  Update  288 | Ep  1184 | reward:    119.0 | mean(100):    129.5 | actor_loss: -0.0007 | value_loss: 5.2784 | lr: 1.23e-04
  Update  289 | Ep  1186 | reward:    141.5 | mean(100):    128.6 | actor_loss: -0.0004 | value_loss: 4.1112 | lr: 1.22e-04
  Update  290 | Ep  1189 | reward:    227.2 | mean(100):    132.4 | actor_loss: -0.0021 | value_loss: 5.9876 | lr: 1.22e-04
  Update  291 | Ep  1192 | reward:    129.3 | mean(100):    134.1 | actor_loss: -0.0005 | value_loss: 5.0771 | lr: 1.22e-04
  Update  292 | Ep  1194 | reward:    221.4 | mean(100):    134.0 | actor_loss: -0.0012 | value_loss: 3.6083 | lr: 1.21e-04
  Update  293 | Ep  1196 | reward:     96.4 | mean(100):    134.1 | actor_loss: -0.0042 | value_loss: 1.5692 | lr: 1.21e-04
  Update  294 | Ep  1198 | reward:    250.0 | mean(100):    134.9 | actor_loss: -0.0052 | value_loss: 3.9416 | lr: 1.21e-04
  Update  295 | Ep  1200 | reward:    220.3 | mean(100):    136.1 | actor_loss: -0.0007 | value_loss: 3.8887 | lr: 1.20e-04
  Update  296 | Ep  1202 | reward:    121.4 | mean(100):    137.5 | actor_loss: -0.0039 | value_loss: 1.1533 | lr: 1.20e-04
  Update  297 | Ep  1205 | reward:     39.4 | mean(100):    142.0 | actor_loss: -0.0032 | value_loss: 7.1930 | lr: 1.20e-04
  Update  298 | Ep  1207 | reward:    169.0 | mean(100):    142.5 | actor_loss: -0.0015 | value_loss: 1.9959 | lr: 1.19e-04
  Update  299 | Ep  1209 | reward:     99.9 | mean(100):    142.3 | actor_loss: -0.0028 | value_loss: 2.0502 | lr: 1.19e-04
  Update  300 | Ep  1211 | reward:    143.6 | mean(100):    142.4 | actor_loss: 0.0021 | value_loss: 1.5065 | lr: 1.19e-04
  Update  301 | Ep  1213 | reward:    183.0 | mean(100):    142.8 | actor_loss: -0.0039 | value_loss: 2.3546 | lr: 1.18e-04
  Update  302 | Ep  1215 | reward:    112.6 | mean(100):    141.8 | actor_loss: -0.0005 | value_loss: 2.1700 | lr: 1.18e-04
  Update  303 | Ep  1217 | reward:    129.9 | mean(100):    143.1 | actor_loss: -0.0016 | value_loss: 1.9683 | lr: 1.18e-04
  Update  304 | Ep  1220 | reward:    203.0 | mean(100):    142.2 | actor_loss: -0.0001 | value_loss: 6.9684 | lr: 1.17e-04
  Update  305 | Ep  1222 | reward:    149.1 | mean(100):    143.4 | actor_loss: -0.0001 | value_loss: 3.8844 | lr: 1.17e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  306 | Ep  1225 | reward:      9.8 | mean(100):    141.8 | actor_loss: -0.0037 | value_loss: 6.5941 | lr: 1.17e-04
  Update  307 | Ep  1227 | reward:    122.1 | mean(100):    142.1 | actor_loss: -0.0030 | value_loss: 1.3191 | lr: 1.16e-04
  Update  308 | Ep  1229 | reward:    140.7 | mean(100):    142.9 | actor_loss: -0.0028 | value_loss: 1.0947 | lr: 1.16e-04
  Update  309 | Ep  1231 | reward:    115.6 | mean(100):    142.1 | actor_loss: -0.0022 | value_loss: 0.9145 | lr: 1.16e-04
  Update  310 | Ep  1235 | reward:    243.9 | mean(100):    145.1 | actor_loss: -0.0012 | value_loss: 7.9813 | lr: 1.15e-04
  Update  311 | Ep  1237 | reward:    130.0 | mean(100):    145.1 | actor_loss: -0.0013 | value_loss: 1.6391 | lr: 1.15e-04
  Update  312 | Ep  1239 | reward:    140.1 | mean(100):    145.5 | actor_loss: -0.0002 | value_loss: 3.8566 | lr: 1.14e-04
  Update  313 | Ep  1241 | reward:    152.9 | mean(100):    149.2 | actor_loss: -0.0029 | value_loss: 1.8230 | lr: 1.14e-04
  Update  314 | Ep  1243 | reward:    132.4 | mean(100):    150.5 | actor_loss: -0.0022 | value_loss: 0.8996 | lr: 1.14e-04
  Update  315 | Ep  1245 | reward:    134.7 | mean(100):    149.3 | actor_loss: 0.0007 | value_loss: 4.3999 | lr: 1.14e-04
  Update  316 | Ep  1247 | reward:    141.1 | mean(100):    147.7 | actor_loss: -0.0032 | value_loss: 1.5757 | lr: 1.13e-04
  Update  317 | Ep  1250 | reward:     -9.2 | mean(100):    146.9 | actor_loss: 0.0008 | value_loss: 7.4750 | lr: 1.13e-04
  Update  318 | Ep  1252 | reward:    150.8 | mean(100):    147.6 | actor_loss: -0.0010 | value_loss: 3.3735 | lr: 1.12e-04
  Update  319 | Ep  1256 | reward:     15.6 | mean(100):    149.3 | actor_loss: -0.0026 | value_loss: 8.4797 | lr: 1.12e-04
  Update  320 | Ep  1258 | reward:    229.2 | mean(100):    150.7 | actor_loss: -0.0023 | value_loss: 2.9281 | lr: 1.12e-04
  Update  321 | Ep  1260 | reward:     95.1 | mean(100):    149.5 | actor_loss: -0.0039 | value_loss: 1.0288 | lr: 1.11e-04
  Update  322 | Ep  1262 | reward:    105.8 | mean(100):    146.5 | actor_loss: -0.0012 | value_loss: 1.5137 | lr: 1.11e-04
  Update  323 | Ep  1264 | reward:    227.0 | mean(100):    146.7 | actor_loss: -0.0007 | value_loss: 2.6725 | lr: 1.11e-04
  Update  324 | Ep  1266 | reward:    132.0 | mean(100):    145.8 | actor_loss: -0.0052 | value_loss: 1.6672 | lr: 1.10e-04
  Update  325 | Ep  1269 | reward:    245.1 | mean(100):    146.3 | actor_loss: -0.0010 | value_loss: 6.0798 | lr: 1.10e-04
  Update  326 | Ep  1271 | reward:    171.5 | mean(100):    147.0 | actor_loss: -0.0020 | value_loss: 1.9828 | lr: 1.10e-04
  Update  327 | Ep  1273 | reward:    152.9 | mean(100):    146.7 | actor_loss: -0.0015 | value_loss: 3.7502 | lr: 1.09e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  328 | Ep  1275 | reward:    163.1 | mean(100):    146.1 | actor_loss: -0.0003 | value_loss: 2.2348 | lr: 1.09e-04
  Update  329 | Ep  1277 | reward:    161.1 | mean(100):    147.5 | actor_loss: -0.0051 | value_loss: 4.6130 | lr: 1.09e-04
  Update  330 | Ep  1279 | reward:     98.2 | mean(100):    145.9 | actor_loss: -0.0035 | value_loss: 1.3456 | lr: 1.08e-04
  Update  331 | Ep  1283 | reward:    154.3 | mean(100):    142.6 | actor_loss: -0.0029 | value_loss: 8.5960 | lr: 1.08e-04
  Update  332 | Ep  1286 | reward:     19.8 | mean(100):    141.3 | actor_loss: -0.0030 | value_loss: 7.4363 | lr: 1.08e-04
  Update  333 | Ep  1288 | reward:    120.3 | mean(100):    141.0 | actor_loss: -0.0005 | value_loss: 1.5738 | lr: 1.07e-04
  Update  334 | Ep  1290 | reward:    123.0 | mean(100):    137.8 | actor_loss: -0.0028 | value_loss: 5.1295 | lr: 1.07e-04
  Update  335 | Ep  1292 | reward:    -13.6 | mean(100):    135.5 | actor_loss: -0.0002 | value_loss: 3.9936 | lr: 1.06e-04
  Update  336 | Ep  1295 | reward:    188.6 | mean(100):    134.4 | actor_loss: -0.0045 | value_loss: 6.3053 | lr: 1.06e-04
  Update  337 | Ep  1297 | reward:     86.8 | mean(100):    132.7 | actor_loss: -0.0032 | value_loss: 4.6453 | lr: 1.06e-04
  Update  338 | Ep  1301 | reward:    215.0 | mean(100):    134.1 | actor_loss: -0.0011 | value_loss: 8.0036 | lr: 1.05e-04
  Update  339 | Ep  1304 | reward:     99.2 | mean(100):    132.5 | actor_loss: -0.0017 | value_loss: 6.0767 | lr: 1.05e-04
  Update  340 | Ep  1306 | reward:    211.5 | mean(100):    134.2 | actor_loss: -0.0008 | value_loss: 3.0588 | lr: 1.04e-04
  Update  341 | Ep  1308 | reward:     -8.2 | mean(100):    133.3 | actor_loss: -0.0044 | value_loss: 6.1052 | lr: 1.04e-04
  Update  342 | Ep  1311 | reward:    219.7 | mean(100):    133.2 | actor_loss: -0.0019 | value_loss: 5.5742 | lr: 1.04e-04
  Update  343 | Ep  1315 | reward:     36.3 | mean(100):    132.0 | actor_loss: -0.0020 | value_loss: 9.5230 | lr: 1.03e-04
  Update  344 | Ep  1319 | reward:    185.9 | mean(100):    132.6 | actor_loss: -0.0031 | value_loss: 7.8122 | lr: 1.03e-04
  Update  345 | Ep  1321 | reward:    126.7 | mean(100):    130.8 | actor_loss: -0.0036 | value_loss: 1.0545 | lr: 1.02e-04
  Update  346 | Ep  1326 | reward:    228.8 | mean(100):    132.6 | actor_loss: -0.0022 | value_loss: 9.3319 | lr: 1.02e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  347 | Ep  1329 | reward:     81.0 | mean(100):    131.1 | actor_loss: -0.0010 | value_loss: 7.1161 | lr: 1.01e-04
  Update  348 | Ep  1333 | reward:    151.5 | mean(100):    128.8 | actor_loss: -0.0034 | value_loss: 8.5092 | lr: 1.01e-04
  Update  349 | Ep  1335 | reward:    136.9 | mean(100):    126.7 | actor_loss: -0.0019 | value_loss: 1.2594 | lr: 1.00e-04
  Update  350 | Ep  1340 | reward:    204.8 | mean(100):    129.8 | actor_loss: -0.0019 | value_loss: 11.8669 | lr: 9.97e-05
  Update  351 | Ep  1345 | reward:    157.8 | mean(100):    128.8 | actor_loss: -0.0038 | value_loss: 12.4031 | lr: 9.90e-05
  Update  352 | Ep  1348 | reward:    248.1 | mean(100):    131.6 | actor_loss: -0.0001 | value_loss: 7.3312 | lr: 9.82e-05
  Update  353 | Ep  1350 | reward:    193.6 | mean(100):    134.4 | actor_loss: -0.0012 | value_loss: 2.8631 | lr: 9.78e-05
  Update  354 | Ep  1353 | reward:    -13.7 | mean(100):    132.1 | actor_loss: -0.0026 | value_loss: 6.4582 | lr: 9.75e-05
  Update  355 | Ep  1356 | reward:     14.9 | mean(100):    132.2 | actor_loss: -0.0036 | value_loss: 5.6049 | lr: 9.71e-05
  Update  356 | Ep  1361 | reward:     34.4 | mean(100):    127.3 | actor_loss: -0.0029 | value_loss: 12.1250 | lr: 9.66e-05
  Update  357 | Ep  1364 | reward:    -10.9 | mean(100):    124.6 | actor_loss: -0.0018 | value_loss: 7.8485 | lr: 9.58e-05
  Update  358 | Ep  1369 | reward:     35.9 | mean(100):    125.0 | actor_loss: -0.0023 | value_loss: 10.6483 | lr: 9.54e-05
  Update  359 | Ep  1371 | reward:    170.9 | mean(100):    123.9 | actor_loss: -0.0011 | value_loss: 4.3166 | lr: 9.46e-05
  Update  360 | Ep  1374 | reward:    214.5 | mean(100):    122.6 | actor_loss: -0.0001 | value_loss: 6.8409 | lr: 9.43e-05
  Update  361 | Ep  1376 | reward:    217.8 | mean(100):    123.7 | actor_loss: -0.0005 | value_loss: 3.4117 | lr: 9.39e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  362 | Ep  1380 | reward:      5.8 | mean(100):    118.1 | actor_loss: -0.0013 | value_loss: 13.1824 | lr: 9.36e-05
  Update  363 | Ep  1385 | reward:    219.6 | mean(100):    121.4 | actor_loss: -0.0010 | value_loss: 11.0600 | lr: 9.30e-05
  Update  364 | Ep  1387 | reward:     99.0 | mean(100):    122.4 | actor_loss: -0.0007 | value_loss: 1.6328 | lr: 9.22e-05
  Update  365 | Ep  1390 | reward:    113.4 | mean(100):    123.4 | actor_loss: -0.0029 | value_loss: 5.0191 | lr: 9.19e-05
  Update  366 | Ep  1395 | reward:    146.9 | mean(100):    122.7 | actor_loss: -0.0029 | value_loss: 11.6412 | lr: 9.15e-05
  Update  367 | Ep  1400 | reward:    209.6 | mean(100):    121.0 | actor_loss: -0.0031 | value_loss: 11.2650 | lr: 9.07e-05
  Update  368 | Ep  1403 | reward:    117.4 | mean(100):    119.7 | actor_loss: -0.0007 | value_loss: 5.9015 | lr: 9.00e-05
  Update  369 | Ep  1407 | reward:    147.5 | mean(100):    119.6 | actor_loss: -0.0025 | value_loss: 9.4290 | lr: 8.95e-05
  Update  370 | Ep  1412 | reward:     32.7 | mean(100):    120.8 | actor_loss: -0.0065 | value_loss: 12.0526 | lr: 8.89e-05
  Update  371 | Ep  1415 | reward:      9.1 | mean(100):    119.6 | actor_loss: -0.0040 | value_loss: 8.8425 | lr: 8.82e-05
  Update  372 | Ep  1419 | reward:    206.9 | mean(100):    120.7 | actor_loss: -0.0028 | value_loss: 7.0062 | lr: 8.77e-05
  Update  373 | Ep  1422 | reward:     38.1 | mean(100):    120.1 | actor_loss: -0.0010 | value_loss: 6.1973 | lr: 8.71e-05
  Update  374 | Ep  1426 | reward:     28.4 | mean(100):    115.0 | actor_loss: -0.0045 | value_loss: 10.5420 | lr: 8.67e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  375 | Ep  1433 | reward:    231.0 | mean(100):    116.5 | actor_loss: -0.0036 | value_loss: 17.5869 | lr: 8.61e-05
  Update  376 | Ep  1437 | reward:    142.5 | mean(100):    114.0 | actor_loss: -0.0006 | value_loss: 7.0733 | lr: 8.50e-05
  Update  377 | Ep  1440 | reward:    213.2 | mean(100):    110.5 | actor_loss: -0.0017 | value_loss: 5.4825 | lr: 8.44e-05
  Update  378 | Ep  1444 | reward:    221.9 | mean(100):    112.7 | actor_loss: -0.0061 | value_loss: 10.3889 | lr: 8.40e-05
  Update  379 | Ep  1452 | reward:     32.2 | mean(100):    100.7 | actor_loss: -0.0047 | value_loss: 18.9385 | lr: 8.34e-05
  Update  380 | Ep  1457 | reward:    121.4 | mean(100):    103.1 | actor_loss: -0.0009 | value_loss: 9.9427 | lr: 8.22e-05
  Update  381 | Ep  1462 | reward:    228.6 | mean(100):    105.4 | actor_loss: -0.0037 | value_loss: 11.5801 | lr: 8.14e-05
  Update  382 | Ep  1465 | reward:     50.2 | mean(100):    104.3 | actor_loss: -0.0045 | value_loss: 7.0607 | lr: 8.07e-05
  Update  383 | Ep  1467 | reward:    173.3 | mean(100):    103.8 | actor_loss: -0.0027 | value_loss: 1.6657 | lr: 8.02e-05
  Update  384 | Ep  1469 | reward:     39.3 | mean(100):    102.1 | actor_loss: -0.0021 | value_loss: 3.3511 | lr: 7.99e-05
  Update  385 | Ep  1472 | reward:    172.5 | mean(100):    103.9 | actor_loss: -0.0035 | value_loss: 7.0745 | lr: 7.96e-05
  Update  386 | Ep  1476 | reward:    235.5 | mean(100):    101.4 | actor_loss: -0.0007 | value_loss: 8.5382 | lr: 7.92e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  387 | Ep  1480 | reward:    197.3 | mean(100):    104.9 | actor_loss: -0.0008 | value_loss: 9.3155 | lr: 7.86e-05
  Update  388 | Ep  1488 | reward:    223.6 | mean(100):    106.0 | actor_loss: -0.0015 | value_loss: 19.5904 | lr: 7.80e-05
  Update  389 | Ep  1492 | reward:    228.3 | mean(100):    108.0 | actor_loss: -0.0032 | value_loss: 10.3786 | lr: 7.68e-05
  Update  390 | Ep  1494 | reward:    137.2 | mean(100):    110.7 | actor_loss: -0.0051 | value_loss: 1.5667 | lr: 7.62e-05
  Update  391 | Ep  1498 | reward:    213.9 | mean(100):    113.5 | actor_loss: -0.0023 | value_loss: 9.4323 | lr: 7.59e-05
  Update  392 | Ep  1500 | reward:    -20.0 | mean(100):    111.0 | actor_loss: -0.0018 | value_loss: 4.4144 | lr: 7.53e-05
  Update  393 | Ep  1506 | reward:    203.8 | mean(100):    108.2 | actor_loss: -0.0018 | value_loss: 13.5617 | lr: 7.50e-05
  Update  394 | Ep  1508 | reward:     83.7 | mean(100):    109.2 | actor_loss: -0.0035 | value_loss: 3.6895 | lr: 7.41e-05
  Update  395 | Ep  1513 | reward:    177.4 | mean(100):    107.8 | actor_loss: -0.0019 | value_loss: 10.7306 | lr: 7.38e-05
  Update  396 | Ep  1517 | reward:     -7.5 | mean(100):    107.6 | actor_loss: -0.0028 | value_loss: 10.6185 | lr: 7.31e-05
  Update  397 | Ep  1521 | reward:    153.7 | mean(100):    109.7 | actor_loss: -0.0009 | value_loss: 8.6767 | lr: 7.25e-05
  Update  398 | Ep  1524 | reward:     96.9 | mean(100):    113.6 | actor_loss: -0.0015 | value_loss: 5.5219 | lr: 7.19e-05
  Update  399 | Ep  1529 | reward:    253.2 | mean(100):    121.6 | actor_loss: -0.0019 | value_loss: 8.9417 | lr: 7.14e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  400 | Ep  1535 | reward:     13.0 | mean(100):    118.5 | actor_loss: -0.0025 | value_loss: 12.8702 | lr: 7.07e-05
  Update  401 | Ep  1537 | reward:     91.7 | mean(100):    117.9 | actor_loss: -0.0036 | value_loss: 2.9459 | lr: 6.98e-05
  Update  402 | Ep  1541 | reward:     17.1 | mean(100):    114.4 | actor_loss: -0.0057 | value_loss: 8.2368 | lr: 6.95e-05
  Update  403 | Ep  1548 | reward:    214.8 | mean(100):    116.2 | actor_loss: -0.0016 | value_loss: 18.3774 | lr: 6.89e-05
  Update  404 | Ep  1554 | reward:    182.7 | mean(100):    117.1 | actor_loss: -0.0013 | value_loss: 14.0454 | lr: 6.78e-05
  Update  405 | Ep  1558 | reward:     44.5 | mean(100):    116.3 | actor_loss: -0.0033 | value_loss: 6.6989 | lr: 6.69e-05
  Update  406 | Ep  1560 | reward:    140.5 | mean(100):    118.8 | actor_loss: -0.0021 | value_loss: 1.7924 | lr: 6.63e-05
  Update  407 | Ep  1562 | reward:    114.4 | mean(100):    116.7 | actor_loss: -0.0023 | value_loss: 3.6769 | lr: 6.60e-05
  Update  408 | Ep  1567 | reward:     18.2 | mean(100):    114.0 | actor_loss: -0.0042 | value_loss: 11.4017 | lr: 6.57e-05
  Update  409 | Ep  1573 | reward:     -0.5 | mean(100):    111.2 | actor_loss: -0.0015 | value_loss: 12.3828 | lr: 6.50e-05
  Update  410 | Ep  1576 | reward:    143.9 | mean(100):    111.8 | actor_loss: -0.0004 | value_loss: 5.6503 | lr: 6.40e-05
  Update  411 | Ep  1582 | reward:     31.0 | mean(100):    109.4 | actor_loss: -0.0012 | value_loss: 15.9115 | lr: 6.36e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  412 | Ep  1585 | reward:     13.0 | mean(100):    106.0 | actor_loss: -0.0026 | value_loss: 6.2524 | lr: 6.27e-05
  Update  413 | Ep  1591 | reward:    200.4 | mean(100):    104.4 | actor_loss: -0.0028 | value_loss: 13.1298 | lr: 6.22e-05
  Update  414 | Ep  1597 | reward:     13.8 | mean(100):     98.5 | actor_loss: -0.0029 | value_loss: 14.0985 | lr: 6.14e-05
  Update  415 | Ep  1604 | reward:    -24.6 | mean(100):     98.5 | actor_loss: -0.0021 | value_loss: 17.9682 | lr: 6.04e-05
  Update  416 | Ep  1608 | reward:    -20.7 | mean(100):     99.3 | actor_loss: -0.0021 | value_loss: 8.4525 | lr: 5.94e-05
  Update  417 | Ep  1615 | reward:    -21.1 | mean(100):     93.0 | actor_loss: -0.0036 | value_loss: 17.3622 | lr: 5.88e-05
  Update  418 | Ep  1618 | reward:     -5.1 | mean(100):     90.3 | actor_loss: -0.0038 | value_loss: 9.6170 | lr: 5.77e-05
  Update  419 | Ep  1625 | reward:    -42.1 | mean(100):     76.9 | actor_loss: -0.0027 | value_loss: 21.1894 | lr: 5.73e-05
  Update  420 | Ep  1630 | reward:    183.1 | mean(100):     72.3 | actor_loss: -0.0033 | value_loss: 9.7943 | lr: 5.62e-05
  Update  421 | Ep  1633 | reward:    229.2 | mean(100):     75.3 | actor_loss: -0.0004 | value_loss: 8.1861 | lr: 5.55e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  422 | Ep  1637 | reward:    230.3 | mean(100):     78.0 | actor_loss: -0.0012 | value_loss: 7.6566 | lr: 5.50e-05
  Update  423 | Ep  1642 | reward:    152.7 | mean(100):     79.9 | actor_loss: -0.0007 | value_loss: 10.6000 | lr: 5.44e-05
  Update  424 | Ep  1645 | reward:    -11.2 | mean(100):     80.4 | actor_loss: -0.0025 | value_loss: 5.8288 | lr: 5.37e-05
  Update  425 | Ep  1649 | reward:     15.1 | mean(100):     77.0 | actor_loss: -0.0033 | value_loss: 9.2371 | lr: 5.32e-05
  Update  426 | Ep  1654 | reward:     -4.9 | mean(100):     74.6 | actor_loss: -0.0017 | value_loss: 11.7935 | lr: 5.26e-05
  Update  427 | Ep  1657 | reward:    104.7 | mean(100):     73.9 | actor_loss: -0.0013 | value_loss: 6.3522 | lr: 5.19e-05
  Update  428 | Ep  1663 | reward:      1.1 | mean(100):     71.0 | actor_loss: -0.0018 | value_loss: 14.0109 | lr: 5.14e-05
  Update  429 | Ep  1669 | reward:     26.5 | mean(100):     71.5 | actor_loss: -0.0049 | value_loss: 13.7550 | lr: 5.05e-05
  Update  430 | Ep  1676 | reward:    -33.6 | mean(100):     64.5 | actor_loss: -0.0014 | value_loss: 18.7562 | lr: 4.96e-05
  Update  431 | Ep  1682 | reward:     21.0 | mean(100):     64.4 | actor_loss: -0.0005 | value_loss: 15.1153 | lr: 4.86e-05
  Update  432 | Ep  1690 | reward:     -0.6 | mean(100):     57.2 | actor_loss: -0.0021 | value_loss: 22.7224 | lr: 4.77e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  433 | Ep  1696 | reward:     21.3 | mean(100):     56.9 | actor_loss: -0.0019 | value_loss: 13.8240 | lr: 4.65e-05
  Update  434 | Ep  1700 | reward:      6.3 | mean(100):     53.9 | actor_loss: -0.0032 | value_loss: 11.0858 | lr: 4.56e-05
  Update  435 | Ep  1704 | reward:    273.8 | mean(100):     57.9 | actor_loss: -0.0014 | value_loss: 8.7972 | lr: 4.50e-05
  Update  436 | Ep  1709 | reward:    122.7 | mean(100):     51.9 | actor_loss: -0.0006 | value_loss: 11.2900 | lr: 4.44e-05
  Update  437 | Ep  1714 | reward:    115.5 | mean(100):     54.4 | actor_loss: -0.0029 | value_loss: 12.0849 | lr: 4.36e-05
  Update  438 | Ep  1718 | reward:    115.9 | mean(100):     57.8 | actor_loss: -0.0030 | value_loss: 8.2455 | lr: 4.29e-05
  Update  439 | Ep  1720 | reward:    -25.3 | mean(100):     60.7 | actor_loss: -0.0010 | value_loss: 4.4989 | lr: 4.23e-05
  Update  440 | Ep  1727 | reward:      3.5 | mean(100):     64.2 | actor_loss: -0.0008 | value_loss: 17.5893 | lr: 4.20e-05
  Update  441 | Ep  1733 | reward:    134.9 | mean(100):     58.5 | actor_loss: -0.0014 | value_loss: 13.8697 | lr: 4.09e-05
  Update  442 | Ep  1735 | reward:    177.6 | mean(100):     59.0 | actor_loss: -0.0035 | value_loss: 6.2860 | lr: 4.00e-05
  Update  443 | Ep  1744 | reward:    -49.1 | mean(100):     51.8 | actor_loss: -0.0019 | value_loss: 25.4584 | lr: 3.97e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  444 | Ep  1747 | reward:     49.2 | mean(100):     54.4 | actor_loss: -0.0017 | value_loss: 4.9059 | lr: 3.84e-05
  Update  445 | Ep  1753 | reward:     40.4 | mean(100):     59.6 | actor_loss: -0.0007 | value_loss: 11.9910 | lr: 3.79e-05
  Update  446 | Ep  1757 | reward:     40.5 | mean(100):     64.1 | actor_loss: -0.0010 | value_loss: 10.0002 | lr: 3.71e-05
  Update  447 | Ep  1763 | reward:     20.5 | mean(100):     64.9 | actor_loss: -0.0015 | value_loss: 13.9147 | lr: 3.65e-05
  Update  448 | Ep  1768 | reward:    157.5 | mean(100):     67.6 | actor_loss: -0.0004 | value_loss: 12.5124 | lr: 3.56e-05
  Update  449 | Ep  1779 | reward:   -127.2 | mean(100):     69.1 | actor_loss: -0.0043 | value_loss: 28.5081 | lr: 3.48e-05
  Update  450 | Ep  1785 | reward:    -16.7 | mean(100):     67.3 | actor_loss: -0.0037 | value_loss: 13.6819 | lr: 3.32e-05
  Update  451 | Ep  1790 | reward:      2.1 | mean(100):     70.1 | actor_loss: -0.0011 | value_loss: 11.4612 | lr: 3.23e-05
  Update  452 | Ep  1793 | reward:    -20.5 | mean(100):     67.4 | actor_loss: -0.0007 | value_loss: 6.2334 | lr: 3.15e-05
  Update  453 | Ep  1798 | reward:     15.2 | mean(100):     68.8 | actor_loss: -0.0023 | value_loss: 10.6548 | lr: 3.11e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  454 | Ep  1804 | reward:    229.2 | mean(100):     65.6 | actor_loss: -0.0006 | value_loss: 14.5553 | lr: 3.03e-05
  Update  455 | Ep  1810 | reward:     99.0 | mean(100):     70.0 | actor_loss: -0.0018 | value_loss: 14.3331 | lr: 2.94e-05
  Update  456 | Ep  1812 | reward:    -54.4 | mean(100):     68.4 | actor_loss: -0.0002 | value_loss: 5.1881 | lr: 2.85e-05
  Update  457 | Ep  1817 | reward:     28.8 | mean(100):     70.0 | actor_loss: -0.0008 | value_loss: 13.1820 | lr: 2.82e-05
  Update  458 | Ep  1822 | reward:    225.7 | mean(100):     73.6 | actor_loss: -0.0005 | value_loss: 10.4505 | lr: 2.75e-05
  Update  459 | Ep  1827 | reward:    211.3 | mean(100):     74.5 | actor_loss: -0.0008 | value_loss: 10.4663 | lr: 2.67e-05
  Update  460 | Ep  1829 | reward:    123.6 | mean(100):     74.7 | actor_loss: -0.0010 | value_loss: 1.7900 | lr: 2.60e-05
  Update  461 | Ep  1832 | reward:    176.7 | mean(100):     76.5 | actor_loss: -0.0011 | value_loss: 7.4306 | lr: 2.57e-05
  Update  462 | Ep  1838 | reward:     -0.2 | mean(100):     75.4 | actor_loss: -0.0028 | value_loss: 13.7138 | lr: 2.52e-05
  Update  463 | Ep  1843 | reward:    130.7 | mean(100):     78.1 | actor_loss: -0.0011 | value_loss: 10.6722 | lr: 2.43e-05
  Update  464 | Ep  1848 | reward:    206.1 | mean(100):     79.1 | actor_loss: -0.0007 | value_loss: 10.7400 | lr: 2.36e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  465 | Ep  1852 | reward:     21.9 | mean(100):     77.6 | actor_loss: -0.0005 | value_loss: 7.9710 | lr: 2.28e-05
  Update  466 | Ep  1854 | reward:    176.3 | mean(100):     78.3 | actor_loss: -0.0019 | value_loss: 2.2289 | lr: 2.22e-05
  Update  467 | Ep  1856 | reward:    131.1 | mean(100):     76.9 | actor_loss: -0.0038 | value_loss: 2.4192 | lr: 2.19e-05
  Update  468 | Ep  1858 | reward:    196.7 | mean(100):     78.4 | actor_loss: -0.0032 | value_loss: 2.4189 | lr: 2.16e-05
  Update  469 | Ep  1860 | reward:     24.0 | mean(100):     80.2 | actor_loss: -0.0006 | value_loss: 4.0072 | lr: 2.13e-05
  Update  470 | Ep  1865 | reward:      6.4 | mean(100):     79.4 | actor_loss: -0.0025 | value_loss: 12.1041 | lr: 2.10e-05
  Update  471 | Ep  1867 | reward:    127.9 | mean(100):     81.0 | actor_loss: -0.0004 | value_loss: 3.8749 | lr: 2.03e-05
  Update  472 | Ep  1869 | reward:    113.3 | mean(100):     81.4 | actor_loss: -0.0003 | value_loss: 1.0813 | lr: 2.00e-05
  Update  473 | Ep  1871 | reward:    154.9 | mean(100):     81.6 | actor_loss: -0.0008 | value_loss: 2.9216 | lr: 1.96e-05
  Update  474 | Ep  1874 | reward:    203.7 | mean(100):     87.3 | actor_loss: -0.0001 | value_loss: 6.4550 | lr: 1.93e-05
  Update  475 | Ep  1876 | reward:    252.6 | mean(100):     91.1 | actor_loss: -0.0001 | value_loss: 3.9218 | lr: 1.89e-05
  Update  476 | Ep  1878 | reward:    219.3 | mean(100):     95.0 | actor_loss: -0.0003 | value_loss: 3.5793 | lr: 1.86e-05
  Update  477 | Ep  1884 | reward:   -118.2 | mean(100):     96.6 | actor_loss: -0.0003 | value_loss: 19.8558 | lr: 1.83e-05
  Update  478 | Ep  1886 | reward:    123.4 | mean(100):     97.6 | actor_loss: -0.0018 | value_loss: 2.3901 | lr: 1.74e-05
  Update  479 | Ep  1890 | reward:      2.7 | mean(100):     99.5 | actor_loss: -0.0020 | value_loss: 8.8911 | lr: 1.71e-05
  Update  480 | Ep  1894 | reward:    181.9 | mean(100):    105.2 | actor_loss: -0.0006 | value_loss: 9.3085 | lr: 1.65e-05
  Update  481 | Ep  1896 | reward:    151.9 | mean(100):    108.0 | actor_loss: -0.0002 | value_loss: 3.3262 | lr: 1.59e-05
  Update  482 | Ep  1899 | reward:    109.0 | mean(100):    110.5 | actor_loss: -0.0009 | value_loss: 8.6282 | lr: 1.56e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  483 | Ep  1905 | reward:    -26.9 | mean(100):    110.3 | actor_loss: -0.0026 | value_loss: 14.2517 | lr: 1.51e-05
  Update  484 | Ep  1907 | reward:    159.3 | mean(100):    110.7 | actor_loss: -0.0001 | value_loss: 5.5994 | lr: 1.42e-05
  Update  485 | Ep  1911 | reward:    179.2 | mean(100):    110.3 | actor_loss: -0.0009 | value_loss: 8.7671 | lr: 1.39e-05
  Update  486 | Ep  1915 | reward:      5.9 | mean(100):    109.3 | actor_loss: -0.0010 | value_loss: 9.2651 | lr: 1.33e-05
  Update  487 | Ep  1917 | reward:    121.8 | mean(100):    112.3 | actor_loss: -0.0001 | value_loss: 1.5824 | lr: 1.27e-05
  Update  488 | Ep  1920 | reward:    139.5 | mean(100):    112.1 | actor_loss: -0.0007 | value_loss: 6.2063 | lr: 1.24e-05
  Update  489 | Ep  1922 | reward:    155.4 | mean(100):    112.1 | actor_loss: -0.0001 | value_loss: 1.6985 | lr: 1.20e-05
  Update  490 | Ep  1927 | reward:    -35.4 | mean(100):    111.8 | actor_loss: -0.0018 | value_loss: 12.2590 | lr: 1.17e-05
  Update  491 | Ep  1929 | reward:    127.0 | mean(100):    111.5 | actor_loss: -0.0004 | value_loss: 1.2917 | lr: 1.09e-05
  Update  492 | Ep  1934 | reward:      1.4 | mean(100):    111.3 | actor_loss: -0.0002 | value_loss: 11.4199 | lr: 1.06e-05
  Update  493 | Ep  1938 | reward:    228.7 | mean(100):    117.1 | actor_loss: -0.0004 | value_loss: 9.5896 | lr: 9.90e-06
  Update  494 | Ep  1942 | reward:     17.1 | mean(100):    117.0 | actor_loss: -0.0001 | value_loss: 7.8380 | lr: 9.30e-06
  Update  495 | Ep  1945 | reward:    106.9 | mean(100):    115.0 | actor_loss: -0.0006 | value_loss: 6.0349 | lr: 8.70e-06
  Update  496 | Ep  1948 | reward:    263.3 | mean(100):    115.8 | actor_loss: -0.0001 | value_loss: 6.6364 | lr: 8.25e-06
  Update  497 | Ep  1952 | reward:    207.7 | mean(100):    121.1 | actor_loss: -0.0002 | value_loss: 10.3559 | lr: 7.80e-06
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
  Update  498 | Ep  1956 | reward:    155.0 | mean(100):    121.4 | actor_loss: -0.0001 | value_loss: 8.5523 | lr: 7.20e-06
  Update  499 | Ep  1958 | reward:     18.4 | mean(100):    119.5 | actor_loss: -0.0017 | value_loss: 3.4638 | lr: 6.60e-06
  Update  500 | Ep  1964 | reward:    212.6 | mean(100):    123.2 | actor_loss: 0.0000 | value_loss: 14.2321 | lr: 6.30e-06
  Update  501 | Ep  1966 | reward:    168.0 | mean(100):    123.8 | actor_loss: -0.0005 | value_loss: 1.5322 | lr: 5.40e-06
  Update  502 | Ep  1968 | reward:    133.8 | mean(100):    124.6 | actor_loss: -0.0001 | value_loss: 2.3979 | lr: 5.10e-06
  Update  503 | Ep  1970 | reward:    124.9 | mean(100):    125.2 | actor_loss: -0.0003 | value_loss: 1.1253 | lr: 4.80e-06
  Update  504 | Ep  1972 | reward:    100.0 | mean(100):    124.0 | actor_loss: -0.0001 | value_loss: 3.3209 | lr: 4.50e-06
  Update  505 | Ep  1976 | reward:    184.6 | mean(100):    121.4 | actor_loss: -0.0002 | value_loss: 8.6939 | lr: 4.20e-06
  Update  506 | Ep  1978 | reward:    139.0 | mean(100):    118.5 | actor_loss: -0.0000 | value_loss: 6.4290 | lr: 3.60e-06
  Update  507 | Ep  1980 | reward:    217.7 | mean(100):    120.7 | actor_loss: -0.0001 | value_loss: 3.7951 | lr: 3.30e-06
  Update  508 | Ep  1983 | reward:    199.3 | mean(100):    124.9 | actor_loss: -0.0001 | value_loss: 7.8487 | lr: 3.00e-06
  Update  509 | Ep  1985 | reward:    190.6 | mean(100):    128.6 | actor_loss: -0.0004 | value_loss: 2.1014 | lr: 2.55e-06
  Update  510 | Ep  1988 | reward:    227.2 | mean(100):    129.6 | actor_loss: -0.0000 | value_loss: 5.4539 | lr: 2.25e-06
  Update  511 | Ep  1991 | reward:    161.9 | mean(100):    134.4 | actor_loss: -0.0000 | value_loss: 5.4567 | lr: 1.80e-06
  Update  512 | Ep  1996 | reward:     -6.4 | mean(100):    129.2 | actor_loss: -0.0001 | value_loss: 11.5309 | lr: 1.35e-06
  Update  513 | Ep  2000 | reward:    207.6 | mean(100):    126.5 | actor_loss: -0.0000 | value_loss: 10.3877 | lr: 6.00e-07
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_4.png
