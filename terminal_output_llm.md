Using device: cuda
Training PPO+LLM on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5
  analyzer_every=5  analyzer_topk=2  unlikelihood_lr=0.0001
  summary_every=10  summary_n_traj=2  llm_model=gpt-4o-mini
  warmup_episodes=100 (analyzer/summary updates disabled until this many episodes complete)

  Update    1 | Ep    20 | reward:   -140.2 | mean(100):   -206.6 | actor_loss: -0.0056 | value_loss: 32.8080 | lr: 3.00e-04
  Update    2 | Ep    40 | reward:    -64.8 | mean(100):   -173.5 | actor_loss: -0.0042 | value_loss: 21.8166 | lr: 2.97e-04
  Update    3 | Ep    61 | reward:   -111.8 | mean(100):   -151.7 | actor_loss: -0.0047 | value_loss: 19.9377 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update    4 | Ep    83 | reward:   -114.7 | mean(100):   -136.3 | actor_loss: -0.0084 | value_loss: 17.8502 | lr: 2.91e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2996 | mean p(bad) before update=0.2524
  Update    5 | Ep   105 | reward:    -83.6 | mean(100):   -125.1 | actor_loss: -0.0037 | value_loss: 16.2034 | lr: 2.88e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2345 | mean p(bad) before update=0.2061
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3005 | mean p(bad) before update=0.2570
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3554 | mean p(bad) before update=0.2884
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2644 | mean p(bad) before update=0.2269

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    6 | Ep   128 | reward:    -53.9 | mean(100):    -99.6 | actor_loss: -0.0059 | value_loss: 15.5973 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2329 | mean p(bad) before update=0.2059
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2363 | mean p(bad) before update=0.2068
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3037 | mean p(bad) before update=0.2600
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3822 | mean p(bad) before update=0.3067

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    7 | Ep   148 | reward:   -146.3 | mean(100):    -91.9 | actor_loss: -0.0041 | value_loss: 16.4269 | lr: 2.81e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2589 | mean p(bad) before update=0.2252
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3239 | mean p(bad) before update=0.2600
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2526 | mean p(bad) before update=0.2142
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.1865 | mean p(bad) before update=0.1665

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    8 | Ep   168 | reward:    -54.5 | mean(100):    -88.6 | actor_loss: -0.0100 | value_loss: 15.9507 | lr: 2.78e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3013 | mean p(bad) before update=0.2578
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2583 | mean p(bad) before update=0.2187
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3591 | mean p(bad) before update=0.2882
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2575 | mean p(bad) before update=0.2233

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update    9 | Ep   188 | reward:    -97.5 | mean(100):    -82.1 | actor_loss: -0.0100 | value_loss: 12.6640 | lr: 2.75e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2804 | mean p(bad) before update=0.2311
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3338 | mean p(bad) before update=0.2734
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2270 | mean p(bad) before update=0.1999
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2567 | mean p(bad) before update=0.2231

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   10 | Ep   207 | reward:    -46.4 | mean(100):    -72.2 | actor_loss: -0.0100 | value_loss: 12.9679 | lr: 2.72e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3364 | mean p(bad) before update=0.2817
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2165 | mean p(bad) before update=0.1923
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2259 | mean p(bad) before update=0.1986
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2044 | mean p(bad) before update=0.1825

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   11 | Ep   226 | reward:    -12.9 | mean(100):    -70.0 | actor_loss: -0.0095 | value_loss: 13.7561 | lr: 2.69e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2397 | mean p(bad) before update=0.2094
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2509 | mean p(bad) before update=0.2145
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3171 | mean p(bad) before update=0.2683

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   12 | Ep   241 | reward:    -80.8 | mean(100):    -64.9 | actor_loss: -0.0036 | value_loss: 12.9928 | lr: 2.66e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2031 | mean p(bad) before update=0.1803
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2709 | mean p(bad) before update=0.2332
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2260 | mean p(bad) before update=0.1978

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   13 | Ep   258 | reward:      2.7 | mean(100):    -51.9 | actor_loss: -0.0086 | value_loss: 12.4605 | lr: 2.64e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2524 | mean p(bad) before update=0.2199
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2724 | mean p(bad) before update=0.2302

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   14 | Ep   267 | reward:     26.9 | mean(100):    -48.1 | actor_loss: -0.0092 | value_loss: 10.1936 | lr: 2.61e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2404 | mean p(bad) before update=0.2093
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2109 | mean p(bad) before update=0.1874
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2632 | mean p(bad) before update=0.2031

[AI Agent] Updating 10-point summary with new PPO episodes...

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   15 | Ep   282 | reward:      7.9 | mean(100):    -41.4 | actor_loss: -0.0063 | value_loss: 13.1000 | lr: 2.60e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.1994 | mean p(bad) before update=0.1771
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3160 | mean p(bad) before update=0.2586

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   16 | Ep   289 | reward:    -15.4 | mean(100):    -36.9 | actor_loss: -0.0109 | value_loss: 8.0332 | lr: 2.58e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2463 | mean p(bad) before update=0.2071
  Update   17 | Ep   295 | reward:    -19.9 | mean(100):    -33.6 | actor_loss: -0.0088 | value_loss: 8.1601 | lr: 2.57e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.2112 | mean p(bad) before update=0.1744
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3286 | mean p(bad) before update=0.2654

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   18 | Ep   304 | reward:    -33.5 | mean(100):    -33.2 | actor_loss: -0.0059 | value_loss: 10.4722 | lr: 2.56e-04
  Update   19 | Ep   306 | reward:      4.3 | mean(100):    -32.8 | actor_loss: -0.0128 | value_loss: 7.2624 | lr: 2.54e-04
  Update   20 | Ep   308 | reward:     46.5 | mean(100):    -30.6 | actor_loss: -0.0087 | value_loss: 6.5066 | lr: 2.54e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 198329 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   21 | Ep   312 | reward:     59.0 | mean(100):    -28.1 | actor_loss: -0.0072 | value_loss: 7.1067 | lr: 2.54e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 214725 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   22 | Ep   314 | reward:     86.7 | mean(100):    -25.2 | actor_loss: -0.0066 | value_loss: 4.2893 | lr: 2.53e-04
  Update   23 | Ep   317 | reward:    -34.4 | mean(100):    -24.0 | actor_loss: -0.0071 | value_loss: 4.7040 | lr: 2.53e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 172045 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   24 | Ep   319 | reward:    105.7 | mean(100):    -22.6 | actor_loss: -0.0027 | value_loss: 4.4736 | lr: 2.52e-04
  Update   25 | Ep   321 | reward:    110.8 | mean(100):    -18.6 | actor_loss: -0.0060 | value_loss: 3.8717 | lr: 2.52e-04
  Update   26 | Ep   323 | reward:    -20.2 | mean(100):    -18.3 | actor_loss: -0.0059 | value_loss: 3.9105 | lr: 2.52e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 267993 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   27 | Ep   325 | reward:     44.5 | mean(100):    -16.1 | actor_loss: -0.0073 | value_loss: 3.5477 | lr: 2.52e-04
  Update   28 | Ep   327 | reward:    107.8 | mean(100):    -13.2 | actor_loss: -0.0038 | value_loss: 3.1016 | lr: 2.51e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 285803 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   29 | Ep   329 | reward:   -215.0 | mean(100):    -14.1 | actor_loss: -0.0037 | value_loss: 4.8444 | lr: 2.51e-04
  Update   30 | Ep   331 | reward:     36.0 | mean(100):    -11.7 | actor_loss: -0.0062 | value_loss: 4.3709 | lr: 2.51e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 173641 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   31 | Ep   334 | reward:    -61.3 | mean(100):    -13.1 | actor_loss: -0.0017 | value_loss: 5.6100 | lr: 2.50e-04
  Update   32 | Ep   336 | reward:    -97.6 | mean(100):    -14.8 | actor_loss: 0.0015 | value_loss: 3.6870 | lr: 2.50e-04
  Update   33 | Ep   338 | reward:    108.5 | mean(100):    -14.0 | actor_loss: -0.0054 | value_loss: 3.3079 | lr: 2.50e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 257320 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   34 | Ep   340 | reward:     42.0 | mean(100):    -11.6 | actor_loss: -0.0027 | value_loss: 3.8080 | lr: 2.49e-04
  Update   35 | Ep   342 | reward:     46.2 | mean(100):    -10.0 | actor_loss: -0.0020 | value_loss: 2.6741 | lr: 2.49e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 286927 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   36 | Ep   344 | reward:      8.6 | mean(100):     -9.8 | actor_loss: -0.0058 | value_loss: 2.5200 | lr: 2.49e-04
  Update   37 | Ep   346 | reward:   -120.2 | mean(100):    -10.2 | actor_loss: -0.0054 | value_loss: 3.0958 | lr: 2.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update   38 | Ep   348 | reward:    130.2 | mean(100):     -9.8 | actor_loss: -0.0012 | value_loss: 4.2360 | lr: 2.48e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 229961 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   39 | Ep   350 | reward:    -89.1 | mean(100):    -10.5 | actor_loss: -0.0003 | value_loss: 3.1383 | lr: 2.48e-04
  Update   40 | Ep   352 | reward:     82.6 | mean(100):     -8.0 | actor_loss: -0.0027 | value_loss: 2.1857 | lr: 2.47e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 211335 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   41 | Ep   354 | reward:    -90.0 | mean(100):     -9.7 | actor_loss: -0.0071 | value_loss: 4.1371 | lr: 2.47e-04
  Update   42 | Ep   356 | reward:     43.0 | mean(100):     -9.2 | actor_loss: -0.0019 | value_loss: 3.0518 | lr: 2.47e-04
  Update   43 | Ep   358 | reward:      9.2 | mean(100):     -8.1 | actor_loss: -0.0053 | value_loss: 1.7527 | lr: 2.47e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 248746 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   44 | Ep   360 | reward:    126.9 | mean(100):     -5.0 | actor_loss: -0.0105 | value_loss: 3.6702 | lr: 2.46e-04
  Update   45 | Ep   362 | reward:    143.3 | mean(100):     -3.8 | actor_loss: -0.0010 | value_loss: 3.9079 | lr: 2.46e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 252051 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   46 | Ep   364 | reward:     74.0 | mean(100):     -1.9 | actor_loss: -0.0026 | value_loss: 1.9274 | lr: 2.46e-04
  Update   47 | Ep   366 | reward:    118.7 | mean(100):      1.5 | actor_loss: -0.0051 | value_loss: 3.5588 | lr: 2.45e-04
  Update   48 | Ep   368 | reward:    115.2 | mean(100):      4.0 | actor_loss: -0.0011 | value_loss: 4.4313 | lr: 2.45e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 244107 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   49 | Ep   370 | reward:     50.4 | mean(100):      5.7 | actor_loss: -0.0016 | value_loss: 1.8375 | lr: 2.45e-04
  Update   50 | Ep   372 | reward:      8.8 | mean(100):      7.0 | actor_loss: -0.0115 | value_loss: 2.1852 | lr: 2.44e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 266638 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   51 | Ep   374 | reward:    -81.7 | mean(100):      7.1 | actor_loss: -0.0001 | value_loss: 4.7173 | lr: 2.44e-04
  Update   52 | Ep   376 | reward:      1.9 | mean(100):      7.6 | actor_loss: -0.0021 | value_loss: 1.7425 | lr: 2.44e-04
  Update   53 | Ep   378 | reward:     30.7 | mean(100):      7.5 | actor_loss: -0.0054 | value_loss: 3.0654 | lr: 2.44e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 259687 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   54 | Ep   381 | reward:    -33.7 | mean(100):      8.5 | actor_loss: 0.0019 | value_loss: 3.3018 | lr: 2.43e-04
  Update   55 | Ep   383 | reward:    111.8 | mean(100):     10.4 | actor_loss: -0.0016 | value_loss: 3.7857 | lr: 2.43e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 223764 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   56 | Ep   385 | reward:    102.3 | mean(100):     12.4 | actor_loss: -0.0056 | value_loss: 3.1241 | lr: 2.43e-04
  Update   57 | Ep   388 | reward:    166.2 | mean(100):     15.7 | actor_loss: -0.0016 | value_loss: 3.7435 | lr: 2.42e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 221638 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   58 | Ep   391 | reward:   -102.6 | mean(100):     15.0 | actor_loss: -0.0078 | value_loss: 3.2226 | lr: 2.42e-04
  Update   59 | Ep   393 | reward:     66.7 | mean(100):     16.2 | actor_loss: -0.0009 | value_loss: 2.6639 | lr: 2.41e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 218627 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   60 | Ep   395 | reward:     50.2 | mean(100):     17.4 | actor_loss: -0.0026 | value_loss: 1.9366 | lr: 2.41e-04
  Update   61 | Ep   397 | reward:     68.2 | mean(100):     20.3 | actor_loss: -0.0044 | value_loss: 2.6732 | lr: 2.41e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 231826 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   62 | Ep   399 | reward:    -81.4 | mean(100):     20.5 | actor_loss: 0.0004 | value_loss: 3.8235 | lr: 2.40e-04
  Update   63 | Ep   401 | reward:    108.2 | mean(100):     22.7 | actor_loss: -0.0057 | value_loss: 2.8391 | lr: 2.40e-04
  Update   64 | Ep   403 | reward:    -68.6 | mean(100):     22.8 | actor_loss: -0.0127 | value_loss: 2.8062 | lr: 2.40e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 244136 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   65 | Ep   405 | reward:     71.2 | mean(100):     25.4 | actor_loss: -0.0011 | value_loss: 2.7868 | lr: 2.40e-04
  Update   66 | Ep   407 | reward:     79.5 | mean(100):     26.4 | actor_loss: -0.0048 | value_loss: 2.4717 | lr: 2.39e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 292659 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   67 | Ep   409 | reward:     82.8 | mean(100):     28.2 | actor_loss: -0.0075 | value_loss: 1.5129 | lr: 2.39e-04
  Update   68 | Ep   411 | reward:    198.3 | mean(100):     32.7 | actor_loss: -0.0051 | value_loss: 3.0565 | lr: 2.39e-04
  Update   69 | Ep   413 | reward:     64.5 | mean(100):     33.5 | actor_loss: -0.0003 | value_loss: 2.7748 | lr: 2.38e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 198273 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   70 | Ep   417 | reward:    176.3 | mean(100):     36.8 | actor_loss: -0.0020 | value_loss: 6.1043 | lr: 2.38e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 178584 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   71 | Ep   420 | reward:    -54.9 | mean(100):     37.6 | actor_loss: -0.0035 | value_loss: 3.7902 | lr: 2.37e-04
  Update   72 | Ep   423 | reward:    -70.5 | mean(100):     36.5 | actor_loss: -0.0076 | value_loss: 3.4524 | lr: 2.37e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 192348 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   73 | Ep   425 | reward:    167.6 | mean(100):     37.7 | actor_loss: -0.0013 | value_loss: 2.8602 | lr: 2.37e-04
  Update   74 | Ep   427 | reward:    120.6 | mean(100):     38.2 | actor_loss: -0.0043 | value_loss: 2.8733 | lr: 2.36e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 205517 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   75 | Ep   430 | reward:    193.9 | mean(100):     44.0 | actor_loss: -0.0009 | value_loss: 3.4008 | lr: 2.36e-04
  Update   76 | Ep   432 | reward:     72.5 | mean(100):     47.1 | actor_loss: -0.0054 | value_loss: 2.8412 | lr: 2.35e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 194473 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   77 | Ep   435 | reward:    156.7 | mean(100):     50.0 | actor_loss: 0.0010 | value_loss: 5.9963 | lr: 2.35e-04
  Update   78 | Ep   437 | reward:    134.2 | mean(100):     55.1 | actor_loss: -0.0012 | value_loss: 4.2210 | lr: 2.35e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 186782 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   79 | Ep   439 | reward:    157.6 | mean(100):     56.1 | actor_loss: -0.0010 | value_loss: 2.6043 | lr: 2.34e-04
  Update   80 | Ep   441 | reward:    108.1 | mean(100):     57.0 | actor_loss: -0.0040 | value_loss: 1.2855 | lr: 2.34e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 193310 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   81 | Ep   444 | reward:    -51.4 | mean(100):     57.4 | actor_loss: -0.0064 | value_loss: 3.9635 | lr: 2.34e-04
  Update   82 | Ep   446 | reward:    109.2 | mean(100):     61.2 | actor_loss: -0.0022 | value_loss: 2.4153 | lr: 2.33e-04
  Update   83 | Ep   448 | reward:    167.5 | mean(100):     63.3 | actor_loss: -0.0013 | value_loss: 2.0165 | lr: 2.33e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 225157 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   84 | Ep   450 | reward:    113.3 | mean(100):     67.3 | actor_loss: -0.0093 | value_loss: 2.3051 | lr: 2.33e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 173938 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   85 | Ep   454 | reward:    190.4 | mean(100):     76.0 | actor_loss: -0.0023 | value_loss: 5.4607 | lr: 2.32e-04
  Update   86 | Ep   457 | reward:    -56.7 | mean(100):     76.5 | actor_loss: 0.0002 | value_loss: 4.2125 | lr: 2.32e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 178166 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   87 | Ep   461 | reward:    -76.3 | mean(100):     75.2 | actor_loss: -0.0021 | value_loss: 5.1849 | lr: 2.31e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6249 | mean p(bad) before update=0.4007
  Update   88 | Ep   464 | reward:    -97.5 | mean(100):     74.9 | actor_loss: -0.0013 | value_loss: 5.1779 | lr: 2.31e-04
  Update   89 | Ep   468 | reward:    -29.7 | mean(100):     70.1 | actor_loss: -0.0036 | value_loss: 4.2736 | lr: 2.30e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 134890 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   90 | Ep   471 | reward:    -59.3 | mean(100):     70.4 | actor_loss: -0.0016 | value_loss: 3.6447 | lr: 2.30e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 180900 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   91 | Ep   474 | reward:   -183.6 | mean(100):     68.4 | actor_loss: -0.0044 | value_loss: 4.5483 | lr: 2.29e-04
  Update   92 | Ep   477 | reward:    116.2 | mean(100):     70.8 | actor_loss: -0.0002 | value_loss: 3.4380 | lr: 2.29e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 228110 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   93 | Ep   479 | reward:     97.1 | mean(100):     71.9 | actor_loss: -0.0054 | value_loss: 0.9089 | lr: 2.28e-04
  Update   94 | Ep   481 | reward:    116.0 | mean(100):     74.9 | actor_loss: -0.0062 | value_loss: 1.0177 | lr: 2.28e-04
  Update   95 | Ep   483 | reward:    173.3 | mean(100):     75.8 | actor_loss: -0.0010 | value_loss: 2.7088 | lr: 2.28e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 224164 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   96 | Ep   486 | reward:    -26.7 | mean(100):     73.9 | actor_loss: -0.0026 | value_loss: 4.3678 | lr: 2.28e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 164607 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update   97 | Ep   489 | reward:    204.5 | mean(100):     74.6 | actor_loss: -0.0050 | value_loss: 3.0589 | lr: 2.27e-04
  Update   98 | Ep   491 | reward:     41.9 | mean(100):     77.8 | actor_loss: -0.0041 | value_loss: 2.4658 | lr: 2.27e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 191441 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update   99 | Ep   495 | reward:   -140.3 | mean(100):     77.7 | actor_loss: -0.0050 | value_loss: 4.4815 | lr: 2.26e-04
  Update  100 | Ep   497 | reward:    140.5 | mean(100):     77.8 | actor_loss: -0.0048 | value_loss: 2.5475 | lr: 2.26e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 137392 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  101 | Ep   501 | reward:    -73.7 | mean(100):     80.5 | actor_loss: -0.0030 | value_loss: 6.7111 | lr: 2.25e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 130987 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  102 | Ep   504 | reward:    -32.1 | mean(100):     82.4 | actor_loss: -0.0042 | value_loss: 3.1433 | lr: 2.25e-04
  Update  103 | Ep   507 | reward:    -49.8 | mean(100):     80.4 | actor_loss: -0.0089 | value_loss: 3.1795 | lr: 2.24e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8926 | mean p(bad) before update=0.5220

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  104 | Ep   511 | reward:    -40.9 | mean(100):     76.4 | actor_loss: -0.0066 | value_loss: 4.9171 | lr: 2.24e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 145582 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  105 | Ep   514 | reward:     97.2 | mean(100):     77.1 | actor_loss: -0.0077 | value_loss: 3.2210 | lr: 2.23e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5567 | mean p(bad) before update=0.3700

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  106 | Ep   519 | reward:    179.8 | mean(100):     79.4 | actor_loss: -0.0052 | value_loss: 6.2423 | lr: 2.23e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3981 | mean p(bad) before update=0.3040
  Update  107 | Ep   524 | reward:   -163.3 | mean(100):     80.8 | actor_loss: -0.0060 | value_loss: 7.1355 | lr: 2.22e-04
  Update  108 | Ep   528 | reward:    174.2 | mean(100):     82.6 | actor_loss: -0.0030 | value_loss: 5.3668 | lr: 2.21e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 137471 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  109 | Ep   531 | reward:     98.5 | mean(100):     83.1 | actor_loss: -0.0006 | value_loss: 3.3341 | lr: 2.21e-04
  Update  110 | Ep   533 | reward:    188.2 | mean(100):     87.6 | actor_loss: -0.0029 | value_loss: 2.4614 | lr: 2.20e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 221439 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  111 | Ep   536 | reward:    189.2 | mean(100):     88.5 | actor_loss: -0.0013 | value_loss: 3.4507 | lr: 2.20e-04
  Update  112 | Ep   538 | reward:     66.0 | mean(100):     88.4 | actor_loss: -0.0035 | value_loss: 1.6378 | lr: 2.20e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 167200 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  113 | Ep   542 | reward:    215.7 | mean(100):     86.9 | actor_loss: -0.0019 | value_loss: 4.9170 | lr: 2.19e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2004 | mean p(bad) before update=0.4866
  Update  114 | Ep   546 | reward:    -29.2 | mean(100):     85.8 | actor_loss: -0.0031 | value_loss: 3.5207 | lr: 2.19e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6141 | mean p(bad) before update=0.4086

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  115 | Ep   549 | reward:    111.0 | mean(100):     84.1 | actor_loss: -0.0025 | value_loss: 3.0599 | lr: 2.18e-04
  Update  116 | Ep   551 | reward:     94.2 | mean(100):     83.8 | actor_loss: -0.0028 | value_loss: 2.3738 | lr: 2.18e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  117 | Ep   553 | reward:    118.6 | mean(100):     84.1 | actor_loss: -0.0032 | value_loss: 1.8607 | lr: 2.17e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 187125 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  118 | Ep   556 | reward:    125.8 | mean(100):     86.3 | actor_loss: -0.0034 | value_loss: 2.9291 | lr: 2.17e-04
  Update  119 | Ep   558 | reward:    209.3 | mean(100):     88.5 | actor_loss: -0.0018 | value_loss: 1.8365 | lr: 2.17e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 175906 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  120 | Ep   562 | reward:    -15.5 | mean(100):     88.2 | actor_loss: -0.0041 | value_loss: 4.9515 | lr: 2.16e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4515 | mean p(bad) before update=0.3378
  Update  121 | Ep   566 | reward:    219.7 | mean(100):     91.4 | actor_loss: -0.0025 | value_loss: 4.4037 | lr: 2.16e-04
  Update  122 | Ep   568 | reward:    110.3 | mean(100):     94.1 | actor_loss: -0.0084 | value_loss: 1.0130 | lr: 2.15e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 254137 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  123 | Ep   570 | reward:    109.3 | mean(100):     93.3 | actor_loss: -0.0039 | value_loss: 1.4605 | lr: 2.15e-04
  Update  124 | Ep   572 | reward:     79.8 | mean(100):     97.6 | actor_loss: -0.0063 | value_loss: 1.9909 | lr: 2.15e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 232619 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  125 | Ep   574 | reward:    102.1 | mean(100):    100.9 | actor_loss: -0.0030 | value_loss: 2.2906 | lr: 2.14e-04
  Update  126 | Ep   577 | reward:    222.7 | mean(100):    103.1 | actor_loss: -0.0018 | value_loss: 3.1933 | lr: 2.14e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 171926 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  127 | Ep   580 | reward:    154.9 | mean(100):    103.4 | actor_loss: -0.0059 | value_loss: 2.7865 | lr: 2.13e-04
  Update  128 | Ep   582 | reward:    109.5 | mean(100):    104.0 | actor_loss: -0.0019 | value_loss: 1.9895 | lr: 2.13e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 246009 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  129 | Ep   584 | reward:    152.1 | mean(100):    102.7 | actor_loss: -0.0003 | value_loss: 2.1595 | lr: 2.13e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5017 | mean p(bad) before update=0.3350

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  130 | Ep   589 | reward:    196.4 | mean(100):    106.5 | actor_loss: -0.0018 | value_loss: 5.6442 | lr: 2.12e-04
  Update  131 | Ep   592 | reward:     71.7 | mean(100):    106.1 | actor_loss: -0.0021 | value_loss: 3.3050 | lr: 2.12e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 145364 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  132 | Ep   595 | reward:     85.1 | mean(100):    104.8 | actor_loss: -0.0054 | value_loss: 2.9551 | lr: 2.11e-04
  Update  133 | Ep   598 | reward:    -87.5 | mean(100):    102.9 | actor_loss: -0.0035 | value_loss: 3.4182 | lr: 2.11e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 209581 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  134 | Ep   602 | reward:      4.2 | mean(100):    105.8 | actor_loss: -0.0031 | value_loss: 3.7935 | lr: 2.10e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5118 | mean p(bad) before update=0.3592
  Update  135 | Ep   606 | reward:    172.9 | mean(100):    107.6 | actor_loss: -0.0008 | value_loss: 3.6528 | lr: 2.10e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 175250 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  136 | Ep   610 | reward:    202.5 | mean(100):    112.3 | actor_loss: -0.0071 | value_loss: 3.6676 | lr: 2.09e-04
  Update  137 | Ep   612 | reward:    120.7 | mean(100):    116.7 | actor_loss: -0.0029 | value_loss: 1.9563 | lr: 2.08e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 185332 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  138 | Ep   615 | reward:      9.6 | mean(100):    115.0 | actor_loss: -0.0029 | value_loss: 3.1284 | lr: 2.08e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3766 | mean p(bad) before update=0.2740

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  139 | Ep   620 | reward:    229.1 | mean(100):    117.4 | actor_loss: -0.0025 | value_loss: 6.2187 | lr: 2.08e-04
  Update  140 | Ep   622 | reward:     92.3 | mean(100):    119.7 | actor_loss: -0.0040 | value_loss: 2.6794 | lr: 2.07e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 167554 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  141 | Ep   626 | reward:    195.7 | mean(100):    123.0 | actor_loss: -0.0038 | value_loss: 4.0186 | lr: 2.07e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.7044 | mean p(bad) before update=0.4211

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  142 | Ep   632 | reward:    -21.7 | mean(100):    123.2 | actor_loss: -0.0050 | value_loss: 7.1351 | lr: 2.06e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 177521 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  143 | Ep   634 | reward:    103.4 | mean(100):    122.4 | actor_loss: -0.0083 | value_loss: 1.0495 | lr: 2.05e-04
  Update  144 | Ep   637 | reward:    132.0 | mean(100):    122.4 | actor_loss: -0.0018 | value_loss: 2.7806 | lr: 2.05e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 131141 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  145 | Ep   642 | reward:     10.1 | mean(100):    123.7 | actor_loss: -0.0050 | value_loss: 4.5972 | lr: 2.04e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 158639 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  146 | Ep   644 | reward:    250.9 | mean(100):    126.4 | actor_loss: -0.0042 | value_loss: 2.5937 | lr: 2.04e-04
  Update  147 | Ep   647 | reward:    129.7 | mean(100):    129.7 | actor_loss: -0.0038 | value_loss: 3.4616 | lr: 2.03e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6125 | mean p(bad) before update=0.4092

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  148 | Ep   652 | reward:    216.3 | mean(100):    130.2 | actor_loss: -0.0018 | value_loss: 6.5607 | lr: 2.03e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6358 | mean p(bad) before update=0.3925
  Update  149 | Ep   655 | reward:     59.0 | mean(100):    129.5 | actor_loss: -0.0026 | value_loss: 4.1015 | lr: 2.02e-04
  Update  150 | Ep   657 | reward:     17.3 | mean(100):    128.4 | actor_loss: -0.0082 | value_loss: 2.0134 | lr: 2.02e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 162131 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  151 | Ep   661 | reward:    102.8 | mean(100):    130.9 | actor_loss: -0.0032 | value_loss: 3.5316 | lr: 2.01e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 169448 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  152 | Ep   665 | reward:    209.3 | mean(100):    135.8 | actor_loss: -0.0016 | value_loss: 3.8619 | lr: 2.01e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6911 | mean p(bad) before update=0.4245

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  153 | Ep   672 | reward:    169.3 | mean(100):    136.7 | actor_loss: -0.0042 | value_loss: 7.3315 | lr: 2.00e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5704 | mean p(bad) before update=0.4114
  Update  154 | Ep   677 | reward:    116.6 | mean(100):    137.0 | actor_loss: -0.0026 | value_loss: 4.9239 | lr: 1.99e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9963 | mean p(bad) before update=0.5011

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  155 | Ep   681 | reward:    155.1 | mean(100):    139.0 | actor_loss: -0.0011 | value_loss: 3.7553 | lr: 1.98e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 185940 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  156 | Ep   684 | reward:    184.5 | mean(100):    140.5 | actor_loss: -0.0020 | value_loss: 2.2089 | lr: 1.98e-04
  Update  157 | Ep   686 | reward:    144.5 | mean(100):    138.7 | actor_loss: -0.0038 | value_loss: 1.7681 | lr: 1.97e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7494 | mean p(bad) before update=0.4167

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  158 | Ep   692 | reward:    186.7 | mean(100):    135.0 | actor_loss: -0.0034 | value_loss: 7.1789 | lr: 1.97e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3362 | mean p(bad) before update=0.2592
  Update  159 | Ep   696 | reward:     14.0 | mean(100):    137.9 | actor_loss: -0.0036 | value_loss: 3.7503 | lr: 1.96e-04
  Update  160 | Ep   698 | reward:    193.7 | mean(100):    141.0 | actor_loss: -0.0021 | value_loss: 2.0924 | lr: 1.96e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 187252 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  161 | Ep   700 | reward:    135.2 | mean(100):    140.5 | actor_loss: -0.0027 | value_loss: 0.7318 | lr: 1.95e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 170074 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  162 | Ep   704 | reward:    -62.1 | mean(100):    141.8 | actor_loss: -0.0085 | value_loss: 3.9866 | lr: 1.95e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  163 | Ep   708 | reward:    208.1 | mean(100):    141.2 | actor_loss: -0.0027 | value_loss: 5.4892 | lr: 1.94e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 132977 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  164 | Ep   712 | reward:    204.6 | mean(100):    141.7 | actor_loss: -0.0032 | value_loss: 4.3730 | lr: 1.94e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 162424 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  165 | Ep   716 | reward:    220.1 | mean(100):    141.3 | actor_loss: -0.0036 | value_loss: 4.5296 | lr: 1.93e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 140801 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  166 | Ep   719 | reward:    230.5 | mean(100):    141.4 | actor_loss: -0.0031 | value_loss: 2.5327 | lr: 1.93e-04
  Update  167 | Ep   722 | reward:    -37.0 | mean(100):    136.6 | actor_loss: -0.0054 | value_loss: 3.1251 | lr: 1.92e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5155 | mean p(bad) before update=0.3605
  Update  168 | Ep   726 | reward:    136.0 | mean(100):    136.9 | actor_loss: -0.0016 | value_loss: 4.3299 | lr: 1.92e-04
  Update  169 | Ep   728 | reward:    134.9 | mean(100):    135.7 | actor_loss: -0.0051 | value_loss: 0.8638 | lr: 1.91e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 248876 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  170 | Ep   733 | reward:    223.3 | mean(100):    134.8 | actor_loss: -0.0042 | value_loss: 4.6980 | lr: 1.91e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4415 | mean p(bad) before update=0.3291
  Update  171 | Ep   735 | reward:    117.0 | mean(100):    132.2 | actor_loss: -0.0059 | value_loss: 1.6091 | lr: 1.90e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4254 | mean p(bad) before update=0.2562

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  172 | Ep   739 | reward:    236.0 | mean(100):    133.4 | actor_loss: -0.0027 | value_loss: 5.2068 | lr: 1.90e-04
  Update  173 | Ep   743 | reward:    125.0 | mean(100):    132.6 | actor_loss: -0.0036 | value_loss: 4.3732 | lr: 1.89e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 131476 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  174 | Ep   745 | reward:    102.0 | mean(100):    131.2 | actor_loss: -0.0036 | value_loss: 1.7523 | lr: 1.89e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 160404 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  175 | Ep   749 | reward:     22.4 | mean(100):    131.6 | actor_loss: -0.0025 | value_loss: 3.3959 | lr: 1.88e-04
  Update  176 | Ep   752 | reward:    114.7 | mean(100):    132.7 | actor_loss: -0.0014 | value_loss: 2.1367 | lr: 1.88e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2252 | mean p(bad) before update=0.5903
  Update  177 | Ep   757 | reward:    224.3 | mean(100):    135.4 | actor_loss: -0.0017 | value_loss: 4.2434 | lr: 1.87e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 163656 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  178 | Ep   762 | reward:     31.4 | mean(100):    134.3 | actor_loss: -0.0035 | value_loss: 4.6039 | lr: 1.86e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8743 | mean p(bad) before update=0.4703
  Update  179 | Ep   767 | reward:    234.0 | mean(100):    130.5 | actor_loss: -0.0027 | value_loss: 5.0159 | lr: 1.86e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 153748 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  180 | Ep   769 | reward:    140.9 | mean(100):    128.6 | actor_loss: -0.0073 | value_loss: 0.4651 | lr: 1.85e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4763 | mean p(bad) before update=0.3022
  Update  181 | Ep   774 | reward:    233.1 | mean(100):    131.4 | actor_loss: -0.0059 | value_loss: 4.2420 | lr: 1.85e-04
  Update  182 | Ep   778 | reward:     -3.6 | mean(100):    130.1 | actor_loss: -0.0050 | value_loss: 4.1191 | lr: 1.84e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6677 | mean p(bad) before update=0.3790

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  183 | Ep   782 | reward:    200.6 | mean(100):    130.6 | actor_loss: -0.0008 | value_loss: 3.5147 | lr: 1.83e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 160185 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  184 | Ep   784 | reward:     13.2 | mean(100):    129.1 | actor_loss: -0.0035 | value_loss: 1.4359 | lr: 1.83e-04
  Update  185 | Ep   787 | reward:    242.4 | mean(100):    131.6 | actor_loss: -0.0065 | value_loss: 2.8505 | lr: 1.82e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0994 | mean p(bad) before update=0.5454

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  186 | Ep   791 | reward:    143.6 | mean(100):    136.1 | actor_loss: -0.0020 | value_loss: 4.0418 | lr: 1.82e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 163995 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  187 | Ep   796 | reward:    218.8 | mean(100):    138.9 | actor_loss: -0.0023 | value_loss: 4.8358 | lr: 1.81e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8680 | mean p(bad) before update=0.5226

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  188 | Ep   800 | reward:    102.2 | mean(100):    140.6 | actor_loss: -0.0022 | value_loss: 3.2826 | lr: 1.81e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 166536 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  189 | Ep   804 | reward:    101.7 | mean(100):    143.5 | actor_loss: -0.0045 | value_loss: 3.7964 | lr: 1.80e-04
  Update  190 | Ep   806 | reward:    154.2 | mean(100):    146.7 | actor_loss: -0.0013 | value_loss: 1.6662 | lr: 1.79e-04
  [Analyzer] 5 episodes -> 8 bad pairs | unlikelihood_loss=0.8871 | mean p(bad) before update=0.4331

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  191 | Ep   811 | reward:     22.9 | mean(100):    140.8 | actor_loss: -0.0066 | value_loss: 5.4328 | lr: 1.79e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 151969 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  192 | Ep   814 | reward:    203.4 | mean(100):    141.1 | actor_loss: -0.0014 | value_loss: 2.5873 | lr: 1.78e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7523 | mean p(bad) before update=0.4009

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  193 | Ep   819 | reward:    229.3 | mean(100):    140.3 | actor_loss: -0.0034 | value_loss: 4.2774 | lr: 1.78e-04
  Update  194 | Ep   822 | reward:    231.9 | mean(100):    145.1 | actor_loss: -0.0023 | value_loss: 2.7459 | lr: 1.77e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.4153 | mean p(bad) before update=0.5804
  Update  195 | Ep   827 | reward:    135.3 | mean(100):    141.8 | actor_loss: -0.0065 | value_loss: 4.7797 | lr: 1.77e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 168216 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  196 | Ep   829 | reward:    165.0 | mean(100):    142.7 | actor_loss: -0.0023 | value_loss: 2.1234 | lr: 1.76e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9444 | mean p(bad) before update=0.4756
  Update  197 | Ep   834 | reward:     25.4 | mean(100):    146.8 | actor_loss: -0.0021 | value_loss: 6.5611 | lr: 1.76e-04
  Update  198 | Ep   838 | reward:    -38.1 | mean(100):    141.9 | actor_loss: -0.0060 | value_loss: 3.8803 | lr: 1.75e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 147868 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  199 | Ep   840 | reward:    145.9 | mean(100):    140.7 | actor_loss: -0.0035 | value_loss: 1.4168 | lr: 1.74e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 162802 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  200 | Ep   844 | reward:    124.4 | mean(100):    141.3 | actor_loss: -0.0012 | value_loss: 3.1750 | lr: 1.74e-04
  Update  201 | Ep   846 | reward:    225.2 | mean(100):    142.9 | actor_loss: -0.0011 | value_loss: 1.0817 | lr: 1.73e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8019 | mean p(bad) before update=0.4605

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  202 | Ep   852 | reward:    160.6 | mean(100):    142.2 | actor_loss: -0.0044 | value_loss: 6.7422 | lr: 1.73e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.3418 | mean p(bad) before update=0.5227
  Update  203 | Ep   857 | reward:    196.5 | mean(100):    142.8 | actor_loss: -0.0053 | value_loss: 6.4862 | lr: 1.72e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0365 | mean p(bad) before update=0.5480

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  204 | Ep   860 | reward:    208.5 | mean(100):    142.2 | actor_loss: -0.0011 | value_loss: 2.1810 | lr: 1.71e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7440 | mean p(bad) before update=0.4059
  Update  205 | Ep   865 | reward:     16.6 | mean(100):    142.4 | actor_loss: -0.0039 | value_loss: 5.2914 | lr: 1.71e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  206 | Ep   867 | reward:    165.7 | mean(100):    143.0 | actor_loss: -0.0015 | value_loss: 1.0493 | lr: 1.70e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 206167 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  207 | Ep   871 | reward:    229.4 | mean(100):    146.5 | actor_loss: -0.0038 | value_loss: 3.7394 | lr: 1.70e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7924 | mean p(bad) before update=0.4793
  Update  208 | Ep   878 | reward:     -1.0 | mean(100):    144.4 | actor_loss: -0.0066 | value_loss: 8.8661 | lr: 1.69e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3674 | mean p(bad) before update=0.2804

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  209 | Ep   881 | reward:    244.2 | mean(100):    145.1 | actor_loss: -0.0019 | value_loss: 2.3430 | lr: 1.68e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5039 | mean p(bad) before update=0.3323
  Update  210 | Ep   884 | reward:    111.0 | mean(100):    142.5 | actor_loss: -0.0060 | value_loss: 3.0503 | lr: 1.68e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7721 | mean p(bad) before update=0.3487

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  211 | Ep   889 | reward:    225.1 | mean(100):    142.1 | actor_loss: -0.0018 | value_loss: 4.9204 | lr: 1.67e-04
  Update  212 | Ep   893 | reward:    131.8 | mean(100):    136.2 | actor_loss: -0.0088 | value_loss: 3.8196 | lr: 1.67e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7955 | mean p(bad) before update=0.4478
  Update  213 | Ep   897 | reward:     -6.3 | mean(100):    129.3 | actor_loss: -0.0027 | value_loss: 3.6781 | lr: 1.66e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4206 | mean p(bad) before update=0.3079

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  214 | Ep   901 | reward:    142.7 | mean(100):    126.0 | actor_loss: -0.0042 | value_loss: 4.0619 | lr: 1.65e-04
  Update  215 | Ep   903 | reward:    142.7 | mean(100):    124.3 | actor_loss: -0.0035 | value_loss: 1.6621 | lr: 1.65e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 199361 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  216 | Ep   907 | reward:    257.5 | mean(100):    129.4 | actor_loss: -0.0011 | value_loss: 3.4401 | lr: 1.65e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 136002 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  217 | Ep   911 | reward:      6.5 | mean(100):    131.9 | actor_loss: -0.0050 | value_loss: 3.5010 | lr: 1.64e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 172993 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  218 | Ep   915 | reward:    213.1 | mean(100):    135.3 | actor_loss: -0.0010 | value_loss: 3.3981 | lr: 1.63e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0905 | mean p(bad) before update=0.6079

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  219 | Ep   920 | reward:    229.3 | mean(100):    136.6 | actor_loss: -0.0021 | value_loss: 4.1075 | lr: 1.63e-04
  Update  220 | Ep   922 | reward:    127.9 | mean(100):    135.6 | actor_loss: -0.0044 | value_loss: 1.3222 | lr: 1.62e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 209729 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  221 | Ep   925 | reward:   -118.2 | mean(100):    135.8 | actor_loss: -0.0027 | value_loss: 4.6056 | lr: 1.62e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.3792 | mean p(bad) before update=0.6578

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  222 | Ep   930 | reward:    141.2 | mean(100):    137.1 | actor_loss: -0.0015 | value_loss: 4.3977 | lr: 1.61e-04
  Update  223 | Ep   932 | reward:    122.6 | mean(100):    135.3 | actor_loss: -0.0035 | value_loss: 0.5073 | lr: 1.60e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 244348 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  224 | Ep   936 | reward:    251.5 | mean(100):    138.1 | actor_loss: -0.0020 | value_loss: 3.8331 | lr: 1.60e-04
  Update  225 | Ep   938 | reward:    175.5 | mean(100):    142.0 | actor_loss: -0.0009 | value_loss: 1.3530 | lr: 1.60e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8164 | mean p(bad) before update=0.4369

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  226 | Ep   940 | reward:    142.3 | mean(100):    142.7 | actor_loss: -0.0024 | value_loss: 1.4769 | lr: 1.59e-04
  Update  227 | Ep   942 | reward:    103.5 | mean(100):    141.5 | actor_loss: -0.0050 | value_loss: 1.5824 | lr: 1.59e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 153109 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  228 | Ep   947 | reward:    160.1 | mean(100):    142.8 | actor_loss: -0.0033 | value_loss: 3.6925 | lr: 1.59e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2950 | mean p(bad) before update=0.5556

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  229 | Ep   952 | reward:    154.4 | mean(100):    140.7 | actor_loss: -0.0039 | value_loss: 3.8037 | lr: 1.58e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4231 | mean p(bad) before update=0.2770
  Update  230 | Ep   958 | reward:      6.3 | mean(100):    134.1 | actor_loss: -0.0116 | value_loss: 5.4745 | lr: 1.57e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4923 | mean p(bad) before update=0.3018

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  231 | Ep   961 | reward:    160.0 | mean(100):    131.6 | actor_loss: -0.0041 | value_loss: 2.3216 | lr: 1.56e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0812 | mean p(bad) before update=0.6026
  Update  232 | Ep   968 | reward:     32.2 | mean(100):    129.5 | actor_loss: -0.0038 | value_loss: 7.1263 | lr: 1.56e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7216 | mean p(bad) before update=0.4706
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8870 | mean p(bad) before update=0.5425

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  233 | Ep   974 | reward:    -29.8 | mean(100):    124.1 | actor_loss: -0.0032 | value_loss: 5.7004 | lr: 1.55e-04
  Update  234 | Ep   978 | reward:    148.2 | mean(100):    125.2 | actor_loss: -0.0004 | value_loss: 3.2558 | lr: 1.54e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 157778 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0030 | mean p(bad) before update=0.5211

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  235 | Ep   984 | reward:     33.5 | mean(100):    124.3 | actor_loss: -0.0034 | value_loss: 5.1896 | lr: 1.53e-04
  Update  236 | Ep   986 | reward:    138.9 | mean(100):    126.7 | actor_loss: -0.0010 | value_loss: 1.3111 | lr: 1.52e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 161624 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  237 | Ep   989 | reward:    217.9 | mean(100):    126.1 | actor_loss: -0.0012 | value_loss: 2.3321 | lr: 1.52e-04
  Update  238 | Ep   991 | reward:    177.0 | mean(100):    128.1 | actor_loss: -0.0038 | value_loss: 2.1473 | lr: 1.52e-04
  Update  239 | Ep   993 | reward:    115.8 | mean(100):    128.9 | actor_loss: -0.0059 | value_loss: 0.5421 | lr: 1.51e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 203859 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  240 | Ep   998 | reward:    131.9 | mean(100):    134.4 | actor_loss: -0.0017 | value_loss: 5.2568 | lr: 1.51e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9988 | mean p(bad) before update=0.5593

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  241 | Ep  1003 | reward:    209.2 | mean(100):    133.0 | actor_loss: -0.0039 | value_loss: 4.1878 | lr: 1.50e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3866 | mean p(bad) before update=0.2954
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.5556 | mean p(bad) before update=0.6229

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  242 | Ep  1009 | reward:     -2.8 | mean(100):    126.2 | actor_loss: -0.0024 | value_loss: 4.9886 | lr: 1.50e-04
  Update  243 | Ep  1013 | reward:    218.4 | mean(100):    129.9 | actor_loss: -0.0019 | value_loss: 4.3942 | lr: 1.49e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9235 | mean p(bad) before update=0.4463
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.1030 | mean p(bad) before update=0.5693

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  244 | Ep  1020 | reward:     -5.4 | mean(100):    126.0 | actor_loss: -0.0013 | value_loss: 7.8635 | lr: 1.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6016 | mean p(bad) before update=0.3874
  Update  245 | Ep  1025 | reward:    213.3 | mean(100):    126.7 | actor_loss: -0.0025 | value_loss: 4.2699 | lr: 1.47e-04
  Update  246 | Ep  1028 | reward:    152.9 | mean(100):    126.2 | actor_loss: -0.0017 | value_loss: 2.3168 | lr: 1.46e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9868 | mean p(bad) before update=0.5282

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  247 | Ep  1033 | reward:    140.8 | mean(100):    130.3 | actor_loss: -0.0008 | value_loss: 4.0928 | lr: 1.46e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 129892 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  248 | Ep  1038 | reward:     -6.5 | mean(100):    127.9 | actor_loss: -0.0032 | value_loss: 3.9517 | lr: 1.45e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 146575 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  249 | Ep  1041 | reward:     -2.4 | mean(100):    125.7 | actor_loss: -0.0046 | value_loss: 2.7404 | lr: 1.44e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.1542 | mean p(bad) before update=0.5840
  Update  250 | Ep  1046 | reward:    235.4 | mean(100):    122.5 | actor_loss: -0.0054 | value_loss: 4.8620 | lr: 1.44e-04
  Update  251 | Ep  1048 | reward:    138.1 | mean(100):    121.8 | actor_loss: -0.0046 | value_loss: 2.2378 | lr: 1.43e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.5618 | mean p(bad) before update=0.6884
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7880 | mean p(bad) before update=0.4737

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  252 | Ep  1054 | reward:    242.0 | mean(100):    121.1 | actor_loss: -0.0059 | value_loss: 5.2934 | lr: 1.43e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2007 | mean p(bad) before update=0.5651

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  253 | Ep  1060 | reward:     48.9 | mean(100):    122.6 | actor_loss: -0.0021 | value_loss: 4.6625 | lr: 1.42e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6903 | mean p(bad) before update=0.3838
  Update  254 | Ep  1064 | reward:     29.8 | mean(100):    122.9 | actor_loss: -0.0067 | value_loss: 3.3826 | lr: 1.41e-04
  Update  255 | Ep  1068 | reward:    243.2 | mean(100):    127.9 | actor_loss: -0.0025 | value_loss: 4.0407 | lr: 1.40e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0665 | mean p(bad) before update=0.4925

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  256 | Ep  1072 | reward:    128.9 | mean(100):    130.6 | actor_loss: -0.0015 | value_loss: 3.7111 | lr: 1.40e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 149396 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6733 | mean p(bad) before update=0.4738

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  257 | Ep  1079 | reward:    252.7 | mean(100):    127.5 | actor_loss: -0.0036 | value_loss: 6.8992 | lr: 1.39e-04
  Update  258 | Ep  1082 | reward:    147.0 | mean(100):    128.7 | actor_loss: -0.0011 | value_loss: 2.9688 | lr: 1.38e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 171241 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  259 | Ep  1084 | reward:     65.0 | mean(100):    130.7 | actor_loss: -0.0027 | value_loss: 1.4188 | lr: 1.38e-04
  Update  260 | Ep  1086 | reward:    120.6 | mean(100):    130.5 | actor_loss: -0.0029 | value_loss: 1.3970 | lr: 1.37e-04
  Update  261 | Ep  1088 | reward:     13.9 | mean(100):    130.8 | actor_loss: -0.0050 | value_loss: 1.1145 | lr: 1.37e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 149698 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6338 | mean p(bad) before update=0.3936

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  262 | Ep  1094 | reward:     30.5 | mean(100):    129.1 | actor_loss: -0.0013 | value_loss: 5.0332 | lr: 1.37e-04
  Update  263 | Ep  1096 | reward:     29.1 | mean(100):    128.7 | actor_loss: -0.0052 | value_loss: 1.8122 | lr: 1.36e-04
  Update  264 | Ep  1098 | reward:    131.9 | mean(100):    127.6 | actor_loss: -0.0052 | value_loss: 0.6365 | lr: 1.36e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 239722 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  265 | Ep  1100 | reward:    122.3 | mean(100):    128.1 | actor_loss: -0.0050 | value_loss: 0.6194 | lr: 1.35e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 149781 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  266 | Ep  1105 | reward:    171.0 | mean(100):    128.2 | actor_loss: -0.0028 | value_loss: 4.4138 | lr: 1.35e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4621 | mean p(bad) before update=0.3345

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  267 | Ep  1110 | reward:   -116.4 | mean(100):    128.7 | actor_loss: -0.0010 | value_loss: 6.0697 | lr: 1.34e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4664 | mean p(bad) before update=0.2584
  Update  268 | Ep  1114 | reward:    211.3 | mean(100):    128.4 | actor_loss: -0.0017 | value_loss: 3.2659 | lr: 1.33e-04
  Update  269 | Ep  1118 | reward:    218.2 | mean(100):    127.8 | actor_loss: -0.0007 | value_loss: 2.6600 | lr: 1.33e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2802 | mean p(bad) before update=0.5217

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  270 | Ep  1120 | reward:    159.7 | mean(100):    127.2 | actor_loss: -0.0008 | value_loss: 1.2281 | lr: 1.32e-04
  Update  271 | Ep  1122 | reward:    228.2 | mean(100):    129.1 | actor_loss: -0.0009 | value_loss: 1.2275 | lr: 1.32e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 194921 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  272 | Ep  1124 | reward:    131.8 | mean(100):    128.9 | actor_loss: -0.0043 | value_loss: 1.7585 | lr: 1.32e-04
  Update  273 | Ep  1126 | reward:    141.2 | mean(100):    128.1 | actor_loss: -0.0020 | value_loss: 1.4413 | lr: 1.31e-04
  Update  274 | Ep  1128 | reward:    136.6 | mean(100):    127.3 | actor_loss: -0.0038 | value_loss: 1.0106 | lr: 1.31e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 244620 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  275 | Ep  1131 | reward:      7.7 | mean(100):    122.4 | actor_loss: -0.0057 | value_loss: 2.2809 | lr: 1.31e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8966 | mean p(bad) before update=0.5332
  Update  276 | Ep  1137 | reward:    213.0 | mean(100):    120.6 | actor_loss: -0.0026 | value_loss: 5.3339 | lr: 1.30e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9551 | mean p(bad) before update=0.4227

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  277 | Ep  1140 | reward:    235.2 | mean(100):    123.1 | actor_loss: -0.0010 | value_loss: 2.0706 | lr: 1.29e-04
  Update  278 | Ep  1143 | reward:    220.6 | mean(100):    129.6 | actor_loss: -0.0017 | value_loss: 2.5845 | lr: 1.29e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 161445 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  279 | Ep  1146 | reward:    215.2 | mean(100):    130.6 | actor_loss: -0.0018 | value_loss: 2.7452 | lr: 1.29e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9913 | mean p(bad) before update=0.4806

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  280 | Ep  1152 | reward:      3.5 | mean(100):    136.8 | actor_loss: -0.0029 | value_loss: 4.5909 | lr: 1.28e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5869 | mean p(bad) before update=0.3829
  Update  281 | Ep  1155 | reward:     40.5 | mean(100):    134.2 | actor_loss: -0.0046 | value_loss: 2.2097 | lr: 1.27e-04
  Update  282 | Ep  1158 | reward:     42.2 | mean(100):    133.6 | actor_loss: -0.0033 | value_loss: 2.1477 | lr: 1.27e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 144470 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  283 | Ep  1160 | reward:      0.6 | mean(100):    133.4 | actor_loss: -0.0011 | value_loss: 1.6157 | lr: 1.26e-04
  Update  284 | Ep  1162 | reward:    147.1 | mean(100):    133.7 | actor_loss: -0.0032 | value_loss: 0.1972 | lr: 1.26e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 146492 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  285 | Ep  1165 | reward:    166.6 | mean(100):    134.6 | actor_loss: -0.0067 | value_loss: 2.7104 | lr: 1.26e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 159264 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  286 | Ep  1170 | reward:    212.9 | mean(100):    132.1 | actor_loss: -0.0045 | value_loss: 4.2158 | lr: 1.25e-04
  Update  287 | Ep  1172 | reward:    135.2 | mean(100):    131.9 | actor_loss: -0.0053 | value_loss: 1.4327 | lr: 1.24e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6634 | mean p(bad) before update=0.4275
  Update  288 | Ep  1176 | reward:     15.9 | mean(100):    136.6 | actor_loss: 0.0001 | value_loss: 4.6695 | lr: 1.24e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8207 | mean p(bad) before update=0.4616

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  289 | Ep  1179 | reward:      8.9 | mean(100):    137.6 | actor_loss: -0.0013 | value_loss: 2.1803 | lr: 1.24e-04
  Update  290 | Ep  1181 | reward:    250.2 | mean(100):    137.1 | actor_loss: -0.0056 | value_loss: 1.4738 | lr: 1.23e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7596 | mean p(bad) before update=0.4566
  Update  291 | Ep  1186 | reward:      8.3 | mean(100):    134.2 | actor_loss: -0.0058 | value_loss: 4.5443 | lr: 1.23e-04
  Update  292 | Ep  1188 | reward:    134.4 | mean(100):    134.0 | actor_loss: -0.0016 | value_loss: 1.1831 | lr: 1.22e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 195147 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  293 | Ep  1192 | reward:     -0.6 | mean(100):    135.6 | actor_loss: -0.0040 | value_loss: 3.1526 | lr: 1.22e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9934 | mean p(bad) before update=0.4470
  Update  294 | Ep  1195 | reward:    225.9 | mean(100):    138.8 | actor_loss: -0.0013 | value_loss: 3.0851 | lr: 1.21e-04
  Update  295 | Ep  1197 | reward:    166.3 | mean(100):    140.1 | actor_loss: -0.0069 | value_loss: 0.6759 | lr: 1.21e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 216355 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  296 | Ep  1199 | reward:    133.3 | mean(100):    141.0 | actor_loss: -0.0017 | value_loss: 1.7660 | lr: 1.20e-04
  Update  297 | Ep  1203 | reward:    212.2 | mean(100):    144.8 | actor_loss: -0.0032 | value_loss: 5.8611 | lr: 1.20e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.6895 | mean p(bad) before update=0.7126
  Update  298 | Ep  1205 | reward:    146.5 | mean(100):    144.0 | actor_loss: -0.0045 | value_loss: 1.7107 | lr: 1.20e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 165488 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  299 | Ep  1210 | reward:     44.8 | mean(100):    142.9 | actor_loss: -0.0050 | value_loss: 4.7251 | lr: 1.19e-04
  Update  300 | Ep  1213 | reward:      6.9 | mean(100):    143.0 | actor_loss: -0.0011 | value_loss: 3.1177 | lr: 1.18e-04
  [Analyzer] 5 episodes -> 8 bad pairs | unlikelihood_loss=0.4587 | mean p(bad) before update=0.3208
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6807 | mean p(bad) before update=0.4240

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  301 | Ep  1219 | reward:    148.5 | mean(100):    137.0 | actor_loss: -0.0055 | value_loss: 8.9262 | lr: 1.18e-04
  Update  302 | Ep  1221 | reward:    136.5 | mean(100):    137.4 | actor_loss: -0.0004 | value_loss: 1.0671 | lr: 1.17e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 162978 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  303 | Ep  1224 | reward:    214.9 | mean(100):    137.3 | actor_loss: -0.0072 | value_loss: 3.1659 | lr: 1.17e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  304 | Ep  1226 | reward:     98.1 | mean(100):    136.3 | actor_loss: -0.0047 | value_loss: 0.7297 | lr: 1.16e-04
  Update  305 | Ep  1228 | reward:    177.7 | mean(100):    136.3 | actor_loss: -0.0050 | value_loss: 0.9278 | lr: 1.16e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 292283 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  306 | Ep  1232 | reward:    155.0 | mean(100):    139.0 | actor_loss: -0.0015 | value_loss: 3.0120 | lr: 1.16e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 175383 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  307 | Ep  1234 | reward:    127.4 | mean(100):    137.5 | actor_loss: -0.0082 | value_loss: 0.8463 | lr: 1.15e-04
  Update  308 | Ep  1238 | reward:    -56.6 | mean(100):    139.9 | actor_loss: -0.0034 | value_loss: 3.7456 | lr: 1.15e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0414 | mean p(bad) before update=0.5298

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  309 | Ep  1240 | reward:    148.2 | mean(100):    137.6 | actor_loss: -0.0045 | value_loss: 1.4622 | lr: 1.14e-04
  Update  310 | Ep  1242 | reward:    167.7 | mean(100):    136.8 | actor_loss: -0.0047 | value_loss: 0.4908 | lr: 1.14e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 250369 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  311 | Ep  1246 | reward:    172.2 | mean(100):    136.2 | actor_loss: -0.0006 | value_loss: 2.9772 | lr: 1.14e-04
  Update  312 | Ep  1248 | reward:    146.1 | mean(100):    135.4 | actor_loss: -0.0051 | value_loss: 0.3630 | lr: 1.13e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 209120 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  313 | Ep  1252 | reward:    186.6 | mean(100):    137.7 | actor_loss: -0.0019 | value_loss: 2.8538 | lr: 1.13e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5559 | mean p(bad) before update=0.3761
  Update  314 | Ep  1256 | reward:    172.2 | mean(100):    139.9 | actor_loss: -0.0034 | value_loss: 3.0797 | lr: 1.12e-04
  Update  315 | Ep  1258 | reward:    153.0 | mean(100):    140.0 | actor_loss: -0.0039 | value_loss: 0.7213 | lr: 1.12e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 205041 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  316 | Ep  1261 | reward:    138.8 | mean(100):    142.8 | actor_loss: -0.0013 | value_loss: 1.7956 | lr: 1.11e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 156071 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  317 | Ep  1266 | reward:      4.2 | mean(100):    142.3 | actor_loss: -0.0025 | value_loss: 3.8031 | lr: 1.11e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0364 | mean p(bad) before update=0.5202

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  318 | Ep  1269 | reward:    111.2 | mean(100):    141.4 | actor_loss: -0.0018 | value_loss: 2.1963 | lr: 1.10e-04
  Update  319 | Ep  1272 | reward:    246.8 | mean(100):    143.9 | actor_loss: -0.0007 | value_loss: 2.1913 | lr: 1.10e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 200602 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  320 | Ep  1274 | reward:    171.9 | mean(100):    143.4 | actor_loss: -0.0042 | value_loss: 0.5233 | lr: 1.09e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  321 | Ep  1278 | reward:    121.5 | mean(100):    142.3 | actor_loss: -0.0028 | value_loss: 4.4591 | lr: 1.09e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5458 | mean p(bad) before update=0.3510

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  322 | Ep  1281 | reward:    204.6 | mean(100):    141.4 | actor_loss: -0.0017 | value_loss: 2.4137 | lr: 1.08e-04
  Update  323 | Ep  1283 | reward:    138.2 | mean(100):    142.5 | actor_loss: -0.0025 | value_loss: 1.2219 | lr: 1.08e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 160994 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  324 | Ep  1286 | reward:    107.0 | mean(100):    146.4 | actor_loss: -0.0014 | value_loss: 2.4101 | lr: 1.08e-04
  Update  325 | Ep  1288 | reward:    245.7 | mean(100):    148.9 | actor_loss: -0.0007 | value_loss: 1.1168 | lr: 1.07e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 205320 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  326 | Ep  1292 | reward:    221.2 | mean(100):    148.7 | actor_loss: -0.0052 | value_loss: 3.3595 | lr: 1.07e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6244 | mean p(bad) before update=0.4425
  Update  327 | Ep  1296 | reward:    215.8 | mean(100):    148.2 | actor_loss: -0.0047 | value_loss: 4.0122 | lr: 1.06e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 155028 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  328 | Ep  1299 | reward:    252.2 | mean(100):    146.6 | actor_loss: -0.0037 | value_loss: 2.7635 | lr: 1.06e-04
  Update  329 | Ep  1303 | reward:    227.4 | mean(100):    145.7 | actor_loss: -0.0015 | value_loss: 2.7839 | lr: 1.05e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 131341 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  330 | Ep  1307 | reward:    161.2 | mean(100):    148.5 | actor_loss: -0.0008 | value_loss: 2.7187 | lr: 1.05e-04
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8025 | mean p(bad) before update=0.4617

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  331 | Ep  1310 | reward:    145.9 | mean(100):    148.2 | actor_loss: -0.0014 | value_loss: 2.5895 | lr: 1.04e-04
  Update  332 | Ep  1313 | reward:    241.1 | mean(100):    150.3 | actor_loss: -0.0015 | value_loss: 1.9867 | lr: 1.03e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 166632 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5023 | mean p(bad) before update=0.3441

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  333 | Ep  1320 | reward:     31.2 | mean(100):    155.4 | actor_loss: -0.0099 | value_loss: 6.6176 | lr: 1.03e-04
  Update  334 | Ep  1322 | reward:    143.8 | mean(100):    155.6 | actor_loss: -0.0013 | value_loss: 0.3680 | lr: 1.02e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 241238 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  335 | Ep  1324 | reward:    147.4 | mean(100):    156.3 | actor_loss: -0.0024 | value_loss: 0.3565 | lr: 1.02e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  336 | Ep  1326 | reward:    234.6 | mean(100):    157.4 | actor_loss: -0.0006 | value_loss: 0.9521 | lr: 1.01e-04
  Update  337 | Ep  1328 | reward:    205.2 | mean(100):    158.0 | actor_loss: -0.0047 | value_loss: 1.4868 | lr: 1.01e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 156160 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  338 | Ep  1330 | reward:    157.9 | mean(100):    158.7 | actor_loss: -0.0012 | value_loss: 1.0339 | lr: 1.01e-04
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 152359 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  339 | Ep  1335 | reward:    233.0 | mean(100):    158.5 | actor_loss: -0.0010 | value_loss: 4.0030 | lr: 1.00e-04
  Update  340 | Ep  1338 | reward:    165.2 | mean(100):    157.5 | actor_loss: -0.0088 | value_loss: 2.3972 | lr: 9.97e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 153738 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  341 | Ep  1340 | reward:    228.6 | mean(100):    159.8 | actor_loss: -0.0012 | value_loss: 1.0522 | lr: 9.93e-05
  Update  342 | Ep  1342 | reward:    131.2 | mean(100):    160.1 | actor_loss: -0.0017 | value_loss: 1.3755 | lr: 9.90e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9137 | mean p(bad) before update=0.5051
  Update  343 | Ep  1346 | reward:    137.6 | mean(100):    161.0 | actor_loss: -0.0013 | value_loss: 2.9627 | lr: 9.87e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 160181 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  344 | Ep  1350 | reward:    192.3 | mean(100):    160.3 | actor_loss: -0.0065 | value_loss: 3.8358 | lr: 9.81e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=2.1295 | mean p(bad) before update=0.7724
  Update  345 | Ep  1355 | reward:    230.8 | mean(100):    160.3 | actor_loss: -0.0016 | value_loss: 4.5096 | lr: 9.75e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9633 | mean p(bad) before update=0.4335

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  346 | Ep  1360 | reward:    235.5 | mean(100):    161.4 | actor_loss: -0.0018 | value_loss: 3.5170 | lr: 9.67e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8900 | mean p(bad) before update=0.4754
  Update  347 | Ep  1365 | reward:     21.9 | mean(100):    162.5 | actor_loss: -0.0035 | value_loss: 4.2571 | lr: 9.60e-05
  Update  348 | Ep  1367 | reward:    133.7 | mean(100):    163.6 | actor_loss: -0.0034 | value_loss: 1.3816 | lr: 9.52e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 194967 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  349 | Ep  1369 | reward:    165.1 | mean(100):    165.3 | actor_loss: -0.0049 | value_loss: 0.3910 | lr: 9.49e-05
  Update  350 | Ep  1372 | reward:    211.4 | mean(100):    165.3 | actor_loss: -0.0007 | value_loss: 2.0221 | lr: 9.46e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 201204 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  351 | Ep  1374 | reward:    110.7 | mean(100):    164.7 | actor_loss: -0.0049 | value_loss: 1.3381 | lr: 9.42e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  Update  352 | Ep  1376 | reward:    126.2 | mean(100):    164.3 | actor_loss: -0.0014 | value_loss: 1.3478 | lr: 9.39e-05
  Update  353 | Ep  1378 | reward:    171.0 | mean(100):    166.2 | actor_loss: -0.0054 | value_loss: 0.3591 | lr: 9.36e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 245154 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  354 | Ep  1380 | reward:    137.0 | mean(100):    168.1 | actor_loss: -0.0037 | value_loss: 1.0449 | lr: 9.33e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 162538 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  355 | Ep  1384 | reward:     15.8 | mean(100):    165.6 | actor_loss: -0.0012 | value_loss: 4.2460 | lr: 9.30e-05
  Update  356 | Ep  1386 | reward:     26.3 | mean(100):    164.4 | actor_loss: -0.0054 | value_loss: 1.0754 | lr: 9.24e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 142463 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  357 | Ep  1389 | reward:    147.2 | mean(100):    160.8 | actor_loss: -0.0031 | value_loss: 2.3410 | lr: 9.21e-05
  Update  358 | Ep  1392 | reward:    246.1 | mean(100):    162.3 | actor_loss: -0.0017 | value_loss: 2.0811 | lr: 9.16e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 168314 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  359 | Ep  1394 | reward:    128.1 | mean(100):    163.4 | actor_loss: -0.0052 | value_loss: 1.3191 | lr: 9.12e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8997 | mean p(bad) before update=0.5100

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  360 | Ep  1399 | reward:    -16.5 | mean(100):    161.3 | actor_loss: -0.0019 | value_loss: 4.8285 | lr: 9.09e-05
  Update  361 | Ep  1401 | reward:    148.5 | mean(100):    160.6 | actor_loss: -0.0040 | value_loss: 0.7806 | lr: 9.01e-05
  Update  362 | Ep  1403 | reward:    107.0 | mean(100):    158.2 | actor_loss: -0.0049 | value_loss: 1.3954 | lr: 8.98e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 242619 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  363 | Ep  1405 | reward:    128.9 | mean(100):    156.6 | actor_loss: -0.0029 | value_loss: 0.4203 | lr: 8.95e-05
  Update  364 | Ep  1407 | reward:    138.2 | mean(100):    155.8 | actor_loss: -0.0018 | value_loss: 0.5321 | lr: 8.92e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 245843 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  365 | Ep  1411 | reward:    222.2 | mean(100):    159.4 | actor_loss: -0.0008 | value_loss: 2.8083 | lr: 8.89e-05
  Update  366 | Ep  1413 | reward:    150.8 | mean(100):    158.4 | actor_loss: -0.0074 | value_loss: 0.3496 | lr: 8.83e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 204268 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)
  Update  367 | Ep  1417 | reward:      7.8 | mean(100):    150.7 | actor_loss: -0.0059 | value_loss: 3.3990 | lr: 8.80e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8249 | mean p(bad) before update=0.4787

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  368 | Ep  1420 | reward:    185.4 | mean(100):    153.6 | actor_loss: -0.0025 | value_loss: 2.7790 | lr: 8.74e-05
  Update  369 | Ep  1422 | reward:      2.4 | mean(100):    152.2 | actor_loss: -0.0046 | value_loss: 1.4726 | lr: 8.70e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.4501 | mean p(bad) before update=0.5476
  Update  370 | Ep  1427 | reward:    217.8 | mean(100):    151.8 | actor_loss: -0.0026 | value_loss: 4.6926 | lr: 8.67e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 152172 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  371 | Ep  1430 | reward:    249.5 | mean(100):    152.9 | actor_loss: -0.0007 | value_loss: 2.8711 | lr: 8.59e-05
  Update  372 | Ep  1433 | reward:    162.0 | mean(100):    155.7 | actor_loss: -0.0001 | value_loss: 2.0510 | lr: 8.55e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7508 | mean p(bad) before update=0.3656
  Update  373 | Ep  1436 | reward:    268.1 | mean(100):    153.1 | actor_loss: -0.0056 | value_loss: 3.7589 | lr: 8.50e-05
  Update  374 | Ep  1438 | reward:    139.1 | mean(100):    155.7 | actor_loss: -0.0023 | value_loss: 1.5730 | lr: 8.46e-05
  [Analyzer failed: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 166930 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}] — skipping unlikelihood update this round
  [Analyzer] 5 episodes -> 0 bad pairs (skipped update)

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  375 | Ep  1443 | reward:    173.7 | mean(100):    154.9 | actor_loss: -0.0052 | value_loss: 4.9931 | lr: 8.43e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4562 | mean p(bad) before update=0.3226
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6237 | mean p(bad) before update=0.4248
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.6315 | mean p(bad) before update=0.4189

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  376 | Ep  1455 | reward:    -29.9 | mean(100):    147.9 | actor_loss: -0.0046 | value_loss: 11.7702 | lr: 8.35e-05
  Update  377 | Ep  1458 | reward:    147.5 | mean(100):    146.6 | actor_loss: -0.0016 | value_loss: 3.5389 | lr: 8.17e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.9597 | mean p(bad) before update=0.5440
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2135 | mean p(bad) before update=0.5644

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  378 | Ep  1466 | reward:    158.2 | mean(100):    135.8 | actor_loss: -0.0046 | value_loss: 7.2817 | lr: 8.13e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4227 | mean p(bad) before update=0.2803

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  379 | Ep  1473 | reward:    228.6 | mean(100):    137.7 | actor_loss: -0.0033 | value_loss: 6.0642 | lr: 8.01e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4244 | mean p(bad) before update=0.3098
  Update  380 | Ep  1478 | reward:    199.9 | mean(100):    138.1 | actor_loss: -0.0037 | value_loss: 5.2407 | lr: 7.90e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_llm.png
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.8134 | mean p(bad) before update=0.4645
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5744 | mean p(bad) before update=0.3662

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  381 | Ep  1484 | reward:     -2.7 | mean(100):    138.7 | actor_loss: -0.0036 | value_loss: 5.1571 | lr: 7.83e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.4642 | mean p(bad) before update=0.3067

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  382 | Ep  1492 | reward:    259.6 | mean(100):    144.9 | actor_loss: -0.0070 | value_loss: 7.8103 | lr: 7.74e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.7277 | mean p(bad) before update=0.4755
  Update  383 | Ep  1497 | reward:    200.6 | mean(100):    144.5 | actor_loss: -0.0020 | value_loss: 6.1921 | lr: 7.62e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0358 | mean p(bad) before update=0.4871

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  384 | Ep  1501 | reward:    245.0 | mean(100):    144.5 | actor_loss: -0.0044 | value_loss: 6.7272 | lr: 7.54e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.3973 | mean p(bad) before update=0.2918
  Update  385 | Ep  1507 | reward:    218.1 | mean(100):    150.7 | actor_loss: -0.0049 | value_loss: 4.9721 | lr: 7.49e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=0.5381 | mean p(bad) before update=0.3784

[AI Agent] Updating 10-point summary with new PPO episodes...
  Update  386 | Ep  1512 | reward:    274.6 | mean(100):    153.7 | actor_loss: -0.0009 | value_loss: 5.6983 | lr: 7.40e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.0280 | mean p(bad) before update=0.5184
  Update  387 | Ep  1518 | reward:    251.6 | mean(100):    160.4 | actor_loss: -0.0024 | value_loss: 4.4905 | lr: 7.32e-05
  [Analyzer] 5 episodes -> 10 bad pairs | unlikelihood_loss=1.2282 | mean p(bad) before update=0.5844

[AI Agent] Updating 10-point summary with new PPO episodes...
