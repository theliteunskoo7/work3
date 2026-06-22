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
