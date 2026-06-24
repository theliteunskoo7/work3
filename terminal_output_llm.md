Using device: cuda (rollout collection stays on CPU; batched updates use cuda)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=gpt-4o-mini

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2240 | mean p(bad) before update=0.2006
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2788 | mean p(bad) before update=0.2430

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    1 | Ep    21 | reward:    -34.9 | mean(100):   -193.8 | actor_loss: -0.0055 | value_loss: 32.4345 | lr: 3.00e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2355 | mean p(bad) before update=0.2092
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2182 | mean p(bad) before update=0.1957

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    2 | Ep    41 | reward:    -46.8 | mean(100):   -182.0 | actor_loss: -0.0072 | value_loss: 27.3470 | lr: 2.97e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2366 | mean p(bad) before update=0.2093
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2358 | mean p(bad) before update=0.2097

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    3 | Ep    62 | reward:   -109.0 | mean(100):   -182.0 | actor_loss: -0.0090 | value_loss: 31.2863 | lr: 2.94e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2948 | mean p(bad) before update=0.2449
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2018 | mean p(bad) before update=0.1824

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    4 | Ep    83 | reward:      1.0 | mean(100):   -170.5 | actor_loss: -0.0044 | value_loss: 25.5203 | lr: 2.91e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2149 | mean p(bad) before update=0.1934
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2375 | mean p(bad) before update=0.2109

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    5 | Ep   104 | reward:    -79.6 | mean(100):   -163.6 | actor_loss: -0.0063 | value_loss: 24.2682 | lr: 2.88e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3404 | mean p(bad) before update=0.2595
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2516 | mean p(bad) before update=0.2209

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    6 | Ep   125 | reward:    -93.7 | mean(100):   -148.7 | actor_loss: -0.0070 | value_loss: 22.4917 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2536 | mean p(bad) before update=0.2193
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2737 | mean p(bad) before update=0.2390

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    7 | Ep   147 | reward:    -86.7 | mean(100):   -136.5 | actor_loss: -0.0065 | value_loss: 19.3395 | lr: 2.81e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2449 | mean p(bad) before update=0.2164
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2174 | mean p(bad) before update=0.1930

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   168 | reward:   -113.5 | mean(100):   -123.3 | actor_loss: -0.0079 | value_loss: 17.7683 | lr: 2.78e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2855 | mean p(bad) before update=0.2481
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2387 | mean p(bad) before update=0.2080
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2199 | mean p(bad) before update=0.1960

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    9 | Ep   191 | reward:    -84.9 | mean(100):   -108.5 | actor_loss: -0.0057 | value_loss: 16.2768 | lr: 2.75e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2950 | mean p(bad) before update=0.2539
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2519 | mean p(bad) before update=0.2195

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   10 | Ep   211 | reward:    -55.1 | mean(100):    -99.4 | actor_loss: -0.0081 | value_loss: 15.4516 | lr: 2.71e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3771 | mean p(bad) before update=0.2912
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5565 | mean p(bad) before update=0.4034

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   231 | reward:    -36.5 | mean(100):    -90.2 | actor_loss: -0.0079 | value_loss: 17.8978 | lr: 2.68e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3979 | mean p(bad) before update=0.2965
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2417 | mean p(bad) before update=0.2126

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   252 | reward:    -28.6 | mean(100):    -85.1 | actor_loss: -0.0070 | value_loss: 15.2473 | lr: 2.65e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3281 | mean p(bad) before update=0.2789

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   269 | reward:    -40.6 | mean(100):    -78.8 | actor_loss: -0.0080 | value_loss: 15.3859 | lr: 2.62e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1503 | mean p(bad) before update=0.1395
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1691 | mean p(bad) before update=0.1550

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   286 | reward:    -29.5 | mean(100):    -70.3 | actor_loss: -0.0131 | value_loss: 12.1728 | lr: 2.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1963 | mean p(bad) before update=0.1739

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   295 | reward:    -13.9 | mean(100):    -65.7 | actor_loss: -0.0075 | value_loss: 10.3500 | lr: 2.57e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4381 | mean p(bad) before update=0.3435
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1588 | mean p(bad) before update=0.1447

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   311 | reward:    -46.1 | mean(100):    -58.0 | actor_loss: -0.0048 | value_loss: 11.9738 | lr: 2.56e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2358 | mean p(bad) before update=0.1976

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   320 | reward:    -48.0 | mean(100):    -48.1 | actor_loss: -0.0085 | value_loss: 9.6995 | lr: 2.53e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   18 | Ep   326 | reward:      7.5 | mean(100):    -45.8 | actor_loss: -0.0066 | value_loss: 9.5064 | lr: 2.52e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   19 | Ep   328 | reward:    121.1 | mean(100):    -42.7 | actor_loss: -0.0098 | value_loss: 6.5266 | lr: 2.51e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1765 | mean p(bad) before update=0.1587
  Update   20 | Ep   330 | reward:     99.2 | mean(100):    -40.1 | actor_loss: -0.0054 | value_loss: 6.1331 | lr: 2.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   333 | reward:   -152.8 | mean(100):    -39.2 | actor_loss: -0.0063 | value_loss: 7.1387 | lr: 2.50e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   22 | Ep   335 | reward:     29.9 | mean(100):    -36.7 | actor_loss: -0.0120 | value_loss: 5.1855 | lr: 2.50e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1246 | mean p(bad) before update=0.1132

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   23 | Ep   340 | reward:    -61.4 | mean(100):    -35.4 | actor_loss: -0.0012 | value_loss: 8.4548 | lr: 2.50e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   24 | Ep   344 | reward:    -64.3 | mean(100):    -38.0 | actor_loss: -0.0053 | value_loss: 8.3062 | lr: 2.49e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   25 | Ep   346 | reward:     72.0 | mean(100):    -36.9 | actor_loss: -0.0043 | value_loss: 4.6342 | lr: 2.48e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   26 | Ep   349 | reward:     97.8 | mean(100):    -38.2 | actor_loss: -0.0100 | value_loss: 6.0753 | lr: 2.48e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4017 | mean p(bad) before update=0.3024

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   27 | Ep   352 | reward:   -147.7 | mean(100):    -37.2 | actor_loss: -0.0042 | value_loss: 6.0580 | lr: 2.48e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   28 | Ep   356 | reward:    -36.1 | mean(100):    -33.6 | actor_loss: -0.0072 | value_loss: 5.6066 | lr: 2.47e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   29 | Ep   358 | reward:    -21.2 | mean(100):    -33.0 | actor_loss: -0.0073 | value_loss: 3.9199 | lr: 2.47e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2719 | mean p(bad) before update=0.2365

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   30 | Ep   360 | reward:     39.0 | mean(100):    -33.1 | actor_loss: -0.0122 | value_loss: 4.9522 | lr: 2.46e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   31 | Ep   362 | reward:     23.8 | mean(100):    -31.3 | actor_loss: -0.0069 | value_loss: 3.5290 | lr: 2.46e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   32 | Ep   364 | reward:      9.3 | mean(100):    -30.2 | actor_loss: -0.0044 | value_loss: 2.9392 | lr: 2.46e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   33 | Ep   366 | reward:    -17.2 | mean(100):    -25.5 | actor_loss: -0.0065 | value_loss: 2.9561 | lr: 2.45e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   34 | Ep   368 | reward:     38.6 | mean(100):    -23.9 | actor_loss: -0.0033 | value_loss: 2.6931 | lr: 2.45e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3251 | mean p(bad) before update=0.2716

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   35 | Ep   370 | reward:    -78.2 | mean(100):    -25.7 | actor_loss: -0.0086 | value_loss: 3.4790 | lr: 2.45e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   36 | Ep   372 | reward:     -5.1 | mean(100):    -25.7 | actor_loss: -0.0015 | value_loss: 2.4900 | lr: 2.44e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   37 | Ep   374 | reward:     71.2 | mean(100):    -25.5 | actor_loss: -0.0010 | value_loss: 2.9949 | lr: 2.44e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   38 | Ep   376 | reward:     61.0 | mean(100):    -26.1 | actor_loss: -0.0068 | value_loss: 3.0909 | lr: 2.44e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   39 | Ep   378 | reward:     20.2 | mean(100):    -27.4 | actor_loss: -0.0061 | value_loss: 3.1890 | lr: 2.44e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5407 | mean p(bad) before update=0.3057

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   40 | Ep   380 | reward:    -51.6 | mean(100):    -26.1 | actor_loss: -0.0063 | value_loss: 2.7924 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   41 | Ep   382 | reward:    -99.9 | mean(100):    -26.1 | actor_loss: -0.0057 | value_loss: 3.5010 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   42 | Ep   384 | reward:     48.2 | mean(100):    -24.2 | actor_loss: -0.0049 | value_loss: 3.9832 | lr: 2.43e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   43 | Ep   386 | reward:     27.3 | mean(100):    -22.3 | actor_loss: -0.0047 | value_loss: 2.6475 | lr: 2.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   44 | Ep   388 | reward:     49.1 | mean(100):    -21.1 | actor_loss: -0.0089 | value_loss: 2.8049 | lr: 2.42e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2587 | mean p(bad) before update=0.2216
  Update   45 | Ep   390 | reward:    120.2 | mean(100):    -18.4 | actor_loss: -0.0091 | value_loss: 3.0844 | lr: 2.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   46 | Ep   392 | reward:    -51.8 | mean(100):    -17.6 | actor_loss: -0.0029 | value_loss: 2.7980 | lr: 2.41e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   47 | Ep   394 | reward:     56.1 | mean(100):    -15.5 | actor_loss: -0.0035 | value_loss: 1.9898 | lr: 2.41e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   48 | Ep   396 | reward:   -133.2 | mean(100):    -16.3 | actor_loss: -0.0063 | value_loss: 2.8908 | lr: 2.41e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   49 | Ep   398 | reward:     47.4 | mean(100):    -13.6 | actor_loss: -0.0043 | value_loss: 3.0785 | lr: 2.41e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.9949 | mean p(bad) before update=0.4886
  Update   50 | Ep   400 | reward:     39.6 | mean(100):    -12.0 | actor_loss: -0.0020 | value_loss: 1.8380 | lr: 2.40e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   51 | Ep   403 | reward:   -154.3 | mean(100):    -14.9 | actor_loss: -0.0018 | value_loss: 4.7371 | lr: 2.40e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   52 | Ep   405 | reward:    109.9 | mean(100):    -13.6 | actor_loss: -0.0069 | value_loss: 3.3801 | lr: 2.40e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   53 | Ep   407 | reward:     40.6 | mean(100):    -12.9 | actor_loss: -0.0024 | value_loss: 2.1290 | lr: 2.39e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   54 | Ep   409 | reward:   -104.0 | mean(100):    -12.5 | actor_loss: -0.0026 | value_loss: 1.9323 | lr: 2.39e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3001 | mean p(bad) before update=0.2402
  Update   55 | Ep   411 | reward:     98.8 | mean(100):    -10.8 | actor_loss: -0.0028 | value_loss: 2.7914 | lr: 2.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   56 | Ep   413 | reward:   -102.4 | mean(100):    -10.5 | actor_loss: 0.0017 | value_loss: 3.1338 | lr: 2.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   57 | Ep   415 | reward:     64.5 | mean(100):     -9.3 | actor_loss: -0.0022 | value_loss: 1.6489 | lr: 2.38e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   58 | Ep   418 | reward:   -115.8 | mean(100):    -11.3 | actor_loss: 0.0001 | value_loss: 3.6518 | lr: 2.38e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4053 | mean p(bad) before update=0.3076
  Update   59 | Ep   420 | reward:     47.4 | mean(100):    -11.0 | actor_loss: -0.0043 | value_loss: 3.3648 | lr: 2.37e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   60 | Ep   422 | reward:    124.9 | mean(100):     -8.1 | actor_loss: -0.0023 | value_loss: 3.0772 | lr: 2.37e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   61 | Ep   424 | reward:    104.9 | mean(100):     -7.2 | actor_loss: -0.0081 | value_loss: 2.6200 | lr: 2.37e-04

  Update   62 | Ep   426 | reward:     57.1 | mean(100):     -6.4 | actor_loss: -0.0073 | value_loss: 2.1851 | lr: 2.36e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   63 | Ep   428 | reward:    141.5 | mean(100):     -3.7 | actor_loss: -0.0037 | value_loss: 3.4904 | lr: 2.36e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5819 | mean p(bad) before update=0.3382
  Update   64 | Ep   430 | reward:     81.7 | mean(100):     -2.6 | actor_loss: -0.0021 | value_loss: 2.5138 | lr: 2.36e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   65 | Ep   433 | reward:    150.6 | mean(100):      2.1 | actor_loss: -0.0012 | value_loss: 4.0549 | lr: 2.35e-04
  Update   66 | Ep   436 | reward:    104.1 | mean(100):      1.4 | actor_loss: -0.0022 | value_loss: 3.5921 | lr: 2.35e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2829 | mean p(bad) before update=0.2327

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   67 | Ep   440 | reward:    165.6 | mean(100):      6.2 | actor_loss: -0.0020 | value_loss: 5.4529 | lr: 2.35e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   68 | Ep   444 | reward:    -32.9 | mean(100):     13.3 | actor_loss: -0.0064 | value_loss: 5.2717 | lr: 2.34e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   69 | Ep   446 | reward:     70.0 | mean(100):     15.3 | actor_loss: -0.0030 | value_loss: 3.3354 | lr: 2.33e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4211 | mean p(bad) before update=0.3145
  Update   70 | Ep   450 | reward:    190.7 | mean(100):     21.7 | actor_loss: -0.0023 | value_loss: 6.0060 | lr: 2.33e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   71 | Ep   453 | reward:    152.1 | mean(100):     28.6 | actor_loss: 0.0001 | value_loss: 4.4773 | lr: 2.32e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   72 | Ep   455 | reward:     76.7 | mean(100):     28.4 | actor_loss: -0.0002 | value_loss: 3.3349 | lr: 2.32e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6323 | mean p(bad) before update=0.4476

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   73 | Ep   460 | reward:    -78.3 | mean(100):     32.9 | actor_loss: -0.0016 | value_loss: 6.6661 | lr: 2.32e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   74 | Ep   463 | reward:    198.6 | mean(100):     36.6 | actor_loss: -0.0024 | value_loss: 4.6409 | lr: 2.31e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   75 | Ep   468 | reward:    -44.0 | mean(100):     39.6 | actor_loss: -0.0030 | value_loss: 6.8390 | lr: 2.31e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4957 | mean p(bad) before update=0.3443

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   76 | Ep   471 | reward:    143.4 | mean(100):     45.4 | actor_loss: -0.0028 | value_loss: 4.7289 | lr: 2.30e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   77 | Ep   476 | reward:    -25.6 | mean(100):     46.0 | actor_loss: -0.0004 | value_loss: 6.8458 | lr: 2.29e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2086 | mean p(bad) before update=0.1811
  Update   78 | Ep   480 | reward:    -34.0 | mean(100):     49.3 | actor_loss: -0.0070 | value_loss: 6.2265 | lr: 2.29e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   79 | Ep   482 | reward:    143.2 | mean(100):     52.1 | actor_loss: -0.0035 | value_loss: 3.3637 | lr: 2.28e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   80 | Ep   484 | reward:    129.3 | mean(100):     53.8 | actor_loss: -0.0024 | value_loss: 4.1849 | lr: 2.28e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   81 | Ep   486 | reward:     55.0 | mean(100):     52.8 | actor_loss: 0.0003 | value_loss: 2.7388 | lr: 2.27e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   82 | Ep   489 | reward:    183.1 | mean(100):     52.9 | actor_loss: -0.0012 | value_loss: 3.7701 | lr: 2.27e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4876 | mean p(bad) before update=0.3832

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   83 | Ep   493 | reward:    176.8 | mean(100):     56.5 | actor_loss: -0.0026 | value_loss: 4.9023 | lr: 2.27e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   84 | Ep   495 | reward:    103.1 | mean(100):     59.1 | actor_loss: -0.0041 | value_loss: 2.7696 | lr: 2.26e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   85 | Ep   497 | reward:    100.8 | mean(100):     62.4 | actor_loss: -0.0013 | value_loss: 2.3897 | lr: 2.26e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.9506 | mean p(bad) before update=0.5585

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   86 | Ep   501 | reward:    -79.2 | mean(100):     63.9 | actor_loss: -0.0094 | value_loss: 5.5688 | lr: 2.25e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   87 | Ep   503 | reward:    125.3 | mean(100):     68.3 | actor_loss: -0.0044 | value_loss: 1.6787 | lr: 2.25e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   88 | Ep   505 | reward:    117.9 | mean(100):     69.1 | actor_loss: -0.0052 | value_loss: 2.3601 | lr: 2.25e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3117 | mean p(bad) before update=0.2331

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   89 | Ep   510 | reward:    184.1 | mean(100):     68.1 | actor_loss: -0.0035 | value_loss: 6.4302 | lr: 2.24e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   90 | Ep   512 | reward:    188.0 | mean(100):     68.9 | actor_loss: -0.0058 | value_loss: 3.1343 | lr: 2.23e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   91 | Ep   516 | reward:    -55.3 | mean(100):     70.9 | actor_loss: -0.0014 | value_loss: 4.6069 | lr: 2.23e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   92 | Ep   519 | reward:    180.9 | mean(100):     76.8 | actor_loss: -0.0023 | value_loss: 3.4995 | lr: 2.23e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6501 | mean p(bad) before update=0.4447
  Update   93 | Ep   521 | reward:     70.3 | mean(100):     78.4 | actor_loss: -0.0043 | value_loss: 2.3251 | lr: 2.22e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   94 | Ep   524 | reward:    122.6 | mean(100):     80.1 | actor_loss: -0.0025 | value_loss: 2.8052 | lr: 2.22e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   95 | Ep   527 | reward:    195.4 | mean(100):     81.9 | actor_loss: -0.0019 | value_loss: 3.9797 | lr: 2.21e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4257 | mean p(bad) before update=0.2887

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   96 | Ep   533 | reward:    -15.1 | mean(100):     75.6 | actor_loss: -0.0045 | value_loss: 6.8745 | lr: 2.21e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   97 | Ep   536 | reward:    -57.1 | mean(100):     75.4 | actor_loss: -0.0027 | value_loss: 3.5228 | lr: 2.20e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6582 | mean p(bad) before update=0.4087
  Update   98 | Ep   540 | reward:    -61.8 | mean(100):     78.4 | actor_loss: -0.0040 | value_loss: 4.9987 | lr: 2.20e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   99 | Ep   542 | reward:    135.4 | mean(100):     79.6 | actor_loss: -0.0045 | value_loss: 3.1337 | lr: 2.19e-04

  Update  100 | Ep   544 | reward:     94.1 | mean(100):     80.5 | actor_loss: -0.0012 | value_loss: 2.6834 | lr: 2.19e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  101 | Ep   547 | reward:     84.5 | mean(100):     81.5 | actor_loss: -0.0009 | value_loss: 3.6415 | lr: 2.18e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  102 | Ep   549 | reward:     76.7 | mean(100):     80.4 | actor_loss: -0.0019 | value_loss: 2.3303 | lr: 2.18e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5971 | mean p(bad) before update=0.4073

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  103 | Ep   552 | reward:     -7.1 | mean(100):     76.9 | actor_loss: -0.0075 | value_loss: 3.8392 | lr: 2.18e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  104 | Ep   556 | reward:    -81.2 | mean(100):     71.9 | actor_loss: -0.0069 | value_loss: 4.7435 | lr: 2.17e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  105 | Ep   558 | reward:    169.8 | mean(100):     74.3 | actor_loss: -0.0020 | value_loss: 4.5161 | lr: 2.17e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7987 | mean p(bad) before update=0.5250
  Update  106 | Ep   561 | reward:    163.4 | mean(100):     76.6 | actor_loss: -0.0008 | value_loss: 3.0783 | lr: 2.16e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  107 | Ep   563 | reward:     86.2 | mean(100):     75.0 | actor_loss: -0.0078 | value_loss: 1.1827 | lr: 2.16e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  108 | Ep   566 | reward:    167.6 | mean(100):     74.8 | actor_loss: -0.0064 | value_loss: 3.0251 | lr: 2.16e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  109 | Ep   569 | reward:    184.7 | mean(100):     79.0 | actor_loss: -0.0026 | value_loss: 4.1728 | lr: 2.15e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.3874 | mean p(bad) before update=0.5103

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  110 | Ep   573 | reward:     96.8 | mean(100):     73.5 | actor_loss: -0.0033 | value_loss: 4.5819 | lr: 2.15e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  111 | Ep   576 | reward:    -61.4 | mean(100):     77.2 | actor_loss: -0.0025 | value_loss: 3.6250 | lr: 2.14e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  112 | Ep   578 | reward:     78.9 | mean(100):     78.1 | actor_loss: -0.0074 | value_loss: 1.4424 | lr: 2.14e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2671 | mean p(bad) before update=0.2114
  Update  113 | Ep   581 | reward:    -76.3 | mean(100):     75.4 | actor_loss: 0.0014 | value_loss: 3.3784 | lr: 2.13e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  114 | Ep   584 | reward:     30.4 | mean(100):     72.9 | actor_loss: -0.0008 | value_loss: 3.5722 | lr: 2.13e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  115 | Ep   588 | reward:     94.1 | mean(100):     77.1 | actor_loss: -0.0019 | value_loss: 4.2895 | lr: 2.12e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6017 | mean p(bad) before update=0.4256

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  116 | Ep   591 | reward:   -163.9 | mean(100):     73.6 | actor_loss: -0.0019 | value_loss: 4.3220 | lr: 2.12e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  117 | Ep   594 | reward:    -53.0 | mean(100):     70.6 | actor_loss: -0.0058 | value_loss: 4.2410 | lr: 2.11e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  118 | Ep   597 | reward:    189.5 | mean(100):     72.1 | actor_loss: -0.0014 | value_loss: 2.8896 | lr: 2.11e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8869 | mean p(bad) before update=0.5602
  Update  119 | Ep   601 | reward:    176.3 | mean(100):     73.6 | actor_loss: -0.0002 | value_loss: 6.9340 | lr: 2.10e-04
[AI Agent] Updating 10-point summary with new PPO episodes...


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  120 | Ep   605 | reward:    175.0 | mean(100):     74.4 | actor_loss: -0.0022 | value_loss: 4.8300 | lr: 2.10e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  121 | Ep   608 | reward:    196.3 | mean(100):     79.9 | actor_loss: -0.0033 | value_loss: 3.4776 | lr: 2.09e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4872 | mean p(bad) before update=0.3434

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  122 | Ep   613 | reward:    174.9 | mean(100):     77.1 | actor_loss: -0.0050 | value_loss: 6.3006 | lr: 2.09e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  123 | Ep   615 | reward:    148.6 | mean(100):     78.5 | actor_loss: -0.0036 | value_loss: 3.4822 | lr: 2.08e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3589 | mean p(bad) before update=0.2727

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  124 | Ep   621 | reward:    -46.9 | mean(100):     75.4 | actor_loss: -0.0017 | value_loss: 7.6000 | lr: 2.08e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  125 | Ep   625 | reward:    -54.4 | mean(100):     74.1 | actor_loss: -0.0093 | value_loss: 3.6487 | lr: 2.07e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.2233 | mean p(bad) before update=0.6276

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  126 | Ep   630 | reward:    173.8 | mean(100):     78.8 | actor_loss: -0.0056 | value_loss: 6.4508 | lr: 2.06e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  127 | Ep   634 | reward:    218.6 | mean(100):     82.1 | actor_loss: -0.0039 | value_loss: 4.6356 | lr: 2.06e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  128 | Ep   637 | reward:    199.8 | mean(100):     86.4 | actor_loss: -0.0031 | value_loss: 4.7822 | lr: 2.05e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4872 | mean p(bad) before update=0.3478

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  129 | Ep   640 | reward:    209.3 | mean(100):     87.9 | actor_loss: -0.0021 | value_loss: 4.4844 | lr: 2.04e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  130 | Ep   644 | reward:    200.2 | mean(100):     88.4 | actor_loss: -0.0013 | value_loss: 3.5233 | lr: 2.04e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  131 | Ep   649 | reward:    -43.7 | mean(100):     84.0 | actor_loss: -0.0042 | value_loss: 4.3883 | lr: 2.03e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5999 | mean p(bad) before update=0.4464

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  132 | Ep   656 | reward:    -74.9 | mean(100):     85.5 | actor_loss: -0.0050 | value_loss: 8.7106 | lr: 2.03e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7735 | mean p(bad) before update=0.4624

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  133 | Ep   661 | reward:     90.3 | mean(100):     81.0 | actor_loss: -0.0036 | value_loss: 4.6873 | lr: 2.02e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  134 | Ep   667 | reward:     -2.9 | mean(100):     79.7 | actor_loss: -0.0055 | value_loss: 6.6188 | lr: 2.01e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3332 | mean p(bad) before update=0.2769

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  135 | Ep   671 | reward:     -3.6 | mean(100):     81.3 | actor_loss: -0.0046 | value_loss: 4.8639 | lr: 2.00e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  136 | Ep   674 | reward:    191.2 | mean(100):     84.8 | actor_loss: -0.0011 | value_loss: 4.1193 | lr: 1.99e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  137 | Ep   678 | reward:    -19.3 | mean(100):     85.8 | actor_loss: -0.0006 | value_loss: 5.4293 | lr: 1.99e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3212 | mean p(bad) before update=0.2441

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  138 | Ep   681 | reward:    -71.0 | mean(100):     88.6 | actor_loss: -0.0043 | value_loss: 4.1921 | lr: 1.98e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  139 | Ep   687 | reward:     -9.4 | mean(100):     84.5 | actor_loss: 0.0003 | value_loss: 5.6841 | lr: 1.98e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4141 | mean p(bad) before update=0.3112

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  140 | Ep   694 | reward:    -58.2 | mean(100):     84.1 | actor_loss: -0.0024 | value_loss: 9.4218 | lr: 1.97e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  141 | Ep   697 | reward:     77.4 | mean(100):     83.4 | actor_loss: -0.0025 | value_loss: 4.5793 | lr: 1.96e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  142 | Ep   699 | reward:    129.7 | mean(100):     82.9 | actor_loss: -0.0094 | value_loss: 1.2309 | lr: 1.95e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.1867 | mean p(bad) before update=0.1639

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  143 | Ep   703 | reward:    140.5 | mean(100):     84.6 | actor_loss: -0.0024 | value_loss: 4.6735 | lr: 1.95e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  144 | Ep   706 | reward:    157.6 | mean(100):     80.9 | actor_loss: -0.0009 | value_loss: 5.0825 | lr: 1.95e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  145 | Ep   709 | reward:    167.4 | mean(100):     84.5 | actor_loss: -0.0030 | value_loss: 2.8494 | lr: 1.94e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4209 | mean p(bad) before update=0.3190
  Update  146 | Ep   711 | reward:    138.0 | mean(100):     86.9 | actor_loss: -0.0051 | value_loss: 2.8483 | lr: 1.94e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  147 | Ep   713 | reward:    107.7 | mean(100):     88.3 | actor_loss: -0.0011 | value_loss: 2.0515 | lr: 1.93e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  148 | Ep   717 | reward:     90.2 | mean(100):     87.8 | actor_loss: -0.0017 | value_loss: 4.5470 | lr: 1.93e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5987 | mean p(bad) before update=0.4116
  Update  149 | Ep   720 | reward:    124.6 | mean(100):     87.7 | actor_loss: -0.0009 | value_loss: 3.0518 | lr: 1.92e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  150 | Ep   723 | reward:    -32.4 | mean(100):     89.9 | actor_loss: -0.0043 | value_loss: 3.8416 | lr: 1.92e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  151 | Ep   725 | reward:    121.1 | mean(100):     90.4 | actor_loss: -0.0082 | value_loss: 0.7723 | lr: 1.92e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  152 | Ep   729 | reward:     -9.3 | mean(100):     87.8 | actor_loss: -0.0031 | value_loss: 4.1479 | lr: 1.91e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5731 | mean p(bad) before update=0.3694
  Update  153 | Ep   733 | reward:    109.1 | mean(100):     88.8 | actor_loss: -0.0012 | value_loss: 4.5588 | lr: 1.91e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  154 | Ep   737 | reward:    223.4 | mean(100):     86.1 | actor_loss: -0.0035 | value_loss: 4.2992 | lr: 1.90e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7586 | mean p(bad) before update=0.4029
  Update  155 | Ep   743 | reward:     -8.4 | mean(100):     86.4 | actor_loss: -0.0026 | value_loss: 8.4561 | lr: 1.89e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  156 | Ep   745 | reward:    189.5 | mean(100):     86.2 | actor_loss: -0.0043 | value_loss: 2.0795 | lr: 1.89e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  157 | Ep   749 | reward:    218.3 | mean(100):     92.1 | actor_loss: -0.0080 | value_loss: 4.1121 | lr: 1.88e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5532 | mean p(bad) before update=0.3753
  Update  158 | Ep   751 | reward:    114.0 | mean(100):     93.0 | actor_loss: -0.0028 | value_loss: 2.2684 | lr: 1.88e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  159 | Ep   753 | reward:    126.2 | mean(100):     94.3 | actor_loss: -0.0074 | value_loss: 1.6088 | lr: 1.87e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  160 | Ep   757 | reward:     84.1 | mean(100):    101.6 | actor_loss: -0.0011 | value_loss: 5.4041 | lr: 1.87e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8959 | mean p(bad) before update=0.5285

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  161 | Ep   760 | reward:     15.9 | mean(100):    103.6 | actor_loss: -0.0042 | value_loss: 2.7536 | lr: 1.86e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  162 | Ep   767 | reward:    201.4 | mean(100):    103.1 | actor_loss: -0.0018 | value_loss: 10.1085 | lr: 1.86e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  163 | Ep   769 | reward:    138.1 | mean(100):    101.9 | actor_loss: -0.0012 | value_loss: 2.3871 | lr: 1.85e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2393 | mean p(bad) before update=0.2003

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  164 | Ep   773 | reward:    149.2 | mean(100):    103.0 | actor_loss: -0.0011 | value_loss: 4.0449 | lr: 1.85e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  165 | Ep   777 | reward:    101.4 | mean(100):    100.7 | actor_loss: -0.0042 | value_loss: 4.2406 | lr: 1.84e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  166 | Ep   779 | reward:    198.4 | mean(100):    103.5 | actor_loss: -0.0021 | value_loss: 1.9253 | lr: 1.83e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.3387 | mean p(bad) before update=0.6933

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  167 | Ep   782 | reward:    -45.2 | mean(100):    102.0 | actor_loss: -0.0055 | value_loss: 3.0448 | lr: 1.83e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  168 | Ep   787 | reward:    -38.1 | mean(100):    102.6 | actor_loss: -0.0044 | value_loss: 4.2631 | lr: 1.83e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8398 | mean p(bad) before update=0.5640

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  169 | Ep   792 | reward:    195.0 | mean(100):    110.4 | actor_loss: -0.0021 | value_loss: 6.1014 | lr: 1.82e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  170 | Ep   795 | reward:    103.4 | mean(100):    112.4 | actor_loss: -0.0029 | value_loss: 4.1529 | lr: 1.81e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8709 | mean p(bad) before update=0.5241

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  171 | Ep   800 | reward:    -43.5 | mean(100):    109.3 | actor_loss: -0.0027 | value_loss: 6.7852 | lr: 1.81e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  172 | Ep   804 | reward:    141.7 | mean(100):    108.4 | actor_loss: -0.0039 | value_loss: 3.8199 | lr: 1.80e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4323 | mean p(bad) before update=0.3311

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  173 | Ep   812 | reward:   -161.4 | mean(100):     99.3 | actor_loss: -0.0069 | value_loss: 10.3931 | lr: 1.79e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  174 | Ep   815 | reward:    178.1 | mean(100):    102.6 | actor_loss: -0.0046 | value_loss: 4.4122 | lr: 1.78e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3035 | mean p(bad) before update=0.2569

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  175 | Ep   822 | reward:    -53.3 | mean(100):    104.1 | actor_loss: -0.0049 | value_loss: 8.1593 | lr: 1.78e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  176 | Ep   825 | reward:    163.7 | mean(100):    106.9 | actor_loss: -0.0023 | value_loss: 3.3024 | lr: 1.77e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  177 | Ep   828 | reward:    219.3 | mean(100):    107.9 | actor_loss: -0.0037 | value_loss: 2.4381 | lr: 1.76e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.3437 | mean p(bad) before update=0.3278

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  178 | Ep   834 | reward:    171.2 | mean(100):    107.5 | actor_loss: -0.0015 | value_loss: 7.0897 | lr: 1.76e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  179 | Ep   837 | reward:    194.0 | mean(100):    106.7 | actor_loss: -0.0013 | value_loss: 2.8182 | lr: 1.75e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3814 | mean p(bad) before update=0.3081

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  180 | Ep   842 | reward:    195.3 | mean(100):    100.6 | actor_loss: -0.0031 | value_loss: 7.0503 | lr: 1.74e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  181 | Ep   847 | reward:   -158.8 | mean(100):     93.9 | actor_loss: -0.0013 | value_loss: 5.4355 | lr: 1.74e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6590 | mean p(bad) before update=0.4482

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  182 | Ep   852 | reward:    -59.5 | mean(100):     92.2 | actor_loss: -0.0017 | value_loss: 4.1739 | lr: 1.73e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  183 | Ep   856 | reward:   -126.2 | mean(100):     88.6 | actor_loss: -0.0022 | value_loss: 5.3234 | lr: 1.72e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3596 | mean p(bad) before update=0.2818

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  184 | Ep   862 | reward:    -51.0 | mean(100):     89.2 | actor_loss: -0.0041 | value_loss: 7.4849 | lr: 1.72e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  185 | Ep   864 | reward:    122.5 | mean(100):     89.6 | actor_loss: -0.0035 | value_loss: 1.6684 | lr: 1.71e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  186 | Ep   869 | reward:    -74.0 | mean(100):     87.3 | actor_loss: -0.0000 | value_loss: 4.1291 | lr: 1.70e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6774 | mean p(bad) before update=0.4794
  Update  187 | Ep   874 | reward:    116.3 | mean(100):     87.0 | actor_loss: -0.0010 | value_loss: 4.8623 | lr: 1.70e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  188 | Ep   876 | reward:    124.1 | mean(100):     86.3 | actor_loss: -0.0035 | value_loss: 1.6495 | lr: 1.69e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4990 | mean p(bad) before update=0.3807

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  189 | Ep   881 | reward:   -147.0 | mean(100):     81.8 | actor_loss: -0.0014 | value_loss: 9.0245 | lr: 1.69e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  190 | Ep   885 | reward:    224.8 | mean(100):     84.9 | actor_loss: -0.0020 | value_loss: 4.1527 | lr: 1.68e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  191 | Ep   889 | reward:    113.2 | mean(100):     87.4 | actor_loss: -0.0032 | value_loss: 4.0697 | lr: 1.67e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8415 | mean p(bad) before update=0.5617

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  192 | Ep   893 | reward:     -6.2 | mean(100):     82.3 | actor_loss: -0.0034 | value_loss: 3.9736 | lr: 1.67e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  193 | Ep   898 | reward:    -56.6 | mean(100):     81.6 | actor_loss: -0.0028 | value_loss: 5.9473 | lr: 1.66e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2558 | mean p(bad) before update=0.2088
  Update  194 | Ep   900 | reward:    122.7 | mean(100):     85.4 | actor_loss: -0.0049 | value_loss: 1.2046 | lr: 1.65e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  195 | Ep   903 | reward:    165.4 | mean(100):     85.3 | actor_loss: -0.0021 | value_loss: 3.5429 | lr: 1.65e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  196 | Ep   906 | reward:    -26.4 | mean(100):     88.8 | actor_loss: -0.0016 | value_loss: 2.4106 | lr: 1.65e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3985 | mean p(bad) before update=0.3243

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  197 | Ep   910 | reward:    144.3 | mean(100):     87.9 | actor_loss: -0.0031 | value_loss: 4.3657 | lr: 1.64e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  198 | Ep   913 | reward:    -33.7 | mean(100):     90.8 | actor_loss: -0.0017 | value_loss: 2.3474 | lr: 1.63e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  199 | Ep   917 | reward:    117.3 | mean(100):     90.0 | actor_loss: -0.0041 | value_loss: 4.9459 | lr: 1.63e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4346 | mean p(bad) before update=0.3106
  Update  200 | Ep   920 | reward:    201.4 | mean(100):     89.8 | actor_loss: -0.0011 | value_loss: 3.0519 | lr: 1.62e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  201 | Ep   924 | reward:    108.7 | mean(100):     85.5 | actor_loss: -0.0032 | value_loss: 3.8085 | lr: 1.62e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  202 | Ep   929 | reward:    -51.6 | mean(100):     86.2 | actor_loss: -0.0041 | value_loss: 4.5771 | lr: 1.61e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8877 | mean p(bad) before update=0.5853
  Update  203 | Ep   931 | reward:    120.9 | mean(100):     87.1 | actor_loss: -0.0057 | value_loss: 1.2316 | lr: 1.61e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  204 | Ep   935 | reward:    201.2 | mean(100):     86.9 | actor_loss: -0.0033 | value_loss: 3.5598 | lr: 1.60e-04
  Update  205 | Ep   937 | reward:    197.7 | mean(100):     86.8 | actor_loss: -0.0025 | value_loss: 2.3158 | lr: 1.60e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4197 | mean p(bad) before update=0.3405
  Update  206 | Ep   940 | reward:     92.3 | mean(100):     91.3 | actor_loss: -0.0040 | value_loss: 3.0880 | lr: 1.59e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  207 | Ep   944 | reward:    231.4 | mean(100):     96.0 | actor_loss: -0.0042 | value_loss: 3.9988 | lr: 1.59e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6800 | mean p(bad) before update=0.4619

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  208 | Ep   952 | reward:    -47.2 | mean(100):     96.6 | actor_loss: -0.0034 | value_loss: 8.7993 | lr: 1.58e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  209 | Ep   958 | reward:    183.3 | mean(100):     99.8 | actor_loss: -0.0029 | value_loss: 6.5324 | lr: 1.57e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6743 | mean p(bad) before update=0.4346

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  210 | Ep   964 | reward:      3.4 | mean(100):    100.4 | actor_loss: -0.0021 | value_loss: 5.2296 | lr: 1.56e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  211 | Ep   969 | reward:      4.4 | mean(100):     99.9 | actor_loss: -0.0020 | value_loss: 4.0964 | lr: 1.55e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7210 | mean p(bad) before update=0.4381

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  212 | Ep   976 | reward:    176.7 | mean(100):    103.6 | actor_loss: -0.0016 | value_loss: 7.2544 | lr: 1.55e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  213 | Ep   979 | reward:    182.7 | mean(100):    109.6 | actor_loss: -0.0016 | value_loss: 3.2677 | lr: 1.54e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.9494 | mean p(bad) before update=0.5964
  Update  214 | Ep   983 | reward:    121.4 | mean(100):    112.2 | actor_loss: -0.0014 | value_loss: 4.2708 | lr: 1.53e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  215 | Ep   988 | reward:   -135.3 | mean(100):    109.9 | actor_loss: -0.0032 | value_loss: 5.4477 | lr: 1.53e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6280 | mean p(bad) before update=0.4294
  Update  216 | Ep   993 | reward:    119.7 | mean(100):    109.1 | actor_loss: -0.0059 | value_loss: 4.8273 | lr: 1.52e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  217 | Ep   998 | reward:    186.7 | mean(100):    106.1 | actor_loss: -0.0035 | value_loss: 4.9183 | lr: 1.51e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3093 | mean p(bad) before update=0.2417

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  218 | Ep  1005 | reward:    223.7 | mean(100):    106.6 | actor_loss: -0.0027 | value_loss: 8.1678 | lr: 1.50e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  219 | Ep  1008 | reward:    180.6 | mean(100):    105.7 | actor_loss: -0.0029 | value_loss: 3.5168 | lr: 1.49e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.1619 | mean p(bad) before update=0.6809

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  220 | Ep  1010 | reward:    205.6 | mean(100):    108.3 | actor_loss: -0.0046 | value_loss: 2.2778 | lr: 1.49e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  221 | Ep  1012 | reward:     27.5 | mean(100):    106.5 | actor_loss: -0.0059 | value_loss: 2.0484 | lr: 1.48e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  222 | Ep  1014 | reward:     98.1 | mean(100):    109.4 | actor_loss: -0.0070 | value_loss: 2.3385 | lr: 1.48e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  223 | Ep  1016 | reward:    119.9 | mean(100):    107.1 | actor_loss: -0.0076 | value_loss: 0.4052 | lr: 1.48e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  224 | Ep  1018 | reward:     92.6 | mean(100):    106.0 | actor_loss: -0.0025 | value_loss: 1.8236 | lr: 1.48e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7901 | mean p(bad) before update=0.4873

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  225 | Ep  1021 | reward:     21.2 | mean(100):    105.9 | actor_loss: -0.0038 | value_loss: 3.2931 | lr: 1.47e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  226 | Ep  1028 | reward:    224.0 | mean(100):    102.1 | actor_loss: -0.0067 | value_loss: 7.2445 | lr: 1.47e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.0872 | mean p(bad) before update=0.4225

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  227 | Ep  1033 | reward:    132.8 | mean(100):    106.6 | actor_loss: -0.0015 | value_loss: 4.7390 | lr: 1.46e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  228 | Ep  1036 | reward:    145.2 | mean(100):    105.0 | actor_loss: -0.0042 | value_loss: 2.9033 | lr: 1.45e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8497 | mean p(bad) before update=0.5166

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  229 | Ep  1042 | reward:    214.1 | mean(100):    109.7 | actor_loss: -0.0032 | value_loss: 6.3116 | lr: 1.45e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  230 | Ep  1045 | reward:    123.8 | mean(100):    111.9 | actor_loss: -0.0034 | value_loss: 3.2546 | lr: 1.44e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4058 | mean p(bad) before update=0.3016

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  231 | Ep  1051 | reward:    218.2 | mean(100):    114.8 | actor_loss: -0.0064 | value_loss: 5.5896 | lr: 1.43e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  232 | Ep  1056 | reward:    222.5 | mean(100):    119.3 | actor_loss: -0.0030 | value_loss: 5.6242 | lr: 1.42e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2840 | mean p(bad) before update=0.2436

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  233 | Ep  1060 | reward:    -58.0 | mean(100):    116.7 | actor_loss: -0.0039 | value_loss: 4.3184 | lr: 1.42e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  234 | Ep  1065 | reward:    204.7 | mean(100):    117.8 | actor_loss: -0.0039 | value_loss: 5.3516 | lr: 1.41e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5224 | mean p(bad) before update=0.3841

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  235 | Ep  1070 | reward:      2.5 | mean(100):    113.5 | actor_loss: -0.0029 | value_loss: 5.4249 | lr: 1.40e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  236 | Ep  1075 | reward:     15.1 | mean(100):    110.3 | actor_loss: -0.0048 | value_loss: 3.8168 | lr: 1.39e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4118 | mean p(bad) before update=0.2711

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  237 | Ep  1081 | reward:    -58.5 | mean(100):     99.7 | actor_loss: -0.0040 | value_loss: 5.3706 | lr: 1.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  238 | Ep  1085 | reward:    210.9 | mean(100):    103.1 | actor_loss: -0.0037 | value_loss: 4.6067 | lr: 1.38e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  239 | Ep  1088 | reward:     41.7 | mean(100):    102.9 | actor_loss: -0.0037 | value_loss: 2.9341 | lr: 1.37e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.0931 | mean p(bad) before update=0.6357
  Update  240 | Ep  1090 | reward:    132.5 | mean(100):    103.7 | actor_loss: -0.0054 | value_loss: 0.7891 | lr: 1.37e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  241 | Ep  1095 | reward:    179.9 | mean(100):    106.7 | actor_loss: -0.0007 | value_loss: 6.1450 | lr: 1.36e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2703 | mean p(bad) before update=0.2351
  Update  242 | Ep  1100 | reward:    221.6 | mean(100):    110.9 | actor_loss: -0.0043 | value_loss: 6.0810 | lr: 1.36e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  243 | Ep  1106 | reward:     -4.5 | mean(100):    110.5 | actor_loss: -0.0040 | value_loss: 6.1623 | lr: 1.35e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  244 | Ep  1108 | reward:    -17.2 | mean(100):    110.1 | actor_loss: -0.0029 | value_loss: 2.1907 | lr: 1.34e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.8016 | mean p(bad) before update=0.5317

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  245 | Ep  1111 | reward:   -104.7 | mean(100):    108.1 | actor_loss: -0.0049 | value_loss: 3.7409 | lr: 1.34e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  246 | Ep  1116 | reward:    220.0 | mean(100):    106.1 | actor_loss: -0.0022 | value_loss: 7.0586 | lr: 1.33e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5985 | mean p(bad) before update=0.3990

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  247 | Ep  1121 | reward:    161.0 | mean(100):    105.4 | actor_loss: -0.0031 | value_loss: 4.3146 | lr: 1.33e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  248 | Ep  1127 | reward:     17.0 | mean(100):    106.9 | actor_loss: -0.0030 | value_loss: 5.8027 | lr: 1.32e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  249 | Ep  1129 | reward:    141.4 | mean(100):    105.6 | actor_loss: -0.0010 | value_loss: 3.0803 | lr: 1.31e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.9309 | mean p(bad) before update=0.4187

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  250 | Ep  1132 | reward:    203.5 | mean(100):    104.6 | actor_loss: -0.0047 | value_loss: 3.2244 | lr: 1.31e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  251 | Ep  1137 | reward:    194.0 | mean(100):    108.4 | actor_loss: -0.0018 | value_loss: 4.6445 | lr: 1.30e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.4185 | mean p(bad) before update=0.3342

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  252 | Ep  1142 | reward:    206.0 | mean(100):    106.7 | actor_loss: -0.0033 | value_loss: 5.1921 | lr: 1.29e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  253 | Ep  1148 | reward:    -19.7 | mean(100):    105.9 | actor_loss: -0.0052 | value_loss: 6.6959 | lr: 1.29e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.5137 | mean p(bad) before update=0.6790

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  254 | Ep  1151 | reward:    197.9 | mean(100):    107.6 | actor_loss: -0.0027 | value_loss: 2.8496 | lr: 1.28e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  255 | Ep  1153 | reward:    244.4 | mean(100):    109.4 | actor_loss: -0.0027 | value_loss: 2.1208 | lr: 1.27e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  256 | Ep  1157 | reward:     18.6 | mean(100):    105.5 | actor_loss: -0.0032 | value_loss: 3.9636 | lr: 1.27e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  257 | Ep  1159 | reward:    216.6 | mean(100):    108.1 | actor_loss: -0.0027 | value_loss: 1.6195 | lr: 1.26e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.9187 | mean p(bad) before update=0.5576

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  258 | Ep  1162 | reward:      9.7 | mean(100):    110.9 | actor_loss: -0.0017 | value_loss: 3.1752 | lr: 1.26e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  259 | Ep  1167 | reward:    217.4 | mean(100):    115.9 | actor_loss: -0.0013 | value_loss: 5.0229 | lr: 1.26e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3638 | mean p(bad) before update=0.2786

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  260 | Ep  1170 | reward:    150.9 | mean(100):    117.7 | actor_loss: -0.0035 | value_loss: 2.5689 | lr: 1.25e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  261 | Ep  1172 | reward:    106.8 | mean(100):    117.4 | actor_loss: -0.0067 | value_loss: 1.3038 | lr: 1.24e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  262 | Ep  1177 | reward:    226.4 | mean(100):    123.8 | actor_loss: -0.0018 | value_loss: 5.6480 | lr: 1.24e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3004 | mean p(bad) before update=0.2543
  Update  263 | Ep  1182 | reward:    154.7 | mean(100):    128.5 | actor_loss: -0.0025 | value_loss: 7.6294 | lr: 1.23e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  264 | Ep  1188 | reward:    -21.3 | mean(100):    128.4 | actor_loss: -0.0027 | value_loss: 6.9499 | lr: 1.23e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5471 | mean p(bad) before update=0.3969

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  265 | Ep  1193 | reward:    -18.0 | mean(100):    127.9 | actor_loss: -0.0031 | value_loss: 5.9177 | lr: 1.22e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  266 | Ep  1197 | reward:    238.9 | mean(100):    130.9 | actor_loss: -0.0036 | value_loss: 3.9072 | lr: 1.21e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.9085 | mean p(bad) before update=0.4652

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  267 | Ep  1200 | reward:      4.4 | mean(100):    126.4 | actor_loss: -0.0024 | value_loss: 3.0810 | lr: 1.20e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  268 | Ep  1205 | reward:     42.0 | mean(100):    123.8 | actor_loss: -0.0030 | value_loss: 4.0893 | lr: 1.20e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2032 | mean p(bad) before update=0.1774

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  269 | Ep  1216 | reward:     13.2 | mean(100):    125.3 | actor_loss: -0.0037 | value_loss: 14.1019 | lr: 1.19e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.2456 | mean p(bad) before update=0.2120

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  270 | Ep  1223 | reward:    220.2 | mean(100):    116.5 | actor_loss: -0.0080 | value_loss: 10.6443 | lr: 1.18e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  271 | Ep  1226 | reward:    123.7 | mean(100):    117.0 | actor_loss: -0.0037 | value_loss: 2.5770 | lr: 1.17e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3773 | mean p(bad) before update=0.2902

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  272 | Ep  1233 | reward:     -6.3 | mean(100):    111.0 | actor_loss: -0.0030 | value_loss: 9.8040 | lr: 1.16e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  273 | Ep  1237 | reward:    -22.5 | mean(100):    105.7 | actor_loss: -0.0076 | value_loss: 3.8573 | lr: 1.15e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.6704 | mean p(bad) before update=0.4203
  Update  274 | Ep  1240 | reward:    240.6 | mean(100):    105.9 | actor_loss: -0.0040 | value_loss: 3.4555 | lr: 1.14e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  275 | Ep  1242 | reward:      5.8 | mean(100):    103.2 | actor_loss: -0.0022 | value_loss: 2.5500 | lr: 1.14e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  276 | Ep  1248 | reward:     37.4 | mean(100):     97.6 | actor_loss: -0.0042 | value_loss: 6.8711 | lr: 1.14e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=1.1961 | mean p(bad) before update=0.6836
  Update  277 | Ep  1251 | reward:    -33.7 | mean(100):     95.0 | actor_loss: -0.0028 | value_loss: 3.5643 | lr: 1.13e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  278 | Ep  1256 | reward:    246.1 | mean(100):     95.9 | actor_loss: -0.0026 | value_loss: 6.1129 | lr: 1.12e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  279 | Ep  1259 | reward:    114.6 | mean(100):     93.5 | actor_loss: -0.0051 | value_loss: 2.8191 | lr: 1.12e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3170 | mean p(bad) before update=0.2670

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  280 | Ep  1261 | reward:    -31.0 | mean(100):     90.2 | actor_loss: -0.0047 | value_loss: 2.0274 | lr: 1.11e-04
  Update  281 | Ep  1263 | reward:    123.4 | mean(100):     91.0 | actor_loss: -0.0047 | value_loss: 1.8712 | lr: 1.11e-04

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  282 | Ep  1267 | reward:    146.0 | mean(100):     88.0 | actor_loss: -0.0012 | value_loss: 3.6628 | lr: 1.11e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5622 | mean p(bad) before update=0.4167

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  283 | Ep  1272 | reward:    186.1 | mean(100):     90.9 | actor_loss: -0.0009 | value_loss: 4.4978 | lr: 1.10e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  284 | Ep  1279 | reward:    200.6 | mean(100):     86.7 | actor_loss: -0.0034 | value_loss: 9.2089 | lr: 1.09e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.5375 | mean p(bad) before update=0.3925

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  285 | Ep  1284 | reward:    -19.8 | mean(100):     83.1 | actor_loss: -0.0026 | value_loss: 4.8668 | lr: 1.08e-04
  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7717 | mean p(bad) before update=0.4755

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  286 | Ep  1293 | reward:      6.0 | mean(100):     80.4 | actor_loss: -0.0055 | value_loss: 9.5753 | lr: 1.07e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  287 | Ep  1296 | reward:    120.1 | mean(100):     80.7 | actor_loss: -0.0024 | value_loss: 3.3620 | lr: 1.06e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.3107 | mean p(bad) before update=0.2558

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  288 | Ep  1302 | reward:      1.3 | mean(100):     81.3 | actor_loss: -0.0024 | value_loss: 6.4424 | lr: 1.06e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  289 | Ep  1308 | reward:   -126.3 | mean(100):     79.4 | actor_loss: -0.0046 | value_loss: 8.1016 | lr: 1.05e-04

  [Analyzer] 2 episodes -> 4 bad pairs | unlikelihood_loss=0.7200 | mean p(bad) before update=0.4747

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  290 | Ep  1310 | reward:    137.7 | mean(100):     82.2 | actor_loss: -0.0024 | value_loss: 0.8070 | lr: 1.04e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update  291 | Ep  1315 | reward:    128.5 | mean(100):     82.8 | actor_loss: -0.0016 | value_loss: 4.5623 | lr: 1.03e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update  292 | Ep  1319 | reward:     29.1 | mean(100):     91.6 | actor_loss: -0.0022 | value_loss: 3.5102 | lr: 1.03e-04

