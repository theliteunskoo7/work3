Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5

  Update   10 | Ep   180 | reward:     25.3 | mean(100):    -82.3 | actor_loss: -0.0100 | value_loss: 12.9843 | lr: 2.75e-04
  Update   20 | Ep   251 | reward:     24.8 | mean(100):    -28.4 | actor_loss: -0.0069 | value_loss: 4.9183 | lr: 2.63e-04
  Update   30 | Ep   271 | reward:     12.8 | mean(100):    -25.4 | actor_loss: -0.0061 | value_loss: 2.1246 | lr: 2.60e-04
  Update   40 | Ep   291 | reward:    -77.7 | mean(100):    -12.0 | actor_loss: -0.0100 | value_loss: 2.8225 | lr: 2.57e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   50 | Ep   313 | reward:      2.8 | mean(100):      0.9 | actor_loss: -0.0027 | value_loss: 1.5837 | lr: 2.53e-04
  Update   60 | Ep   337 | reward:    209.1 | mean(100):     33.3 | actor_loss: -0.0027 | value_loss: 5.7113 | lr: 2.50e-04
  Update   70 | Ep   378 | reward:    -44.7 | mean(100):    108.5 | actor_loss: -0.0039 | value_loss: 5.6952 | lr: 2.44e-04
  Update   80 | Ep   417 | reward:    -12.3 | mean(100):    155.9 | actor_loss: -0.0017 | value_loss: 5.9050 | lr: 2.38e-04
  Update   90 | Ep   465 | reward:    262.3 | mean(100):    165.4 | actor_loss: -0.0018 | value_loss: 6.6168 | lr: 2.31e-04
  Update  100 | Ep   520 | reward:     37.5 | mean(100):    173.3 | actor_loss: -0.0077 | value_loss: 8.4601 | lr: 2.23e-04
  Update  110 | Ep   586 | reward:    294.6 | mean(100):    195.0 | actor_loss: -0.0073 | value_loss: 9.4775 | lr: 2.13e-04

Solved at episode 623 (update 116) with mean 203.6!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
