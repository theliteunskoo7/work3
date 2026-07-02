Using device: cpu (rollout collection stays on CPU; batched updates use cpu)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  analyzer_threshold=200  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=unsloth/gemma-4-26B-A4B-it-GGUF

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3126 | mean p(bad) before update=0.2674 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2329 | mean p(bad) before update=0.2077 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    1 | Ep    22 | reward:    -85.4 | mean(100):   -191.1 | actor_loss: -0.0100 | value_loss: 32.9811 | lr: 3.00e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2520 | mean p(bad) before update=0.2225 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2433 | mean p(bad) before update=0.2159 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    2 | Ep    44 | reward:   -170.9 | mean(100):   -168.9 | actor_loss: -0.0092 | value_loss: 27.9374 | lr: 2.97e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3788 | mean p(bad) before update=0.3153 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3598 | mean p(bad) before update=0.2988 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    3 | Ep    64 | reward:   -108.1 | mean(100):   -156.9 | actor_loss: -0.0084 | value_loss: 21.7894 | lr: 2.93e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2311 | mean p(bad) before update=0.2033 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2940 | mean p(bad) before update=0.2508 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    4 | Ep    86 | reward:    -96.6 | mean(100):   -148.3 | actor_loss: -0.0067 | value_loss: 20.7971 | lr: 2.90e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2055 | mean p(bad) before update=0.1854 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2977 | mean p(bad) before update=0.2529 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    5 | Ep   108 | reward:    -75.3 | mean(100):   -139.7 | actor_loss: -0.0100 | value_loss: 23.8239 | lr: 2.87e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1872 | mean p(bad) before update=0.1705 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2448 | mean p(bad) before update=0.2137 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    6 | Ep   127 | reward:   -120.6 | mean(100):   -125.8 | actor_loss: -0.0073 | value_loss: 20.4949 | lr: 2.84e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1615 | mean p(bad) before update=0.1483 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2104 | mean p(bad) before update=0.1896 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    7 | Ep   148 | reward:    -44.2 | mean(100):   -117.3 | actor_loss: -0.0089 | value_loss: 17.7433 | lr: 2.81e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2957 | mean p(bad) before update=0.2525 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1568 | mean p(bad) before update=0.1443 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    8 | Ep   169 | reward:   -126.0 | mean(100):   -110.8 | actor_loss: -0.0130 | value_loss: 19.2218 | lr: 2.78e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3099 | mean p(bad) before update=0.2591 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2032 | mean p(bad) before update=0.1826 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    9 | Ep   188 | reward:    -76.7 | mean(100):   -108.8 | actor_loss: -0.0074 | value_loss: 17.5591 | lr: 2.75e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4606 | mean p(bad) before update=0.3261 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3409 | mean p(bad) before update=0.2706 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   10 | Ep   207 | reward:    -71.9 | mean(100):   -102.6 | actor_loss: -0.0112 | value_loss: 16.7686 | lr: 2.72e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2735 | mean p(bad) before update=0.2241 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1318 | mean p(bad) before update=0.1229 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   11 | Ep   226 | reward:    -14.3 | mean(100):    -93.5 | actor_loss: -0.0109 | value_loss: 14.2993 | lr: 2.69e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.6369 | mean p(bad) before update=0.4429 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.7975 | mean p(bad) before update=0.5118 | ul_lr=1.00e-04 (scale=1.00)
  Update   12 | Ep   240 | reward:     -4.8 | mean(100):    -91.2 | actor_loss: -0.0066 | value_loss: 15.6579 | lr: 2.66e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5740 | mean p(bad) before update=0.4096 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   13 | Ep   254 | reward:   -208.9 | mean(100):    -95.5 | actor_loss: -0.0055 | value_loss: 15.8107 | lr: 2.64e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3454 | mean p(bad) before update=0.2750 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   14 | Ep   268 | reward:    -86.1 | mean(100):    -87.9 | actor_loss: -0.0078 | value_loss: 12.3032 | lr: 2.62e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.6650 | mean p(bad) before update=0.4606 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4731 | mean p(bad) before update=0.3398 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   280 | reward:   -206.0 | mean(100):    -84.0 | actor_loss: -0.0067 | value_loss: 13.5643 | lr: 2.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4610 | mean p(bad) before update=0.3231 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   294 | reward:     20.3 | mean(100):    -73.9 | actor_loss: -0.0032 | value_loss: 13.5274 | lr: 2.58e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2812 | mean p(bad) before update=0.2241 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   301 | reward:    -21.7 | mean(100):    -65.5 | actor_loss: -0.0072 | value_loss: 8.3977 | lr: 2.56e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   18 | Ep   307 | reward:    119.4 | mean(100):    -63.3 | actor_loss: -0.0093 | value_loss: 10.0667 | lr: 2.55e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5502 | mean p(bad) before update=0.4131 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   19 | Ep   315 | reward:   -108.8 | mean(100):    -67.8 | actor_loss: -0.0056 | value_loss: 13.2603 | lr: 2.54e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   20 | Ep   319 | reward:    119.6 | mean(100):    -64.4 | actor_loss: -0.0085 | value_loss: 5.6561 | lr: 2.53e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4142 | mean p(bad) before update=0.3315 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   21 | Ep   324 | reward:      3.0 | mean(100):    -62.6 | actor_loss: -0.0054 | value_loss: 7.3492 | lr: 2.52e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4084 | mean p(bad) before update=0.3110 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   22 | Ep   333 | reward:   -100.9 | mean(100):    -65.5 | actor_loss: -0.0059 | value_loss: 12.4115 | lr: 2.51e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   23 | Ep   337 | reward:     50.8 | mean(100):    -63.0 | actor_loss: -0.0058 | value_loss: 8.1014 | lr: 2.50e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2712 | mean p(bad) before update=0.2354 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   24 | Ep   340 | reward:   -115.6 | mean(100):    -62.6 | actor_loss: -0.0081 | value_loss: 7.1684 | lr: 2.49e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   25 | Ep   343 | reward:   -132.4 | mean(100):    -60.8 | actor_loss: -0.0052 | value_loss: 6.9715 | lr: 2.49e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   26 | Ep   346 | reward:    -17.1 | mean(100):    -56.4 | actor_loss: -0.0071 | value_loss: 6.0456 | lr: 2.49e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   27 | Ep   349 | reward:    -25.8 | mean(100):    -53.4 | actor_loss: -0.0055 | value_loss: 5.8620 | lr: 2.48e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4022 | mean p(bad) before update=0.3140 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   28 | Ep   351 | reward:     62.4 | mean(100):    -51.2 | actor_loss: -0.0077 | value_loss: 4.0244 | lr: 2.48e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   29 | Ep   353 | reward:     35.9 | mean(100):    -47.1 | actor_loss: -0.0077 | value_loss: 4.3291 | lr: 2.47e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   30 | Ep   355 | reward:   -129.5 | mean(100):    -47.1 | actor_loss: -0.0049 | value_loss: 5.1257 | lr: 2.47e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   31 | Ep   357 | reward:   -154.4 | mean(100):    -49.9 | actor_loss: -0.0064 | value_loss: 5.6347 | lr: 2.47e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   32 | Ep   359 | reward:    101.6 | mean(100):    -50.1 | actor_loss: -0.0011 | value_loss: 4.0364 | lr: 2.46e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3226 | mean p(bad) before update=0.2497 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   33 | Ep   361 | reward:    -65.9 | mean(100):    -50.3 | actor_loss: -0.0158 | value_loss: 3.8387 | lr: 2.46e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   34 | Ep   363 | reward:     21.3 | mean(100):    -48.5 | actor_loss: -0.0125 | value_loss: 2.8644 | lr: 2.46e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   35 | Ep   365 | reward:     10.3 | mean(100):    -46.4 | actor_loss: -0.0044 | value_loss: 2.6801 | lr: 2.46e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   36 | Ep   367 | reward:    -67.9 | mean(100):    -45.3 | actor_loss: -0.0137 | value_loss: 3.1713 | lr: 2.45e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   37 | Ep   369 | reward:     71.5 | mean(100):    -43.2 | actor_loss: -0.0060 | value_loss: 2.3609 | lr: 2.45e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2596 | mean p(bad) before update=0.2070 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   38 | Ep   371 | reward:    -76.8 | mean(100):    -44.8 | actor_loss: -0.0079 | value_loss: 3.1818 | lr: 2.45e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   39 | Ep   373 | reward:     62.9 | mean(100):    -42.6 | actor_loss: -0.0065 | value_loss: 2.3618 | lr: 2.44e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   40 | Ep   375 | reward:    -44.9 | mean(100):    -42.6 | actor_loss: -0.0085 | value_loss: 2.8982 | lr: 2.44e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   41 | Ep   377 | reward:    -46.4 | mean(100):    -42.2 | actor_loss: -0.0055 | value_loss: 2.5969 | lr: 2.44e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   42 | Ep   379 | reward:     39.6 | mean(100):    -39.1 | actor_loss: -0.0056 | value_loss: 2.7819 | lr: 2.43e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.5293 | mean p(bad) before update=0.4037 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   43 | Ep   381 | reward:    174.3 | mean(100):    -35.5 | actor_loss: -0.0099 | value_loss: 3.8670 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   44 | Ep   383 | reward:    -48.7 | mean(100):    -33.4 | actor_loss: -0.0044 | value_loss: 2.7436 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   45 | Ep   385 | reward:   -108.4 | mean(100):    -34.4 | actor_loss: -0.0037 | value_loss: 2.7628 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   46 | Ep   387 | reward:     36.0 | mean(100):    -32.7 | actor_loss: -0.0062 | value_loss: 2.4635 | lr: 2.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   47 | Ep   389 | reward:     34.4 | mean(100):    -31.8 | actor_loss: -0.0046 | value_loss: 2.0157 | lr: 2.42e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.4886 | mean p(bad) before update=0.3578 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   48 | Ep   391 | reward:   -176.0 | mean(100):    -34.5 | actor_loss: -0.0009 | value_loss: 3.4896 | lr: 2.42e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   49 | Ep   393 | reward:    -39.5 | mean(100):    -33.6 | actor_loss: -0.0023 | value_loss: 2.1896 | lr: 2.41e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   50 | Ep   395 | reward:     29.6 | mean(100):    -34.0 | actor_loss: -0.0039 | value_loss: 2.0471 | lr: 2.41e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   51 | Ep   397 | reward:     39.1 | mean(100):    -32.8 | actor_loss: -0.0053 | value_loss: 1.9522 | lr: 2.41e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   52 | Ep   399 | reward:     43.2 | mean(100):    -33.9 | actor_loss: -0.0034 | value_loss: 2.5347 | lr: 2.40e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.6924 | mean p(bad) before update=0.4469 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   53 | Ep   401 | reward:   -123.5 | mean(100):    -36.4 | actor_loss: -0.0026 | value_loss: 4.4889 | lr: 2.40e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   54 | Ep   404 | reward:    147.7 | mean(100):    -33.0 | actor_loss: -0.0055 | value_loss: 4.9205 | lr: 2.40e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   55 | Ep   406 | reward:    123.6 | mean(100):    -32.0 | actor_loss: -0.0031 | value_loss: 2.7755 | lr: 2.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   56 | Ep   408 | reward:   -108.6 | mean(100):    -31.7 | actor_loss: -0.0043 | value_loss: 3.5916 | lr: 2.39e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.5276 | mean p(bad) before update=0.7234 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   57 | Ep   410 | reward:     34.4 | mean(100):    -23.7 | actor_loss: -0.0022 | value_loss: 3.0922 | lr: 2.39e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   58 | Ep   413 | reward:    -47.3 | mean(100):    -25.2 | actor_loss: -0.0042 | value_loss: 5.2733 | lr: 2.38e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   59 | Ep   415 | reward:     45.0 | mean(100):    -22.7 | actor_loss: -0.0081 | value_loss: 2.8271 | lr: 2.38e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   60 | Ep   417 | reward:    158.2 | mean(100):    -20.1 | actor_loss: -0.0026 | value_loss: 2.6489 | lr: 2.38e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   61 | Ep   419 | reward:     80.7 | mean(100):    -21.3 | actor_loss: -0.0064 | value_loss: 2.9570 | lr: 2.37e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.2457 | mean p(bad) before update=0.5634 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   62 | Ep   421 | reward:     72.9 | mean(100):    -17.2 | actor_loss: -0.0026 | value_loss: 1.6371 | lr: 2.37e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   63 | Ep   423 | reward:     87.3 | mean(100):    -15.8 | actor_loss: -0.0059 | value_loss: 2.1204 | lr: 2.37e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   64 | Ep   426 | reward:    174.7 | mean(100):    -10.9 | actor_loss: -0.0051 | value_loss: 3.8098 | lr: 2.37e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   65 | Ep   428 | reward:    141.8 | mean(100):     -5.6 | actor_loss: -0.0058 | value_loss: 4.5895 | lr: 2.36e-04

  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=1.7859 | mean p(bad) before update=0.5642 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   66 | Ep   430 | reward:    119.5 | mean(100):     -1.3 | actor_loss: -0.0040 | value_loss: 2.7649 | lr: 2.36e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   67 | Ep   432 | reward:    190.5 | mean(100):      3.7 | actor_loss: -0.0055 | value_loss: 2.6065 | lr: 2.35e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   68 | Ep   434 | reward:     83.0 | mean(100):      8.6 | actor_loss: -0.0062 | value_loss: 1.6141 | lr: 2.35e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   69 | Ep   436 | reward:     97.4 | mean(100):     11.3 | actor_loss: -0.0022 | value_loss: 3.0000 | lr: 2.35e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   70 | Ep   438 | reward:     73.7 | mean(100):     14.9 | actor_loss: -0.0032 | value_loss: 2.2983 | lr: 2.35e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=3.7742 | mean p(bad) before update=0.9756 | ul_lr=9.21e-05 (scale=0.92)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   71 | Ep   442 | reward:    -59.2 | mean(100):     15.9 | actor_loss: -0.0022 | value_loss: 5.6994 | lr: 2.34e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   72 | Ep   445 | reward:    204.2 | mean(100):     18.6 | actor_loss: -0.0003 | value_loss: 3.7967 | lr: 2.34e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   73 | Ep   448 | reward:   -104.4 | mean(100):     17.6 | actor_loss: -0.0010 | value_loss: 5.3672 | lr: 2.33e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.7671 | mean p(bad) before update=0.5277 | ul_lr=9.05e-05 (scale=0.91)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   74 | Ep   452 | reward:    128.0 | mean(100):     19.0 | actor_loss: -0.0032 | value_loss: 6.0728 | lr: 2.33e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   75 | Ep   454 | reward:     79.6 | mean(100):     21.6 | actor_loss: 0.0001 | value_loss: 2.0690 | lr: 2.32e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   76 | Ep   456 | reward:    153.6 | mean(100):     27.3 | actor_loss: -0.0043 | value_loss: 3.2117 | lr: 2.32e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   77 | Ep   459 | reward:    -75.0 | mean(100):     29.6 | actor_loss: -0.0022 | value_loss: 3.2710 | lr: 2.32e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.6880 | mean p(bad) before update=0.4443 | ul_lr=8.33e-05 (scale=0.83)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   78 | Ep   461 | reward:    196.4 | mean(100):     33.4 | actor_loss: -0.0039 | value_loss: 2.5266 | lr: 2.31e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   79 | Ep   464 | reward:    169.9 | mean(100):     37.3 | actor_loss: -0.0021 | value_loss: 3.4205 | lr: 2.31e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   80 | Ep   467 | reward:    110.2 | mean(100):     43.3 | actor_loss: -0.0023 | value_loss: 3.3151 | lr: 2.30e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   81 | Ep   469 | reward:     97.5 | mean(100):     43.8 | actor_loss: -0.0045 | value_loss: 1.1595 | lr: 2.30e-04

  [Analyzer] 2 episodes -> 4 bad pairs (4 dropped by adv filter, 0 applied)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   82 | Ep   472 | reward:    150.8 | mean(100):     50.3 | actor_loss: -0.0004 | value_loss: 3.4523 | lr: 2.30e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   83 | Ep   475 | reward:    -42.0 | mean(100):     51.0 | actor_loss: -0.0045 | value_loss: 3.3457 | lr: 2.29e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   84 | Ep   477 | reward:     85.2 | mean(100):     52.0 | actor_loss: -0.0006 | value_loss: 2.1387 | lr: 2.29e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   85 | Ep   479 | reward:    108.3 | mean(100):     52.9 | actor_loss: -0.0031 | value_loss: 1.2792 | lr: 2.28e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5598 | mean p(bad) before update=0.3942 | ul_lr=7.42e-05 (scale=0.74)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   86 | Ep   481 | reward:     97.2 | mean(100):     51.6 | actor_loss: -0.0125 | value_loss: 2.1885 | lr: 2.28e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   87 | Ep   484 | reward:    179.4 | mean(100):     52.7 | actor_loss: 0.0033 | value_loss: 3.8201 | lr: 2.28e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   88 | Ep   489 | reward:    207.9 | mean(100):     59.8 | actor_loss: -0.0028 | value_loss: 6.2767 | lr: 2.27e-04
  [Analyzer] 1 episodes -> 2 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.3643 | mean p(bad) before update=0.3053 | ul_lr=6.73e-05 (scale=0.67)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   89 | Ep   492 | reward:    177.1 | mean(100):     65.3 | actor_loss: -0.0026 | value_loss: 4.8951 | lr: 2.27e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   90 | Ep   494 | reward:    118.9 | mean(100):     67.5 | actor_loss: -0.0009 | value_loss: 2.2243 | lr: 2.26e-04

  Update   91 | Ep   496 | reward:    164.5 | mean(100):     70.2 | actor_loss: -0.0055 | value_loss: 3.6559 | lr: 2.26e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   92 | Ep   499 | reward:    164.9 | mean(100):     72.0 | actor_loss: -0.0029 | value_loss: 3.5330 | lr: 2.26e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8164 | mean p(bad) before update=0.4783 | ul_lr=6.10e-05 (scale=0.61)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   93 | Ep   502 | reward:    116.2 | mean(100):     78.0 | actor_loss: -0.0019 | value_loss: 3.3356 | lr: 2.25e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   94 | Ep   504 | reward:    168.0 | mean(100):     79.5 | actor_loss: -0.0029 | value_loss: 2.2017 | lr: 2.25e-04
  Update   95 | Ep   508 | reward:    174.1 | mean(100):     82.9 | actor_loss: -0.0019 | value_loss: 6.5969 | lr: 2.24e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3264 | mean p(bad) before update=0.2766 | ul_lr=5.96e-05 (scale=0.60)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   96 | Ep   510 | reward:     48.4 | mean(100):     80.9 | actor_loss: -0.0036 | value_loss: 2.6345 | lr: 2.24e-04
  Update   97 | Ep   513 | reward:     94.8 | mean(100):     87.5 | actor_loss: -0.0020 | value_loss: 3.4887 | lr: 2.23e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   98 | Ep   516 | reward:    -78.2 | mean(100):     85.3 | actor_loss: -0.0084 | value_loss: 3.5006 | lr: 2.23e-04
  Update   99 | Ep   518 | reward:     99.5 | mean(100):     86.5 | actor_loss: -0.0033 | value_loss: 1.0858 | lr: 2.23e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5050 | mean p(bad) before update=0.3116 | ul_lr=5.63e-05 (scale=0.56)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  100 | Ep   520 | reward:    159.3 | mean(100):     87.5 | actor_loss: -0.0021 | value_loss: 2.0425 | lr: 2.22e-04

  Update  101 | Ep   523 | reward:    198.9 | mean(100):     89.9 | actor_loss: -0.0029 | value_loss: 3.4125 | lr: 2.22e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  102 | Ep   526 | reward:    132.1 | mean(100):     93.2 | actor_loss: -0.0011 | value_loss: 3.8688 | lr: 2.22e-04
  Update  103 | Ep   528 | reward:     99.5 | mean(100):     92.5 | actor_loss: -0.0025 | value_loss: 2.3421 | lr: 2.21e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2313 | mean p(bad) before update=0.1871 | ul_lr=5.34e-05 (scale=0.53)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  104 | Ep   530 | reward:    206.6 | mean(100):     93.3 | actor_loss: -0.0016 | value_loss: 1.9682 | lr: 2.21e-04

  Update  105 | Ep   535 | reward:    -33.4 | mean(100):     89.4 | actor_loss: -0.0036 | value_loss: 6.9891 | lr: 2.20e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  106 | Ep   538 | reward:    130.6 | mean(100):     88.6 | actor_loss: -0.0039 | value_loss: 2.8747 | lr: 2.20e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4311 | mean p(bad) before update=0.3300 | ul_lr=5.59e-05 (scale=0.56)
  Update  107 | Ep   542 | reward:     78.0 | mean(100):     88.3 | actor_loss: -0.0042 | value_loss: 3.9627 | lr: 2.19e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  108 | Ep   544 | reward:     62.9 | mean(100):     89.1 | actor_loss: -0.0030 | value_loss: 2.3448 | lr: 2.19e-04

  Update  109 | Ep   548 | reward:    -37.5 | mean(100):     89.9 | actor_loss: -0.0077 | value_loss: 4.9465 | lr: 2.18e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2876 | mean p(bad) before update=0.2215 | ul_lr=5.28e-05 (scale=0.53)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  110 | Ep   553 | reward:    201.1 | mean(100):     94.4 | actor_loss: -0.0038 | value_loss: 5.9363 | lr: 2.18e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  111 | Ep   555 | reward:    107.0 | mean(100):     92.8 | actor_loss: -0.0028 | value_loss: 2.0199 | lr: 2.17e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  112 | Ep   558 | reward:    110.4 | mean(100):     92.8 | actor_loss: -0.0075 | value_loss: 3.0172 | lr: 2.17e-04

  [Analyzer] 1 episodes -> 2 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.1802 | mean p(bad) before update=0.1649 | ul_lr=5.18e-05 (scale=0.52)
  Update  113 | Ep   561 | reward:    166.5 | mean(100):     96.4 | actor_loss: -0.0021 | value_loss: 4.2295 | lr: 2.16e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  114 | Ep   564 | reward:     92.6 | mean(100):     97.0 | actor_loss: -0.0023 | value_loss: 2.7318 | lr: 2.16e-04

  Update  115 | Ep   566 | reward:     83.1 | mean(100):     96.5 | actor_loss: -0.0047 | value_loss: 2.8732 | lr: 2.15e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  116 | Ep   568 | reward:     86.9 | mean(100):     95.0 | actor_loss: -0.0123 | value_loss: 2.6883 | lr: 2.15e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.3847 | mean p(bad) before update=0.3070 | ul_lr=5.22e-05 (scale=0.52)
  Update  117 | Ep   571 | reward:    193.6 | mean(100):     95.5 | actor_loss: -0.0024 | value_loss: 3.0969 | lr: 2.15e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  118 | Ep   574 | reward:     86.6 | mean(100):     97.9 | actor_loss: -0.0025 | value_loss: 2.6682 | lr: 2.14e-04
  Update  119 | Ep   578 | reward:    160.5 | mean(100):    104.5 | actor_loss: -0.0010 | value_loss: 5.6851 | lr: 2.14e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.7789 | mean p(bad) before update=0.7576 | ul_lr=4.60e-05 (scale=0.46)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  120 | Ep   581 | reward:    115.6 | mean(100):    108.0 | actor_loss: -0.0038 | value_loss: 2.7128 | lr: 2.13e-04

  Update  121 | Ep   586 | reward:    198.1 | mean(100):    109.7 | actor_loss: -0.0046 | value_loss: 6.7367 | lr: 2.13e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  122 | Ep   588 | reward:    109.1 | mean(100):    107.8 | actor_loss: -0.0033 | value_loss: 1.3255 | lr: 2.12e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2135 | mean p(bad) before update=0.1921 | ul_lr=4.55e-05 (scale=0.45)
  Update  123 | Ep   591 | reward:     85.5 | mean(100):    109.1 | actor_loss: -0.0021 | value_loss: 3.2960 | lr: 2.12e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  124 | Ep   594 | reward:    217.8 | mean(100):    109.4 | actor_loss: -0.0033 | value_loss: 3.3493 | lr: 2.11e-04
  Update  125 | Ep   598 | reward:    176.8 | mean(100):    110.3 | actor_loss: 0.0006 | value_loss: 4.6100 | lr: 2.11e-04
  [Analyzer] 1 episodes -> 2 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.9793 | mean p(bad) before update=0.8618 | ul_lr=4.51e-05 (scale=0.45)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  126 | Ep   601 | reward:    -59.1 | mean(100):    109.7 | actor_loss: -0.0068 | value_loss: 3.2234 | lr: 2.10e-04

  Update  127 | Ep   603 | reward:    183.6 | mean(100):    110.5 | actor_loss: -0.0016 | value_loss: 2.6131 | lr: 2.10e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  128 | Ep   606 | reward:    187.9 | mean(100):    112.9 | actor_loss: -0.0019 | value_loss: 4.1598 | lr: 2.10e-04

  Update  129 | Ep   608 | reward:    100.5 | mean(100):    112.7 | actor_loss: -0.0027 | value_loss: 2.9317 | lr: 2.09e-04
  [Analyzer] 1 episodes -> 2 bad pairs (2 dropped by adv filter, 0 applied)
  Update  130 | Ep   610 | reward:    114.6 | mean(100):    115.9 | actor_loss: -0.0033 | value_loss: 3.0305 | lr: 2.09e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  Update  131 | Ep   613 | reward:    -40.8 | mean(100):    114.0 | actor_loss: -0.0023 | value_loss: 3.4301 | lr: 2.08e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  132 | Ep   618 | reward:    211.7 | mean(100):    118.1 | actor_loss: -0.0013 | value_loss: 6.5578 | lr: 2.08e-04

  Update  133 | Ep   621 | reward:    162.1 | mean(100):    120.0 | actor_loss: -0.0022 | value_loss: 5.1751 | lr: 2.07e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  134 | Ep   626 | reward:   -162.7 | mean(100):    114.5 | actor_loss: -0.0011 | value_loss: 6.6863 | lr: 2.07e-04
  Update  135 | Ep   628 | reward:    105.1 | mean(100):    111.2 | actor_loss: 0.0029 | value_loss: 3.8105 | lr: 2.06e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.2913 | mean p(bad) before update=0.2192 | ul_lr=4.57e-05 (scale=0.46)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  136 | Ep   630 | reward:    -32.3 | mean(100):    108.6 | actor_loss: -0.0020 | value_loss: 1.5494 | lr: 2.06e-04

  Update  137 | Ep   634 | reward:    -18.9 | mean(100):    106.9 | actor_loss: -0.0032 | value_loss: 3.8221 | lr: 2.06e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  138 | Ep   637 | reward:    157.8 | mean(100):    111.3 | actor_loss: -0.0010 | value_loss: 3.5305 | lr: 2.05e-04

  Update  139 | Ep   639 | reward:     97.9 | mean(100):    110.9 | actor_loss: -0.0044 | value_loss: 2.9158 | lr: 2.04e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3144 | mean p(bad) before update=0.2526 | ul_lr=4.26e-05 (scale=0.43)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  140 | Ep   641 | reward:    221.6 | mean(100):    114.7 | actor_loss: -0.0009 | value_loss: 1.5428 | lr: 2.04e-04
  Update  141 | Ep   644 | reward:    138.3 | mean(100):    117.7 | actor_loss: -0.0012 | value_loss: 2.5740 | lr: 2.04e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4453 | mean p(bad) before update=0.3593 | ul_lr=4.07e-05 (scale=0.41)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  142 | Ep   650 | reward:    -67.4 | mean(100):    118.5 | actor_loss: -0.0009 | value_loss: 6.4254 | lr: 2.03e-04
  Update  143 | Ep   652 | reward:    112.3 | mean(100):    116.3 | actor_loss: -0.0042 | value_loss: 3.1010 | lr: 2.02e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  144 | Ep   655 | reward:    144.2 | mean(100):    117.9 | actor_loss: -0.0007 | value_loss: 4.1745 | lr: 2.02e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  145 | Ep   658 | reward:    104.9 | mean(100):    121.1 | actor_loss: -0.0012 | value_loss: 3.4110 | lr: 2.02e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1669 | mean p(bad) before update=0.1430 | ul_lr=3.98e-05 (scale=0.40)
  Update  146 | Ep   662 | reward:    168.6 | mean(100):    120.5 | actor_loss: -0.0006 | value_loss: 3.5594 | lr: 2.01e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  147 | Ep   667 | reward:    -45.1 | mean(100):    121.5 | actor_loss: -0.0031 | value_loss: 6.1596 | lr: 2.01e-04

  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4030 | mean p(bad) before update=0.3265 | ul_lr=3.95e-05 (scale=0.39)
  Update  148 | Ep   672 | reward:    -59.7 | mean(100):    121.0 | actor_loss: -0.0043 | value_loss: 7.8909 | lr: 2.00e-04
  Update  149 | Ep   675 | reward:    188.5 | mean(100):    121.0 | actor_loss: -0.0021 | value_loss: 3.3653 | lr: 1.99e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  150 | Ep   678 | reward:    149.5 | mean(100):    119.8 | actor_loss: -0.0024 | value_loss: 3.6810 | lr: 1.99e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.5969 | mean p(bad) before update=0.3196 | ul_lr=4.09e-05 (scale=0.41)
  Update  151 | Ep   682 | reward:    -25.7 | mean(100):    118.2 | actor_loss: -0.0048 | value_loss: 3.8372 | lr: 1.98e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  152 | Ep   688 | reward:     15.0 | mean(100):    117.8 | actor_loss: -0.0027 | value_loss: 7.0913 | lr: 1.98e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.0859 | mean p(bad) before update=0.6488 | ul_lr=4.08e-05 (scale=0.41)
  Update  153 | Ep   693 | reward:    207.0 | mean(100):    118.4 | actor_loss: -0.0064 | value_loss: 6.1081 | lr: 1.97e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  154 | Ep   696 | reward:    -57.3 | mean(100):    117.0 | actor_loss: -0.0050 | value_loss: 5.6299 | lr: 1.96e-04
  Update  155 | Ep   698 | reward:    121.9 | mean(100):    116.2 | actor_loss: -0.0010 | value_loss: 1.4448 | lr: 1.96e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.7991 | mean p(bad) before update=0.5306 | ul_lr=4.11e-05 (scale=0.41)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  156 | Ep   702 | reward:    -11.0 | mean(100):    117.8 | actor_loss: -0.0052 | value_loss: 3.9738 | lr: 1.95e-04

  Update  157 | Ep   705 | reward:    219.8 | mean(100):    118.8 | actor_loss: -0.0024 | value_loss: 4.9714 | lr: 1.95e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  158 | Ep   708 | reward:    251.3 | mean(100):    119.9 | actor_loss: -0.0025 | value_loss: 5.6884 | lr: 1.94e-04

  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4360 | mean p(bad) before update=0.3498 | ul_lr=3.92e-05 (scale=0.39)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  159 | Ep   713 | reward:    209.8 | mean(100):    121.6 | actor_loss: -0.0018 | value_loss: 6.6595 | lr: 1.94e-04

  Update  160 | Ep   716 | reward:    214.4 | mean(100):    125.5 | actor_loss: -0.0028 | value_loss: 4.4118 | lr: 1.93e-04
  Update  161 | Ep   719 | reward:    171.4 | mean(100):    125.1 | actor_loss: -0.0018 | value_loss: 4.7117 | lr: 1.93e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=2.8865 | mean p(bad) before update=0.7779 | ul_lr=3.79e-05 (scale=0.38)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  162 | Ep   721 | reward:    118.0 | mean(100):    124.2 | actor_loss: -0.0013 | value_loss: 2.3033 | lr: 1.92e-04

  Update  163 | Ep   724 | reward:    129.9 | mean(100):    124.2 | actor_loss: -0.0007 | value_loss: 3.1265 | lr: 1.92e-04
  Update  164 | Ep   727 | reward:    218.8 | mean(100):    130.1 | actor_loss: -0.0083 | value_loss: 3.7016 | lr: 1.91e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5217 | mean p(bad) before update=0.3270 | ul_lr=3.40e-05 (scale=0.34)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  165 | Ep   730 | reward:    206.2 | mean(100):    131.9 | actor_loss: -0.0050 | value_loss: 2.5799 | lr: 1.91e-04

  Update  166 | Ep   736 | reward:    207.7 | mean(100):    133.7 | actor_loss: -0.0027 | value_loss: 7.1740 | lr: 1.90e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1561 | mean p(bad) before update=0.1446 | ul_lr=3.16e-05 (scale=0.32)
  Update  167 | Ep   740 | reward:    -32.6 | mean(100):    136.8 | actor_loss: -0.0054 | value_loss: 4.8224 | lr: 1.90e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  168 | Ep   743 | reward:    234.1 | mean(100):    134.1 | actor_loss: -0.0024 | value_loss: 3.2185 | lr: 1.89e-04

  Update  169 | Ep   747 | reward:    195.6 | mean(100):    134.3 | actor_loss: -0.0009 | value_loss: 3.8601 | lr: 1.89e-04
  Update  170 | Ep   749 | reward:    189.4 | mean(100):    135.6 | actor_loss: -0.0044 | value_loss: 2.8766 | lr: 1.88e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4718 | mean p(bad) before update=0.3227 | ul_lr=3.01e-05 (scale=0.30)
  Update  171 | Ep   751 | reward:    121.9 | mean(100):    139.8 | actor_loss: -0.0026 | value_loss: 1.4899 | lr: 1.88e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  Update  172 | Ep   754 | reward:    170.0 | mean(100):    138.6 | actor_loss: -0.0030 | value_loss: 4.5155 | lr: 1.87e-04
  Update  173 | Ep   758 | reward:    209.1 | mean(100):    137.7 | actor_loss: -0.0067 | value_loss: 5.5609 | lr: 1.87e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.5956 | mean p(bad) before update=0.4273 | ul_lr=3.22e-05 (scale=0.32)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  174 | Ep   762 | reward:     19.4 | mean(100):    135.6 | actor_loss: -0.0034 | value_loss: 4.0590 | lr: 1.86e-04

  Update  175 | Ep   766 | reward:    214.5 | mean(100):    135.8 | actor_loss: -0.0021 | value_loss: 4.2205 | lr: 1.86e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.1543 | mean p(bad) before update=0.5503 | ul_lr=3.28e-05 (scale=0.33)
  Update  176 | Ep   771 | reward:    205.4 | mean(100):    134.4 | actor_loss: -0.0023 | value_loss: 5.6758 | lr: 1.85e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  177 | Ep   774 | reward:   -114.1 | mean(100):    135.3 | actor_loss: -0.0024 | value_loss: 4.3720 | lr: 1.84e-04
  Update  178 | Ep   778 | reward:    130.9 | mean(100):    137.0 | actor_loss: -0.0021 | value_loss: 3.9100 | lr: 1.84e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.6440 | mean p(bad) before update=0.4682 | ul_lr=3.00e-05 (scale=0.30)
  Update  179 | Ep   782 | reward:    145.3 | mean(100):    140.0 | actor_loss: -0.0010 | value_loss: 3.4938 | lr: 1.83e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  180 | Ep   786 | reward:    204.8 | mean(100):    142.8 | actor_loss: -0.0010 | value_loss: 3.6378 | lr: 1.83e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3573 | mean p(bad) before update=0.2987 | ul_lr=2.84e-05 (scale=0.28)
  Update  181 | Ep   790 | reward:     22.3 | mean(100):    143.3 | actor_loss: -0.0076 | value_loss: 4.3651 | lr: 1.82e-04
  Update  182 | Ep   792 | reward:     87.9 | mean(100):    143.3 | actor_loss: -0.0083 | value_loss: 1.1220 | lr: 1.81e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  183 | Ep   795 | reward:    200.2 | mean(100):    143.5 | actor_loss: -0.0009 | value_loss: 2.7292 | lr: 1.81e-04

  Update  184 | Ep   801 | reward:    225.2 | mean(100):    147.7 | actor_loss: -0.0035 | value_loss: 6.2794 | lr: 1.81e-04
  Update  185 | Ep   803 | reward:    114.7 | mean(100):    147.2 | actor_loss: -0.0004 | value_loss: 1.5333 | lr: 1.80e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  186 | Ep   806 | reward:    200.4 | mean(100):    144.6 | actor_loss: -0.0027 | value_loss: 3.5072 | lr: 1.80e-04

  Update  187 | Ep   808 | reward:    -17.8 | mean(100):    141.3 | actor_loss: -0.0038 | value_loss: 2.6967 | lr: 1.79e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4016 | mean p(bad) before update=0.3249 | ul_lr=2.79e-05 (scale=0.28)
  Update  188 | Ep   812 | reward:    206.1 | mean(100):    144.2 | actor_loss: -0.0021 | value_loss: 3.3496 | lr: 1.79e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  189 | Ep   815 | reward:    115.4 | mean(100):    142.3 | actor_loss: -0.0023 | value_loss: 2.8405 | lr: 1.78e-04

  Update  190 | Ep   817 | reward:    127.4 | mean(100):    141.7 | actor_loss: -0.0030 | value_loss: 2.7960 | lr: 1.78e-04
  Update  191 | Ep   819 | reward:    139.6 | mean(100):    140.7 | actor_loss: -0.0080 | value_loss: 0.5025 | lr: 1.77e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4057 | mean p(bad) before update=0.3108 | ul_lr=2.96e-05 (scale=0.30)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  192 | Ep   821 | reward:    191.8 | mean(100):    140.7 | actor_loss: -0.0022 | value_loss: 1.8027 | lr: 1.77e-04

  Update  193 | Ep   825 | reward:    214.6 | mean(100):    139.4 | actor_loss: -0.0046 | value_loss: 4.1029 | lr: 1.77e-04
  Update  194 | Ep   827 | reward:    110.3 | mean(100):    140.6 | actor_loss: -0.0029 | value_loss: 1.8773 | lr: 1.76e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1018 | mean p(bad) before update=0.0967 | ul_lr=2.76e-05 (scale=0.28)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  195 | Ep   832 | reward:    212.1 | mean(100):    144.8 | actor_loss: -0.0017 | value_loss: 7.9137 | lr: 1.76e-04

  Update  196 | Ep   836 | reward:    207.5 | mean(100):    146.3 | actor_loss: -0.0024 | value_loss: 4.3217 | lr: 1.75e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=2.4873 | mean p(bad) before update=0.7353 | ul_lr=2.78e-05 (scale=0.28)
  Update  197 | Ep   840 | reward:    -27.0 | mean(100):    144.3 | actor_loss: -0.0041 | value_loss: 5.5404 | lr: 1.75e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  198 | Ep   844 | reward:    206.4 | mean(100):    146.9 | actor_loss: -0.0013 | value_loss: 3.0753 | lr: 1.74e-04

  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3521 | mean p(bad) before update=0.2922 | ul_lr=2.74e-05 (scale=0.27)
  Update  199 | Ep   850 | reward:     20.4 | mean(100):    145.2 | actor_loss: -0.0054 | value_loss: 8.0008 | lr: 1.73e-04
  Update  200 | Ep   853 | reward:    133.8 | mean(100):    145.8 | actor_loss: -0.0048 | value_loss: 3.2451 | lr: 1.72e-04
  Update  201 | Ep   856 | reward:    -16.0 | mean(100):    142.5 | actor_loss: -0.0059 | value_loss: 3.5239 | lr: 1.72e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.6891 | mean p(bad) before update=0.5208 | ul_lr=2.99e-05 (scale=0.30)
  Update  202 | Ep   860 | reward:    -25.0 | mean(100):    140.3 | actor_loss: -0.0018 | value_loss: 3.7665 | lr: 1.72e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  203 | Ep   862 | reward:    -11.9 | mean(100):    139.1 | actor_loss: -0.0033 | value_loss: 1.2553 | lr: 1.71e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  204 | Ep   867 | reward:     32.2 | mean(100):    137.9 | actor_loss: -0.0069 | value_loss: 4.3816 | lr: 1.71e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3742 | mean p(bad) before update=0.2975 | ul_lr=3.27e-05 (scale=0.33)
  Update  205 | Ep   871 | reward:    -34.8 | mean(100):    134.6 | actor_loss: -0.0053 | value_loss: 3.7942 | lr: 1.70e-04
  Update  206 | Ep   873 | reward:    157.2 | mean(100):    133.4 | actor_loss: -0.0041 | value_loss: 1.3049 | lr: 1.69e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  207 | Ep   878 | reward:     -3.6 | mean(100):    131.2 | actor_loss: -0.0029 | value_loss: 4.1378 | lr: 1.69e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3608 | mean p(bad) before update=0.3017 | ul_lr=3.69e-05 (scale=0.37)
  Update  208 | Ep   885 | reward:    217.7 | mean(100):    126.1 | actor_loss: -0.0025 | value_loss: 9.6534 | lr: 1.68e-04
  Update  209 | Ep   889 | reward:    105.8 | mean(100):    128.1 | actor_loss: -0.0047 | value_loss: 3.3790 | lr: 1.67e-04
  [Analyzer] 1 episodes -> 2 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.2249 | mean p(bad) before update=0.2014 | ul_lr=3.57e-05 (scale=0.36)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  210 | Ep   896 | reward:    -43.1 | mean(100):    128.5 | actor_loss: -0.0016 | value_loss: 7.3541 | lr: 1.67e-04

  Update  211 | Ep   898 | reward:    140.7 | mean(100):    127.5 | actor_loss: -0.0021 | value_loss: 1.3407 | lr: 1.66e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.5064 | mean p(bad) before update=0.6503 | ul_lr=3.83e-05 (scale=0.38)
  Update  212 | Ep   902 | reward:    135.3 | mean(100):    123.5 | actor_loss: -0.0012 | value_loss: 3.6080 | lr: 1.65e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  213 | Ep   904 | reward:    203.6 | mean(100):    125.9 | actor_loss: -0.0012 | value_loss: 1.6072 | lr: 1.65e-04

  Update  214 | Ep   906 | reward:    134.7 | mean(100):    125.0 | actor_loss: -0.0051 | value_loss: 1.5277 | lr: 1.64e-04
  Update  215 | Ep   908 | reward:    126.2 | mean(100):    126.7 | actor_loss: -0.0030 | value_loss: 1.8152 | lr: 1.64e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3774 | mean p(bad) before update=0.2967 | ul_lr=3.78e-05 (scale=0.38)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  216 | Ep   911 | reward:    237.0 | mean(100):    124.4 | actor_loss: -0.0033 | value_loss: 3.1440 | lr: 1.64e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  217 | Ep   915 | reward:    211.9 | mean(100):    126.4 | actor_loss: -0.0022 | value_loss: 4.6002 | lr: 1.63e-04
  Update  218 | Ep   917 | reward:    144.3 | mean(100):    125.6 | actor_loss: -0.0054 | value_loss: 0.2835 | lr: 1.63e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=3.3635 | mean p(bad) before update=0.8378 | ul_lr=3.63e-05 (scale=0.36)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  219 | Ep   921 | reward:    138.4 | mean(100):    127.3 | actor_loss: -0.0013 | value_loss: 4.2047 | lr: 1.62e-04
  Update  220 | Ep   923 | reward:    223.2 | mean(100):    129.0 | actor_loss: -0.0012 | value_loss: 1.5598 | lr: 1.62e-04
  Update  221 | Ep   928 | reward:    114.4 | mean(100):    126.5 | actor_loss: -0.0020 | value_loss: 4.8657 | lr: 1.62e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8853 | mean p(bad) before update=0.5164 | ul_lr=3.67e-05 (scale=0.37)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  222 | Ep   932 | reward:    229.5 | mean(100):    126.7 | actor_loss: -0.0029 | value_loss: 4.3691 | lr: 1.61e-04

  Update  223 | Ep   937 | reward:      6.7 | mean(100):    124.7 | actor_loss: -0.0033 | value_loss: 4.6622 | lr: 1.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3270 | mean p(bad) before update=0.2700 | ul_lr=3.85e-05 (scale=0.39)
  Update  224 | Ep   941 | reward:    125.9 | mean(100):    123.0 | actor_loss: -0.0026 | value_loss: 3.9506 | lr: 1.59e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  225 | Ep   943 | reward:    186.9 | mean(100):    122.6 | actor_loss: -0.0027 | value_loss: 2.1213 | lr: 1.59e-04
  Update  226 | Ep   945 | reward:    154.4 | mean(100):    123.8 | actor_loss: -0.0040 | value_loss: 0.4016 | lr: 1.59e-04
  Update  227 | Ep   949 | reward:    127.1 | mean(100):    121.4 | actor_loss: -0.0020 | value_loss: 3.7616 | lr: 1.58e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4720 | mean p(bad) before update=0.3405 | ul_lr=3.80e-05 (scale=0.38)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  228 | Ep   951 | reward:    132.5 | mean(100):    124.0 | actor_loss: -0.0055 | value_loss: 0.4496 | lr: 1.58e-04

  Update  229 | Ep   953 | reward:    143.4 | mean(100):    123.3 | actor_loss: -0.0037 | value_loss: 0.3552 | lr: 1.57e-04
  Update  230 | Ep   959 | reward:    217.9 | mean(100):    124.0 | actor_loss: -0.0058 | value_loss: 7.4823 | lr: 1.57e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3472 | mean p(bad) before update=0.2564 | ul_lr=3.60e-05 (scale=0.36)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  231 | Ep   963 | reward:    185.0 | mean(100):    128.1 | actor_loss: -0.0015 | value_loss: 3.4030 | lr: 1.56e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  232 | Ep   965 | reward:    203.2 | mean(100):    130.8 | actor_loss: -0.0025 | value_loss: 2.4981 | lr: 1.56e-04
  Update  233 | Ep   969 | reward:    132.8 | mean(100):    134.7 | actor_loss: -0.0022 | value_loss: 4.1737 | lr: 1.55e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=0.1651 | mean p(bad) before update=0.1322 | ul_lr=3.20e-05 (scale=0.32)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  234 | Ep   971 | reward:    141.6 | mean(100):    136.0 | actor_loss: -0.0013 | value_loss: 0.4298 | lr: 1.55e-04

  Update  235 | Ep   975 | reward:    188.1 | mean(100):    136.4 | actor_loss: -0.0004 | value_loss: 4.2267 | lr: 1.54e-04
  Update  236 | Ep   978 | reward:    117.6 | mean(100):    135.9 | actor_loss: -0.0060 | value_loss: 2.4154 | lr: 1.54e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5375 | mean p(bad) before update=0.4111 | ul_lr=3.16e-05 (scale=0.32)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  237 | Ep   981 | reward:    128.4 | mean(100):    136.7 | actor_loss: -0.0051 | value_loss: 3.0089 | lr: 1.53e-04
  Update  238 | Ep   983 | reward:    130.0 | mean(100):    138.9 | actor_loss: -0.0056 | value_loss: 1.0822 | lr: 1.53e-04
  Update  239 | Ep   985 | reward:     11.4 | mean(100):    136.6 | actor_loss: -0.0053 | value_loss: 1.3557 | lr: 1.53e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  240 | Ep   989 | reward:    182.3 | mean(100):    134.0 | actor_loss: -0.0019 | value_loss: 3.7077 | lr: 1.52e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1824 | mean p(bad) before update=0.1665 | ul_lr=3.35e-05 (scale=0.34)
  Update  241 | Ep   994 | reward:    188.7 | mean(100):    132.9 | actor_loss: -0.0014 | value_loss: 4.3852 | lr: 1.52e-04
  Update  242 | Ep   999 | reward:    226.6 | mean(100):    137.8 | actor_loss: -0.0032 | value_loss: 4.9213 | lr: 1.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  243 | Ep  1001 | reward:    217.2 | mean(100):    141.0 | actor_loss: -0.0048 | value_loss: 2.1551 | lr: 1.50e-04
  Update  244 | Ep  1007 | reward:      1.4 | mean(100):    133.2 | actor_loss: -0.0058 | value_loss: 6.8279 | lr: 1.50e-04
  Update  245 | Ep  1009 | reward:    212.0 | mean(100):    134.0 | actor_loss: -0.0006 | value_loss: 2.5916 | lr: 1.49e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  246 | Ep  1012 | reward:    228.8 | mean(100):    135.9 | actor_loss: -0.0054 | value_loss: 2.5789 | lr: 1.49e-04

  Update  247 | Ep  1017 | reward:    195.8 | mean(100):    135.5 | actor_loss: -0.0014 | value_loss: 4.1457 | lr: 1.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.4687 | mean p(bad) before update=0.6919 | ul_lr=3.26e-05 (scale=0.33)
  Update  248 | Ep  1022 | reward:    -34.7 | mean(100):    134.8 | actor_loss: -0.0034 | value_loss: 4.2062 | lr: 1.47e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  249 | Ep  1024 | reward:    138.7 | mean(100):    135.8 | actor_loss: -0.0016 | value_loss: 1.6378 | lr: 1.47e-04
  Update  250 | Ep  1027 | reward:    206.7 | mean(100):    134.8 | actor_loss: -0.0056 | value_loss: 2.9746 | lr: 1.46e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3173 | mean p(bad) before update=0.2304 | ul_lr=3.45e-05 (scale=0.34)
  Update  251 | Ep  1030 | reward:      2.8 | mean(100):    131.0 | actor_loss: -0.0033 | value_loss: 3.0959 | lr: 1.46e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  252 | Ep  1035 | reward:     12.1 | mean(100):    129.4 | actor_loss: -0.0020 | value_loss: 4.8546 | lr: 1.45e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.9891 | mean p(bad) before update=0.6039 | ul_lr=3.54e-05 (scale=0.35)
  Update  253 | Ep  1042 | reward:    191.2 | mean(100):    129.2 | actor_loss: -0.0042 | value_loss: 7.0826 | lr: 1.45e-04
  Update  254 | Ep  1044 | reward:    137.1 | mean(100):    128.2 | actor_loss: -0.0050 | value_loss: 1.0463 | lr: 1.44e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8051 | mean p(bad) before update=0.5035 | ul_lr=3.47e-05 (scale=0.35)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  255 | Ep  1050 | reward:     14.2 | mean(100):    130.6 | actor_loss: -0.0043 | value_loss: 6.5557 | lr: 1.43e-04

  Update  256 | Ep  1052 | reward:    163.0 | mean(100):    130.8 | actor_loss: -0.0046 | value_loss: 2.6185 | lr: 1.42e-04
  Update  257 | Ep  1054 | reward:    148.7 | mean(100):    129.3 | actor_loss: -0.0013 | value_loss: 1.4667 | lr: 1.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  258 | Ep  1059 | reward:     14.2 | mean(100):    128.7 | actor_loss: -0.0078 | value_loss: 4.9070 | lr: 1.42e-04

  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.1651 | mean p(bad) before update=0.1520 | ul_lr=3.51e-05 (scale=0.35)
  Update  259 | Ep  1062 | reward:    225.6 | mean(100):    129.8 | actor_loss: -0.0017 | value_loss: 4.0958 | lr: 1.41e-04
  Update  260 | Ep  1069 | reward:    184.9 | mean(100):    126.6 | actor_loss: -0.0020 | value_loss: 9.5478 | lr: 1.41e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.3067 | mean p(bad) before update=0.7256 | ul_lr=3.64e-05 (scale=0.36)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  261 | Ep  1072 | reward:    139.7 | mean(100):    127.2 | actor_loss: -0.0013 | value_loss: 2.2932 | lr: 1.40e-04

  Update  262 | Ep  1074 | reward:    142.6 | mean(100):    130.2 | actor_loss: -0.0015 | value_loss: 2.8339 | lr: 1.39e-04
  Update  263 | Ep  1077 | reward:    233.2 | mean(100):    129.5 | actor_loss: -0.0026 | value_loss: 3.4853 | lr: 1.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  264 | Ep  1081 | reward:    113.7 | mean(100):    132.5 | actor_loss: -0.0020 | value_loss: 3.9263 | lr: 1.38e-04
  Update  265 | Ep  1086 | reward:    -12.7 | mean(100):    132.3 | actor_loss: -0.0036 | value_loss: 7.0421 | lr: 1.38e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8962 | mean p(bad) before update=0.5192 | ul_lr=3.36e-05 (scale=0.34)
  Update  266 | Ep  1090 | reward:    212.3 | mean(100):    132.7 | actor_loss: -0.0030 | value_loss: 3.1485 | lr: 1.37e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  267 | Ep  1093 | reward:    191.2 | mean(100):    134.5 | actor_loss: -0.0022 | value_loss: 2.7635 | lr: 1.36e-04

  Update  268 | Ep  1096 | reward:    201.8 | mean(100):    132.7 | actor_loss: -0.0020 | value_loss: 2.8119 | lr: 1.36e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.2866 | mean p(bad) before update=0.7193 | ul_lr=3.48e-05 (scale=0.35)
  Update  269 | Ep  1101 | reward:     -7.0 | mean(100):    130.4 | actor_loss: -0.0024 | value_loss: 5.3407 | lr: 1.36e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  270 | Ep  1106 | reward:    205.5 | mean(100):    132.0 | actor_loss: -0.0049 | value_loss: 5.0636 | lr: 1.35e-04

  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2543 | mean p(bad) before update=0.2239 | ul_lr=3.33e-05 (scale=0.33)
  Update  271 | Ep  1110 | reward:    198.2 | mean(100):    133.4 | actor_loss: -0.0017 | value_loss: 5.9215 | lr: 1.34e-04
  Update  272 | Ep  1117 | reward:    219.0 | mean(100):    132.5 | actor_loss: -0.0036 | value_loss: 7.5963 | lr: 1.33e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.3195 | mean p(bad) before update=0.2369 | ul_lr=3.58e-05 (scale=0.36)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  273 | Ep  1121 | reward:    206.7 | mean(100):    128.4 | actor_loss: -0.0027 | value_loss: 4.0457 | lr: 1.32e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  274 | Ep  1123 | reward:    128.3 | mean(100):    129.2 | actor_loss: -0.0030 | value_loss: 2.6599 | lr: 1.32e-04
  Update  275 | Ep  1128 | reward:    208.2 | mean(100):    132.3 | actor_loss: -0.0027 | value_loss: 5.7152 | lr: 1.32e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.7694 | mean p(bad) before update=0.6124 | ul_lr=3.35e-05 (scale=0.34)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  276 | Ep  1132 | reward:     24.5 | mean(100):    133.0 | actor_loss: -0.0040 | value_loss: 3.5198 | lr: 1.31e-04
  Update  277 | Ep  1135 | reward:    211.5 | mean(100):    134.8 | actor_loss: -0.0020 | value_loss: 4.2441 | lr: 1.30e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2888 | mean p(bad) before update=0.2470 | ul_lr=3.13e-05 (scale=0.31)
  Update  278 | Ep  1140 | reward:    222.8 | mean(100):    137.5 | actor_loss: -0.0023 | value_loss: 4.7657 | lr: 1.30e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  279 | Ep  1147 | reward:    216.9 | mean(100):    138.9 | actor_loss: -0.0014 | value_loss: 8.6897 | lr: 1.29e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter) | unlikelihood_loss=1.9547 | mean p(bad) before update=0.6330 | ul_lr=3.00e-05 (scale=0.30)
  Update  280 | Ep  1150 | reward:    194.6 | mean(100):    140.0 | actor_loss: -0.0021 | value_loss: 3.9417 | lr: 1.28e-04
  Update  281 | Ep  1159 | reward:     45.0 | mean(100):    136.1 | actor_loss: -0.0067 | value_loss: 9.0186 | lr: 1.28e-04
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2452 | mean p(bad) before update=0.2174 | ul_lr=3.23e-05 (scale=0.32)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  282 | Ep  1162 | reward:    127.9 | mean(100):    135.4 | actor_loss: -0.0005 | value_loss: 2.6100 | lr: 1.26e-04

  Update  283 | Ep  1166 | reward:    247.5 | mean(100):    138.0 | actor_loss: -0.0026 | value_loss: 3.1470 | lr: 1.26e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4571 | mean p(bad) before update=0.3352 | ul_lr=3.27e-05 (scale=0.33)
  Update  284 | Ep  1172 | reward:    240.7 | mean(100):    134.5 | actor_loss: -0.0012 | value_loss: 4.9546 | lr: 1.25e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  285 | Ep  1177 | reward:    -62.5 | mean(100):    130.4 | actor_loss: -0.0064 | value_loss: 4.9647 | lr: 1.24e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.2190 | mean p(bad) before update=0.1885 | ul_lr=3.76e-05 (scale=0.38)
  Update  286 | Ep  1180 | reward:      6.4 | mean(100):    124.8 | actor_loss: -0.0044 | value_loss: 2.9430 | lr: 1.23e-04
  Update  287 | Ep  1185 | reward:     25.7 | mean(100):    124.2 | actor_loss: -0.0006 | value_loss: 6.1656 | lr: 1.23e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.8100 | mean p(bad) before update=0.6421 | ul_lr=3.93e-05 (scale=0.39)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  288 | Ep  1191 | reward:    -17.2 | mean(100):    121.3 | actor_loss: -0.0019 | value_loss: 6.4556 | lr: 1.22e-04

  Update  289 | Ep  1198 | reward:     -5.1 | mean(100):    122.7 | actor_loss: -0.0032 | value_loss: 8.1754 | lr: 1.21e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4062 | mean p(bad) before update=0.2589 | ul_lr=4.10e-05 (scale=0.41)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  290 | Ep  1205 | reward:    -10.2 | mean(100):    118.1 | actor_loss: -0.0020 | value_loss: 7.1580 | lr: 1.20e-04

  Update  291 | Ep  1208 | reward:     64.1 | mean(100):    117.8 | actor_loss: -0.0024 | value_loss: 2.6775 | lr: 1.19e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.7567 | mean p(bad) before update=0.4535 | ul_lr=4.36e-05 (scale=0.44)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  292 | Ep  1213 | reward:    216.1 | mean(100):    112.9 | actor_loss: -0.0041 | value_loss: 5.3792 | lr: 1.19e-04

  Update  293 | Ep  1215 | reward:    196.1 | mean(100):    114.2 | actor_loss: -0.0008 | value_loss: 1.5016 | lr: 1.18e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  294 | Ep  1219 | reward:    243.8 | mean(100):    113.8 | actor_loss: -0.0007 | value_loss: 4.7581 | lr: 1.18e-04

  Update  295 | Ep  1224 | reward:    -59.2 | mean(100):    108.4 | actor_loss: -0.0009 | value_loss: 5.3546 | lr: 1.17e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  296 | Ep  1230 | reward:    225.6 | mean(100):    107.4 | actor_loss: -0.0023 | value_loss: 5.2465 | lr: 1.16e-04

  Update  297 | Ep  1232 | reward:    160.5 | mean(100):    109.9 | actor_loss: -0.0036 | value_loss: 3.0196 | lr: 1.15e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  298 | Ep  1239 | reward:      7.4 | mean(100):    100.8 | actor_loss: -0.0069 | value_loss: 7.7678 | lr: 1.15e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.5037 | mean p(bad) before update=0.3625 | ul_lr=5.00e-05 (scale=0.50)
  Update  299 | Ep  1241 | reward:    217.3 | mean(100):    100.0 | actor_loss: -0.0015 | value_loss: 1.9806 | lr: 1.14e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  300 | Ep  1246 | reward:    110.3 | mean(100):     97.3 | actor_loss: -0.0033 | value_loss: 5.7479 | lr: 1.14e-04

  Update  301 | Ep  1248 | reward:    248.2 | mean(100):     97.0 | actor_loss: -0.0003 | value_loss: 1.5691 | lr: 1.13e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8803 | mean p(bad) before update=0.4102 | ul_lr=5.28e-05 (scale=0.53)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  302 | Ep  1251 | reward:    -32.6 | mean(100):     94.4 | actor_loss: -0.0036 | value_loss: 4.5314 | lr: 1.13e-04
  Update  303 | Ep  1257 | reward:    137.1 | mean(100):     95.4 | actor_loss: -0.0017 | value_loss: 6.3854 | lr: 1.12e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.4793 | mean p(bad) before update=0.2732 | ul_lr=5.67e-05 (scale=0.57)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  304 | Ep  1265 | reward:    -31.6 | mean(100):     86.7 | actor_loss: -0.0039 | value_loss: 6.9067 | lr: 1.11e-04

  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8284 | mean p(bad) before update=0.5477 | ul_lr=5.71e-05 (scale=0.57)
  Update  305 | Ep  1271 | reward:    -56.1 | mean(100):     85.8 | actor_loss: -0.0045 | value_loss: 6.3817 | lr: 1.10e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  306 | Ep  1277 | reward:     33.3 | mean(100):     88.4 | actor_loss: -0.0014 | value_loss: 5.0369 | lr: 1.09e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 1 episodes -> 2 bad pairs (0 dropped by adv filter) | unlikelihood_loss=0.8207 | mean p(bad) before update=0.4756 | ul_lr=5.62e-05 (scale=0.56)
  Update  307 | Ep  1283 | reward:    208.2 | mean(100):     87.7 | actor_loss: -0.0026 | value_loss: 7.9545 | lr: 1.08e-04
  [Analyzer] 2 episodes -> 4 bad pairs (2 dropped by adv filter) | unlikelihood_loss=0.9207 | mean p(bad) before update=0.5895 | ul_lr=5.64e-05 (scale=0.56)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  308 | Ep  1292 | reward:   -148.5 | mean(100):     87.3 | actor_loss: -0.0030 | value_loss: 12.1639 | lr: 1.08e-04
  Update  309 | Ep  1298 | reward:    181.5 | mean(100):     83.6 | actor_loss: -0.0048 | value_loss: 5.7795 | lr: 1.06e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter) | unlikelihood_loss=1.1502 | mean p(bad) before update=0.5316 | ul_lr=5.56e-05 (scale=0.56)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  310 | Ep  1303 | reward:    148.8 | mean(100):     88.9 | actor_loss: -0.0028 | value_loss: 5.2825 | lr: 1.05e-04
