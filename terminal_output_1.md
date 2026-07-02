Using device: cpu (rollout collection stays on CPU; batched PPO update uses cpu)
Training PPO on CartPole-v1 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    88 | reward:     18.0 | mean(100):     23.2 | actor_loss: -0.0176 | value_loss: 7.9725 | lr: 3.00e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    2 | Ep   151 | reward:     25.0 | mean(100):     28.5 | actor_loss: -0.0193 | value_loss: 9.5573 | lr: 2.87e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    3 | Ep   194 | reward:     24.0 | mean(100):     38.7 | actor_loss: -0.0182 | value_loss: 10.9970 | lr: 2.77e-04
  Update    4 | Ep   211 | reward:     38.0 | mean(100):     53.0 | actor_loss: -0.0091 | value_loss: 13.5303 | lr: 2.71e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    5 | Ep   223 | reward:    288.0 | mean(100):     70.1 | actor_loss: -0.0058 | value_loss: 13.9788 | lr: 2.68e-04
  Update    6 | Ep   235 | reward:     79.0 | mean(100):     85.2 | actor_loss: -0.0066 | value_loss: 13.7342 | lr: 2.67e-04
  Update    7 | Ep   243 | reward:    293.0 | mean(100):    100.5 | actor_loss: 0.0007 | value_loss: 14.1362 | lr: 2.65e-04
  Update    8 | Ep   252 | reward:    219.0 | mean(100):    117.8 | actor_loss: -0.0000 | value_loss: 13.8665 | lr: 2.64e-04
  Update    9 | Ep   261 | reward:    327.0 | mean(100):    131.5 | actor_loss: -0.0031 | value_loss: 13.5689 | lr: 2.62e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   10 | Ep   268 | reward:    306.0 | mean(100):    147.3 | actor_loss: -0.0016 | value_loss: 13.6403 | lr: 2.61e-04
  Update   11 | Ep   274 | reward:    294.0 | mean(100):    162.8 | actor_loss: -0.0021 | value_loss: 13.5800 | lr: 2.60e-04
  Update   12 | Ep   282 | reward:    268.0 | mean(100):    179.5 | actor_loss: 0.0004 | value_loss: 13.0376 | lr: 2.59e-04
  Update   13 | Ep   289 | reward:    500.0 | mean(100):    195.5 | actor_loss: 0.0002 | value_loss: 12.9137 | lr: 2.58e-04
  Update   14 | Ep   295 | reward:    242.0 | mean(100):    208.7 | actor_loss: -0.0018 | value_loss: 12.8694 | lr: 2.57e-04
  Update   15 | Ep   299 | reward:    500.0 | mean(100):    220.8 | actor_loss: -0.0016 | value_loss: 12.9766 | lr: 2.56e-04
  Update   16 | Ep   304 | reward:    500.0 | mean(100):    236.2 | actor_loss: 0.0004 | value_loss: 12.6828 | lr: 2.55e-04
  Update   17 | Ep   309 | reward:    276.0 | mean(100):    248.0 | actor_loss: -0.0011 | value_loss: 12.4130 | lr: 2.54e-04
  Update   18 | Ep   317 | reward:    209.0 | mean(100):    256.4 | actor_loss: -0.0053 | value_loss: 11.8817 | lr: 2.54e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   19 | Ep   323 | reward:    245.0 | mean(100):    264.9 | actor_loss: -0.0044 | value_loss: 11.8662 | lr: 2.52e-04
  Update   20 | Ep   328 | reward:    183.0 | mean(100):    273.4 | actor_loss: -0.0058 | value_loss: 11.8061 | lr: 2.52e-04
  Update   21 | Ep   336 | reward:    182.0 | mean(100):    280.1 | actor_loss: -0.0002 | value_loss: 11.2724 | lr: 2.51e-04
  Update   22 | Ep   347 | reward:     66.0 | mean(100):    273.9 | actor_loss: -0.0062 | value_loss: 10.7710 | lr: 2.50e-04
  Update   23 | Ep   357 | reward:    170.0 | mean(100):    274.8 | actor_loss: -0.0015 | value_loss: 10.8245 | lr: 2.48e-04
  Update   24 | Ep   367 | reward:     25.0 | mean(100):    270.0 | actor_loss: 0.0001 | value_loss: 10.7579 | lr: 2.46e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   25 | Ep   377 | reward:    237.0 | mean(100):    259.2 | actor_loss: -0.0048 | value_loss: 10.6800 | lr: 2.45e-04
  Update   26 | Ep   385 | reward:    293.0 | mean(100):    261.0 | actor_loss: -0.0031 | value_loss: 10.6841 | lr: 2.43e-04
  Update   27 | Ep   393 | reward:    246.0 | mean(100):    255.8 | actor_loss: -0.0055 | value_loss: 10.5319 | lr: 2.42e-04
  Update   28 | Ep   402 | reward:    237.0 | mean(100):    239.8 | actor_loss: -0.0010 | value_loss: 10.3092 | lr: 2.41e-04
  Update   29 | Ep   413 | reward:    146.0 | mean(100):    221.2 | actor_loss: -0.0037 | value_loss: 10.0706 | lr: 2.40e-04
  Update   30 | Ep   422 | reward:    215.0 | mean(100):    214.9 | actor_loss: -0.0009 | value_loss: 10.1311 | lr: 2.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   31 | Ep   433 | reward:    201.0 | mean(100):    201.6 | actor_loss: -0.0029 | value_loss: 9.9445 | lr: 2.37e-04
  Update   32 | Ep   443 | reward:    185.0 | mean(100):    200.7 | actor_loss: -0.0014 | value_loss: 9.8986 | lr: 2.35e-04
  Update   33 | Ep   451 | reward:    367.0 | mean(100):    204.3 | actor_loss: -0.0005 | value_loss: 9.9066 | lr: 2.34e-04
  Update   34 | Ep   460 | reward:    192.0 | mean(100):    204.2 | actor_loss: -0.0027 | value_loss: 9.7411 | lr: 2.32e-04
  Update   35 | Ep   470 | reward:    178.0 | mean(100):    205.6 | actor_loss: -0.0005 | value_loss: 9.6167 | lr: 2.31e-04
  Update   36 | Ep   481 | reward:    214.0 | mean(100):    202.4 | actor_loss: -0.0024 | value_loss: 9.4841 | lr: 2.29e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   37 | Ep   494 | reward:    141.0 | mean(100):    189.6 | actor_loss: -0.0022 | value_loss: 9.3990 | lr: 2.28e-04
  Update   38 | Ep   507 | reward:    210.0 | mean(100):    183.9 | actor_loss: -0.0006 | value_loss: 9.4132 | lr: 2.26e-04
  Update   39 | Ep   519 | reward:    160.0 | mean(100):    181.4 | actor_loss: -0.0028 | value_loss: 9.3891 | lr: 2.24e-04
  Update   40 | Ep   527 | reward:    163.0 | mean(100):    184.9 | actor_loss: -0.0031 | value_loss: 9.3427 | lr: 2.22e-04
  Update   41 | Ep   540 | reward:    123.0 | mean(100):    181.2 | actor_loss: -0.0073 | value_loss: 9.1956 | lr: 2.21e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   42 | Ep   552 | reward:    139.0 | mean(100):    174.4 | actor_loss: -0.0005 | value_loss: 9.0401 | lr: 2.19e-04
  Update   43 | Ep   562 | reward:    170.0 | mean(100):    173.2 | actor_loss: -0.0030 | value_loss: 9.0633 | lr: 2.17e-04
  Update   44 | Ep   571 | reward:    165.0 | mean(100):    176.4 | actor_loss: -0.0018 | value_loss: 8.9815 | lr: 2.16e-04
  Update   45 | Ep   584 | reward:    177.0 | mean(100):    173.2 | actor_loss: -0.0015 | value_loss: 9.0136 | lr: 2.14e-04
  Update   46 | Ep   597 | reward:    128.0 | mean(100):    173.2 | actor_loss: -0.0067 | value_loss: 8.9505 | lr: 2.12e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   47 | Ep   609 | reward:    158.0 | mean(100):    173.4 | actor_loss: -0.0079 | value_loss: 8.7221 | lr: 2.10e-04
  Update   48 | Ep   620 | reward:    171.0 | mean(100):    173.6 | actor_loss: -0.0025 | value_loss: 8.1373 | lr: 2.09e-04
  Update   49 | Ep   632 | reward:    166.0 | mean(100):    168.1 | actor_loss: -0.0040 | value_loss: 8.3971 | lr: 2.07e-04
  Update   50 | Ep   641 | reward:    169.0 | mean(100):    173.3 | actor_loss: -0.0052 | value_loss: 8.1649 | lr: 2.05e-04
  Update   51 | Ep   651 | reward:    177.0 | mean(100):    176.8 | actor_loss: -0.0034 | value_loss: 7.7882 | lr: 2.04e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   52 | Ep   660 | reward:    161.0 | mean(100):    178.9 | actor_loss: -0.0017 | value_loss: 7.7015 | lr: 2.02e-04
  Update   53 | Ep   670 | reward:    166.0 | mean(100):    173.8 | actor_loss: -0.0020 | value_loss: 7.7606 | lr: 2.01e-04
  Update   54 | Ep   677 | reward:    204.0 | mean(100):    182.2 | actor_loss: -0.0031 | value_loss: 7.8189 | lr: 1.99e-04
  Update   55 | Ep   689 | reward:    186.0 | mean(100):    184.1 | actor_loss: -0.0054 | value_loss: 7.6825 | lr: 1.98e-04
  Update   56 | Ep   700 | reward:    191.0 | mean(100):    188.0 | actor_loss: -0.0035 | value_loss: 7.2513 | lr: 1.97e-04
  Update   57 | Ep   711 | reward:    178.0 | mean(100):    189.5 | actor_loss: -0.0006 | value_loss: 7.1123 | lr: 1.95e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   58 | Ep   723 | reward:    176.0 | mean(100):    190.1 | actor_loss: -0.0031 | value_loss: 6.8405 | lr: 1.93e-04
  Update   59 | Ep   737 | reward:    156.0 | mean(100):    183.6 | actor_loss: -0.0061 | value_loss: 7.0437 | lr: 1.92e-04
  Update   60 | Ep   749 | reward:    177.0 | mean(100):    180.3 | actor_loss: -0.0070 | value_loss: 6.4330 | lr: 1.89e-04
  Update   61 | Ep   759 | reward:    201.0 | mean(100):    181.1 | actor_loss: -0.0041 | value_loss: 5.5463 | lr: 1.88e-04
  Update   62 | Ep   769 | reward:    214.0 | mean(100):    181.4 | actor_loss: -0.0078 | value_loss: 5.9478 | lr: 1.86e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   63 | Ep   776 | reward:    265.0 | mean(100):    182.6 | actor_loss: -0.0111 | value_loss: 6.4865 | lr: 1.85e-04
  Update   64 | Ep   780 | reward:    500.0 | mean(100):    195.4 | actor_loss: -0.0027 | value_loss: 6.9229 | lr: 1.84e-04
  Update   65 | Ep   784 | reward:    500.0 | mean(100):    208.4 | actor_loss: -0.0016 | value_loss: 6.8434 | lr: 1.83e-04
  Update   66 | Ep   788 | reward:    500.0 | mean(100):    222.1 | actor_loss: -0.0009 | value_loss: 6.6672 | lr: 1.82e-04
  Update   67 | Ep   792 | reward:    500.0 | mean(100):    234.2 | actor_loss: -0.0010 | value_loss: 6.5975 | lr: 1.82e-04
  Update   68 | Ep   796 | reward:    500.0 | mean(100):    247.0 | actor_loss: -0.0011 | value_loss: 6.5265 | lr: 1.81e-04
  Update   69 | Ep   800 | reward:    500.0 | mean(100):    259.9 | actor_loss: -0.0002 | value_loss: 6.4736 | lr: 1.81e-04
  Update   70 | Ep   805 | reward:    500.0 | mean(100):    271.0 | actor_loss: -0.0054 | value_loss: 6.6636 | lr: 1.80e-04
  Update   71 | Ep   810 | reward:     46.0 | mean(100):    279.7 | actor_loss: -0.0028 | value_loss: 6.5633 | lr: 1.79e-04
  Update   72 | Ep   815 | reward:    500.0 | mean(100):    291.1 | actor_loss: -0.0006 | value_loss: 6.5058 | lr: 1.78e-04
  Update   73 | Ep   819 | reward:    500.0 | mean(100):    304.2 | actor_loss: -0.0009 | value_loss: 6.1328 | lr: 1.78e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   74 | Ep   823 | reward:    500.0 | mean(100):    317.7 | actor_loss: -0.0010 | value_loss: 6.0556 | lr: 1.77e-04
  Update   75 | Ep   827 | reward:    500.0 | mean(100):    330.9 | actor_loss: -0.0019 | value_loss: 5.9820 | lr: 1.77e-04
  Update   76 | Ep   831 | reward:    500.0 | mean(100):    340.8 | actor_loss: -0.0025 | value_loss: 5.9046 | lr: 1.76e-04
  Update   77 | Ep   835 | reward:    173.0 | mean(100):    352.6 | actor_loss: -0.0029 | value_loss: 5.8252 | lr: 1.75e-04
  Update   78 | Ep   839 | reward:    500.0 | mean(100):    367.1 | actor_loss: -0.0019 | value_loss: 5.7539 | lr: 1.75e-04
  Update   79 | Ep   843 | reward:    500.0 | mean(100):    378.0 | actor_loss: -0.0028 | value_loss: 5.6726 | lr: 1.74e-04
  Update   80 | Ep   847 | reward:    500.0 | mean(100):    391.1 | actor_loss: -0.0030 | value_loss: 5.5973 | lr: 1.74e-04
  Update   81 | Ep   851 | reward:    500.0 | mean(100):    402.9 | actor_loss: -0.0003 | value_loss: 5.5233 | lr: 1.73e-04
  Update   82 | Ep   855 | reward:    500.0 | mean(100):    414.9 | actor_loss: -0.0038 | value_loss: 5.4498 | lr: 1.72e-04
  Update   83 | Ep   859 | reward:    500.0 | mean(100):    426.7 | actor_loss: -0.0013 | value_loss: 5.3855 | lr: 1.72e-04
  Update   84 | Ep   863 | reward:    500.0 | mean(100):    437.5 | actor_loss: -0.0028 | value_loss: 5.3134 | lr: 1.71e-04
  Update   85 | Ep   867 | reward:    500.0 | mean(100):    450.5 | actor_loss: -0.0016 | value_loss: 5.2439 | lr: 1.71e-04
  Update   86 | Ep   871 | reward:    500.0 | mean(100):    462.1 | actor_loss: -0.0003 | value_loss: 5.1783 | lr: 1.70e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   87 | Ep   875 | reward:    500.0 | mean(100):    469.5 | actor_loss: 0.0001 | value_loss: 5.0697 | lr: 1.69e-04
  Update   88 | Ep   879 | reward:    500.0 | mean(100):    471.9 | actor_loss: -0.0023 | value_loss: 5.0195 | lr: 1.69e-04
  Update   89 | Ep   883 | reward:    500.0 | mean(100):    471.9 | actor_loss: 0.0002 | value_loss: 4.9551 | lr: 1.68e-04
  Update   90 | Ep   887 | reward:    500.0 | mean(100):    471.3 | actor_loss: 0.0005 | value_loss: 4.6663 | lr: 1.68e-04
  Update   91 | Ep   893 | reward:    154.0 | mean(100):    460.4 | actor_loss: -0.0038 | value_loss: 4.8373 | lr: 1.67e-04
  Update   92 | Ep   897 | reward:    500.0 | mean(100):    460.4 | actor_loss: -0.0017 | value_loss: 4.5362 | lr: 1.66e-04
  Update   93 | Ep   901 | reward:    500.0 | mean(100):    457.0 | actor_loss: -0.0006 | value_loss: 4.4235 | lr: 1.65e-04
  Update   94 | Ep   905 | reward:    500.0 | mean(100):    461.8 | actor_loss: -0.0018 | value_loss: 4.3726 | lr: 1.65e-04
  Update   95 | Ep   909 | reward:    500.0 | mean(100):    465.0 | actor_loss: -0.0009 | value_loss: 4.5417 | lr: 1.64e-04
  Update   96 | Ep   913 | reward:    500.0 | mean(100):    474.4 | actor_loss: -0.0010 | value_loss: 4.4789 | lr: 1.64e-04
  Update   97 | Ep   917 | reward:    431.0 | mean(100):    470.2 | actor_loss: -0.0017 | value_loss: 4.3955 | lr: 1.63e-04
  Update   98 | Ep   921 | reward:    500.0 | mean(100):    470.2 | actor_loss: -0.0017 | value_loss: 4.3468 | lr: 1.62e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   99 | Ep   925 | reward:    500.0 | mean(100):    470.2 | actor_loss: -0.0020 | value_loss: 4.2867 | lr: 1.62e-04
  Update  100 | Ep   929 | reward:    500.0 | mean(100):    470.7 | actor_loss: -0.0039 | value_loss: 4.2153 | lr: 1.61e-04
  Update  101 | Ep   933 | reward:    500.0 | mean(100):    469.9 | actor_loss: 0.0001 | value_loss: 4.1609 | lr: 1.61e-04
  Update  102 | Ep   937 | reward:    500.0 | mean(100):    471.9 | actor_loss: -0.0023 | value_loss: 3.9886 | lr: 1.60e-04
  Update  103 | Ep   941 | reward:    500.0 | mean(100):    475.5 | actor_loss: -0.0021 | value_loss: 4.0371 | lr: 1.59e-04

Solved at episode 941 (update 103) with mean 475.5!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
