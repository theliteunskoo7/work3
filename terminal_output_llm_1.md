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
