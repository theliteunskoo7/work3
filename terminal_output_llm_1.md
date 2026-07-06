Using device: cuda (rollout collection stays on CPU; batched updates use cuda)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  analyzer_threshold=200  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=unsloth/gemma-4-26B-A4B-it-GGUF

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2621 | mean p(bad) before update=0.2302 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2757 | mean p(bad) before update=0.2409 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    1 | Ep    22 | reward:    -85.4 | mean(100):   -191.1 | actor_loss: -0.0100 | value_loss: 72.8860 | lr: 3.00e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2215 | mean p(bad) before update=0.1934 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3164 | mean p(bad) before update=0.2699 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    2 | Ep    42 | reward:   -115.0 | mean(100):   -169.2 | actor_loss: -0.0100 | value_loss: 54.0695 | lr: 2.97e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2836 | mean p(bad) before update=0.2384 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2320 | mean p(bad) before update=0.2059 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    3 | Ep    66 | reward:   -169.1 | mean(100):   -147.6 | actor_loss: -0.0062 | value_loss: 46.0941 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3475 | mean p(bad) before update=0.2917 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1391 | mean p(bad) before update=0.1296 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    4 | Ep    87 | reward:   -355.4 | mean(100):   -143.0 | actor_loss: -0.0077 | value_loss: 49.7440 | lr: 2.90e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2076 | mean p(bad) before update=0.1874 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4019 | mean p(bad) before update=0.3209 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    5 | Ep   109 | reward:    -63.6 | mean(100):   -129.6 | actor_loss: -0.0050 | value_loss: 38.1330 | lr: 2.87e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2488 | mean p(bad) before update=0.2199 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2810 | mean p(bad) before update=0.2442 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    6 | Ep   129 | reward:    -84.7 | mean(100):   -113.9 | actor_loss: -0.0095 | value_loss: 41.3647 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2343 | mean p(bad) before update=0.2084 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2071 | mean p(bad) before update=0.1862 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2140 | mean p(bad) before update=0.1918 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    7 | Ep   150 | reward:   -104.2 | mean(100):   -113.0 | actor_loss: -0.0064 | value_loss: 41.0454 | lr: 2.81e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2935 | mean p(bad) before update=0.2541 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1490 | mean p(bad) before update=0.1373 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   173 | reward:   -106.1 | mean(100):   -107.6 | actor_loss: -0.0057 | value_loss: 33.6404 | lr: 2.77e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2029 | mean p(bad) before update=0.1796 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3840 | mean p(bad) before update=0.3050 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    9 | Ep   194 | reward:    -46.5 | mean(100):    -95.6 | actor_loss: -0.0055 | value_loss: 26.1816 | lr: 2.74e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3023 | mean p(bad) before update=0.2484 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1813 | mean p(bad) before update=0.1635 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   10 | Ep   215 | reward:    -60.0 | mean(100):    -92.7 | actor_loss: -0.0102 | value_loss: 28.9285 | lr: 2.71e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2524 | mean p(bad) before update=0.2040 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1687 | mean p(bad) before update=0.1488 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   233 | reward:    -20.5 | mean(100):    -79.5 | actor_loss: -0.0102 | value_loss: 23.2293 | lr: 2.68e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1748 | mean p(bad) before update=0.1586 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2790 | mean p(bad) before update=0.2309 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   251 | reward:    -57.4 | mean(100):    -66.9 | actor_loss: -0.0065 | value_loss: 19.9364 | lr: 2.65e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5254 | mean p(bad) before update=0.3967 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   269 | reward:   -134.4 | mean(100):    -57.6 | actor_loss: -0.0080 | value_loss: 24.4724 | lr: 2.62e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.7417 | mean p(bad) before update=0.4707 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3680 | mean p(bad) before update=0.2769 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   284 | reward:     -1.5 | mean(100):    -49.2 | actor_loss: -0.0055 | value_loss: 23.0402 | lr: 2.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1258 | mean p(bad) before update=0.1164 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   293 | reward:     -4.9 | mean(100):    -42.6 | actor_loss: -0.0086 | value_loss: 20.6202 | lr: 2.57e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   297 | reward:    -57.3 | mean(100):    -39.6 | actor_loss: -0.0066 | value_loss: 23.1086 | lr: 2.56e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2266 | mean p(bad) before update=0.1906 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   302 | reward:     38.2 | mean(100):    -34.9 | actor_loss: -0.0087 | value_loss: 17.6295 | lr: 2.55e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   18 | Ep   304 | reward:     12.6 | mean(100):    -34.0 | actor_loss: -0.0047 | value_loss: 15.0826 | lr: 2.55e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.7688 | mean p(bad) before update=0.5039 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   19 | Ep   310 | reward:    -32.0 | mean(100):    -27.8 | actor_loss: -0.0096 | value_loss: 17.4422 | lr: 2.54e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   20 | Ep   312 | reward:     53.9 | mean(100):    -25.5 | actor_loss: -0.0075 | value_loss: 9.2459 | lr: 2.53e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   314 | reward:    -27.9 | mean(100):    -23.3 | actor_loss: -0.0061 | value_loss: 11.3282 | lr: 2.53e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   22 | Ep   318 | reward:    -58.4 | mean(100):    -21.5 | actor_loss: -0.0025 | value_loss: 16.2602 | lr: 2.53e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2750 | mean p(bad) before update=0.2357 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   23 | Ep   321 | reward:      8.3 | mean(100):    -21.0 | actor_loss: -0.0062 | value_loss: 11.4705 | lr: 2.52e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   24 | Ep   324 | reward:    -82.0 | mean(100):    -18.9 | actor_loss: -0.0078 | value_loss: 13.3563 | lr: 2.52e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   25 | Ep   326 | reward:     43.7 | mean(100):    -16.0 | actor_loss: -0.0028 | value_loss: 8.3972 | lr: 2.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   26 | Ep   328 | reward:     -6.3 | mean(100):    -14.0 | actor_loss: -0.0014 | value_loss: 10.0653 | lr: 2.51e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.1888 | mean p(bad) before update=0.1619 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   27 | Ep   330 | reward:     81.7 | mean(100):    -11.7 | actor_loss: -0.0039 | value_loss: 8.6376 | lr: 2.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   28 | Ep   332 | reward:    104.3 | mean(100):    -10.1 | actor_loss: -0.0044 | value_loss: 8.7050 | lr: 2.50e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   29 | Ep   335 | reward:     28.6 | mean(100):     -9.9 | actor_loss: -0.0035 | value_loss: 11.9494 | lr: 2.50e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   30 | Ep   337 | reward:      8.6 | mean(100):     -7.1 | actor_loss: -0.0035 | value_loss: 8.5857 | lr: 2.50e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   31 | Ep   339 | reward:     33.4 | mean(100):     -5.6 | actor_loss: -0.0042 | value_loss: 4.3306 | lr: 2.49e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.4556 | mean p(bad) before update=0.3317 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   32 | Ep   341 | reward:     70.3 | mean(100):     -2.9 | actor_loss: -0.0026 | value_loss: 5.1746 | lr: 2.49e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   33 | Ep   343 | reward:     95.8 | mean(100):     -0.6 | actor_loss: -0.0058 | value_loss: 5.1106 | lr: 2.49e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   34 | Ep   345 | reward:   -123.7 | mean(100):     -0.2 | actor_loss: -0.0043 | value_loss: 9.3428 | lr: 2.49e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   35 | Ep   347 | reward:     27.9 | mean(100):      0.1 | actor_loss: -0.0034 | value_loss: 7.2654 | lr: 2.48e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   36 | Ep   349 | reward:     67.5 | mean(100):      2.0 | actor_loss: -0.0044 | value_loss: 5.9215 | lr: 2.48e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4751 | mean p(bad) before update=0.3628 | ul_lr=9.88e-05 (scale=0.99)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   37 | Ep   351 | reward:    -75.6 | mean(100):      2.3 | actor_loss: -0.0054 | value_loss: 6.9726 | lr: 2.48e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   38 | Ep   353 | reward:     35.5 | mean(100):      3.3 | actor_loss: -0.0049 | value_loss: 5.5459 | lr: 2.47e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   39 | Ep   355 | reward:     50.9 | mean(100):      5.3 | actor_loss: -0.0037 | value_loss: 4.2869 | lr: 2.47e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   40 | Ep   358 | reward:    -84.6 | mean(100):      5.3 | actor_loss: -0.0058 | value_loss: 8.9682 | lr: 2.47e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.6045 | mean p(bad) before update=0.4297 | ul_lr=9.75e-05 (scale=0.97)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   41 | Ep   360 | reward:   -171.6 | mean(100):      5.1 | actor_loss: -0.0047 | value_loss: 10.8859 | lr: 2.46e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   42 | Ep   362 | reward:     90.9 | mean(100):      8.1 | actor_loss: -0.0032 | value_loss: 4.7328 | lr: 2.46e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   43 | Ep   365 | reward:    -35.6 | mean(100):      8.4 | actor_loss: -0.0021 | value_loss: 7.7606 | lr: 2.46e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   44 | Ep   368 | reward:    -11.9 | mean(100):      8.5 | actor_loss: -0.0028 | value_loss: 9.2734 | lr: 2.45e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3211 | mean p(bad) before update=0.2660 | ul_lr=9.41e-05 (scale=0.94)
  Update   45 | Ep   370 | reward:     87.9 | mean(100):     11.8 | actor_loss: -0.0047 | value_loss: 5.6429 | lr: 2.45e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   46 | Ep   372 | reward:     19.2 | mean(100):     12.8 | actor_loss: -0.0015 | value_loss: 4.5408 | lr: 2.44e-04
  Update   47 | Ep   374 | reward:     74.3 | mean(100):     14.1 | actor_loss: -0.0025 | value_loss: 3.7833 | lr: 2.44e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   48 | Ep   376 | reward:   -193.4 | mean(100):     13.5 | actor_loss: -0.0088 | value_loss: 10.1334 | lr: 2.44e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   49 | Ep   378 | reward:     78.4 | mean(100):     15.7 | actor_loss: -0.0041 | value_loss: 3.7637 | lr: 2.44e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.4460 | mean p(bad) before update=0.3503 | ul_lr=9.11e-05 (scale=0.91)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   50 | Ep   380 | reward:    105.2 | mean(100):     17.7 | actor_loss: -0.0050 | value_loss: 3.8988 | lr: 2.43e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   51 | Ep   382 | reward:    112.6 | mean(100):     20.4 | actor_loss: -0.0009 | value_loss: 4.8078 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   52 | Ep   384 | reward:     85.5 | mean(100):     23.9 | actor_loss: -0.0075 | value_loss: 4.9120 | lr: 2.43e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   53 | Ep   386 | reward:    144.3 | mean(100):     25.8 | actor_loss: -0.0042 | value_loss: 4.8115 | lr: 2.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   54 | Ep   388 | reward:    135.9 | mean(100):     28.4 | actor_loss: -0.0018 | value_loss: 5.0126 | lr: 2.42e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.5024 | mean p(bad) before update=0.3619 | ul_lr=8.53e-05 (scale=0.85)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   55 | Ep   390 | reward:     96.2 | mean(100):     29.4 | actor_loss: -0.0027 | value_loss: 4.3989 | lr: 2.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   56 | Ep   392 | reward:    107.4 | mean(100):     30.7 | actor_loss: -0.0037 | value_loss: 4.0826 | lr: 2.41e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   57 | Ep   394 | reward:     50.7 | mean(100):     32.5 | actor_loss: -0.0029 | value_loss: 3.3355 | lr: 2.41e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   58 | Ep   396 | reward:     85.1 | mean(100):     33.7 | actor_loss: -0.0030 | value_loss: 3.3715 | lr: 2.41e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   59 | Ep   398 | reward:     93.0 | mean(100):     35.6 | actor_loss: -0.0019 | value_loss: 3.5076 | lr: 2.41e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.9015 | mean p(bad) before update=0.5265 | ul_lr=8.08e-05 (scale=0.81)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   60 | Ep   400 | reward:     29.7 | mean(100):     38.3 | actor_loss: -0.0034 | value_loss: 6.7395 | lr: 2.40e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   61 | Ep   402 | reward:    114.3 | mean(100):     39.1 | actor_loss: -0.0002 | value_loss: 4.2128 | lr: 2.40e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   62 | Ep   404 | reward:     74.0 | mean(100):     41.3 | actor_loss: -0.0049 | value_loss: 2.8736 | lr: 2.40e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   63 | Ep   406 | reward:     75.5 | mean(100):     43.2 | actor_loss: -0.0036 | value_loss: 2.7193 | lr: 2.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   64 | Ep   408 | reward:     82.6 | mean(100):     43.7 | actor_loss: -0.0025 | value_loss: 2.7353 | lr: 2.39e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3113 | mean p(bad) before update=0.2484 | ul_lr=7.72e-05 (scale=0.77)
  Update   65 | Ep   410 | reward:     56.1 | mean(100):     45.5 | actor_loss: -0.0006 | value_loss: 2.7579 | lr: 2.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   66 | Ep   412 | reward:     63.8 | mean(100):     45.6 | actor_loss: -0.0040 | value_loss: 3.4203 | lr: 2.38e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   67 | Ep   414 | reward:     65.0 | mean(100):     46.2 | actor_loss: -0.0044 | value_loss: 3.1614 | lr: 2.38e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   68 | Ep   416 | reward:     88.7 | mean(100):     48.8 | actor_loss: -0.0027 | value_loss: 3.3575 | lr: 2.38e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   69 | Ep   418 | reward:     86.5 | mean(100):     50.4 | actor_loss: -0.0024 | value_loss: 3.2769 | lr: 2.38e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4967 | mean p(bad) before update=0.3349 | ul_lr=7.43e-05 (scale=0.74)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   70 | Ep   420 | reward:     47.4 | mean(100):     51.3 | actor_loss: -0.0043 | value_loss: 2.8885 | lr: 2.37e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   71 | Ep   422 | reward:     89.7 | mean(100):     52.0 | actor_loss: -0.0010 | value_loss: 3.5665 | lr: 2.37e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   72 | Ep   424 | reward:     75.6 | mean(100):     54.8 | actor_loss: -0.0027 | value_loss: 3.5882 | lr: 2.37e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   73 | Ep   426 | reward:    225.6 | mean(100):     57.0 | actor_loss: -0.0010 | value_loss: 7.2612 | lr: 2.36e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   74 | Ep   428 | reward:     57.1 | mean(100):     58.0 | actor_loss: -0.0019 | value_loss: 2.9598 | lr: 2.36e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.5521 | mean p(bad) before update=0.4233 | ul_lr=7.12e-05 (scale=0.71)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   75 | Ep   430 | reward:     43.2 | mean(100):     57.6 | actor_loss: -0.0030 | value_loss: 2.2808 | lr: 2.36e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   76 | Ep   432 | reward:     44.1 | mean(100):     58.3 | actor_loss: -0.0026 | value_loss: 2.9174 | lr: 2.35e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   77 | Ep   434 | reward:     41.7 | mean(100):     60.5 | actor_loss: 0.0002 | value_loss: 2.7029 | lr: 2.35e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   78 | Ep   436 | reward:     97.0 | mean(100):     60.8 | actor_loss: -0.0041 | value_loss: 3.0977 | lr: 2.35e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   79 | Ep   438 | reward:     92.9 | mean(100):     61.5 | actor_loss: -0.0029 | value_loss: 2.6267 | lr: 2.35e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3770 | mean p(bad) before update=0.2811 | ul_lr=6.91e-05 (scale=0.69)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   80 | Ep   440 | reward:    121.5 | mean(100):     61.8 | actor_loss: -0.0025 | value_loss: 2.5650 | lr: 2.34e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   81 | Ep   442 | reward:    103.8 | mean(100):     62.6 | actor_loss: -0.0017 | value_loss: 2.6772 | lr: 2.34e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   82 | Ep   444 | reward:    137.3 | mean(100):     63.1 | actor_loss: -0.0011 | value_loss: 4.3510 | lr: 2.34e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   83 | Ep   446 | reward:     44.3 | mean(100):     65.7 | actor_loss: -0.0024 | value_loss: 3.7189 | lr: 2.33e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   84 | Ep   448 | reward:    216.2 | mean(100):     68.0 | actor_loss: -0.0156 | value_loss: 6.6991 | lr: 2.33e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.4893 | mean p(bad) before update=0.3753 | ul_lr=6.58e-05 (scale=0.66)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   85 | Ep   450 | reward:     56.6 | mean(100):     68.4 | actor_loss: -0.0039 | value_loss: 2.5629 | lr: 2.33e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   86 | Ep   452 | reward:     25.6 | mean(100):     69.8 | actor_loss: -0.0051 | value_loss: 2.6062 | lr: 2.32e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   87 | Ep   454 | reward:     66.8 | mean(100):     71.8 | actor_loss: -0.0039 | value_loss: 7.5191 | lr: 2.32e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  Update   88 | Ep   456 | reward:     60.8 | mean(100):     73.4 | actor_loss: -0.0016 | value_loss: 2.5010 | lr: 2.32e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   89 | Ep   458 | reward:     43.8 | mean(100):     75.3 | actor_loss: -0.0045 | value_loss: 2.0958 | lr: 2.32e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.1160 | mean p(bad) before update=0.1095 | ul_lr=6.09e-05 (scale=0.61)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   90 | Ep   460 | reward:     59.2 | mean(100):     78.2 | actor_loss: -0.0010 | value_loss: 4.0685 | lr: 2.31e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   91 | Ep   462 | reward:    100.0 | mean(100):     78.4 | actor_loss: 0.0004 | value_loss: 3.3680 | lr: 2.31e-04

  Update   92 | Ep   464 | reward:     66.5 | mean(100):     79.2 | actor_loss: -0.0021 | value_loss: 3.4094 | lr: 2.31e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  Update   93 | Ep   466 | reward:     53.4 | mean(100):     81.4 | actor_loss: -0.0022 | value_loss: 2.5093 | lr: 2.30e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   94 | Ep   468 | reward:     55.6 | mean(100):     83.1 | actor_loss: -0.0014 | value_loss: 3.0100 | lr: 2.30e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1452 | mean p(bad) before update=0.1302 | ul_lr=5.84e-05 (scale=0.58)
  Update   95 | Ep   470 | reward:     93.7 | mean(100):     83.2 | actor_loss: -0.0043 | value_loss: 3.1395 | lr: 2.30e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   96 | Ep   472 | reward:    118.8 | mean(100):     83.9 | actor_loss: -0.0007 | value_loss: 3.6843 | lr: 2.29e-04

  Update   97 | Ep   474 | reward:     67.9 | mean(100):     84.3 | actor_loss: -0.0008 | value_loss: 5.0183 | lr: 2.29e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   98 | Ep   476 | reward:     59.3 | mean(100):     86.6 | actor_loss: -0.0014 | value_loss: 2.1277 | lr: 2.29e-04

  Update   99 | Ep   478 | reward:     75.9 | mean(100):     86.9 | actor_loss: -0.0036 | value_loss: 2.5545 | lr: 2.29e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.0021 | mean p(bad) before update=0.5729 | ul_lr=5.64e-05 (scale=0.56)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  100 | Ep   480 | reward:    112.6 | mean(100):     87.1 | actor_loss: -0.0016 | value_loss: 3.9001 | lr: 2.28e-04
  Update  101 | Ep   482 | reward:     69.3 | mean(100):     86.3 | actor_loss: 0.0000 | value_loss: 2.5282 | lr: 2.28e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  102 | Ep   484 | reward:     30.4 | mean(100):     86.2 | actor_loss: -0.0001 | value_loss: 2.9685 | lr: 2.28e-04

  Update  103 | Ep   486 | reward:     28.0 | mean(100):     85.0 | actor_loss: -0.0015 | value_loss: 3.1769 | lr: 2.27e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  104 | Ep   488 | reward:     52.0 | mean(100):     83.6 | actor_loss: -0.0018 | value_loss: 2.3457 | lr: 2.27e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.0018 | mean p(bad) before update=0.0018 | ul_lr=5.75e-05 (scale=0.58)
  Update  105 | Ep   490 | reward:    112.9 | mean(100):     85.0 | actor_loss: -0.0013 | value_loss: 3.1010 | lr: 2.27e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  106 | Ep   492 | reward:    104.0 | mean(100):     85.6 | actor_loss: 0.0010 | value_loss: 2.7585 | lr: 2.26e-04

  Update  107 | Ep   494 | reward:     86.3 | mean(100):     85.6 | actor_loss: -0.0021 | value_loss: 3.0840 | lr: 2.26e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  108 | Ep   496 | reward:     81.4 | mean(100):     85.7 | actor_loss: 0.0001 | value_loss: 2.6285 | lr: 2.26e-04

  Update  109 | Ep   498 | reward:    122.6 | mean(100):     86.3 | actor_loss: -0.0017 | value_loss: 2.9784 | lr: 2.26e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3746 | mean p(bad) before update=0.2942 | ul_lr=5.71e-05 (scale=0.57)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  110 | Ep   500 | reward:     75.6 | mean(100):     85.8 | actor_loss: -0.0021 | value_loss: 2.6708 | lr: 2.25e-04
  Update  111 | Ep   502 | reward:     67.3 | mean(100):     85.0 | actor_loss: -0.0014 | value_loss: 2.3405 | lr: 2.25e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  112 | Ep   504 | reward:     84.7 | mean(100):     85.1 | actor_loss: -0.0039 | value_loss: 3.2102 | lr: 2.25e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  Update  113 | Ep   506 | reward:     71.0 | mean(100):     85.7 | actor_loss: -0.0090 | value_loss: 5.2733 | lr: 2.24e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  114 | Ep   508 | reward:     58.6 | mean(100):     85.8 | actor_loss: -0.0018 | value_loss: 2.7009 | lr: 2.24e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.1321 | mean p(bad) before update=0.5628 | ul_lr=5.74e-05 (scale=0.57)
  Update  115 | Ep   510 | reward:     41.1 | mean(100):     85.3 | actor_loss: -0.0015 | value_loss: 2.6771 | lr: 2.24e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  116 | Ep   512 | reward:     82.2 | mean(100):     85.1 | actor_loss: -0.0028 | value_loss: 1.6891 | lr: 2.23e-04

  Update  117 | Ep   514 | reward:     47.7 | mean(100):     85.1 | actor_loss: -0.0010 | value_loss: 2.1422 | lr: 2.23e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  118 | Ep   516 | reward:     72.2 | mean(100):     84.8 | actor_loss: -0.0012 | value_loss: 2.3611 | lr: 2.23e-04

  Update  119 | Ep   518 | reward:     57.0 | mean(100):     84.2 | actor_loss: -0.0014 | value_loss: 2.2120 | lr: 2.23e-04
  [Analyzer] 2 episodes -> 4 bad pairs (4 dropped by adv filter, 0 applied)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  120 | Ep   520 | reward:     99.9 | mean(100):     85.4 | actor_loss: 0.0007 | value_loss: 3.9736 | lr: 2.22e-04

  Update  121 | Ep   522 | reward:     66.3 | mean(100):     85.2 | actor_loss: 0.0006 | value_loss: 3.6671 | lr: 2.22e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  122 | Ep   524 | reward:     73.6 | mean(100):     84.9 | actor_loss: -0.0026 | value_loss: 2.4953 | lr: 2.22e-04

  Update  123 | Ep   526 | reward:     78.8 | mean(100):     82.7 | actor_loss: -0.0013 | value_loss: 2.3888 | lr: 2.21e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  124 | Ep   528 | reward:     50.1 | mean(100):     82.9 | actor_loss: -0.0029 | value_loss: 2.7700 | lr: 2.21e-04
  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.3401 | mean p(bad) before update=0.2874 | ul_lr=5.84e-05 (scale=0.58)
  Update  125 | Ep   530 | reward:     93.9 | mean(100):     83.2 | actor_loss: -0.0033 | value_loss: 2.7807 | lr: 2.21e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  126 | Ep   532 | reward:     72.0 | mean(100):     82.8 | actor_loss: -0.0005 | value_loss: 2.8033 | lr: 2.20e-04
  Update  127 | Ep   534 | reward:     66.4 | mean(100):     82.3 | actor_loss: -0.0011 | value_loss: 2.5417 | lr: 2.20e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  128 | Ep   536 | reward:     52.5 | mean(100):     81.2 | actor_loss: -0.0013 | value_loss: 2.3942 | lr: 2.20e-04
  Update  129 | Ep   538 | reward:    109.1 | mean(100):     81.0 | actor_loss: -0.0021 | value_loss: 2.8855 | lr: 2.20e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.6930 | mean p(bad) before update=0.7454 | ul_lr=5.94e-05 (scale=0.59)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  130 | Ep   540 | reward:    155.3 | mean(100):     81.2 | actor_loss: -0.0072 | value_loss: 4.8217 | lr: 2.19e-04
  Update  131 | Ep   542 | reward:     63.6 | mean(100):     80.0 | actor_loss: -0.0026 | value_loss: 2.8380 | lr: 2.19e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  132 | Ep   544 | reward:     51.6 | mean(100):     79.2 | actor_loss: -0.0022 | value_loss: 2.7653 | lr: 2.19e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  133 | Ep   546 | reward:     21.5 | mean(100):     79.5 | actor_loss: -0.0030 | value_loss: 2.9869 | lr: 2.18e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  134 | Ep   548 | reward:     63.0 | mean(100):     78.1 | actor_loss: -0.0025 | value_loss: 1.9285 | lr: 2.18e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.8407 | mean p(bad) before update=0.5047 | ul_lr=6.10e-05 (scale=0.61)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  135 | Ep   550 | reward:     44.4 | mean(100):     78.0 | actor_loss: -0.0019 | value_loss: 2.5151 | lr: 2.18e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  136 | Ep   552 | reward:     99.2 | mean(100):     78.9 | actor_loss: -0.0057 | value_loss: 2.6730 | lr: 2.17e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  137 | Ep   554 | reward:     64.0 | mean(100):     77.7 | actor_loss: 0.0005 | value_loss: 2.8763 | lr: 2.17e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  138 | Ep   556 | reward:     68.5 | mean(100):     78.2 | actor_loss: 0.0004 | value_loss: 2.9565 | lr: 2.17e-04
  Update  139 | Ep   558 | reward:    241.4 | mean(100):     80.6 | actor_loss: -0.0001 | value_loss: 5.8632 | lr: 2.17e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.4488 | mean p(bad) before update=0.4626 | ul_lr=6.01e-05 (scale=0.60)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  140 | Ep   560 | reward:     53.3 | mean(100):     79.9 | actor_loss: -0.0010 | value_loss: 2.1155 | lr: 2.16e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  141 | Ep   562 | reward:     79.2 | mean(100):     79.1 | actor_loss: 0.0005 | value_loss: 2.1783 | lr: 2.16e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  142 | Ep   564 | reward:     91.3 | mean(100):     79.1 | actor_loss: -0.0007 | value_loss: 2.2056 | lr: 2.16e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  143 | Ep   566 | reward:    134.4 | mean(100):     79.9 | actor_loss: -0.0013 | value_loss: 2.4682 | lr: 2.15e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  144 | Ep   568 | reward:     69.0 | mean(100):     81.3 | actor_loss: 0.0005 | value_loss: 4.6952 | lr: 2.15e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.2962 | mean p(bad) before update=0.2259 | ul_lr=5.94e-05 (scale=0.59)
  Update  145 | Ep   570 | reward:     85.1 | mean(100):     81.1 | actor_loss: 0.0021 | value_loss: 2.1034 | lr: 2.15e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  146 | Ep   572 | reward:    133.8 | mean(100):     81.0 | actor_loss: -0.0011 | value_loss: 2.3002 | lr: 2.15e-04

  Update  147 | Ep   574 | reward:     94.5 | mean(100):     82.3 | actor_loss: -0.0023 | value_loss: 4.5275 | lr: 2.14e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  148 | Ep   576 | reward:    110.3 | mean(100):     83.2 | actor_loss: -0.0033 | value_loss: 2.6980 | lr: 2.14e-04

  Update  149 | Ep   578 | reward:    178.8 | mean(100):     83.6 | actor_loss: -0.0015 | value_loss: 3.7147 | lr: 2.14e-04
  [Analyzer] 2 episodes -> 4 bad pairs (3 dropped by adv filter) | unlikelihood_loss=0.2059 | mean p(bad) before update=0.1861 | ul_lr=5.83e-05 (scale=0.58)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  150 | Ep   580 | reward:     85.5 | mean(100):     83.5 | actor_loss: 0.0021 | value_loss: 2.0059 | lr: 2.13e-04
  Update  151 | Ep   582 | reward:    107.1 | mean(100):     84.0 | actor_loss: -0.0025 | value_loss: 2.2609 | lr: 2.13e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  152 | Ep   584 | reward:     85.3 | mean(100):     84.3 | actor_loss: -0.0046 | value_loss: 1.9179 | lr: 2.13e-04

  Update  153 | Ep   586 | reward:     85.0 | mean(100):     84.6 | actor_loss: -0.0043 | value_loss: 1.4663 | lr: 2.12e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  154 | Ep   588 | reward:    113.2 | mean(100):     85.3 | actor_loss: 0.0001 | value_loss: 1.9778 | lr: 2.12e-04

  [Analyzer failed: Expecting value: line 1 column 1 (char 0)] — skipping unlikelihood update this round
  [Analyzer] 2 episodes -> 0 bad pairs (0 dropped by adv filter, 0 applied)
  Update  155 | Ep   590 | reward:     79.3 | mean(100):     84.8 | actor_loss: -0.0023 | value_loss: 1.7736 | lr: 2.12e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  156 | Ep   592 | reward:    127.7 | mean(100):     85.3 | actor_loss: -0.0004 | value_loss: 3.1088 | lr: 2.11e-04

  Update  157 | Ep   594 | reward:     71.0 | mean(100):     85.3 | actor_loss: -0.0034 | value_loss: 1.1914 | lr: 2.11e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  158 | Ep   596 | reward:    122.9 | mean(100):     85.2 | actor_loss: -0.0009 | value_loss: 2.2488 | lr: 2.11e-04

  Update  159 | Ep   598 | reward:     79.9 | mean(100):     84.6 | actor_loss: 0.0002 | value_loss: 1.2304 | lr: 2.11e-04
  [Analyzer] 2 episodes -> 4 bad pairs (3 dropped by adv filter) | unlikelihood_loss=0.3597 | mean p(bad) before update=0.3021 | ul_lr=5.76e-05 (scale=0.58)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  160 | Ep   600 | reward:     93.4 | mean(100):     84.8 | actor_loss: -0.0009 | value_loss: 2.0821 | lr: 2.10e-04
  Update  161 | Ep   602 | reward:     85.8 | mean(100):     85.4 | actor_loss: -0.0013 | value_loss: 1.7934 | lr: 2.10e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  162 | Ep   604 | reward:    174.8 | mean(100):     86.7 | actor_loss: -0.0015 | value_loss: 4.2377 | lr: 2.10e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  Update  163 | Ep   606 | reward:     79.8 | mean(100):     86.0 | actor_loss: -0.0019 | value_loss: 1.8257 | lr: 2.09e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  164 | Ep   608 | reward:     99.1 | mean(100):     86.1 | actor_loss: 0.0004 | value_loss: 2.4898 | lr: 2.09e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=2.5868 | mean p(bad) before update=0.8443 | ul_lr=5.67e-05 (scale=0.57)
  Update  165 | Ep   610 | reward:     92.0 | mean(100):     86.5 | actor_loss: -0.0044 | value_loss: 1.6487 | lr: 2.09e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  166 | Ep   612 | reward:     66.3 | mean(100):     86.2 | actor_loss: -0.0028 | value_loss: 1.3764 | lr: 2.08e-04
  Update  167 | Ep   614 | reward:    107.9 | mean(100):     87.1 | actor_loss: -0.0027 | value_loss: 2.2738 | lr: 2.08e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  168 | Ep   616 | reward:     85.1 | mean(100):     87.2 | actor_loss: 0.0006 | value_loss: 1.7977 | lr: 2.08e-04

  Update  169 | Ep   618 | reward:     94.4 | mean(100):     87.6 | actor_loss: 0.0012 | value_loss: 1.7751 | lr: 2.08e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5541 | mean p(bad) before update=0.2858 | ul_lr=5.61e-05 (scale=0.56)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  170 | Ep   620 | reward:    143.1 | mean(100):     87.8 | actor_loss: -0.0025 | value_loss: 3.5125 | lr: 2.07e-04
  Update  171 | Ep   622 | reward:    169.2 | mean(100):     88.9 | actor_loss: -0.0005 | value_loss: 3.9443 | lr: 2.07e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  172 | Ep   624 | reward:     89.5 | mean(100):     89.3 | actor_loss: 0.0004 | value_loss: 1.9777 | lr: 2.07e-04
  Update  173 | Ep   626 | reward:     81.1 | mean(100):     89.6 | actor_loss: -0.0004 | value_loss: 1.9381 | lr: 2.06e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  174 | Ep   628 | reward:     38.0 | mean(100):     88.8 | actor_loss: -0.0021 | value_loss: 1.8151 | lr: 2.06e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.9474 | mean p(bad) before update=0.8548 | ul_lr=5.59e-05 (scale=0.56)
  Update  175 | Ep   630 | reward:     24.9 | mean(100):     88.2 | actor_loss: -0.0032 | value_loss: 1.5121 | lr: 2.06e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  176 | Ep   632 | reward:    109.8 | mean(100):     89.0 | actor_loss: 0.0006 | value_loss: 1.4303 | lr: 2.06e-04

  Update  177 | Ep   634 | reward:     37.4 | mean(100):     89.7 | actor_loss: -0.0011 | value_loss: 2.2036 | lr: 2.05e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  178 | Ep   636 | reward:    146.0 | mean(100):     92.3 | actor_loss: -0.0007 | value_loss: 6.1468 | lr: 2.05e-04

  Update  179 | Ep   638 | reward:     84.5 | mean(100):     92.4 | actor_loss: -0.0030 | value_loss: 1.2580 | lr: 2.05e-04
  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=1.3796 | mean p(bad) before update=0.5261 | ul_lr=5.39e-05 (scale=0.54)
  Update  180 | Ep   640 | reward:     66.9 | mean(100):     92.2 | actor_loss: 0.0006 | value_loss: 1.7118 | lr: 2.04e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  181 | Ep   642 | reward:     81.0 | mean(100):     93.0 | actor_loss: -0.0025 | value_loss: 1.7718 | lr: 2.04e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  182 | Ep   644 | reward:    191.3 | mean(100):     94.5 | actor_loss: 0.0010 | value_loss: 4.1395 | lr: 2.04e-04

  Update  183 | Ep   646 | reward:     64.9 | mean(100):     94.3 | actor_loss: -0.0027 | value_loss: 1.1351 | lr: 2.03e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  184 | Ep   648 | reward:    174.9 | mean(100):     96.8 | actor_loss: -0.0055 | value_loss: 5.9066 | lr: 2.03e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.1254 | mean p(bad) before update=0.1130 | ul_lr=5.11e-05 (scale=0.51)
  Update  185 | Ep   650 | reward:    158.6 | mean(100):     97.8 | actor_loss: -0.0009 | value_loss: 3.4367 | lr: 2.03e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  186 | Ep   652 | reward:     87.2 | mean(100):     97.3 | actor_loss: -0.0012 | value_loss: 1.2735 | lr: 2.02e-04
  Update  187 | Ep   654 | reward:     72.9 | mean(100):     97.9 | actor_loss: -0.0006 | value_loss: 2.8801 | lr: 2.02e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  188 | Ep   656 | reward:     83.6 | mean(100):     97.5 | actor_loss: -0.0020 | value_loss: 1.6415 | lr: 2.02e-04
  Update  189 | Ep   658 | reward:     70.4 | mean(100):     95.4 | actor_loss: -0.0044 | value_loss: 2.2196 | lr: 2.02e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.4105 | mean p(bad) before update=0.5620 | ul_lr=5.20e-05 (scale=0.52)
  Update  190 | Ep   660 | reward:     82.5 | mean(100):     95.9 | actor_loss: -0.0025 | value_loss: 1.1957 | lr: 2.01e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  191 | Ep   662 | reward:     61.7 | mean(100):     95.9 | actor_loss: 0.0005 | value_loss: 1.3723 | lr: 2.01e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  192 | Ep   664 | reward:     84.3 | mean(100):     96.5 | actor_loss: 0.0017 | value_loss: 1.2122 | lr: 2.01e-04

  Update  193 | Ep   666 | reward:    156.4 | mean(100):     98.0 | actor_loss: -0.0008 | value_loss: 5.8589 | lr: 2.00e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  194 | Ep   668 | reward:     56.7 | mean(100):     96.3 | actor_loss: -0.0024 | value_loss: 1.2189 | lr: 2.00e-04

  [Analyzer] 2 episodes -> 4 bad pairs (4 dropped by adv filter, 0 applied)
  Update  195 | Ep   670 | reward:     95.4 | mean(100):     96.3 | actor_loss: 0.0025 | value_loss: 1.5278 | lr: 2.00e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  196 | Ep   672 | reward:     77.7 | mean(100):     95.5 | actor_loss: -0.0036 | value_loss: 1.1536 | lr: 1.99e-04

  Update  197 | Ep   674 | reward:    121.8 | mean(100):     94.2 | actor_loss: 0.0021 | value_loss: 1.8881 | lr: 1.99e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  198 | Ep   676 | reward:    235.1 | mean(100):     95.5 | actor_loss: 0.0007 | value_loss: 4.4472 | lr: 1.99e-04

  Update  199 | Ep   678 | reward:    195.0 | mean(100):     95.5 | actor_loss: -0.0002 | value_loss: 3.2587 | lr: 1.99e-04
  [Analyzer] 2 episodes -> 4 bad pairs (3 dropped by adv filter) | unlikelihood_loss=4.4193 | mean p(bad) before update=0.9880 | ul_lr=5.23e-05 (scale=0.52)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  200 | Ep   680 | reward:     67.1 | mean(100):     95.5 | actor_loss: 0.0032 | value_loss: 1.3708 | lr: 1.98e-04
  Update  201 | Ep   682 | reward:    193.1 | mean(100):     96.7 | actor_loss: -0.0013 | value_loss: 3.3485 | lr: 1.98e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  202 | Ep   684 | reward:    100.0 | mean(100):     96.7 | actor_loss: -0.0018 | value_loss: 1.2979 | lr: 1.98e-04

  Update  203 | Ep   686 | reward:     50.4 | mean(100):     96.9 | actor_loss: -0.0007 | value_loss: 1.8343 | lr: 1.97e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  204 | Ep   688 | reward:     98.4 | mean(100):     97.9 | actor_loss: -0.0014 | value_loss: 3.8327 | lr: 1.97e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.7449 | mean p(bad) before update=0.3860 | ul_lr=5.10e-05 (scale=0.51)
  Update  205 | Ep   690 | reward:     93.7 | mean(100):     98.0 | actor_loss: -0.0013 | value_loss: 1.3367 | lr: 1.97e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  206 | Ep   692 | reward:     78.8 | mean(100):     97.0 | actor_loss: -0.0001 | value_loss: 1.3790 | lr: 1.96e-04

  Update  207 | Ep   694 | reward:    111.1 | mean(100):     97.2 | actor_loss: -0.0008 | value_loss: 1.7405 | lr: 1.96e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  208 | Ep   696 | reward:     97.7 | mean(100):     97.5 | actor_loss: -0.0024 | value_loss: 1.7583 | lr: 1.96e-04

  Update  209 | Ep   698 | reward:     52.8 | mean(100):     97.6 | actor_loss: -0.0027 | value_loss: 0.9180 | lr: 1.96e-04
  [Analyzer] 2 episodes -> 4 bad pairs (3 dropped by adv filter) | unlikelihood_loss=0.1259 | mean p(bad) before update=0.1183 | ul_lr=5.10e-05 (scale=0.51)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  210 | Ep   700 | reward:     87.8 | mean(100):     98.0 | actor_loss: -0.0036 | value_loss: 1.2112 | lr: 1.95e-04

  Update  211 | Ep   702 | reward:    101.9 | mean(100):     98.2 | actor_loss: -0.0030 | value_loss: 1.2417 | lr: 1.95e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  212 | Ep   704 | reward:    120.5 | mean(100):     97.3 | actor_loss: 0.0004 | value_loss: 1.4037 | lr: 1.95e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_1.png
  Update  213 | Ep   706 | reward:    111.9 | mean(100):     97.5 | actor_loss: -0.0012 | value_loss: 0.8722 | lr: 1.94e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  214 | Ep   708 | reward:     81.3 | mean(100):     97.2 | actor_loss: -0.0007 | value_loss: 1.2528 | lr: 1.94e-04

