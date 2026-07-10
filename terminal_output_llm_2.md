Using device: cuda (rollout collection stays on CPU; batched updates use cuda)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  analyzer_threshold=200  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=unsloth/gemma-4-26B-A4B-it-GGUF
  llm_cutoff_mean=0.0 (analyzer + summary permanently stop once mean(100) first reaches this)

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2716 | mean p(bad) before update=0.2372 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2570 | mean p(bad) before update=0.2262 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    1 | Ep    20 | reward:   -258.7 | mean(100):   -175.7 | actor_loss: -0.0062 | value_loss: 63.5907 | lr: 3.00e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2802 | mean p(bad) before update=0.2443 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2686 | mean p(bad) before update=0.2355 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    2 | Ep    44 | reward:   -231.8 | mean(100):   -197.5 | actor_loss: -0.0108 | value_loss: 87.7063 | lr: 2.97e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2733 | mean p(bad) before update=0.2364 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    3 | Ep    56 | reward:    -46.1 | mean(100):   -185.6 | actor_loss: -0.0089 | value_loss: 36.6179 | lr: 2.93e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3383 | mean p(bad) before update=0.2843 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3861 | mean p(bad) before update=0.3191 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    4 | Ep    78 | reward:    -73.4 | mean(100):   -164.5 | actor_loss: -0.0077 | value_loss: 42.5379 | lr: 2.92e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3750 | mean p(bad) before update=0.3105 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1978 | mean p(bad) before update=0.1789 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4459 | mean p(bad) before update=0.3582 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    5 | Ep   100 | reward:    -96.5 | mean(100):   -148.8 | actor_loss: -0.0066 | value_loss: 35.8112 | lr: 2.88e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1969 | mean p(bad) before update=0.1776 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.3032 | mean p(bad) before update=0.2401 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    6 | Ep   121 | reward:    -92.4 | mean(100):   -126.1 | actor_loss: -0.0061 | value_loss: 29.1746 | lr: 2.85e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.3443 | mean p(bad) before update=0.2852 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2208 | mean p(bad) before update=0.1967 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    7 | Ep   141 | reward:    -76.6 | mean(100):   -100.8 | actor_loss: -0.0064 | value_loss: 24.9480 | lr: 2.82e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.3847 | mean p(bad) before update=0.3044 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2001 | mean p(bad) before update=0.1748 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   160 | reward:    -55.9 | mean(100):    -78.3 | actor_loss: -0.0106 | value_loss: 21.8260 | lr: 2.79e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2254 | mean p(bad) before update=0.1990 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    9 | Ep   178 | reward:    -63.7 | mean(100):    -68.4 | actor_loss: -0.0080 | value_loss: 20.9668 | lr: 2.76e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4093 | mean p(bad) before update=0.3100 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3828 | mean p(bad) before update=0.2906 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   10 | Ep   197 | reward:    -97.3 | mean(100):    -61.4 | actor_loss: -0.0144 | value_loss: 22.5694 | lr: 2.73e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.6459 | mean p(bad) before update=0.4257 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4989 | mean p(bad) before update=0.3452 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   214 | reward:    -23.6 | mean(100):    -53.0 | actor_loss: -0.0069 | value_loss: 20.3590 | lr: 2.70e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.4916 | mean p(bad) before update=0.3596 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   229 | reward:     36.0 | mean(100):    -47.1 | actor_loss: -0.0064 | value_loss: 20.7718 | lr: 2.68e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3948 | mean p(bad) before update=0.3066 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5658 | mean p(bad) before update=0.4047 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   242 | reward:    -25.7 | mean(100):    -40.4 | actor_loss: -0.0040 | value_loss: 20.4884 | lr: 2.66e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4077 | mean p(bad) before update=0.3101 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   254 | reward:   -108.7 | mean(100):    -38.3 | actor_loss: -0.0067 | value_loss: 21.6559 | lr: 2.64e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.6058 | mean p(bad) before update=0.4399 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   265 | reward:    -27.6 | mean(100):    -38.8 | actor_loss: -0.0057 | value_loss: 23.3595 | lr: 2.62e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 4 state-echo mismatches) | unlikelihood_loss=0.2738 | mean p(bad) before update=0.2268 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   276 | reward:    -64.3 | mean(100):    -37.5 | actor_loss: -0.0048 | value_loss: 20.0406 | lr: 2.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2802 | mean p(bad) before update=0.2340 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   282 | reward:      9.3 | mean(100):    -33.6 | actor_loss: -0.0048 | value_loss: 12.6738 | lr: 2.59e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.6136 | mean p(bad) before update=0.4507 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   18 | Ep   290 | reward:      7.1 | mean(100):    -31.7 | actor_loss: -0.0079 | value_loss: 18.5108 | lr: 2.58e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   19 | Ep   292 | reward:   -100.4 | mean(100):    -31.6 | actor_loss: -0.0068 | value_loss: 11.5035 | lr: 2.56e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   20 | Ep   299 | reward:     11.0 | mean(100):    -29.0 | actor_loss: -0.0043 | value_loss: 14.4547 | lr: 2.56e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3653 | mean p(bad) before update=0.2729 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   304 | reward:    -19.1 | mean(100):    -26.7 | actor_loss: -0.0080 | value_loss: 11.0430 | lr: 2.55e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   22 | Ep   306 | reward:     86.5 | mean(100):    -26.2 | actor_loss: -0.0049 | value_loss: 8.3554 | lr: 2.54e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   23 | Ep   308 | reward:    134.7 | mean(100):    -24.8 | actor_loss: -0.0066 | value_loss: 6.7725 | lr: 2.54e-04
  [Analyzer] 2 episodes -> 3 bad pairs (0 dropped by adv filter, 3 state-echo mismatches) | unlikelihood_loss=0.4169 | mean p(bad) before update=0.3370 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   24 | Ep   310 | reward:     64.2 | mean(100):    -25.5 | actor_loss: -0.0073 | value_loss: 10.7818 | lr: 2.54e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   25 | Ep   313 | reward:    -64.6 | mean(100):    -25.9 | actor_loss: -0.0049 | value_loss: 13.5156 | lr: 2.53e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   26 | Ep   316 | reward:     85.6 | mean(100):    -25.3 | actor_loss: -0.0046 | value_loss: 9.0917 | lr: 2.53e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   27 | Ep   319 | reward:    104.2 | mean(100):    -23.1 | actor_loss: -0.0043 | value_loss: 9.7133 | lr: 2.53e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.7690 | mean p(bad) before update=0.4263 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   28 | Ep   321 | reward:    115.8 | mean(100):    -21.6 | actor_loss: -0.0043 | value_loss: 8.8560 | lr: 2.52e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   29 | Ep   323 | reward:    108.4 | mean(100):    -19.9 | actor_loss: -0.0065 | value_loss: 7.2926 | lr: 2.52e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   30 | Ep   325 | reward:    116.9 | mean(100):    -17.3 | actor_loss: -0.0033 | value_loss: 6.4353 | lr: 2.52e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   31 | Ep   327 | reward:     57.8 | mean(100):    -15.3 | actor_loss: -0.0039 | value_loss: 6.8550 | lr: 2.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   32 | Ep   329 | reward:     81.2 | mean(100):    -14.8 | actor_loss: -0.0020 | value_loss: 7.3749 | lr: 2.51e-04

  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.6094 | mean p(bad) before update=0.3213 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   33 | Ep   331 | reward:     70.3 | mean(100):    -12.2 | actor_loss: -0.0031 | value_loss: 5.4584 | lr: 2.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   34 | Ep   333 | reward:     83.3 | mean(100):    -10.9 | actor_loss: -0.0047 | value_loss: 6.6716 | lr: 2.50e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   35 | Ep   336 | reward:    -50.6 | mean(100):    -11.3 | actor_loss: -0.0050 | value_loss: 12.5978 | lr: 2.50e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   36 | Ep   338 | reward:     57.3 | mean(100):     -9.7 | actor_loss: -0.0078 | value_loss: 5.7452 | lr: 2.50e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2025 | mean p(bad) before update=0.1756 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   37 | Ep   340 | reward:    136.7 | mean(100):     -7.7 | actor_loss: -0.0025 | value_loss: 6.6309 | lr: 2.49e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   38 | Ep   342 | reward:    117.6 | mean(100):     -5.4 | actor_loss: -0.0087 | value_loss: 4.8337 | lr: 2.49e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   39 | Ep   344 | reward:     92.2 | mean(100):     -2.5 | actor_loss: -0.0038 | value_loss: 3.9538 | lr: 2.49e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   40 | Ep   347 | reward:    -37.5 | mean(100):     -1.6 | actor_loss: -0.0031 | value_loss: 9.3642 | lr: 2.48e-04
  [LLM] mean(100)=1.8 reached cutoff 0.0 -- permanently disabling the analyzer and summary refresh for the rest of this run.
  Update   41 | Ep   349 | reward:    178.2 | mean(100):      1.8 | actor_loss: -0.0043 | value_loss: 8.5173 | lr: 2.48e-04
  Update   42 | Ep   351 | reward:     -9.4 | mean(100):      1.1 | actor_loss: -0.0055 | value_loss: 12.0985 | lr: 2.48e-04
  Update   43 | Ep   355 | reward:      9.4 | mean(100):      5.3 | actor_loss: -0.0033 | value_loss: 11.2565 | lr: 2.47e-04
  Update   44 | Ep   357 | reward:    110.0 | mean(100):      8.1 | actor_loss: -0.0064 | value_loss: 4.6249 | lr: 2.47e-04
  Update   45 | Ep   362 | reward:    112.2 | mean(100):      9.5 | actor_loss: -0.0058 | value_loss: 14.4432 | lr: 2.46e-04
  Update   46 | Ep   365 | reward:    -52.7 | mean(100):     12.6 | actor_loss: -0.0039 | value_loss: 12.1610 | lr: 2.46e-04
  Update   47 | Ep   367 | reward:    132.9 | mean(100):     15.8 | actor_loss: -0.0050 | value_loss: 4.6670 | lr: 2.45e-04
  Update   48 | Ep   371 | reward:    -51.5 | mean(100):     17.9 | actor_loss: -0.0052 | value_loss: 11.9635 | lr: 2.45e-04
  Update   49 | Ep   373 | reward:    -54.6 | mean(100):     19.1 | actor_loss: -0.0058 | value_loss: 7.6770 | lr: 2.44e-04
  Update   50 | Ep   376 | reward:    -96.4 | mean(100):     20.1 | actor_loss: -0.0053 | value_loss: 10.3507 | lr: 2.44e-04
  Update   51 | Ep   379 | reward:    -10.5 | mean(100):     20.3 | actor_loss: -0.0031 | value_loss: 9.9466 | lr: 2.44e-04
  Update   52 | Ep   382 | reward:    117.5 | mean(100):     21.1 | actor_loss: -0.0032 | value_loss: 9.1812 | lr: 2.43e-04
  Update   53 | Ep   386 | reward:     18.4 | mean(100):     24.6 | actor_loss: -0.0073 | value_loss: 11.0201 | lr: 2.43e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update   54 | Ep   389 | reward:     -8.7 | mean(100):     23.9 | actor_loss: -0.0019 | value_loss: 15.1543 | lr: 2.42e-04
  Update   55 | Ep   391 | reward:    -26.4 | mean(100):     24.7 | actor_loss: -0.0037 | value_loss: 9.4902 | lr: 2.42e-04
  Update   56 | Ep   394 | reward:      9.7 | mean(100):     28.7 | actor_loss: -0.0048 | value_loss: 10.4645 | lr: 2.41e-04
  Update   57 | Ep   396 | reward:    144.1 | mean(100):     31.8 | actor_loss: -0.0043 | value_loss: 4.6152 | lr: 2.41e-04
  Update   58 | Ep   399 | reward:    -54.3 | mean(100):     31.9 | actor_loss: -0.0047 | value_loss: 9.7183 | lr: 2.41e-04
  Update   59 | Ep   403 | reward:    -63.2 | mean(100):     32.0 | actor_loss: -0.0073 | value_loss: 10.2023 | lr: 2.40e-04
  Update   60 | Ep   405 | reward:    -51.0 | mean(100):     33.6 | actor_loss: -0.0052 | value_loss: 8.4251 | lr: 2.40e-04
  Update   61 | Ep   407 | reward:     99.8 | mean(100):     36.3 | actor_loss: -0.0023 | value_loss: 7.7187 | lr: 2.39e-04
  Update   62 | Ep   410 | reward:     18.2 | mean(100):     37.9 | actor_loss: -0.0044 | value_loss: 6.7091 | lr: 2.39e-04
  Update   63 | Ep   414 | reward:    -59.9 | mean(100):     39.2 | actor_loss: -0.0068 | value_loss: 11.6839 | lr: 2.38e-04
  Update   64 | Ep   416 | reward:    102.8 | mean(100):     40.8 | actor_loss: -0.0039 | value_loss: 3.8555 | lr: 2.38e-04
  Update   65 | Ep   418 | reward:    220.2 | mean(100):     43.8 | actor_loss: -0.0027 | value_loss: 8.2122 | lr: 2.38e-04
  Update   66 | Ep   420 | reward:    118.2 | mean(100):     45.5 | actor_loss: -0.0055 | value_loss: 5.1468 | lr: 2.37e-04
  Update   67 | Ep   423 | reward:    220.4 | mean(100):     46.8 | actor_loss: -0.0040 | value_loss: 9.9260 | lr: 2.37e-04
  Update   68 | Ep   425 | reward:    150.4 | mean(100):     47.0 | actor_loss: -0.0011 | value_loss: 4.9002 | lr: 2.37e-04
  Update   69 | Ep   429 | reward:    188.2 | mean(100):     48.5 | actor_loss: -0.0051 | value_loss: 15.9808 | lr: 2.36e-04
  Update   70 | Ep   432 | reward:    202.5 | mean(100):     49.8 | actor_loss: -0.0024 | value_loss: 10.1113 | lr: 2.36e-04
  Update   71 | Ep   435 | reward:    -12.0 | mean(100):     50.5 | actor_loss: -0.0050 | value_loss: 8.8162 | lr: 2.35e-04
  Update   72 | Ep   437 | reward:    132.4 | mean(100):     52.7 | actor_loss: -0.0051 | value_loss: 3.3635 | lr: 2.35e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update   73 | Ep   439 | reward:    120.9 | mean(100):     53.5 | actor_loss: -0.0032 | value_loss: 6.7020 | lr: 2.34e-04
  Update   74 | Ep   441 | reward:    118.1 | mean(100):     53.6 | actor_loss: -0.0037 | value_loss: 3.2912 | lr: 2.34e-04
  Update   75 | Ep   443 | reward:    115.4 | mean(100):     53.8 | actor_loss: -0.0046 | value_loss: 3.7778 | lr: 2.34e-04
  Update   76 | Ep   447 | reward:    145.1 | mean(100):     55.5 | actor_loss: -0.0071 | value_loss: 12.0514 | lr: 2.34e-04
  Update   77 | Ep   449 | reward:    100.0 | mean(100):     53.4 | actor_loss: -0.0033 | value_loss: 5.3891 | lr: 2.33e-04
  Update   78 | Ep   451 | reward:    117.6 | mean(100):     57.4 | actor_loss: -0.0021 | value_loss: 3.4231 | lr: 2.33e-04
  Update   79 | Ep   454 | reward:    146.0 | mean(100):     56.3 | actor_loss: -0.0041 | value_loss: 9.1488 | lr: 2.32e-04
  Update   80 | Ep   456 | reward:      8.8 | mean(100):     56.9 | actor_loss: -0.0008 | value_loss: 5.7237 | lr: 2.32e-04
  Update   81 | Ep   458 | reward:    259.9 | mean(100):     59.9 | actor_loss: -0.0096 | value_loss: 7.2237 | lr: 2.32e-04
  Update   82 | Ep   460 | reward:    111.4 | mean(100):     63.2 | actor_loss: -0.0044 | value_loss: 2.4754 | lr: 2.31e-04
  Update   83 | Ep   462 | reward:    140.6 | mean(100):     65.6 | actor_loss: -0.0009 | value_loss: 6.9171 | lr: 2.31e-04
  Update   84 | Ep   465 | reward:    110.8 | mean(100):     65.5 | actor_loss: -0.0040 | value_loss: 8.5904 | lr: 2.31e-04
  Update   85 | Ep   467 | reward:    118.7 | mean(100):     65.0 | actor_loss: -0.0034 | value_loss: 2.2128 | lr: 2.30e-04
  Update   86 | Ep   469 | reward:     -4.0 | mean(100):     65.6 | actor_loss: -0.0041 | value_loss: 4.5254 | lr: 2.30e-04
  Update   87 | Ep   472 | reward:      1.5 | mean(100):     65.7 | actor_loss: -0.0022 | value_loss: 7.8031 | lr: 2.30e-04
  Update   88 | Ep   475 | reward:     -6.3 | mean(100):     65.8 | actor_loss: -0.0004 | value_loss: 7.2725 | lr: 2.29e-04
  Update   89 | Ep   477 | reward:    122.6 | mean(100):     69.3 | actor_loss: -0.0030 | value_loss: 3.0152 | lr: 2.29e-04
  Update   90 | Ep   479 | reward:     91.9 | mean(100):     69.9 | actor_loss: -0.0023 | value_loss: 1.7109 | lr: 2.28e-04
  Update   91 | Ep   481 | reward:     82.8 | mean(100):     73.5 | actor_loss: -0.0041 | value_loss: 5.0923 | lr: 2.28e-04
  Update   92 | Ep   483 | reward:    123.7 | mean(100):     74.0 | actor_loss: -0.0006 | value_loss: 3.6958 | lr: 2.28e-04
  Update   93 | Ep   486 | reward:    109.4 | mean(100):     77.0 | actor_loss: -0.0014 | value_loss: 9.6431 | lr: 2.28e-04
  Update   94 | Ep   488 | reward:    103.3 | mean(100):     81.0 | actor_loss: -0.0014 | value_loss: 2.3027 | lr: 2.27e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update   95 | Ep   491 | reward:    208.4 | mean(100):     82.7 | actor_loss: -0.0041 | value_loss: 8.9338 | lr: 2.27e-04
  Update   96 | Ep   495 | reward:    182.7 | mean(100):     82.5 | actor_loss: -0.0041 | value_loss: 11.0087 | lr: 2.26e-04
  Update   97 | Ep   497 | reward:    166.7 | mean(100):     84.5 | actor_loss: -0.0019 | value_loss: 3.1939 | lr: 2.26e-04
  Update   98 | Ep   499 | reward:    -62.1 | mean(100):     84.2 | actor_loss: -0.0050 | value_loss: 5.3946 | lr: 2.25e-04
  Update   99 | Ep   501 | reward:    112.9 | mean(100):     85.6 | actor_loss: -0.0045 | value_loss: 3.2606 | lr: 2.25e-04
  Update  100 | Ep   503 | reward:     93.4 | mean(100):     88.3 | actor_loss: -0.0037 | value_loss: 2.0124 | lr: 2.25e-04
  Update  101 | Ep   506 | reward:     93.2 | mean(100):     86.5 | actor_loss: -0.0009 | value_loss: 8.6374 | lr: 2.25e-04
  Update  102 | Ep   508 | reward:    138.9 | mean(100):     87.7 | actor_loss: 0.0005 | value_loss: 2.9518 | lr: 2.24e-04
  Update  103 | Ep   510 | reward:     92.1 | mean(100):     87.3 | actor_loss: -0.0061 | value_loss: 5.2784 | lr: 2.24e-04
  Update  104 | Ep   512 | reward:    136.0 | mean(100):     89.2 | actor_loss: -0.0013 | value_loss: 2.3716 | lr: 2.23e-04
  Update  105 | Ep   514 | reward:    -33.7 | mean(100):     91.1 | actor_loss: -0.0025 | value_loss: 5.9855 | lr: 2.23e-04
  Update  106 | Ep   516 | reward:    173.6 | mean(100):     90.3 | actor_loss: -0.0038 | value_loss: 6.2241 | lr: 2.23e-04
  Update  107 | Ep   518 | reward:    139.9 | mean(100):     89.6 | actor_loss: -0.0015 | value_loss: 3.0801 | lr: 2.23e-04
  Update  108 | Ep   522 | reward:    -26.7 | mean(100):     91.3 | actor_loss: -0.0015 | value_loss: 11.9626 | lr: 2.22e-04
  Update  109 | Ep   525 | reward:    185.6 | mean(100):     90.1 | actor_loss: -0.0055 | value_loss: 9.0432 | lr: 2.22e-04
  Update  110 | Ep   527 | reward:    110.2 | mean(100):     90.2 | actor_loss: -0.0011 | value_loss: 1.6090 | lr: 2.21e-04
  Update  111 | Ep   529 | reward:    157.5 | mean(100):     90.4 | actor_loss: 0.0020 | value_loss: 5.7810 | lr: 2.21e-04
  Update  112 | Ep   532 | reward:    131.2 | mean(100):     88.7 | actor_loss: -0.0034 | value_loss: 8.8128 | lr: 2.21e-04
  Update  113 | Ep   534 | reward:    169.7 | mean(100):     90.1 | actor_loss: -0.0017 | value_loss: 3.3282 | lr: 2.20e-04
  Update  114 | Ep   536 | reward:    120.9 | mean(100):     90.0 | actor_loss: -0.0004 | value_loss: 5.1709 | lr: 2.20e-04
  Update  115 | Ep   540 | reward:      7.6 | mean(100):     89.9 | actor_loss: -0.0023 | value_loss: 11.1886 | lr: 2.20e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  116 | Ep   544 | reward:     95.9 | mean(100):     88.1 | actor_loss: -0.0050 | value_loss: 11.4170 | lr: 2.19e-04
  Update  117 | Ep   547 | reward:    206.9 | mean(100):     90.8 | actor_loss: -0.0021 | value_loss: 9.4500 | lr: 2.18e-04
  Update  118 | Ep   552 | reward:     14.2 | mean(100):     90.1 | actor_loss: -0.0037 | value_loss: 12.5232 | lr: 2.18e-04
  Update  119 | Ep   557 | reward:    -27.0 | mean(100):     88.8 | actor_loss: -0.0012 | value_loss: 14.3607 | lr: 2.17e-04
  Update  120 | Ep   560 | reward:    -10.7 | mean(100):     86.6 | actor_loss: -0.0042 | value_loss: 6.8107 | lr: 2.16e-04
  Update  121 | Ep   565 | reward:      6.8 | mean(100):     88.5 | actor_loss: -0.0022 | value_loss: 12.4591 | lr: 2.16e-04
  Update  122 | Ep   567 | reward:    120.6 | mean(100):     88.9 | actor_loss: -0.0010 | value_loss: 2.5515 | lr: 2.15e-04
  Update  123 | Ep   569 | reward:    102.0 | mean(100):     90.1 | actor_loss: -0.0020 | value_loss: 3.7687 | lr: 2.15e-04
  Update  124 | Ep   572 | reward:    118.1 | mean(100):     95.2 | actor_loss: -0.0023 | value_loss: 9.9434 | lr: 2.15e-04
  Update  125 | Ep   574 | reward:    208.2 | mean(100):     97.8 | actor_loss: -0.0020 | value_loss: 5.9186 | lr: 2.14e-04
  Update  126 | Ep   576 | reward:     95.1 | mean(100):     98.8 | actor_loss: -0.0009 | value_loss: 1.7400 | lr: 2.14e-04
  Update  127 | Ep   579 | reward:     18.4 | mean(100):     99.7 | actor_loss: -0.0009 | value_loss: 7.4691 | lr: 2.14e-04
  Update  128 | Ep   582 | reward:    -19.4 | mean(100):     96.8 | actor_loss: -0.0014 | value_loss: 7.6926 | lr: 2.13e-04
  Update  129 | Ep   585 | reward:    188.2 | mean(100):     95.1 | actor_loss: -0.0034 | value_loss: 7.0366 | lr: 2.13e-04
  Update  130 | Ep   587 | reward:    217.0 | mean(100):     96.3 | actor_loss: -0.0018 | value_loss: 5.0147 | lr: 2.12e-04
  Update  131 | Ep   589 | reward:    132.8 | mean(100):     97.0 | actor_loss: -0.0022 | value_loss: 2.2830 | lr: 2.12e-04
  Update  132 | Ep   591 | reward:    124.7 | mean(100):     97.4 | actor_loss: -0.0032 | value_loss: 5.4190 | lr: 2.12e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  133 | Ep   593 | reward:    115.1 | mean(100):     98.6 | actor_loss: -0.0018 | value_loss: 1.6890 | lr: 2.11e-04
  Update  134 | Ep   595 | reward:     40.5 | mean(100):     97.6 | actor_loss: -0.0026 | value_loss: 6.2938 | lr: 2.11e-04
  Update  135 | Ep   597 | reward:    225.5 | mean(100):     98.1 | actor_loss: -0.0025 | value_loss: 4.6481 | lr: 2.11e-04
  Update  136 | Ep   599 | reward:    159.1 | mean(100):    100.7 | actor_loss: -0.0020 | value_loss: 2.7023 | lr: 2.10e-04
  Update  137 | Ep   602 | reward:    105.5 | mean(100):     98.2 | actor_loss: -0.0031 | value_loss: 6.5347 | lr: 2.10e-04
  Update  138 | Ep   604 | reward:    235.0 | mean(100):    100.5 | actor_loss: -0.0070 | value_loss: 5.7503 | lr: 2.10e-04
  Update  139 | Ep   606 | reward:    139.8 | mean(100):    102.4 | actor_loss: -0.0062 | value_loss: 1.8960 | lr: 2.09e-04
  Update  140 | Ep   608 | reward:    129.1 | mean(100):    102.2 | actor_loss: -0.0014 | value_loss: 2.0027 | lr: 2.09e-04
  Update  141 | Ep   610 | reward:    141.3 | mean(100):    103.9 | actor_loss: -0.0020 | value_loss: 2.1880 | lr: 2.09e-04
  Update  142 | Ep   612 | reward:    114.9 | mean(100):    102.3 | actor_loss: -0.0034 | value_loss: 5.9537 | lr: 2.08e-04
  Update  143 | Ep   616 | reward:    120.2 | mean(100):    108.3 | actor_loss: -0.0021 | value_loss: 10.5207 | lr: 2.08e-04
  Update  144 | Ep   618 | reward:    -12.8 | mean(100):    106.8 | actor_loss: -0.0011 | value_loss: 5.5567 | lr: 2.08e-04
  Update  145 | Ep   623 | reward:     -3.9 | mean(100):    102.9 | actor_loss: -0.0052 | value_loss: 14.3909 | lr: 2.07e-04
  Update  146 | Ep   626 | reward:    219.4 | mean(100):    103.4 | actor_loss: -0.0008 | value_loss: 7.9383 | lr: 2.07e-04
  Update  147 | Ep   628 | reward:     85.2 | mean(100):    104.1 | actor_loss: -0.0016 | value_loss: 1.8619 | lr: 2.06e-04
  Update  148 | Ep   630 | reward:    120.6 | mean(100):    104.2 | actor_loss: -0.0020 | value_loss: 4.6506 | lr: 2.06e-04
  Update  149 | Ep   632 | reward:    120.4 | mean(100):    105.2 | actor_loss: -0.0033 | value_loss: 1.6529 | lr: 2.06e-04
  Update  150 | Ep   635 | reward:    111.9 | mean(100):    106.3 | actor_loss: -0.0021 | value_loss: 7.9947 | lr: 2.05e-04
  Update  151 | Ep   639 | reward:     14.6 | mean(100):    102.0 | actor_loss: -0.0057 | value_loss: 11.6772 | lr: 2.05e-04
  Update  152 | Ep   641 | reward:    156.0 | mean(100):    104.6 | actor_loss: -0.0008 | value_loss: 2.9993 | lr: 2.04e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  153 | Ep   643 | reward:    101.3 | mean(100):    104.6 | actor_loss: -0.0013 | value_loss: 1.5761 | lr: 2.04e-04
  Update  154 | Ep   645 | reward:    143.7 | mean(100):    105.5 | actor_loss: -0.0005 | value_loss: 4.1416 | lr: 2.04e-04
  Update  155 | Ep   647 | reward:    116.9 | mean(100):    105.5 | actor_loss: 0.0010 | value_loss: 1.4081 | lr: 2.03e-04
  Update  156 | Ep   650 | reward:     47.1 | mean(100):    105.3 | actor_loss: -0.0037 | value_loss: 5.9290 | lr: 2.03e-04
  Update  157 | Ep   652 | reward:      4.5 | mean(100):    105.7 | actor_loss: -0.0065 | value_loss: 4.5503 | lr: 2.02e-04
  Update  158 | Ep   654 | reward:    117.9 | mean(100):    106.2 | actor_loss: -0.0016 | value_loss: 1.7569 | lr: 2.02e-04
  Update  159 | Ep   656 | reward:    100.3 | mean(100):    108.7 | actor_loss: -0.0013 | value_loss: 3.6008 | lr: 2.02e-04
  Update  160 | Ep   661 | reward:    211.4 | mean(100):    106.7 | actor_loss: -0.0036 | value_loss: 13.0250 | lr: 2.02e-04
  Update  161 | Ep   663 | reward:      6.8 | mean(100):    104.7 | actor_loss: 0.0005 | value_loss: 4.2857 | lr: 2.01e-04
  Update  162 | Ep   665 | reward:    121.9 | mean(100):    106.7 | actor_loss: -0.0037 | value_loss: 1.7184 | lr: 2.01e-04
  Update  163 | Ep   667 | reward:    121.7 | mean(100):    106.0 | actor_loss: -0.0016 | value_loss: 1.8536 | lr: 2.00e-04
  Update  164 | Ep   669 | reward:    107.0 | mean(100):    104.9 | actor_loss: -0.0004 | value_loss: 4.2781 | lr: 2.00e-04
  Update  165 | Ep   671 | reward:    225.7 | mean(100):    103.6 | actor_loss: -0.0022 | value_loss: 4.4197 | lr: 2.00e-04
  Update  166 | Ep   673 | reward:    122.4 | mean(100):    103.5 | actor_loss: -0.0048 | value_loss: 1.3853 | lr: 1.99e-04
  Update  167 | Ep   675 | reward:     13.6 | mean(100):    101.4 | actor_loss: -0.0011 | value_loss: 4.0320 | lr: 1.99e-04
  Update  168 | Ep   677 | reward:    105.2 | mean(100):    101.3 | actor_loss: -0.0033 | value_loss: 1.8342 | lr: 1.99e-04
  Update  169 | Ep   681 | reward:     10.4 | mean(100):    101.5 | actor_loss: -0.0033 | value_loss: 10.2257 | lr: 1.98e-04
  Update  170 | Ep   683 | reward:    211.4 | mean(100):    103.8 | actor_loss: -0.0013 | value_loss: 5.0392 | lr: 1.98e-04
  Update  171 | Ep   686 | reward:     34.8 | mean(100):    104.3 | actor_loss: -0.0018 | value_loss: 6.7408 | lr: 1.98e-04
  Update  172 | Ep   688 | reward:    152.3 | mean(100):    103.4 | actor_loss: -0.0013 | value_loss: 2.9557 | lr: 1.97e-04
  Update  173 | Ep   692 | reward:    131.5 | mean(100):    100.6 | actor_loss: -0.0020 | value_loss: 10.4171 | lr: 1.97e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  174 | Ep   694 | reward:    120.4 | mean(100):    101.6 | actor_loss: -0.0032 | value_loss: 4.8707 | lr: 1.96e-04
  Update  175 | Ep   696 | reward:    187.3 | mean(100):    103.4 | actor_loss: -0.0021 | value_loss: 5.0667 | lr: 1.96e-04
  Update  176 | Ep   698 | reward:    115.9 | mean(100):    100.9 | actor_loss: -0.0071 | value_loss: 4.4186 | lr: 1.96e-04
  Update  177 | Ep   701 | reward:    139.4 | mean(100):    105.3 | actor_loss: -0.0025 | value_loss: 7.5585 | lr: 1.95e-04
  Update  178 | Ep   703 | reward:     88.8 | mean(100):    105.6 | actor_loss: -0.0024 | value_loss: 2.3236 | lr: 1.95e-04
  Update  179 | Ep   706 | reward:    146.7 | mean(100):    104.3 | actor_loss: -0.0049 | value_loss: 8.1079 | lr: 1.95e-04
  Update  180 | Ep   708 | reward:    119.0 | mean(100):    104.4 | actor_loss: -0.0029 | value_loss: 1.2675 | lr: 1.94e-04
  Update  181 | Ep   710 | reward:     97.0 | mean(100):    104.3 | actor_loss: -0.0040 | value_loss: 1.7240 | lr: 1.94e-04
  Update  182 | Ep   715 | reward:    181.9 | mean(100):     99.4 | actor_loss: -0.0034 | value_loss: 12.9009 | lr: 1.93e-04
  Update  183 | Ep   717 | reward:    134.8 | mean(100):     98.4 | actor_loss: -0.0029 | value_loss: 4.8011 | lr: 1.93e-04
  Update  184 | Ep   721 | reward:    189.0 | mean(100):     99.2 | actor_loss: -0.0011 | value_loss: 12.1892 | lr: 1.92e-04
  Update  185 | Ep   725 | reward:    133.4 | mean(100):    101.3 | actor_loss: -0.0036 | value_loss: 11.7384 | lr: 1.92e-04
  Update  186 | Ep   730 | reward:    -27.3 | mean(100):     98.3 | actor_loss: -0.0020 | value_loss: 12.6667 | lr: 1.91e-04
  Update  187 | Ep   732 | reward:     12.8 | mean(100):     97.6 | actor_loss: -0.0048 | value_loss: 4.1887 | lr: 1.90e-04
  Update  188 | Ep   735 | reward:    216.0 | mean(100):     97.6 | actor_loss: -0.0032 | value_loss: 7.0820 | lr: 1.90e-04
  Update  189 | Ep   737 | reward:    124.6 | mean(100):     99.5 | actor_loss: -0.0022 | value_loss: 3.2491 | lr: 1.90e-04
  Update  190 | Ep   741 | reward:     15.5 | mean(100):     97.6 | actor_loss: -0.0017 | value_loss: 9.5597 | lr: 1.89e-04
  Update  191 | Ep   743 | reward:    114.6 | mean(100):     98.1 | actor_loss: -0.0004 | value_loss: 1.9759 | lr: 1.89e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  192 | Ep   745 | reward:    157.7 | mean(100):     97.2 | actor_loss: -0.0033 | value_loss: 1.5210 | lr: 1.89e-04
  Update  193 | Ep   750 | reward:    -27.1 | mean(100):     95.4 | actor_loss: -0.0037 | value_loss: 10.5088 | lr: 1.88e-04
  Update  194 | Ep   755 | reward:    211.8 | mean(100):     96.9 | actor_loss: -0.0014 | value_loss: 13.6362 | lr: 1.87e-04
  Update  195 | Ep   759 | reward:    147.2 | mean(100):     98.5 | actor_loss: -0.0038 | value_loss: 7.5315 | lr: 1.87e-04
  Update  196 | Ep   761 | reward:     32.1 | mean(100):     97.5 | actor_loss: -0.0049 | value_loss: 4.3314 | lr: 1.86e-04
  Update  197 | Ep   766 | reward:    145.9 | mean(100):     95.2 | actor_loss: -0.0065 | value_loss: 10.7234 | lr: 1.86e-04
  Update  198 | Ep   772 | reward:     11.3 | mean(100):     91.9 | actor_loss: -0.0025 | value_loss: 16.0252 | lr: 1.85e-04
  Update  199 | Ep   777 | reward:     23.0 | mean(100):     90.2 | actor_loss: -0.0034 | value_loss: 9.4881 | lr: 1.84e-04
  Update  200 | Ep   785 | reward:     15.8 | mean(100):     80.7 | actor_loss: -0.0031 | value_loss: 20.7358 | lr: 1.83e-04
  Update  201 | Ep   791 | reward:     48.1 | mean(100):     79.0 | actor_loss: -0.0042 | value_loss: 12.7360 | lr: 1.82e-04
  Update  202 | Ep   797 | reward:      0.8 | mean(100):     71.4 | actor_loss: -0.0027 | value_loss: 15.5767 | lr: 1.81e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  203 | Ep   802 | reward:     -3.0 | mean(100):     66.6 | actor_loss: -0.0063 | value_loss: 12.1114 | lr: 1.80e-04
  Update  204 | Ep   807 | reward:     66.6 | mean(100):     62.5 | actor_loss: -0.0026 | value_loss: 11.1995 | lr: 1.80e-04
  Update  205 | Ep   812 | reward:    -22.7 | mean(100):     59.1 | actor_loss: -0.0029 | value_loss: 11.4297 | lr: 1.79e-04
  Update  206 | Ep   817 | reward:     33.6 | mean(100):     57.3 | actor_loss: -0.0083 | value_loss: 13.6134 | lr: 1.78e-04
  Update  207 | Ep   822 | reward:     25.1 | mean(100):     56.1 | actor_loss: -0.0005 | value_loss: 13.5292 | lr: 1.77e-04
  Update  208 | Ep   826 | reward:    -38.8 | mean(100):     50.4 | actor_loss: -0.0037 | value_loss: 8.5993 | lr: 1.77e-04
  Update  209 | Ep   831 | reward:    173.6 | mean(100):     49.5 | actor_loss: -0.0041 | value_loss: 12.9778 | lr: 1.76e-04
  Update  210 | Ep   839 | reward:    -22.6 | mean(100):     46.8 | actor_loss: -0.0033 | value_loss: 21.0752 | lr: 1.75e-04
  Update  211 | Ep   846 | reward:    168.3 | mean(100):     41.4 | actor_loss: -0.0024 | value_loss: 16.9867 | lr: 1.74e-04
  Update  212 | Ep   855 | reward:    196.9 | mean(100):     35.3 | actor_loss: -0.0051 | value_loss: 23.9521 | lr: 1.73e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  213 | Ep   857 | reward:     97.9 | mean(100):     35.9 | actor_loss: -0.0024 | value_loss: 4.2238 | lr: 1.72e-04
  Update  214 | Ep   862 | reward:    228.3 | mean(100):     35.4 | actor_loss: -0.0039 | value_loss: 17.2819 | lr: 1.71e-04
  Update  215 | Ep   867 | reward:    -29.8 | mean(100):     35.9 | actor_loss: -0.0031 | value_loss: 12.9549 | lr: 1.71e-04
  Update  216 | Ep   870 | reward:     45.5 | mean(100):     39.0 | actor_loss: -0.0049 | value_loss: 8.3822 | lr: 1.70e-04
  Update  217 | Ep   873 | reward:    146.1 | mean(100):     39.6 | actor_loss: -0.0052 | value_loss: 7.7938 | lr: 1.69e-04
  Update  218 | Ep   878 | reward:    -16.4 | mean(100):     38.6 | actor_loss: -0.0042 | value_loss: 9.8348 | lr: 1.69e-04
  Update  219 | Ep   880 | reward:     97.9 | mean(100):     39.7 | actor_loss: -0.0010 | value_loss: 3.5408 | lr: 1.68e-04
  Update  220 | Ep   884 | reward:    -47.4 | mean(100):     41.6 | actor_loss: -0.0025 | value_loss: 10.3241 | lr: 1.68e-04
  Update  221 | Ep   887 | reward:    134.2 | mean(100):     41.1 | actor_loss: -0.0036 | value_loss: 7.1914 | lr: 1.67e-04
  Update  222 | Ep   893 | reward:    -21.4 | mean(100):     44.7 | actor_loss: -0.0010 | value_loss: 15.1382 | lr: 1.67e-04
  Update  223 | Ep   895 | reward:    218.2 | mean(100):     47.4 | actor_loss: -0.0015 | value_loss: 5.9342 | lr: 1.66e-04
  Update  224 | Ep   899 | reward:     11.7 | mean(100):     46.2 | actor_loss: -0.0047 | value_loss: 8.9121 | lr: 1.66e-04
  Update  225 | Ep   901 | reward:      1.8 | mean(100):     46.0 | actor_loss: -0.0027 | value_loss: 4.7597 | lr: 1.65e-04
  Update  226 | Ep   907 | reward:     -1.3 | mean(100):     46.2 | actor_loss: -0.0025 | value_loss: 12.1373 | lr: 1.65e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  227 | Ep   912 | reward:    -16.9 | mean(100):     48.3 | actor_loss: -0.0032 | value_loss: 12.2647 | lr: 1.64e-04
  Update  228 | Ep   916 | reward:    212.7 | mean(100):     53.2 | actor_loss: -0.0030 | value_loss: 10.4079 | lr: 1.63e-04
  Update  229 | Ep   920 | reward:     98.0 | mean(100):     60.1 | actor_loss: -0.0015 | value_loss: 11.1076 | lr: 1.63e-04
  Update  230 | Ep   923 | reward:    235.6 | mean(100):     62.8 | actor_loss: -0.0032 | value_loss: 8.2228 | lr: 1.62e-04
  Update  231 | Ep   928 | reward:     16.7 | mean(100):     67.2 | actor_loss: -0.0039 | value_loss: 10.8260 | lr: 1.62e-04
  Update  232 | Ep   932 | reward:     37.5 | mean(100):     70.0 | actor_loss: -0.0019 | value_loss: 8.9078 | lr: 1.61e-04
  Update  233 | Ep   936 | reward:    -14.3 | mean(100):     72.4 | actor_loss: -0.0039 | value_loss: 10.5652 | lr: 1.60e-04
  Update  234 | Ep   938 | reward:    120.0 | mean(100):     73.8 | actor_loss: -0.0024 | value_loss: 4.2774 | lr: 1.60e-04
  Update  235 | Ep   940 | reward:    112.8 | mean(100):     76.5 | actor_loss: -0.0020 | value_loss: 3.3019 | lr: 1.59e-04
  Update  236 | Ep   942 | reward:     11.2 | mean(100):     78.4 | actor_loss: -0.0042 | value_loss: 5.0617 | lr: 1.59e-04
  Update  237 | Ep   944 | reward:    215.2 | mean(100):     81.0 | actor_loss: -0.0014 | value_loss: 5.3884 | lr: 1.59e-04
  Update  238 | Ep   946 | reward:     33.5 | mean(100):     80.7 | actor_loss: -0.0053 | value_loss: 3.6419 | lr: 1.58e-04
  Update  239 | Ep   948 | reward:    156.3 | mean(100):     83.5 | actor_loss: -0.0065 | value_loss: 4.0500 | lr: 1.58e-04
  Update  240 | Ep   954 | reward:     10.6 | mean(100):     83.0 | actor_loss: -0.0051 | value_loss: 14.1086 | lr: 1.58e-04
  Update  241 | Ep   956 | reward:    -29.2 | mean(100):     81.4 | actor_loss: -0.0038 | value_loss: 4.8686 | lr: 1.57e-04
  Update  242 | Ep   961 | reward:    243.7 | mean(100):     85.3 | actor_loss: -0.0032 | value_loss: 11.9554 | lr: 1.57e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  243 | Ep   965 | reward:    223.3 | mean(100):     86.3 | actor_loss: -0.0039 | value_loss: 12.8993 | lr: 1.56e-04
  Update  244 | Ep   969 | reward:      8.6 | mean(100):     85.4 | actor_loss: -0.0053 | value_loss: 8.5904 | lr: 1.55e-04
  Update  245 | Ep   974 | reward:     48.9 | mean(100):     86.4 | actor_loss: -0.0043 | value_loss: 13.8121 | lr: 1.55e-04
  Update  246 | Ep   977 | reward:    120.7 | mean(100):     90.6 | actor_loss: -0.0007 | value_loss: 7.6452 | lr: 1.54e-04
  Update  247 | Ep   983 | reward:     12.4 | mean(100):     89.9 | actor_loss: -0.0035 | value_loss: 12.0820 | lr: 1.53e-04
  Update  248 | Ep   985 | reward:     94.1 | mean(100):     92.8 | actor_loss: -0.0042 | value_loss: 2.2282 | lr: 1.53e-04
  Update  249 | Ep   987 | reward:     -1.3 | mean(100):     93.4 | actor_loss: -0.0027 | value_loss: 4.6222 | lr: 1.52e-04
  Update  250 | Ep   991 | reward:     -4.7 | mean(100):     93.8 | actor_loss: -0.0071 | value_loss: 8.3249 | lr: 1.52e-04
  Update  251 | Ep   993 | reward:    147.9 | mean(100):     95.8 | actor_loss: -0.0047 | value_loss: 2.6842 | lr: 1.51e-04
  Update  252 | Ep   998 | reward:     16.3 | mean(100):     94.4 | actor_loss: -0.0030 | value_loss: 11.8164 | lr: 1.51e-04
  Update  253 | Ep  1000 | reward:    111.1 | mean(100):     95.0 | actor_loss: -0.0040 | value_loss: 4.9018 | lr: 1.50e-04
  Update  254 | Ep  1004 | reward:     66.7 | mean(100):     98.3 | actor_loss: -0.0027 | value_loss: 8.8272 | lr: 1.50e-04
  Update  255 | Ep  1012 | reward:     13.5 | mean(100):     95.1 | actor_loss: -0.0035 | value_loss: 23.0090 | lr: 1.49e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  256 | Ep  1016 | reward:     22.9 | mean(100):     93.6 | actor_loss: -0.0024 | value_loss: 7.9762 | lr: 1.48e-04
  Update  257 | Ep  1018 | reward:     -9.5 | mean(100):     90.0 | actor_loss: -0.0042 | value_loss: 4.4903 | lr: 1.48e-04
  Update  258 | Ep  1020 | reward:      1.9 | mean(100):     87.9 | actor_loss: -0.0052 | value_loss: 3.8842 | lr: 1.47e-04
  Update  259 | Ep  1022 | reward:    108.8 | mean(100):     87.7 | actor_loss: -0.0065 | value_loss: 4.4808 | lr: 1.47e-04
  Update  260 | Ep  1027 | reward:    210.6 | mean(100):     87.7 | actor_loss: -0.0022 | value_loss: 10.9765 | lr: 1.47e-04
  Update  261 | Ep  1032 | reward:    200.6 | mean(100):     88.7 | actor_loss: -0.0009 | value_loss: 10.8235 | lr: 1.46e-04
  Update  262 | Ep  1034 | reward:     41.0 | mean(100):     85.1 | actor_loss: -0.0015 | value_loss: 3.2246 | lr: 1.45e-04
  Update  263 | Ep  1036 | reward:    132.3 | mean(100):     86.2 | actor_loss: -0.0046 | value_loss: 3.7809 | lr: 1.45e-04
  Update  264 | Ep  1041 | reward:     35.8 | mean(100):     84.6 | actor_loss: -0.0009 | value_loss: 10.6349 | lr: 1.45e-04
  Update  265 | Ep  1047 | reward:    232.4 | mean(100):     84.0 | actor_loss: -0.0034 | value_loss: 12.7173 | lr: 1.44e-04
  Update  266 | Ep  1052 | reward:     24.6 | mean(100):     83.7 | actor_loss: -0.0044 | value_loss: 10.7968 | lr: 1.43e-04
  Update  267 | Ep  1057 | reward:     25.5 | mean(100):     87.5 | actor_loss: -0.0011 | value_loss: 10.9335 | lr: 1.42e-04
  Update  268 | Ep  1060 | reward:    -13.5 | mean(100):     87.8 | actor_loss: -0.0052 | value_loss: 6.3886 | lr: 1.41e-04
  Update  269 | Ep  1062 | reward:    105.6 | mean(100):     88.3 | actor_loss: -0.0021 | value_loss: 3.1304 | lr: 1.41e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  270 | Ep  1071 | reward:     84.2 | mean(100):     77.4 | actor_loss: -0.0042 | value_loss: 19.5337 | lr: 1.41e-04
  Update  271 | Ep  1073 | reward:    122.6 | mean(100):     79.7 | actor_loss: -0.0049 | value_loss: 2.0588 | lr: 1.39e-04
  Update  272 | Ep  1075 | reward:    139.1 | mean(100):     78.4 | actor_loss: -0.0019 | value_loss: 3.8716 | lr: 1.39e-04
  Update  273 | Ep  1077 | reward:    150.5 | mean(100):     77.7 | actor_loss: -0.0017 | value_loss: 2.1200 | lr: 1.39e-04
  Update  274 | Ep  1083 | reward:     16.2 | mean(100):     76.3 | actor_loss: -0.0056 | value_loss: 12.0944 | lr: 1.38e-04
  Update  275 | Ep  1087 | reward:      6.0 | mean(100):     74.1 | actor_loss: -0.0048 | value_loss: 7.0968 | lr: 1.38e-04
  Update  276 | Ep  1093 | reward:     54.7 | mean(100):     69.5 | actor_loss: -0.0047 | value_loss: 13.0574 | lr: 1.37e-04
  Update  277 | Ep  1095 | reward:    106.5 | mean(100):     69.8 | actor_loss: -0.0032 | value_loss: 1.5588 | lr: 1.36e-04
  Update  278 | Ep  1099 | reward:     57.6 | mean(100):     70.5 | actor_loss: -0.0033 | value_loss: 6.7922 | lr: 1.36e-04
  Update  279 | Ep  1102 | reward:     28.5 | mean(100):     73.2 | actor_loss: -0.0018 | value_loss: 7.2768 | lr: 1.35e-04
  Update  280 | Ep  1107 | reward:    -51.3 | mean(100):     73.4 | actor_loss: -0.0034 | value_loss: 13.6592 | lr: 1.35e-04
  Update  281 | Ep  1110 | reward:    128.0 | mean(100):     74.6 | actor_loss: -0.0051 | value_loss: 6.1040 | lr: 1.34e-04
  Update  282 | Ep  1114 | reward:    -31.7 | mean(100):     69.5 | actor_loss: -0.0066 | value_loss: 8.9177 | lr: 1.33e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  283 | Ep  1116 | reward:     39.3 | mean(100):     70.3 | actor_loss: -0.0041 | value_loss: 3.6710 | lr: 1.33e-04
  Update  284 | Ep  1121 | reward:     19.5 | mean(100):     72.7 | actor_loss: -0.0038 | value_loss: 12.5067 | lr: 1.33e-04
  Update  285 | Ep  1127 | reward:    -25.3 | mean(100):     66.2 | actor_loss: -0.0038 | value_loss: 14.6629 | lr: 1.32e-04
  Update  286 | Ep  1130 | reward:    -14.4 | mean(100):     64.2 | actor_loss: -0.0047 | value_loss: 5.4109 | lr: 1.31e-04
  Update  287 | Ep  1135 | reward:    -10.7 | mean(100):     64.7 | actor_loss: -0.0034 | value_loss: 10.3743 | lr: 1.31e-04
  Update  288 | Ep  1141 | reward:     52.4 | mean(100):     65.3 | actor_loss: -0.0034 | value_loss: 11.6434 | lr: 1.30e-04
  Update  289 | Ep  1144 | reward:    265.0 | mean(100):     67.7 | actor_loss: -0.0040 | value_loss: 7.3106 | lr: 1.29e-04
  Update  290 | Ep  1147 | reward:    196.2 | mean(100):     67.9 | actor_loss: -0.0043 | value_loss: 6.1012 | lr: 1.28e-04
  Update  291 | Ep  1151 | reward:    236.8 | mean(100):     69.4 | actor_loss: -0.0032 | value_loss: 8.6551 | lr: 1.28e-04
  Update  292 | Ep  1153 | reward:    144.1 | mean(100):     70.4 | actor_loss: -0.0050 | value_loss: 2.6067 | lr: 1.27e-04
  Update  293 | Ep  1155 | reward:    242.2 | mean(100):     71.0 | actor_loss: -0.0034 | value_loss: 5.3539 | lr: 1.27e-04
  Update  294 | Ep  1158 | reward:    -13.0 | mean(100):     68.7 | actor_loss: -0.0043 | value_loss: 6.8120 | lr: 1.27e-04
  Update  295 | Ep  1161 | reward:    131.2 | mean(100):     68.3 | actor_loss: -0.0041 | value_loss: 6.9022 | lr: 1.26e-04
  Update  296 | Ep  1163 | reward:     31.8 | mean(100):     68.7 | actor_loss: -0.0012 | value_loss: 4.1859 | lr: 1.26e-04
  Update  297 | Ep  1168 | reward:    129.9 | mean(100):     71.8 | actor_loss: -0.0030 | value_loss: 10.1951 | lr: 1.26e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  298 | Ep  1172 | reward:    225.2 | mean(100):     76.3 | actor_loss: -0.0037 | value_loss: 9.7743 | lr: 1.25e-04
  Update  299 | Ep  1174 | reward:     90.9 | mean(100):     77.6 | actor_loss: -0.0019 | value_loss: 2.1166 | lr: 1.24e-04
  Update  300 | Ep  1176 | reward:    135.3 | mean(100):     76.7 | actor_loss: -0.0036 | value_loss: 2.5185 | lr: 1.24e-04
  Update  301 | Ep  1181 | reward:     -7.5 | mean(100):     77.4 | actor_loss: -0.0020 | value_loss: 12.8918 | lr: 1.24e-04
  Update  302 | Ep  1186 | reward:     40.0 | mean(100):     77.2 | actor_loss: -0.0032 | value_loss: 10.6510 | lr: 1.23e-04
  Update  303 | Ep  1188 | reward:     95.5 | mean(100):     80.0 | actor_loss: -0.0053 | value_loss: 4.6087 | lr: 1.22e-04
  Update  304 | Ep  1192 | reward:     52.5 | mean(100):     83.1 | actor_loss: -0.0005 | value_loss: 6.7197 | lr: 1.22e-04
  Update  305 | Ep  1195 | reward:     25.4 | mean(100):     81.7 | actor_loss: -0.0055 | value_loss: 6.8977 | lr: 1.21e-04
  Update  306 | Ep  1199 | reward:     12.9 | mean(100):     81.4 | actor_loss: -0.0014 | value_loss: 6.7261 | lr: 1.21e-04
  Update  307 | Ep  1201 | reward:    157.2 | mean(100):     80.5 | actor_loss: -0.0035 | value_loss: 1.7723 | lr: 1.20e-04
  Update  308 | Ep  1206 | reward:    229.4 | mean(100):     80.1 | actor_loss: -0.0040 | value_loss: 12.1989 | lr: 1.20e-04
  Update  309 | Ep  1211 | reward:    199.0 | mean(100):     82.7 | actor_loss: -0.0029 | value_loss: 12.6227 | lr: 1.19e-04
  Update  310 | Ep  1213 | reward:    178.4 | mean(100):     84.4 | actor_loss: -0.0025 | value_loss: 2.0390 | lr: 1.18e-04
  Update  311 | Ep  1216 | reward:    137.0 | mean(100):     86.9 | actor_loss: -0.0039 | value_loss: 6.3768 | lr: 1.18e-04
  Update  312 | Ep  1220 | reward:     28.1 | mean(100):     84.0 | actor_loss: -0.0054 | value_loss: 6.9853 | lr: 1.18e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  313 | Ep  1222 | reward:    115.1 | mean(100):     85.8 | actor_loss: -0.0031 | value_loss: 1.7183 | lr: 1.17e-04
  Update  314 | Ep  1226 | reward:     10.8 | mean(100):     87.8 | actor_loss: -0.0061 | value_loss: 6.8790 | lr: 1.17e-04
  Update  315 | Ep  1228 | reward:    150.2 | mean(100):     89.2 | actor_loss: -0.0035 | value_loss: 1.1874 | lr: 1.16e-04
  Update  316 | Ep  1232 | reward:    135.6 | mean(100):     92.4 | actor_loss: -0.0023 | value_loss: 8.4870 | lr: 1.16e-04
  Update  317 | Ep  1234 | reward:    128.0 | mean(100):     90.5 | actor_loss: -0.0027 | value_loss: 2.6031 | lr: 1.15e-04
  Update  318 | Ep  1239 | reward:     50.6 | mean(100):     89.9 | actor_loss: -0.0028 | value_loss: 9.6555 | lr: 1.15e-04
  Update  319 | Ep  1241 | reward:    103.4 | mean(100):     90.2 | actor_loss: -0.0028 | value_loss: 3.0359 | lr: 1.14e-04
  Update  320 | Ep  1246 | reward:    112.8 | mean(100):     89.2 | actor_loss: -0.0010 | value_loss: 9.3139 | lr: 1.14e-04
  Update  321 | Ep  1253 | reward:    140.7 | mean(100):     83.4 | actor_loss: -0.0042 | value_loss: 14.2990 | lr: 1.13e-04
  Update  322 | Ep  1256 | reward:     29.9 | mean(100):     82.3 | actor_loss: -0.0022 | value_loss: 7.8601 | lr: 1.12e-04
  Update  323 | Ep  1258 | reward:    128.0 | mean(100):     86.6 | actor_loss: -0.0010 | value_loss: 5.0623 | lr: 1.12e-04
  Update  324 | Ep  1260 | reward:    134.8 | mean(100):     89.1 | actor_loss: -0.0037 | value_loss: 1.3691 | lr: 1.11e-04
  Update  325 | Ep  1262 | reward:    141.4 | mean(100):     89.4 | actor_loss: -0.0040 | value_loss: 2.4120 | lr: 1.11e-04
  Update  326 | Ep  1264 | reward:    140.1 | mean(100):     92.6 | actor_loss: -0.0010 | value_loss: 4.1289 | lr: 1.11e-04
  Update  327 | Ep  1266 | reward:     54.8 | mean(100):     92.0 | actor_loss: -0.0008 | value_loss: 4.3971 | lr: 1.10e-04
  Update  328 | Ep  1268 | reward:    158.3 | mean(100):     94.3 | actor_loss: -0.0018 | value_loss: 4.0785 | lr: 1.10e-04
  Update  329 | Ep  1270 | reward:    156.2 | mean(100):     95.3 | actor_loss: -0.0036 | value_loss: 1.8626 | lr: 1.10e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  330 | Ep  1272 | reward:    132.4 | mean(100):     93.4 | actor_loss: -0.0039 | value_loss: 2.2181 | lr: 1.09e-04
  Update  331 | Ep  1274 | reward:    118.5 | mean(100):     93.6 | actor_loss: -0.0018 | value_loss: 1.8369 | lr: 1.09e-04
  Update  332 | Ep  1276 | reward:    121.9 | mean(100):     94.2 | actor_loss: -0.0011 | value_loss: 1.6037 | lr: 1.09e-04
  Update  333 | Ep  1279 | reward:     24.7 | mean(100):     94.3 | actor_loss: -0.0028 | value_loss: 6.5911 | lr: 1.09e-04
  Update  334 | Ep  1282 | reward:     53.1 | mean(100):     95.7 | actor_loss: -0.0026 | value_loss: 5.2518 | lr: 1.08e-04
  Update  335 | Ep  1285 | reward:     62.6 | mean(100):     99.0 | actor_loss: -0.0035 | value_loss: 7.9138 | lr: 1.08e-04
  Update  336 | Ep  1287 | reward:    135.9 | mean(100):    101.0 | actor_loss: -0.0011 | value_loss: 5.4612 | lr: 1.07e-04
  Update  337 | Ep  1290 | reward:    148.5 | mean(100):     99.1 | actor_loss: -0.0021 | value_loss: 6.2700 | lr: 1.07e-04
  Update  338 | Ep  1292 | reward:     34.0 | mean(100):     98.9 | actor_loss: -0.0032 | value_loss: 4.0011 | lr: 1.06e-04
  Update  339 | Ep  1294 | reward:    124.4 | mean(100):     99.2 | actor_loss: -0.0002 | value_loss: 3.1853 | lr: 1.06e-04
  Update  340 | Ep  1297 | reward:    283.0 | mean(100):    101.3 | actor_loss: -0.0037 | value_loss: 6.8276 | lr: 1.06e-04
  Update  341 | Ep  1300 | reward:    144.8 | mean(100):    102.0 | actor_loss: -0.0024 | value_loss: 4.7798 | lr: 1.05e-04
  Update  342 | Ep  1302 | reward:     14.8 | mean(100):    101.8 | actor_loss: -0.0013 | value_loss: 3.7667 | lr: 1.05e-04
  Update  343 | Ep  1304 | reward:    115.7 | mean(100):    101.8 | actor_loss: -0.0030 | value_loss: 3.3282 | lr: 1.05e-04
  Update  344 | Ep  1310 | reward:     54.8 | mean(100):    102.3 | actor_loss: -0.0031 | value_loss: 10.6492 | lr: 1.04e-04
  Update  345 | Ep  1316 | reward:     21.3 | mean(100):     98.1 | actor_loss: -0.0048 | value_loss: 11.6356 | lr: 1.03e-04
  Update  346 | Ep  1323 | reward:      7.2 | mean(100):     96.8 | actor_loss: -0.0053 | value_loss: 12.7664 | lr: 1.03e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  347 | Ep  1325 | reward:    140.9 | mean(100):     97.4 | actor_loss: -0.0041 | value_loss: 2.1801 | lr: 1.02e-04
  Update  348 | Ep  1331 | reward:     55.1 | mean(100):     95.1 | actor_loss: -0.0036 | value_loss: 11.0341 | lr: 1.01e-04
  Update  349 | Ep  1333 | reward:     34.0 | mean(100):     95.0 | actor_loss: -0.0022 | value_loss: 3.6460 | lr: 1.00e-04
  Update  350 | Ep  1337 | reward:      1.2 | mean(100):     92.8 | actor_loss: -0.0028 | value_loss: 6.3564 | lr: 1.00e-04
  Update  351 | Ep  1339 | reward:     37.7 | mean(100):     94.1 | actor_loss: -0.0010 | value_loss: 3.2277 | lr: 9.94e-05
  Update  352 | Ep  1341 | reward:    154.8 | mean(100):     95.7 | actor_loss: -0.0011 | value_loss: 2.3133 | lr: 9.91e-05
  Update  353 | Ep  1343 | reward:    145.6 | mean(100):     97.9 | actor_loss: -0.0009 | value_loss: 1.7470 | lr: 9.88e-05
  Update  354 | Ep  1347 | reward:     45.8 | mean(100):     96.9 | actor_loss: -0.0034 | value_loss: 8.2801 | lr: 9.85e-05
  Update  355 | Ep  1349 | reward:    143.6 | mean(100):     97.7 | actor_loss: -0.0012 | value_loss: 4.4498 | lr: 9.79e-05
  Update  356 | Ep  1351 | reward:    145.0 | mean(100):    100.5 | actor_loss: -0.0034 | value_loss: 3.0071 | lr: 9.76e-05
  Update  357 | Ep  1354 | reward:      8.3 | mean(100):     98.1 | actor_loss: -0.0036 | value_loss: 6.2865 | lr: 9.73e-05
  Update  358 | Ep  1356 | reward:    152.3 | mean(100):     99.2 | actor_loss: -0.0012 | value_loss: 1.9278 | lr: 9.69e-05
  Update  359 | Ep  1358 | reward:    122.2 | mean(100):     98.2 | actor_loss: -0.0007 | value_loss: 1.4999 | lr: 9.66e-05
  Update  360 | Ep  1360 | reward:    175.9 | mean(100):     97.6 | actor_loss: -0.0050 | value_loss: 3.9628 | lr: 9.63e-05
  Update  361 | Ep  1362 | reward:    175.6 | mean(100):     97.8 | actor_loss: -0.0044 | value_loss: 2.3768 | lr: 9.60e-05
  Update  362 | Ep  1366 | reward:     94.2 | mean(100):     97.4 | actor_loss: -0.0026 | value_loss: 8.9180 | lr: 9.57e-05
  Update  363 | Ep  1369 | reward:    210.7 | mean(100):     97.6 | actor_loss: -0.0022 | value_loss: 6.6093 | lr: 9.51e-05
  Update  364 | Ep  1371 | reward:    157.3 | mean(100):     97.3 | actor_loss: -0.0002 | value_loss: 1.9185 | lr: 9.46e-05
  Update  365 | Ep  1373 | reward:    169.5 | mean(100):     97.7 | actor_loss: -0.0025 | value_loss: 2.8819 | lr: 9.43e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  366 | Ep  1375 | reward:     11.9 | mean(100):     96.9 | actor_loss: -0.0034 | value_loss: 3.5042 | lr: 9.40e-05
  Update  367 | Ep  1377 | reward:    149.4 | mean(100):     95.9 | actor_loss: -0.0023 | value_loss: 1.6868 | lr: 9.37e-05
  Update  368 | Ep  1382 | reward:    210.1 | mean(100):     96.4 | actor_loss: -0.0037 | value_loss: 11.7962 | lr: 9.34e-05
  Update  369 | Ep  1384 | reward:    141.3 | mean(100):     95.2 | actor_loss: -0.0034 | value_loss: 1.7053 | lr: 9.27e-05
  Update  370 | Ep  1386 | reward:    125.0 | mean(100):     94.7 | actor_loss: -0.0049 | value_loss: 1.7910 | lr: 9.24e-05
  Update  371 | Ep  1388 | reward:    158.0 | mean(100):     96.2 | actor_loss: -0.0010 | value_loss: 1.2208 | lr: 9.21e-05
  Update  372 | Ep  1392 | reward:    189.4 | mean(100):    100.2 | actor_loss: -0.0015 | value_loss: 9.4002 | lr: 9.18e-05
  Update  373 | Ep  1394 | reward:    163.1 | mean(100):    101.8 | actor_loss: -0.0037 | value_loss: 1.8592 | lr: 9.12e-05
  Update  374 | Ep  1396 | reward:     40.3 | mean(100):    101.9 | actor_loss: -0.0048 | value_loss: 3.0599 | lr: 9.09e-05
  Update  375 | Ep  1398 | reward:    242.0 | mean(100):    102.2 | actor_loss: -0.0016 | value_loss: 3.2091 | lr: 9.06e-05
  Update  376 | Ep  1400 | reward:    252.4 | mean(100):    104.3 | actor_loss: 0.0002 | value_loss: 3.1866 | lr: 9.03e-05
  Update  377 | Ep  1402 | reward:    111.8 | mean(100):    105.7 | actor_loss: -0.0019 | value_loss: 1.4466 | lr: 9.00e-05
  Update  378 | Ep  1404 | reward:    160.9 | mean(100):    107.4 | actor_loss: -0.0020 | value_loss: 1.9096 | lr: 8.97e-05
  Update  379 | Ep  1406 | reward:    118.6 | mean(100):    109.1 | actor_loss: -0.0030 | value_loss: 1.1189 | lr: 8.94e-05
  Update  380 | Ep  1409 | reward:    144.3 | mean(100):    112.7 | actor_loss: -0.0024 | value_loss: 6.2369 | lr: 8.91e-05
  Update  381 | Ep  1411 | reward:    163.0 | mean(100):    115.0 | actor_loss: -0.0031 | value_loss: 1.2345 | lr: 8.86e-05
  Update  382 | Ep  1415 | reward:    -35.8 | mean(100):    115.2 | actor_loss: -0.0025 | value_loss: 9.5802 | lr: 8.83e-05
  Update  383 | Ep  1417 | reward:    162.6 | mean(100):    116.5 | actor_loss: -0.0026 | value_loss: 1.3641 | lr: 8.77e-05
  Update  384 | Ep  1419 | reward:    157.4 | mean(100):    118.9 | actor_loss: -0.0021 | value_loss: 1.1388 | lr: 8.74e-05
  Update  385 | Ep  1421 | reward:    177.3 | mean(100):    121.1 | actor_loss: -0.0041 | value_loss: 1.6268 | lr: 8.71e-05
  Update  386 | Ep  1423 | reward:    185.4 | mean(100):    124.2 | actor_loss: -0.0046 | value_loss: 2.3575 | lr: 8.68e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  387 | Ep  1425 | reward:    136.9 | mean(100):    124.5 | actor_loss: -0.0025 | value_loss: 1.0147 | lr: 8.65e-05
  Update  388 | Ep  1427 | reward:    241.1 | mean(100):    127.8 | actor_loss: -0.0064 | value_loss: 4.6467 | lr: 8.62e-05
  Update  389 | Ep  1429 | reward:    134.5 | mean(100):    131.4 | actor_loss: -0.0029 | value_loss: 3.6032 | lr: 8.59e-05
  Update  390 | Ep  1432 | reward:     22.1 | mean(100):    132.2 | actor_loss: -0.0016 | value_loss: 6.9290 | lr: 8.56e-05
  Update  391 | Ep  1434 | reward:    276.7 | mean(100):    135.7 | actor_loss: -0.0033 | value_loss: 3.7159 | lr: 8.52e-05
  Update  392 | Ep  1437 | reward:    275.6 | mean(100):    140.3 | actor_loss: -0.0022 | value_loss: 5.8780 | lr: 8.49e-05
  Update  393 | Ep  1439 | reward:    124.4 | mean(100):    141.2 | actor_loss: -0.0048 | value_loss: 0.8735 | lr: 8.44e-05
  Update  394 | Ep  1441 | reward:    144.8 | mean(100):    142.4 | actor_loss: -0.0031 | value_loss: 3.4047 | lr: 8.41e-05
  Update  395 | Ep  1443 | reward:    137.4 | mean(100):    142.4 | actor_loss: -0.0035 | value_loss: 0.9870 | lr: 8.38e-05
  Update  396 | Ep  1446 | reward:    144.8 | mean(100):    147.2 | actor_loss: -0.0028 | value_loss: 6.1267 | lr: 8.35e-05
  Update  397 | Ep  1448 | reward:    158.8 | mean(100):    149.9 | actor_loss: -0.0005 | value_loss: 1.0479 | lr: 8.31e-05
  Update  398 | Ep  1450 | reward:    156.4 | mean(100):    150.1 | actor_loss: -0.0012 | value_loss: 1.3105 | lr: 8.28e-05
  Update  399 | Ep  1454 | reward:    247.1 | mean(100):    153.5 | actor_loss: -0.0028 | value_loss: 8.6436 | lr: 8.25e-05
  Update  400 | Ep  1457 | reward:     15.7 | mean(100):    153.2 | actor_loss: -0.0012 | value_loss: 6.0038 | lr: 8.19e-05
  Update  401 | Ep  1459 | reward:    144.8 | mean(100):    154.9 | actor_loss: -0.0013 | value_loss: 1.3782 | lr: 8.14e-05
  Update  402 | Ep  1461 | reward:    280.8 | mean(100):    156.1 | actor_loss: -0.0035 | value_loss: 4.1202 | lr: 8.11e-05
  Update  403 | Ep  1463 | reward:     37.6 | mean(100):    157.4 | actor_loss: -0.0056 | value_loss: 5.7929 | lr: 8.08e-05
  Update  404 | Ep  1465 | reward:    250.2 | mean(100):    157.3 | actor_loss: -0.0004 | value_loss: 3.4260 | lr: 8.05e-05
  Update  405 | Ep  1468 | reward:    150.5 | mean(100):    159.6 | actor_loss: -0.0020 | value_loss: 6.6404 | lr: 8.02e-05
  Update  406 | Ep  1470 | reward:    170.5 | mean(100):    160.8 | actor_loss: -0.0028 | value_loss: 3.7224 | lr: 7.98e-05
  Update  407 | Ep  1474 | reward:    242.8 | mean(100):    164.4 | actor_loss: -0.0019 | value_loss: 10.6415 | lr: 7.95e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
  Update  408 | Ep  1477 | reward:     42.9 | mean(100):    166.1 | actor_loss: -0.0047 | value_loss: 7.4780 | lr: 7.89e-05
  Update  409 | Ep  1481 | reward:    219.0 | mean(100):    173.7 | actor_loss: -0.0005 | value_loss: 9.4053 | lr: 7.84e-05
  Update  410 | Ep  1485 | reward:    278.5 | mean(100):    176.5 | actor_loss: -0.0033 | value_loss: 8.8716 | lr: 7.78e-05
  Update  411 | Ep  1488 | reward:    135.4 | mean(100):    178.7 | actor_loss: -0.0034 | value_loss: 6.2247 | lr: 7.72e-05
  Update  412 | Ep  1491 | reward:    270.0 | mean(100):    180.8 | actor_loss: -0.0011 | value_loss: 6.9136 | lr: 7.68e-05
  Update  413 | Ep  1498 | reward:    263.5 | mean(100):    189.9 | actor_loss: -0.0024 | value_loss: 20.6991 | lr: 7.63e-05
  Update  414 | Ep  1505 | reward:    276.4 | mean(100):    192.4 | actor_loss: -0.0009 | value_loss: 20.3821 | lr: 7.53e-05
  Update  415 | Ep  1510 | reward:    296.7 | mean(100):    191.4 | actor_loss: -0.0014 | value_loss: 15.1156 | lr: 7.43e-05
  Update  416 | Ep  1515 | reward:    286.1 | mean(100):    193.5 | actor_loss: -0.0031 | value_loss: 12.3976 | lr: 7.35e-05
  Update  417 | Ep  1522 | reward:    248.5 | mean(100):    200.8 | actor_loss: -0.0033 | value_loss: 17.9845 | lr: 7.28e-05

Solved at episode 1522 (update 417) with mean 200.8!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_2.png
