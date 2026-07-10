Using device: cuda (rollout collection stays on CPU; batched updates use cuda)
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=10  analyzer_n_traj=2  analyzer_topk=2  analyzer_threshold=200  unlikelihood_lr=0.0001
  summary_n_traj=2 (AI agent updates summary every PPO update using the last N episodes)  llm_model=unsloth/gemma-4-26B-A4B-it-GGUF
  llm_cutoff_mean=0.0 (analyzer + summary permanently stop once mean(100) first reaches this)

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2529 | mean p(bad) before update=0.2233 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2517 | mean p(bad) before update=0.2213 | ul_lr=1.00e-04 (scale=1.00)
  Update    1 | Ep    21 | reward:   -287.3 | mean(100):   -211.1 | actor_loss: -0.0075 | value_loss: 75.0204 | lr: 3.00e-04
[AI Agent] Updating 10-point summary with new PPO episodes...

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2584 | mean p(bad) before update=0.2251 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2151 | mean p(bad) before update=0.1933 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    2 | Ep    42 | reward:   -162.4 | mean(100):   -186.3 | actor_loss: -0.0049 | value_loss: 59.8222 | lr: 2.97e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2440 | mean p(bad) before update=0.2164 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2511 | mean p(bad) before update=0.2201 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    3 | Ep    67 | reward:   -114.5 | mean(100):   -159.6 | actor_loss: -0.0086 | value_loss: 47.4237 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 3 state-echo mismatches) | unlikelihood_loss=0.4159 | mean p(bad) before update=0.3359 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1994 | mean p(bad) before update=0.1797 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1878 | mean p(bad) before update=0.1711 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    4 | Ep    90 | reward:    -91.7 | mean(100):   -144.8 | actor_loss: -0.0099 | value_loss: 40.1208 | lr: 2.90e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4914 | mean p(bad) before update=0.3671 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4352 | mean p(bad) before update=0.3496 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    5 | Ep   112 | reward:    -90.8 | mean(100):   -127.0 | actor_loss: -0.0158 | value_loss: 33.1073 | lr: 2.86e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2473 | mean p(bad) before update=0.2169 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2684 | mean p(bad) before update=0.2263 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    6 | Ep   133 | reward:    -31.8 | mean(100):    -97.0 | actor_loss: -0.0067 | value_loss: 25.9629 | lr: 2.83e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4412 | mean p(bad) before update=0.3004 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.3701 | mean p(bad) before update=0.2686 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update    7 | Ep   153 | reward:    -37.3 | mean(100):    -83.0 | actor_loss: -0.0085 | value_loss: 30.8205 | lr: 2.80e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2257 | mean p(bad) before update=0.2019 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.1246 | mean p(bad) before update=0.1132 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   173 | reward:    -52.1 | mean(100):    -75.0 | actor_loss: -0.0084 | value_loss: 26.6370 | lr: 2.77e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3389 | mean p(bad) before update=0.2786 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2648 | mean p(bad) before update=0.2314 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    9 | Ep   192 | reward:    -81.8 | mean(100):    -66.9 | actor_loss: -0.0052 | value_loss: 25.3792 | lr: 2.74e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=1.0056 | mean p(bad) before update=0.6252 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3345 | mean p(bad) before update=0.2796 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   10 | Ep   211 | reward:    -29.3 | mean(100):    -62.3 | actor_loss: -0.0055 | value_loss: 27.5156 | lr: 2.71e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2417 | mean p(bad) before update=0.2128 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1956 | mean p(bad) before update=0.1759 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   230 | reward:    -57.6 | mean(100):    -59.0 | actor_loss: -0.0085 | value_loss: 23.4209 | lr: 2.68e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5111 | mean p(bad) before update=0.3667 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   247 | reward:    -11.0 | mean(100):    -49.3 | actor_loss: -0.0066 | value_loss: 22.0810 | lr: 2.66e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3405 | mean p(bad) before update=0.2875 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3126 | mean p(bad) before update=0.2650 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   264 | reward:    -28.4 | mean(100):    -43.7 | actor_loss: -0.0039 | value_loss: 22.5147 | lr: 2.63e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4372 | mean p(bad) before update=0.3042 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.5526 | mean p(bad) before update=0.3584 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   282 | reward:    -17.7 | mean(100):    -36.2 | actor_loss: -0.0062 | value_loss: 19.1851 | lr: 2.60e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4989 | mean p(bad) before update=0.3362 | ul_lr=1.00e-04 (scale=1.00)
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4908 | mean p(bad) before update=0.2984 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   300 | reward:     19.2 | mean(100):    -26.4 | actor_loss: -0.0061 | value_loss: 20.9821 | lr: 2.58e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3463 | mean p(bad) before update=0.2805 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   317 | reward:    -17.4 | mean(100):    -19.3 | actor_loss: -0.0053 | value_loss: 20.3817 | lr: 2.55e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2403 | mean p(bad) before update=0.2115 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   17 | Ep   324 | reward:     80.4 | mean(100):    -18.4 | actor_loss: -0.0060 | value_loss: 13.6409 | lr: 2.52e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.3874 | mean p(bad) before update=0.3153 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   18 | Ep   333 | reward:      5.5 | mean(100):    -12.5 | actor_loss: -0.0029 | value_loss: 14.9403 | lr: 2.51e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   19 | Ep   336 | reward:     -2.5 | mean(100):    -12.9 | actor_loss: -0.0050 | value_loss: 11.9541 | lr: 2.50e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.2819 | mean p(bad) before update=0.2414 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   20 | Ep   342 | reward:     22.9 | mean(100):    -10.0 | actor_loss: -0.0053 | value_loss: 12.5719 | lr: 2.50e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   348 | reward:     53.9 | mean(100):    -11.7 | actor_loss: -0.0070 | value_loss: 14.7220 | lr: 2.49e-04
  [Analyzer] 2 episodes -> 4 bad pairs (1 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.3760 | mean p(bad) before update=0.3080 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   22 | Ep   353 | reward:    -47.1 | mean(100):    -11.5 | actor_loss: -0.0087 | value_loss: 12.9981 | lr: 2.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   23 | Ep   357 | reward:    -30.0 | mean(100):     -9.6 | actor_loss: -0.0042 | value_loss: 10.5549 | lr: 2.47e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.7356 | mean p(bad) before update=0.4621 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   24 | Ep   364 | reward:    100.5 | mean(100):     -8.2 | actor_loss: -0.0037 | value_loss: 14.6700 | lr: 2.46e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   25 | Ep   369 | reward:    154.9 | mean(100):     -8.7 | actor_loss: -0.0065 | value_loss: 16.7251 | lr: 2.45e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.3994 | mean p(bad) before update=0.3084 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   26 | Ep   376 | reward:    -40.7 | mean(100):     -7.9 | actor_loss: -0.0021 | value_loss: 15.6485 | lr: 2.45e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.1743 | mean p(bad) before update=0.1558 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   27 | Ep   382 | reward:   -158.6 | mean(100):    -10.0 | actor_loss: -0.0066 | value_loss: 17.7247 | lr: 2.44e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   28 | Ep   387 | reward:     22.5 | mean(100):    -10.7 | actor_loss: -0.0080 | value_loss: 13.0093 | lr: 2.43e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4569 | mean p(bad) before update=0.3399 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   29 | Ep   398 | reward:     -1.1 | mean(100):    -12.3 | actor_loss: -0.0060 | value_loss: 20.8417 | lr: 2.42e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.0915 | mean p(bad) before update=0.0830 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   30 | Ep   403 | reward:     14.9 | mean(100):     -8.9 | actor_loss: -0.0046 | value_loss: 13.1149 | lr: 2.40e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   31 | Ep   405 | reward:    -80.7 | mean(100):     -9.3 | actor_loss: -0.0015 | value_loss: 8.5576 | lr: 2.40e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   32 | Ep   409 | reward:   -143.7 | mean(100):    -11.3 | actor_loss: -0.0045 | value_loss: 19.1803 | lr: 2.39e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.0752 | mean p(bad) before update=0.0722 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   33 | Ep   415 | reward:   -111.8 | mean(100):    -12.2 | actor_loss: -0.0093 | value_loss: 16.0892 | lr: 2.39e-04

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   34 | Ep   417 | reward:    123.2 | mean(100):     -9.9 | actor_loss: -0.0046 | value_loss: 6.7634 | lr: 2.38e-04
  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4403 | mean p(bad) before update=0.3484 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   35 | Ep   420 | reward:    148.4 | mean(100):     -6.7 | actor_loss: -0.0048 | value_loss: 7.7763 | lr: 2.37e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   36 | Ep   423 | reward:     63.4 | mean(100):     -7.3 | actor_loss: -0.0019 | value_loss: 12.1588 | lr: 2.37e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   37 | Ep   427 | reward:    -42.4 | mean(100):     -9.6 | actor_loss: -0.0019 | value_loss: 12.0888 | lr: 2.37e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   38 | Ep   429 | reward:     81.0 | mean(100):     -8.7 | actor_loss: -0.0064 | value_loss: 5.1600 | lr: 2.36e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 2 state-echo mismatches) | unlikelihood_loss=0.4978 | mean p(bad) before update=0.3813 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   39 | Ep   431 | reward:     76.7 | mean(100):     -7.8 | actor_loss: -0.0035 | value_loss: 5.5704 | lr: 2.36e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   40 | Ep   435 | reward:    -28.7 | mean(100):     -9.4 | actor_loss: -0.0071 | value_loss: 10.4037 | lr: 2.35e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   41 | Ep   437 | reward:    126.5 | mean(100):     -7.5 | actor_loss: -0.0051 | value_loss: 5.1700 | lr: 2.35e-04

  [Analyzer] 2 episodes -> 4 bad pairs (0 dropped by adv filter, 1 state-echo mismatches) | unlikelihood_loss=0.2832 | mean p(bad) before update=0.2380 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   42 | Ep   440 | reward:     36.4 | mean(100):     -7.4 | actor_loss: -0.0095 | value_loss: 6.7325 | lr: 2.34e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   43 | Ep   445 | reward:      7.1 | mean(100):     -4.9 | actor_loss: -0.0051 | value_loss: 15.8120 | lr: 2.34e-04


[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   44 | Ep   447 | reward:    126.1 | mean(100):     -3.3 | actor_loss: -0.0057 | value_loss: 7.2055 | lr: 2.33e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   45 | Ep   449 | reward:    109.9 | mean(100):     -4.7 | actor_loss: -0.0022 | value_loss: 10.0768 | lr: 2.33e-04

  [Analyzer] 2 episodes -> 2 bad pairs (0 dropped by adv filter, 0 state-echo mismatches) | unlikelihood_loss=0.4024 | mean p(bad) before update=0.3016 | ul_lr=1.00e-04 (scale=1.00)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   46 | Ep   452 | reward:    -67.1 | mean(100):     -3.4 | actor_loss: -0.0059 | value_loss: 9.2053 | lr: 2.33e-04

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   47 | Ep   454 | reward:    -16.9 | mean(100):     -2.6 | actor_loss: -0.0025 | value_loss: 5.8497 | lr: 2.32e-04

  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png

[AI Agent] Updating 10-point summary with new PPO episodes...  Update   48 | Ep   457 | reward:    -14.0 | mean(100):     -2.0 | actor_loss: -0.0007 | value_loss: 9.0197 | lr: 2.32e-04


[AI Agent] Updating 10-point summary with new PPO episodes...  Update   49 | Ep   459 | reward:    113.5 | mean(100):     -0.1 | actor_loss: -0.0082 | value_loss: 5.0191 | lr: 2.31e-04

  [LLM] mean(100)=1.7 reached cutoff 0.0 -- permanently disabling the analyzer and summary refresh for the rest of this run.
  Update   50 | Ep   463 | reward:     14.0 | mean(100):      1.7 | actor_loss: -0.0023 | value_loss: 11.7596 | lr: 2.31e-04
  Update   51 | Ep   465 | reward:    104.0 | mean(100):      2.3 | actor_loss: -0.0042 | value_loss: 6.3599 | lr: 2.31e-04
  Update   52 | Ep   467 | reward:   -223.6 | mean(100):      1.6 | actor_loss: -0.0018 | value_loss: 12.3764 | lr: 2.30e-04
  Update   53 | Ep   469 | reward:    -22.4 | mean(100):      2.9 | actor_loss: -0.0058 | value_loss: 5.2266 | lr: 2.30e-04
  Update   54 | Ep   471 | reward:     61.8 | mean(100):      4.2 | actor_loss: -0.0047 | value_loss: 4.9385 | lr: 2.30e-04
  Update   55 | Ep   473 | reward:    233.4 | mean(100):      9.2 | actor_loss: -0.0031 | value_loss: 8.4718 | lr: 2.29e-04
  Update   56 | Ep   475 | reward:    131.1 | mean(100):     10.2 | actor_loss: -0.0026 | value_loss: 7.0648 | lr: 2.29e-04
  Update   57 | Ep   478 | reward:    219.6 | mean(100):     17.8 | actor_loss: -0.0042 | value_loss: 12.1362 | lr: 2.29e-04
  Update   58 | Ep   481 | reward:    -60.9 | mean(100):     20.4 | actor_loss: -0.0080 | value_loss: 9.6472 | lr: 2.28e-04
  Update   59 | Ep   486 | reward:     -4.7 | mean(100):     25.2 | actor_loss: -0.0039 | value_loss: 20.7625 | lr: 2.28e-04
  Update   60 | Ep   491 | reward:     -6.9 | mean(100):     36.2 | actor_loss: -0.0030 | value_loss: 18.5542 | lr: 2.27e-04
  Update   61 | Ep   494 | reward:    219.4 | mean(100):     42.0 | actor_loss: -0.0026 | value_loss: 15.0024 | lr: 2.26e-04
  Update   62 | Ep   498 | reward:    204.1 | mean(100):     49.4 | actor_loss: -0.0032 | value_loss: 17.9629 | lr: 2.26e-04
  Update   63 | Ep   504 | reward:    224.0 | mean(100):     54.2 | actor_loss: -0.0043 | value_loss: 22.1235 | lr: 2.25e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update   64 | Ep   509 | reward:     16.3 | mean(100):     61.3 | actor_loss: -0.0017 | value_loss: 19.4385 | lr: 2.24e-04
  Update   65 | Ep   516 | reward:     11.1 | mean(100):     70.0 | actor_loss: -0.0032 | value_loss: 24.5945 | lr: 2.24e-04
  Update   66 | Ep   521 | reward:     -3.1 | mean(100):     72.7 | actor_loss: -0.0023 | value_loss: 17.0318 | lr: 2.23e-04
  Update   67 | Ep   527 | reward:    263.5 | mean(100):     84.6 | actor_loss: -0.0032 | value_loss: 21.0019 | lr: 2.22e-04
  Update   68 | Ep   533 | reward:     -7.4 | mean(100):     88.2 | actor_loss: -0.0048 | value_loss: 19.2446 | lr: 2.21e-04
  Update   69 | Ep   536 | reward:    186.9 | mean(100):     94.9 | actor_loss: -0.0024 | value_loss: 12.9173 | lr: 2.20e-04
  Update   70 | Ep   540 | reward:    -20.8 | mean(100):     98.4 | actor_loss: -0.0041 | value_loss: 15.5992 | lr: 2.20e-04
  Update   71 | Ep   543 | reward:    118.1 | mean(100):    103.3 | actor_loss: -0.0009 | value_loss: 10.2199 | lr: 2.19e-04
  Update   72 | Ep   548 | reward:     16.3 | mean(100):    109.0 | actor_loss: -0.0045 | value_loss: 17.9334 | lr: 2.19e-04
  Update   73 | Ep   553 | reward:    223.5 | mean(100):    118.8 | actor_loss: -0.0028 | value_loss: 20.6159 | lr: 2.18e-04
  Update   74 | Ep   557 | reward:    208.9 | mean(100):    127.0 | actor_loss: -0.0028 | value_loss: 17.2355 | lr: 2.17e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update   75 | Ep   561 | reward:    -31.5 | mean(100):    129.4 | actor_loss: -0.0023 | value_loss: 15.1387 | lr: 2.16e-04
  Update   76 | Ep   565 | reward:    233.0 | mean(100):    137.1 | actor_loss: -0.0012 | value_loss: 15.4244 | lr: 2.16e-04
  Update   77 | Ep   568 | reward:    192.0 | mean(100):    143.2 | actor_loss: -0.0019 | value_loss: 14.0030 | lr: 2.15e-04
  Update   78 | Ep   571 | reward:    166.9 | mean(100):    147.6 | actor_loss: -0.0023 | value_loss: 14.4187 | lr: 2.15e-04
  Update   79 | Ep   576 | reward:    238.0 | mean(100):    150.0 | actor_loss: -0.0032 | value_loss: 19.0976 | lr: 2.14e-04
  Update   80 | Ep   579 | reward:    217.1 | mean(100):    151.6 | actor_loss: -0.0017 | value_loss: 11.6154 | lr: 2.14e-04
  Update   81 | Ep   582 | reward:    240.5 | mean(100):    159.3 | actor_loss: -0.0028 | value_loss: 14.9625 | lr: 2.13e-04
  Update   82 | Ep   586 | reward:    205.3 | mean(100):    162.7 | actor_loss: -0.0013 | value_loss: 17.1981 | lr: 2.13e-04
  Update   83 | Ep   591 | reward:    -37.6 | mean(100):    158.7 | actor_loss: -0.0028 | value_loss: 19.3295 | lr: 2.12e-04
  Update   84 | Ep   596 | reward:    248.7 | mean(100):    159.6 | actor_loss: -0.0025 | value_loss: 20.6330 | lr: 2.11e-04
  Update   85 | Ep   602 | reward:    222.0 | mean(100):    157.4 | actor_loss: -0.0032 | value_loss: 19.7208 | lr: 2.11e-04
  Update   86 | Ep   607 | reward:    225.3 | mean(100):    160.5 | actor_loss: -0.0068 | value_loss: 18.3157 | lr: 2.10e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update   87 | Ep   612 | reward:    230.6 | mean(100):    164.2 | actor_loss: -0.0018 | value_loss: 18.7360 | lr: 2.09e-04
  Update   88 | Ep   616 | reward:    252.1 | mean(100):    170.0 | actor_loss: -0.0014 | value_loss: 16.8624 | lr: 2.08e-04
  Update   89 | Ep   621 | reward:    251.4 | mean(100):    176.5 | actor_loss: -0.0056 | value_loss: 19.5691 | lr: 2.08e-04
  Update   90 | Ep   626 | reward:    229.3 | mean(100):    180.2 | actor_loss: -0.0023 | value_loss: 18.9817 | lr: 2.07e-04
  Update   91 | Ep   631 | reward:    219.3 | mean(100):    174.9 | actor_loss: -0.0034 | value_loss: 20.9865 | lr: 2.06e-04
  Update   92 | Ep   635 | reward:    225.5 | mean(100):    177.3 | actor_loss: -0.0012 | value_loss: 15.7182 | lr: 2.05e-04
  Update   93 | Ep   639 | reward:    215.1 | mean(100):    177.9 | actor_loss: -0.0025 | value_loss: 17.4115 | lr: 2.05e-04
  Update   94 | Ep   643 | reward:    205.5 | mean(100):    180.7 | actor_loss: -0.0026 | value_loss: 15.9747 | lr: 2.04e-04
  Update   95 | Ep   648 | reward:    254.5 | mean(100):    181.6 | actor_loss: -0.0022 | value_loss: 19.0088 | lr: 2.04e-04
  Update   96 | Ep   653 | reward:    252.3 | mean(100):    176.0 | actor_loss: -0.0031 | value_loss: 23.1902 | lr: 2.03e-04
  Update   97 | Ep   658 | reward:     27.4 | mean(100):    171.7 | actor_loss: -0.0018 | value_loss: 16.5229 | lr: 2.02e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update   98 | Ep   663 | reward:    267.2 | mean(100):    172.5 | actor_loss: -0.0036 | value_loss: 20.6511 | lr: 2.01e-04
  Update   99 | Ep   669 | reward:    217.1 | mean(100):    171.7 | actor_loss: -0.0032 | value_loss: 22.1519 | lr: 2.01e-04
  Update  100 | Ep   676 | reward:    266.7 | mean(100):    171.8 | actor_loss: -0.0059 | value_loss: 27.4075 | lr: 2.00e-04
  Update  101 | Ep   683 | reward:     19.6 | mean(100):    166.9 | actor_loss: -0.0042 | value_loss: 25.5956 | lr: 1.99e-04
  Update  102 | Ep   689 | reward:    258.1 | mean(100):    168.4 | actor_loss: -0.0045 | value_loss: 20.3070 | lr: 1.98e-04
  Update  103 | Ep   693 | reward:    247.0 | mean(100):    170.5 | actor_loss: -0.0015 | value_loss: 14.5362 | lr: 1.97e-04
  Update  104 | Ep   698 | reward:    275.5 | mean(100):    170.9 | actor_loss: -0.0055 | value_loss: 21.7426 | lr: 1.96e-04
  Update  105 | Ep   705 | reward:      9.4 | mean(100):    175.4 | actor_loss: -0.0040 | value_loss: 24.2263 | lr: 1.95e-04
  Update  106 | Ep   711 | reward:    219.7 | mean(100):    178.6 | actor_loss: -0.0048 | value_loss: 22.1150 | lr: 1.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update  107 | Ep   714 | reward:     68.0 | mean(100):    175.5 | actor_loss: -0.0093 | value_loss: 10.0933 | lr: 1.93e-04
  Update  108 | Ep   721 | reward:    272.4 | mean(100):    172.0 | actor_loss: -0.0035 | value_loss: 24.3919 | lr: 1.93e-04
  Update  109 | Ep   726 | reward:     -8.9 | mean(100):    168.5 | actor_loss: -0.0044 | value_loss: 21.5730 | lr: 1.92e-04
  Update  110 | Ep   732 | reward:    240.5 | mean(100):    170.6 | actor_loss: -0.0039 | value_loss: 23.7699 | lr: 1.91e-04
  Update  111 | Ep   738 | reward:    288.3 | mean(100):    169.7 | actor_loss: -0.0063 | value_loss: 22.3384 | lr: 1.90e-04
  Update  112 | Ep   743 | reward:    224.4 | mean(100):    171.2 | actor_loss: -0.0027 | value_loss: 19.2163 | lr: 1.89e-04
  Update  113 | Ep   749 | reward:    237.4 | mean(100):    177.3 | actor_loss: -0.0023 | value_loss: 22.1601 | lr: 1.89e-04
  Update  114 | Ep   755 | reward:    242.3 | mean(100):    181.8 | actor_loss: -0.0031 | value_loss: 21.0815 | lr: 1.88e-04
  Update  115 | Ep   760 | reward:    263.1 | mean(100):    181.0 | actor_loss: -0.0031 | value_loss: 16.7903 | lr: 1.87e-04
  Update  116 | Ep   767 | reward:    216.4 | mean(100):    181.8 | actor_loss: -0.0015 | value_loss: 25.1674 | lr: 1.86e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update  117 | Ep   773 | reward:     23.2 | mean(100):    184.2 | actor_loss: -0.0050 | value_loss: 21.1404 | lr: 1.85e-04
  Update  118 | Ep   780 | reward:     48.9 | mean(100):    184.1 | actor_loss: -0.0014 | value_loss: 23.8664 | lr: 1.84e-04
  Update  119 | Ep   786 | reward:    214.6 | mean(100):    186.5 | actor_loss: -0.0029 | value_loss: 19.1783 | lr: 1.83e-04
  Update  120 | Ep   792 | reward:     33.5 | mean(100):    187.2 | actor_loss: -0.0009 | value_loss: 19.9896 | lr: 1.82e-04
  Update  121 | Ep   798 | reward:    227.4 | mean(100):    184.1 | actor_loss: -0.0038 | value_loss: 21.7326 | lr: 1.81e-04
  Update  122 | Ep   806 | reward:    303.9 | mean(100):    182.4 | actor_loss: -0.0027 | value_loss: 27.4007 | lr: 1.80e-04
  Update  123 | Ep   813 | reward:    258.7 | mean(100):    180.9 | actor_loss: -0.0044 | value_loss: 26.2431 | lr: 1.79e-04
  Update  124 | Ep   819 | reward:     63.7 | mean(100):    185.3 | actor_loss: -0.0028 | value_loss: 21.2023 | lr: 1.78e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update  125 | Ep   827 | reward:    268.9 | mean(100):    186.5 | actor_loss: -0.0021 | value_loss: 27.9409 | lr: 1.77e-04
  Update  126 | Ep   834 | reward:    202.5 | mean(100):    189.0 | actor_loss: -0.0035 | value_loss: 24.4568 | lr: 1.76e-04
  Update  127 | Ep   841 | reward:     21.0 | mean(100):    184.4 | actor_loss: -0.0040 | value_loss: 23.3527 | lr: 1.75e-04
  Update  128 | Ep   847 | reward:    244.7 | mean(100):    186.5 | actor_loss: -0.0037 | value_loss: 19.1601 | lr: 1.74e-04
  Update  129 | Ep   853 | reward:    214.2 | mean(100):    185.1 | actor_loss: -0.0032 | value_loss: 19.2378 | lr: 1.73e-04
  Update  130 | Ep   860 | reward:      4.7 | mean(100):    185.8 | actor_loss: -0.0032 | value_loss: 25.2972 | lr: 1.72e-04
  Update  131 | Ep   867 | reward:    212.7 | mean(100):    189.8 | actor_loss: -0.0018 | value_loss: 25.9848 | lr: 1.71e-04
  Update  132 | Ep   874 | reward:    243.7 | mean(100):    194.1 | actor_loss: -0.0024 | value_loss: 23.4550 | lr: 1.70e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
  Update  133 | Ep   881 | reward:    200.9 | mean(100):    191.0 | actor_loss: -0.0046 | value_loss: 24.1945 | lr: 1.69e-04
  Update  134 | Ep   889 | reward:    248.8 | mean(100):    189.6 | actor_loss: -0.0026 | value_loss: 30.1685 | lr: 1.68e-04
  Update  135 | Ep   894 | reward:    211.2 | mean(100):    193.9 | actor_loss: -0.0037 | value_loss: 19.9610 | lr: 1.67e-04
  Update  136 | Ep   899 | reward:    229.1 | mean(100):    199.7 | actor_loss: -0.0035 | value_loss: 20.2568 | lr: 1.66e-04
  Update  137 | Ep   907 | reward:    241.7 | mean(100):    201.8 | actor_loss: -0.0042 | value_loss: 24.5926 | lr: 1.65e-04

Solved at episode 907 (update 137) with mean 201.8!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm_3.png
