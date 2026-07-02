Using device: cpu (rollout collection stays on CPU; batched PPO update uses cpu)
Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    20 | reward:   -258.7 | mean(100):   -175.7 | actor_loss: -0.0087 | value_loss: 27.8440 | lr: 3.00e-04
  Update    2 | Ep    41 | reward:   -108.7 | mean(100):   -180.5 | actor_loss: -0.0106 | value_loss: 32.5799 | lr: 2.97e-04
  Update    3 | Ep    63 | reward:   -121.8 | mean(100):   -168.7 | actor_loss: -0.0072 | value_loss: 26.5438 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    4 | Ep    83 | reward:   -134.9 | mean(100):   -161.9 | actor_loss: -0.0073 | value_loss: 23.6018 | lr: 2.91e-04
  Update    5 | Ep   104 | reward:   -167.0 | mean(100):   -153.8 | actor_loss: -0.0043 | value_loss: 21.6543 | lr: 2.88e-04
  Update    6 | Ep   124 | reward:    -74.5 | mean(100):   -143.2 | actor_loss: -0.0081 | value_loss: 21.8150 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    7 | Ep   146 | reward:    -93.0 | mean(100):   -124.9 | actor_loss: -0.0057 | value_loss: 16.2625 | lr: 2.81e-04
  Update    8 | Ep   165 | reward:   -168.4 | mean(100):   -124.4 | actor_loss: -0.0077 | value_loss: 21.7588 | lr: 2.78e-04
  Update    9 | Ep   185 | reward:   -365.3 | mean(100):   -126.3 | actor_loss: -0.0049 | value_loss: 21.6962 | lr: 2.75e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   10 | Ep   205 | reward:    -88.6 | mean(100):   -118.6 | actor_loss: -0.0155 | value_loss: 17.8004 | lr: 2.72e-04
  Update   11 | Ep   225 | reward:   -159.1 | mean(100):   -117.2 | actor_loss: -0.0061 | value_loss: 17.6811 | lr: 2.69e-04
  Update   12 | Ep   245 | reward:     19.2 | mean(100):   -116.4 | actor_loss: -0.0062 | value_loss: 15.4066 | lr: 2.66e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   13 | Ep   265 | reward:   -174.7 | mean(100):   -110.3 | actor_loss: -0.0062 | value_loss: 19.2004 | lr: 2.63e-04
  Update   14 | Ep   283 | reward:    -48.0 | mean(100):   -101.7 | actor_loss: -0.0046 | value_loss: 14.8149 | lr: 2.60e-04
  Update   15 | Ep   300 | reward:    -80.9 | mean(100):    -92.2 | actor_loss: -0.0080 | value_loss: 13.7969 | lr: 2.58e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   16 | Ep   313 | reward:    -29.9 | mean(100):    -95.2 | actor_loss: -0.0064 | value_loss: 14.7599 | lr: 2.55e-04
  Update   17 | Ep   326 | reward:   -103.5 | mean(100):    -86.8 | actor_loss: -0.0040 | value_loss: 11.5971 | lr: 2.53e-04
  Update   18 | Ep   341 | reward:   -143.4 | mean(100):    -82.7 | actor_loss: -0.0062 | value_loss: 13.9470 | lr: 2.51e-04
  Update   19 | Ep   355 | reward:      1.5 | mean(100):    -88.4 | actor_loss: -0.0023 | value_loss: 17.3743 | lr: 2.49e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   20 | Ep   367 | reward:   -127.7 | mean(100):    -83.1 | actor_loss: -0.0082 | value_loss: 12.0785 | lr: 2.47e-04
  Update   21 | Ep   379 | reward:    -27.9 | mean(100):    -78.6 | actor_loss: -0.0081 | value_loss: 10.9197 | lr: 2.45e-04
  Update   22 | Ep   392 | reward:    -48.4 | mean(100):    -75.1 | actor_loss: -0.0073 | value_loss: 10.5723 | lr: 2.43e-04
  Update   23 | Ep   398 | reward:   -220.7 | mean(100):    -75.7 | actor_loss: -0.0064 | value_loss: 10.2310 | lr: 2.41e-04
  Update   24 | Ep   409 | reward:    -57.8 | mean(100):    -71.0 | actor_loss: -0.0084 | value_loss: 11.8151 | lr: 2.40e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   25 | Ep   417 | reward:    -36.9 | mean(100):    -67.3 | actor_loss: -0.0034 | value_loss: 8.0707 | lr: 2.39e-04
  Update   26 | Ep   428 | reward:    -34.1 | mean(100):    -62.7 | actor_loss: -0.0086 | value_loss: 8.4626 | lr: 2.37e-04
  Update   27 | Ep   435 | reward:     -2.0 | mean(100):    -62.1 | actor_loss: -0.0075 | value_loss: 9.1529 | lr: 2.36e-04
  Update   28 | Ep   442 | reward:    -23.2 | mean(100):    -53.5 | actor_loss: -0.0073 | value_loss: 9.0588 | lr: 2.35e-04
  Update   29 | Ep   450 | reward:   -106.4 | mean(100):    -46.5 | actor_loss: -0.0039 | value_loss: 8.5987 | lr: 2.34e-04
  Update   30 | Ep   454 | reward:    -34.4 | mean(100):    -43.7 | actor_loss: -0.0061 | value_loss: 7.4545 | lr: 2.32e-04
  Update   31 | Ep   461 | reward:     -9.8 | mean(100):    -44.1 | actor_loss: -0.0076 | value_loss: 8.9337 | lr: 2.32e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   32 | Ep   468 | reward:     -8.3 | mean(100):    -42.7 | actor_loss: -0.0064 | value_loss: 8.8328 | lr: 2.31e-04
  Update   33 | Ep   470 | reward:     72.2 | mean(100):    -41.4 | actor_loss: -0.0073 | value_loss: 5.4107 | lr: 2.30e-04
  Update   34 | Ep   474 | reward:     79.0 | mean(100):    -36.8 | actor_loss: -0.0054 | value_loss: 6.5470 | lr: 2.29e-04
  Update   35 | Ep   479 | reward:    -13.8 | mean(100):    -34.9 | actor_loss: -0.0096 | value_loss: 6.5163 | lr: 2.29e-04
  Update   36 | Ep   481 | reward:     52.5 | mean(100):    -32.6 | actor_loss: -0.0092 | value_loss: 4.5292 | lr: 2.28e-04
  Update   37 | Ep   485 | reward:    -35.6 | mean(100):    -30.5 | actor_loss: -0.0108 | value_loss: 6.5784 | lr: 2.28e-04
  Update   38 | Ep   487 | reward:     30.9 | mean(100):    -28.3 | actor_loss: -0.0057 | value_loss: 4.3535 | lr: 2.27e-04
  Update   39 | Ep   490 | reward:    132.2 | mean(100):    -28.2 | actor_loss: -0.0032 | value_loss: 5.9363 | lr: 2.27e-04
  Update   40 | Ep   492 | reward:     89.5 | mean(100):    -27.0 | actor_loss: -0.0051 | value_loss: 5.1133 | lr: 2.26e-04
  Update   41 | Ep   494 | reward:     28.6 | mean(100):    -24.8 | actor_loss: -0.0038 | value_loss: 4.7653 | lr: 2.26e-04
  Update   42 | Ep   496 | reward:     39.5 | mean(100):    -21.5 | actor_loss: -0.0057 | value_loss: 4.7698 | lr: 2.26e-04
  Update   43 | Ep   498 | reward:   -119.7 | mean(100):    -19.4 | actor_loss: -0.0055 | value_loss: 4.3695 | lr: 2.26e-04
  Update   44 | Ep   500 | reward:     34.1 | mean(100):    -19.8 | actor_loss: -0.0143 | value_loss: 4.5977 | lr: 2.25e-04
  Update   45 | Ep   502 | reward:     22.8 | mean(100):    -16.8 | actor_loss: -0.0071 | value_loss: 2.9374 | lr: 2.25e-04
  Update   46 | Ep   504 | reward:    -76.5 | mean(100):    -15.8 | actor_loss: -0.0077 | value_loss: 3.2184 | lr: 2.25e-04
  Update   47 | Ep   507 | reward:    137.2 | mean(100):    -14.3 | actor_loss: -0.0069 | value_loss: 6.5096 | lr: 2.24e-04
  Update   48 | Ep   509 | reward:   -173.0 | mean(100):    -15.9 | actor_loss: -0.0046 | value_loss: 3.6136 | lr: 2.24e-04
  Update   49 | Ep   511 | reward:   -225.4 | mean(100):    -17.8 | actor_loss: -0.0077 | value_loss: 4.0316 | lr: 2.24e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   50 | Ep   513 | reward:    -28.0 | mean(100):    -16.6 | actor_loss: -0.0044 | value_loss: 3.1604 | lr: 2.23e-04
  Update   51 | Ep   515 | reward:   -122.6 | mean(100):    -18.8 | actor_loss: -0.0010 | value_loss: 3.4393 | lr: 2.23e-04
  Update   52 | Ep   517 | reward:     94.4 | mean(100):    -16.8 | actor_loss: -0.0054 | value_loss: 3.9897 | lr: 2.23e-04
  Update   53 | Ep   519 | reward:     83.7 | mean(100):    -17.4 | actor_loss: 0.0006 | value_loss: 3.2271 | lr: 2.22e-04
  Update   54 | Ep   521 | reward:    -97.1 | mean(100):    -17.8 | actor_loss: -0.0027 | value_loss: 2.9176 | lr: 2.22e-04
  Update   55 | Ep   523 | reward:     90.3 | mean(100):    -16.3 | actor_loss: -0.0063 | value_loss: 2.6699 | lr: 2.22e-04
  Update   56 | Ep   525 | reward:   -111.1 | mean(100):    -15.4 | actor_loss: -0.0027 | value_loss: 3.9509 | lr: 2.22e-04
  Update   57 | Ep   528 | reward:    -61.9 | mean(100):    -15.0 | actor_loss: -0.0034 | value_loss: 3.7820 | lr: 2.21e-04
  Update   58 | Ep   530 | reward:      4.4 | mean(100):    -15.0 | actor_loss: -0.0018 | value_loss: 3.5639 | lr: 2.21e-04
  Update   59 | Ep   532 | reward:     11.5 | mean(100):    -13.3 | actor_loss: -0.0035 | value_loss: 2.8445 | lr: 2.20e-04
  Update   60 | Ep   534 | reward:    136.2 | mean(100):    -11.5 | actor_loss: -0.0046 | value_loss: 3.4248 | lr: 2.20e-04
  Update   61 | Ep   536 | reward:     98.3 | mean(100):     -9.0 | actor_loss: -0.0012 | value_loss: 2.6500 | lr: 2.20e-04
  Update   62 | Ep   538 | reward:     51.7 | mean(100):     -6.4 | actor_loss: -0.0070 | value_loss: 2.7864 | lr: 2.20e-04
  Update   63 | Ep   540 | reward:    120.7 | mean(100):     -3.8 | actor_loss: -0.0017 | value_loss: 2.8191 | lr: 2.19e-04
  Update   64 | Ep   542 | reward:   -241.1 | mean(100):     -7.0 | actor_loss: -0.0089 | value_loss: 3.5194 | lr: 2.19e-04
  Update   65 | Ep   544 | reward:    117.7 | mean(100):     -4.3 | actor_loss: -0.0043 | value_loss: 3.4282 | lr: 2.19e-04
  Update   66 | Ep   546 | reward:     89.2 | mean(100):     -3.8 | actor_loss: -0.0078 | value_loss: 3.3975 | lr: 2.18e-04
  Update   67 | Ep   548 | reward:     48.6 | mean(100):     -2.5 | actor_loss: -0.0060 | value_loss: 2.2374 | lr: 2.18e-04
  Update   68 | Ep   550 | reward:    157.6 | mean(100):      0.7 | actor_loss: -0.0054 | value_loss: 3.0560 | lr: 2.18e-04
  Update   69 | Ep   552 | reward:     56.1 | mean(100):     -0.6 | actor_loss: -0.0048 | value_loss: 3.0026 | lr: 2.17e-04
  Update   70 | Ep   555 | reward:   -131.7 | mean(100):      1.1 | actor_loss: -0.0057 | value_loss: 5.5237 | lr: 2.17e-04
  Update   71 | Ep   558 | reward:   -127.3 | mean(100):      2.3 | actor_loss: -0.0045 | value_loss: 3.6151 | lr: 2.17e-04
  Update   72 | Ep   560 | reward:     58.5 | mean(100):      5.1 | actor_loss: -0.0035 | value_loss: 3.4730 | lr: 2.16e-04
  Update   73 | Ep   564 | reward:   -108.0 | mean(100):      1.7 | actor_loss: -0.0062 | value_loss: 6.1391 | lr: 2.16e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   74 | Ep   567 | reward:    134.9 | mean(100):      4.1 | actor_loss: -0.0024 | value_loss: 3.9669 | lr: 2.15e-04
  Update   75 | Ep   569 | reward:    -72.8 | mean(100):      4.7 | actor_loss: -0.0004 | value_loss: 3.0027 | lr: 2.15e-04
  Update   76 | Ep   571 | reward:   -122.1 | mean(100):      3.2 | actor_loss: -0.0060 | value_loss: 3.1012 | lr: 2.15e-04
  Update   77 | Ep   575 | reward:    -54.6 | mean(100):      1.0 | actor_loss: -0.0047 | value_loss: 4.7348 | lr: 2.14e-04
  Update   78 | Ep   577 | reward:    142.8 | mean(100):      2.0 | actor_loss: -0.0028 | value_loss: 3.0942 | lr: 2.14e-04
  Update   79 | Ep   580 | reward:    160.4 | mean(100):      2.5 | actor_loss: -0.0052 | value_loss: 5.7338 | lr: 2.13e-04
  Update   80 | Ep   583 | reward:     94.8 | mean(100):      2.5 | actor_loss: -0.0032 | value_loss: 6.3433 | lr: 2.13e-04
  Update   81 | Ep   585 | reward:    145.5 | mean(100):      4.2 | actor_loss: -0.0019 | value_loss: 4.0717 | lr: 2.13e-04
  Update   82 | Ep   588 | reward:     63.9 | mean(100):      5.8 | actor_loss: -0.0029 | value_loss: 4.0963 | lr: 2.12e-04
  Update   83 | Ep   590 | reward:     87.2 | mean(100):      7.6 | actor_loss: -0.0033 | value_loss: 2.9827 | lr: 2.12e-04
  Update   84 | Ep   593 | reward:    124.0 | mean(100):      9.5 | actor_loss: -0.0031 | value_loss: 4.7218 | lr: 2.11e-04
  Update   85 | Ep   597 | reward:    -20.9 | mean(100):      7.7 | actor_loss: -0.0039 | value_loss: 5.6264 | lr: 2.11e-04
  Update   86 | Ep   602 | reward:    176.2 | mean(100):     10.4 | actor_loss: -0.0038 | value_loss: 6.9146 | lr: 2.10e-04
  Update   87 | Ep   604 | reward:    193.5 | mean(100):     13.1 | actor_loss: -0.0011 | value_loss: 2.8678 | lr: 2.10e-04
  Update   88 | Ep   607 | reward:   -103.0 | mean(100):     13.9 | actor_loss: -0.0034 | value_loss: 5.0543 | lr: 2.09e-04
  Update   89 | Ep   609 | reward:    138.4 | mean(100):     19.3 | actor_loss: -0.0022 | value_loss: 3.5716 | lr: 2.09e-04
  Update   90 | Ep   611 | reward:    140.6 | mean(100):     24.3 | actor_loss: -0.0031 | value_loss: 3.4309 | lr: 2.09e-04
  Update   91 | Ep   613 | reward:     67.4 | mean(100):     24.3 | actor_loss: -0.0027 | value_loss: 2.5771 | lr: 2.08e-04
  Update   92 | Ep   615 | reward:    203.1 | mean(100):     28.8 | actor_loss: -0.0021 | value_loss: 3.6813 | lr: 2.08e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   93 | Ep   620 | reward:    117.6 | mean(100):     33.2 | actor_loss: -0.0023 | value_loss: 6.9744 | lr: 2.08e-04
  Update   94 | Ep   623 | reward:    -47.4 | mean(100):     34.1 | actor_loss: -0.0058 | value_loss: 5.6763 | lr: 2.07e-04
  Update   95 | Ep   625 | reward:    -54.3 | mean(100):     34.0 | actor_loss: -0.0071 | value_loss: 2.8867 | lr: 2.07e-04
  Update   96 | Ep   628 | reward:    129.9 | mean(100):     37.4 | actor_loss: -0.0037 | value_loss: 5.0804 | lr: 2.06e-04
  Update   97 | Ep   631 | reward:    172.8 | mean(100):     42.6 | actor_loss: -0.0099 | value_loss: 5.6447 | lr: 2.06e-04
  Update   98 | Ep   633 | reward:    199.8 | mean(100):     45.5 | actor_loss: -0.0025 | value_loss: 4.8529 | lr: 2.05e-04
  Update   99 | Ep   636 | reward:    -66.2 | mean(100):     43.2 | actor_loss: -0.0009 | value_loss: 5.8880 | lr: 2.05e-04
  Update  100 | Ep   638 | reward:     98.0 | mean(100):     43.2 | actor_loss: -0.0015 | value_loss: 1.6382 | lr: 2.05e-04
  Update  101 | Ep   642 | reward:    -64.5 | mean(100):     45.9 | actor_loss: -0.0043 | value_loss: 4.7747 | lr: 2.04e-04
  Update  102 | Ep   645 | reward:    160.0 | mean(100):     46.0 | actor_loss: -0.0011 | value_loss: 3.2087 | lr: 2.04e-04
  Update  103 | Ep   648 | reward:    134.8 | mean(100):     45.9 | actor_loss: -0.0025 | value_loss: 4.4326 | lr: 2.03e-04
  Update  104 | Ep   651 | reward:    116.1 | mean(100):     46.5 | actor_loss: -0.0026 | value_loss: 4.3245 | lr: 2.03e-04
  Update  105 | Ep   653 | reward:    -48.5 | mean(100):     44.4 | actor_loss: -0.0049 | value_loss: 2.2965 | lr: 2.02e-04
  Update  106 | Ep   657 | reward:    -40.0 | mean(100):     47.3 | actor_loss: -0.0069 | value_loss: 4.8182 | lr: 2.02e-04
  Update  107 | Ep   659 | reward:    -62.3 | mean(100):     47.1 | actor_loss: -0.0066 | value_loss: 2.8046 | lr: 2.01e-04
  Update  108 | Ep   661 | reward:     61.3 | mean(100):     49.6 | actor_loss: -0.0072 | value_loss: 1.6712 | lr: 2.01e-04
  Update  109 | Ep   664 | reward:    128.0 | mean(100):     55.1 | actor_loss: -0.0009 | value_loss: 3.9160 | lr: 2.01e-04
  Update  110 | Ep   670 | reward:    184.1 | mean(100):     53.3 | actor_loss: -0.0030 | value_loss: 7.4084 | lr: 2.00e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  111 | Ep   673 | reward:    -82.6 | mean(100):     53.9 | actor_loss: -0.0064 | value_loss: 3.3631 | lr: 1.99e-04
  Update  112 | Ep   676 | reward:    -21.9 | mean(100):     55.0 | actor_loss: -0.0043 | value_loss: 3.1768 | lr: 1.99e-04
  Update  113 | Ep   680 | reward:    160.6 | mean(100):     56.6 | actor_loss: -0.0032 | value_loss: 4.4685 | lr: 1.99e-04
  Update  114 | Ep   683 | reward:    184.0 | mean(100):     59.6 | actor_loss: -0.0029 | value_loss: 5.5244 | lr: 1.98e-04
  Update  115 | Ep   685 | reward:    141.1 | mean(100):     60.8 | actor_loss: -0.0045 | value_loss: 1.8826 | lr: 1.98e-04
  Update  116 | Ep   687 | reward:    114.4 | mean(100):     62.8 | actor_loss: -0.0021 | value_loss: 3.2757 | lr: 1.97e-04
  Update  117 | Ep   690 | reward:    -61.9 | mean(100):     59.3 | actor_loss: -0.0005 | value_loss: 3.0342 | lr: 1.97e-04
  Update  118 | Ep   693 | reward:    181.8 | mean(100):     61.1 | actor_loss: -0.0025 | value_loss: 4.1412 | lr: 1.96e-04
  Update  119 | Ep   697 | reward:    -94.3 | mean(100):     61.5 | actor_loss: -0.0032 | value_loss: 5.5072 | lr: 1.96e-04
  Update  120 | Ep   699 | reward:    129.5 | mean(100):     63.7 | actor_loss: -0.0067 | value_loss: 2.0356 | lr: 1.95e-04
  Update  121 | Ep   703 | reward:    129.4 | mean(100):     62.5 | actor_loss: -0.0055 | value_loss: 5.1891 | lr: 1.95e-04
  Update  122 | Ep   705 | reward:    124.6 | mean(100):     61.7 | actor_loss: -0.0049 | value_loss: 1.4094 | lr: 1.95e-04
  Update  123 | Ep   708 | reward:    -26.5 | mean(100):     63.9 | actor_loss: -0.0026 | value_loss: 4.3240 | lr: 1.94e-04
  Update  124 | Ep   712 | reward:    104.5 | mean(100):     62.9 | actor_loss: -0.0007 | value_loss: 3.7028 | lr: 1.94e-04
  Update  125 | Ep   714 | reward:     62.4 | mean(100):     63.2 | actor_loss: -0.0023 | value_loss: 1.3274 | lr: 1.93e-04
  Update  126 | Ep   716 | reward:    126.1 | mean(100):     62.1 | actor_loss: -0.0035 | value_loss: 1.1316 | lr: 1.93e-04
  Update  127 | Ep   718 | reward:    187.5 | mean(100):     62.0 | actor_loss: -0.0018 | value_loss: 2.7732 | lr: 1.93e-04
  Update  128 | Ep   721 | reward:    141.4 | mean(100):     64.6 | actor_loss: -0.0028 | value_loss: 3.0303 | lr: 1.92e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  129 | Ep   723 | reward:      8.2 | mean(100):     65.0 | actor_loss: -0.0077 | value_loss: 5.3793 | lr: 1.92e-04
  Update  130 | Ep   725 | reward:    116.7 | mean(100):     67.8 | actor_loss: -0.0023 | value_loss: 2.4384 | lr: 1.92e-04
  Update  131 | Ep   727 | reward:    -28.8 | mean(100):     67.3 | actor_loss: -0.0061 | value_loss: 2.0296 | lr: 1.91e-04
  Update  132 | Ep   730 | reward:    164.4 | mean(100):     67.4 | actor_loss: -0.0054 | value_loss: 3.6772 | lr: 1.91e-04
  Update  133 | Ep   733 | reward:     72.3 | mean(100):     66.4 | actor_loss: -0.0022 | value_loss: 3.6524 | lr: 1.90e-04
  Update  134 | Ep   736 | reward:     90.4 | mean(100):     68.3 | actor_loss: -0.0040 | value_loss: 5.5501 | lr: 1.90e-04
  Update  135 | Ep   738 | reward:    205.9 | mean(100):     69.9 | actor_loss: -0.0054 | value_loss: 2.1071 | lr: 1.90e-04
  Update  136 | Ep   740 | reward:    126.6 | mean(100):     72.9 | actor_loss: -0.0028 | value_loss: 2.9684 | lr: 1.89e-04
  Update  137 | Ep   742 | reward:     87.8 | mean(100):     73.5 | actor_loss: -0.0062 | value_loss: 1.7163 | lr: 1.89e-04
  Update  138 | Ep   746 | reward:    185.1 | mean(100):     77.3 | actor_loss: -0.0029 | value_loss: 4.3368 | lr: 1.89e-04
  Update  139 | Ep   748 | reward:    100.1 | mean(100):     76.3 | actor_loss: -0.0070 | value_loss: 2.8320 | lr: 1.88e-04
  Update  140 | Ep   751 | reward:    160.2 | mean(100):     77.3 | actor_loss: -0.0038 | value_loss: 3.8951 | lr: 1.88e-04
  Update  141 | Ep   755 | reward:    205.1 | mean(100):     82.2 | actor_loss: -0.0064 | value_loss: 5.2326 | lr: 1.87e-04
  Update  142 | Ep   757 | reward:    192.5 | mean(100):     83.9 | actor_loss: -0.0096 | value_loss: 2.2218 | lr: 1.87e-04
  Update  143 | Ep   761 | reward:    239.4 | mean(100):     87.9 | actor_loss: -0.0037 | value_loss: 5.9258 | lr: 1.86e-04
  Update  144 | Ep   764 | reward:    138.0 | mean(100):     90.4 | actor_loss: -0.0034 | value_loss: 3.5798 | lr: 1.86e-04
  Update  145 | Ep   768 | reward:    169.1 | mean(100):     97.6 | actor_loss: -0.0031 | value_loss: 4.1120 | lr: 1.85e-04
  Update  146 | Ep   771 | reward:    225.5 | mean(100):     98.2 | actor_loss: -0.0015 | value_loss: 4.1544 | lr: 1.85e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  147 | Ep   773 | reward:    101.2 | mean(100):    102.1 | actor_loss: -0.0038 | value_loss: 1.0272 | lr: 1.84e-04
  Update  148 | Ep   775 | reward:     96.6 | mean(100):    104.1 | actor_loss: -0.0053 | value_loss: 1.6115 | lr: 1.84e-04
  Update  149 | Ep   777 | reward:     99.3 | mean(100):    104.9 | actor_loss: -0.0018 | value_loss: 0.8092 | lr: 1.84e-04
  Update  150 | Ep   780 | reward:    220.2 | mean(100):    105.4 | actor_loss: -0.0011 | value_loss: 3.1793 | lr: 1.83e-04
  Update  151 | Ep   782 | reward:    130.1 | mean(100):    104.9 | actor_loss: -0.0071 | value_loss: 0.6948 | lr: 1.83e-04
  Update  152 | Ep   785 | reward:    193.5 | mean(100):    105.6 | actor_loss: -0.0003 | value_loss: 3.0221 | lr: 1.83e-04
  Update  153 | Ep   788 | reward:    142.8 | mean(100):    107.1 | actor_loss: -0.0021 | value_loss: 3.3534 | lr: 1.82e-04
  Update  154 | Ep   791 | reward:    214.4 | mean(100):    108.9 | actor_loss: -0.0053 | value_loss: 2.9858 | lr: 1.82e-04
  Update  155 | Ep   794 | reward:    181.7 | mean(100):    110.5 | actor_loss: -0.0015 | value_loss: 3.0298 | lr: 1.81e-04
  Update  156 | Ep   798 | reward:    214.3 | mean(100):    119.8 | actor_loss: -0.0011 | value_loss: 4.8226 | lr: 1.81e-04
  Update  157 | Ep   802 | reward:    213.2 | mean(100):    123.5 | actor_loss: -0.0040 | value_loss: 5.5535 | lr: 1.80e-04
  Update  158 | Ep   804 | reward:    128.9 | mean(100):    123.8 | actor_loss: -0.0043 | value_loss: 0.8347 | lr: 1.80e-04
  Update  159 | Ep   807 | reward:    211.0 | mean(100):    123.4 | actor_loss: 0.0003 | value_loss: 2.4558 | lr: 1.79e-04
  Update  160 | Ep   809 | reward:     98.7 | mean(100):    125.1 | actor_loss: -0.0030 | value_loss: 2.5782 | lr: 1.79e-04
  Update  161 | Ep   814 | reward:    135.5 | mean(100):    125.3 | actor_loss: -0.0018 | value_loss: 5.0119 | lr: 1.79e-04
  Update  162 | Ep   819 | reward:    -34.4 | mean(100):    122.8 | actor_loss: -0.0023 | value_loss: 4.5201 | lr: 1.78e-04
  Update  163 | Ep   821 | reward:    214.9 | mean(100):    125.6 | actor_loss: -0.0015 | value_loss: 1.8195 | lr: 1.77e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  164 | Ep   827 | reward:    232.9 | mean(100):    123.7 | actor_loss: -0.0031 | value_loss: 5.3690 | lr: 1.77e-04
  Update  165 | Ep   831 | reward:    228.2 | mean(100):    121.2 | actor_loss: -0.0067 | value_loss: 4.4202 | lr: 1.76e-04
  Update  166 | Ep   833 | reward:      1.6 | mean(100):    121.1 | actor_loss: -0.0023 | value_loss: 2.5068 | lr: 1.75e-04
  Update  167 | Ep   837 | reward:    195.4 | mean(100):    122.2 | actor_loss: -0.0047 | value_loss: 3.4337 | lr: 1.75e-04
  Update  168 | Ep   839 | reward:    153.4 | mean(100):    120.3 | actor_loss: -0.0012 | value_loss: 3.2017 | lr: 1.74e-04
  Update  169 | Ep   843 | reward:     16.4 | mean(100):    119.3 | actor_loss: -0.0045 | value_loss: 4.1171 | lr: 1.74e-04
  Update  170 | Ep   847 | reward:    -18.3 | mean(100):    118.3 | actor_loss: -0.0039 | value_loss: 4.0285 | lr: 1.74e-04
  Update  171 | Ep   851 | reward:    249.5 | mean(100):    119.6 | actor_loss: -0.0043 | value_loss: 3.5424 | lr: 1.73e-04
  Update  172 | Ep   853 | reward:    -18.6 | mean(100):    119.0 | actor_loss: -0.0036 | value_loss: 1.4783 | lr: 1.72e-04
  Update  173 | Ep   855 | reward:    148.8 | mean(100):    117.9 | actor_loss: -0.0055 | value_loss: 0.8797 | lr: 1.72e-04
  Update  174 | Ep   859 | reward:    211.0 | mean(100):    118.7 | actor_loss: -0.0025 | value_loss: 5.0354 | lr: 1.72e-04
  Update  175 | Ep   861 | reward:    117.0 | mean(100):    119.6 | actor_loss: -0.0021 | value_loss: 1.3998 | lr: 1.71e-04
  Update  176 | Ep   863 | reward:    116.0 | mean(100):    118.5 | actor_loss: -0.0062 | value_loss: 0.7463 | lr: 1.71e-04
  Update  177 | Ep   865 | reward:      0.0 | mean(100):    116.7 | actor_loss: -0.0076 | value_loss: 2.2239 | lr: 1.71e-04
  Update  178 | Ep   869 | reward:     25.3 | mean(100):    114.4 | actor_loss: -0.0051 | value_loss: 3.6881 | lr: 1.70e-04
  Update  179 | Ep   872 | reward:    227.0 | mean(100):    115.1 | actor_loss: -0.0023 | value_loss: 2.6174 | lr: 1.70e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  180 | Ep   875 | reward:    132.8 | mean(100):    115.0 | actor_loss: -0.0038 | value_loss: 3.0577 | lr: 1.69e-04
  Update  181 | Ep   881 | reward:    -22.0 | mean(100):    114.6 | actor_loss: -0.0052 | value_loss: 6.1555 | lr: 1.69e-04
  Update  182 | Ep   883 | reward:     85.6 | mean(100):    115.1 | actor_loss: -0.0012 | value_loss: 1.8045 | lr: 1.68e-04
  Update  183 | Ep   885 | reward:    121.7 | mean(100):    114.1 | actor_loss: -0.0028 | value_loss: 2.3282 | lr: 1.68e-04
  Update  184 | Ep   887 | reward:    131.7 | mean(100):    114.2 | actor_loss: -0.0053 | value_loss: 0.6121 | lr: 1.67e-04
  Update  185 | Ep   889 | reward:    133.1 | mean(100):    111.9 | actor_loss: -0.0070 | value_loss: 2.8641 | lr: 1.67e-04
  Update  186 | Ep   895 | reward:      1.1 | mean(100):    103.9 | actor_loss: -0.0063 | value_loss: 5.2579 | lr: 1.67e-04
  Update  187 | Ep   897 | reward:    125.6 | mean(100):    104.1 | actor_loss: -0.0006 | value_loss: 2.5331 | lr: 1.66e-04
  Update  188 | Ep   900 | reward:    -21.9 | mean(100):    101.6 | actor_loss: -0.0024 | value_loss: 2.8010 | lr: 1.65e-04
  Update  189 | Ep   902 | reward:    -22.1 | mean(100):     99.3 | actor_loss: -0.0059 | value_loss: 1.8495 | lr: 1.65e-04
  Update  190 | Ep   904 | reward:    116.0 | mean(100):     99.0 | actor_loss: -0.0034 | value_loss: 0.4254 | lr: 1.65e-04
  Update  191 | Ep   907 | reward:      0.1 | mean(100):     98.8 | actor_loss: -0.0019 | value_loss: 3.8332 | lr: 1.64e-04
  Update  192 | Ep   910 | reward:    112.6 | mean(100):    101.4 | actor_loss: -0.0021 | value_loss: 2.3754 | lr: 1.64e-04
  Update  193 | Ep   915 | reward:    141.9 | mean(100):    100.4 | actor_loss: -0.0037 | value_loss: 4.6210 | lr: 1.63e-04
  Update  194 | Ep   918 | reward:    207.7 | mean(100):    100.2 | actor_loss: -0.0028 | value_loss: 3.2175 | lr: 1.63e-04
  Update  195 | Ep   920 | reward:    146.0 | mean(100):    102.6 | actor_loss: -0.0009 | value_loss: 1.8643 | lr: 1.62e-04
  Update  196 | Ep   923 | reward:    118.9 | mean(100):    103.5 | actor_loss: -0.0062 | value_loss: 4.7410 | lr: 1.62e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  197 | Ep   925 | reward:    136.4 | mean(100):    104.6 | actor_loss: -0.0069 | value_loss: 2.3953 | lr: 1.62e-04
  Update  198 | Ep   927 | reward:    248.7 | mean(100):    104.3 | actor_loss: -0.0035 | value_loss: 2.0006 | lr: 1.61e-04
  Update  199 | Ep   929 | reward:    124.4 | mean(100):    106.6 | actor_loss: -0.0018 | value_loss: 0.6260 | lr: 1.61e-04
  Update  200 | Ep   931 | reward:     28.6 | mean(100):    105.1 | actor_loss: -0.0066 | value_loss: 2.6660 | lr: 1.61e-04
  Update  201 | Ep   934 | reward:    117.7 | mean(100):    106.5 | actor_loss: -0.0024 | value_loss: 3.9281 | lr: 1.60e-04
  Update  202 | Ep   936 | reward:      7.6 | mean(100):    106.8 | actor_loss: -0.0044 | value_loss: 2.2255 | lr: 1.60e-04
  Update  203 | Ep   938 | reward:    135.6 | mean(100):    107.5 | actor_loss: -0.0013 | value_loss: 1.7873 | lr: 1.60e-04
  Update  204 | Ep   941 | reward:    142.4 | mean(100):    105.1 | actor_loss: -0.0061 | value_loss: 2.7163 | lr: 1.59e-04
  Update  205 | Ep   947 | reward:      7.7 | mean(100):    106.8 | actor_loss: -0.0034 | value_loss: 5.6998 | lr: 1.59e-04
  Update  206 | Ep   949 | reward:     -3.1 | mean(100):    105.6 | actor_loss: -0.0035 | value_loss: 1.6687 | lr: 1.58e-04
  Update  207 | Ep   953 | reward:    212.5 | mean(100):    104.7 | actor_loss: -0.0056 | value_loss: 3.7033 | lr: 1.58e-04
  Update  208 | Ep   957 | reward:      3.4 | mean(100):    101.9 | actor_loss: -0.0071 | value_loss: 3.0664 | lr: 1.57e-04
  Update  209 | Ep   965 | reward:    -32.5 | mean(100):     92.2 | actor_loss: -0.0077 | value_loss: 7.8298 | lr: 1.56e-04
  Update  210 | Ep   970 | reward:    141.2 | mean(100):     92.1 | actor_loss: -0.0043 | value_loss: 5.0994 | lr: 1.55e-04
  Update  211 | Ep   975 | reward:    -35.8 | mean(100):     86.8 | actor_loss: -0.0035 | value_loss: 5.6787 | lr: 1.54e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  212 | Ep   980 | reward:     59.9 | mean(100):     82.6 | actor_loss: -0.0053 | value_loss: 3.9204 | lr: 1.54e-04
  Update  213 | Ep   993 | reward:     36.0 | mean(100):     74.5 | actor_loss: -0.0064 | value_loss: 12.5085 | lr: 1.53e-04
  Update  214 | Ep   998 | reward:    232.1 | mean(100):     72.9 | actor_loss: -0.0060 | value_loss: 5.1041 | lr: 1.51e-04
  Update  215 | Ep  1004 | reward:    -33.8 | mean(100):     68.6 | actor_loss: -0.0093 | value_loss: 5.5553 | lr: 1.50e-04
  Update  216 | Ep  1010 | reward:    -72.6 | mean(100):     62.6 | actor_loss: -0.0041 | value_loss: 6.1054 | lr: 1.49e-04
  Update  217 | Ep  1014 | reward:     -5.2 | mean(100):     64.2 | actor_loss: -0.0063 | value_loss: 3.5360 | lr: 1.48e-04
  Update  218 | Ep  1023 | reward:     18.6 | mean(100):     58.1 | actor_loss: -0.0043 | value_loss: 8.7445 | lr: 1.48e-04
  Update  219 | Ep  1027 | reward:    -14.9 | mean(100):     54.6 | actor_loss: -0.0049 | value_loss: 3.7923 | lr: 1.47e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  220 | Ep  1033 | reward:    -44.1 | mean(100):     48.4 | actor_loss: -0.0041 | value_loss: 4.9764 | lr: 1.46e-04
  Update  221 | Ep  1038 | reward:     -5.4 | mean(100):     42.4 | actor_loss: -0.0031 | value_loss: 4.0106 | lr: 1.45e-04
  Update  222 | Ep  1043 | reward:    -57.4 | mean(100):     39.3 | actor_loss: -0.0071 | value_loss: 5.1797 | lr: 1.44e-04
  Update  223 | Ep  1049 | reward:     -2.4 | mean(100):     40.5 | actor_loss: -0.0030 | value_loss: 6.3273 | lr: 1.44e-04
  Update  224 | Ep  1056 | reward:    -42.4 | mean(100):     36.7 | actor_loss: -0.0026 | value_loss: 4.9827 | lr: 1.43e-04
  Update  225 | Ep  1061 | reward:    135.7 | mean(100):     38.7 | actor_loss: -0.0050 | value_loss: 4.6942 | lr: 1.42e-04
  Update  226 | Ep  1066 | reward:    -26.4 | mean(100):     43.8 | actor_loss: -0.0039 | value_loss: 4.6417 | lr: 1.41e-04
  Update  227 | Ep  1070 | reward:   -108.8 | mean(100):     42.9 | actor_loss: -0.0033 | value_loss: 3.8382 | lr: 1.40e-04
  Update  228 | Ep  1075 | reward:    -23.4 | mean(100):     46.4 | actor_loss: -0.0024 | value_loss: 4.6940 | lr: 1.39e-04
  Update  229 | Ep  1078 | reward:      2.4 | mean(100):     48.1 | actor_loss: -0.0021 | value_loss: 2.4712 | lr: 1.39e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  230 | Ep  1081 | reward:    133.8 | mean(100):     50.6 | actor_loss: -0.0062 | value_loss: 2.6252 | lr: 1.38e-04
  Update  231 | Ep  1086 | reward:    -23.5 | mean(100):     55.0 | actor_loss: -0.0020 | value_loss: 4.9704 | lr: 1.38e-04
  Update  232 | Ep  1089 | reward:    -10.0 | mean(100):     54.0 | actor_loss: -0.0069 | value_loss: 2.1858 | lr: 1.37e-04
  Update  233 | Ep  1093 | reward:    202.7 | mean(100):     61.7 | actor_loss: -0.0017 | value_loss: 3.9854 | lr: 1.37e-04
  Update  234 | Ep  1101 | reward:    -79.2 | mean(100):     60.4 | actor_loss: -0.0047 | value_loss: 8.1448 | lr: 1.36e-04
  Update  235 | Ep  1103 | reward:    -15.1 | mean(100):     62.0 | actor_loss: -0.0043 | value_loss: 1.7440 | lr: 1.35e-04
  Update  236 | Ep  1109 | reward:    -12.1 | mean(100):     61.2 | actor_loss: -0.0068 | value_loss: 6.0712 | lr: 1.35e-04
  Update  237 | Ep  1115 | reward:      0.5 | mean(100):     59.3 | actor_loss: -0.0045 | value_loss: 5.2490 | lr: 1.34e-04
  Update  238 | Ep  1122 | reward:     30.3 | mean(100):     59.8 | actor_loss: -0.0033 | value_loss: 5.4113 | lr: 1.33e-04
  Update  239 | Ep  1127 | reward:    189.6 | mean(100):     65.4 | actor_loss: -0.0028 | value_loss: 4.8960 | lr: 1.32e-04
  Update  240 | Ep  1129 | reward:    129.7 | mean(100):     66.4 | actor_loss: -0.0032 | value_loss: 0.4703 | lr: 1.31e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  241 | Ep  1131 | reward:    117.8 | mean(100):     68.3 | actor_loss: -0.0076 | value_loss: 1.2236 | lr: 1.31e-04
  Update  242 | Ep  1133 | reward:    110.0 | mean(100):     71.3 | actor_loss: -0.0045 | value_loss: 0.3281 | lr: 1.30e-04
  Update  243 | Ep  1137 | reward:    -60.9 | mean(100):     70.6 | actor_loss: -0.0011 | value_loss: 3.4153 | lr: 1.30e-04
  Update  244 | Ep  1143 | reward:      3.3 | mean(100):     69.3 | actor_loss: -0.0052 | value_loss: 5.4019 | lr: 1.29e-04
  Update  245 | Ep  1145 | reward:    143.7 | mean(100):     68.2 | actor_loss: -0.0057 | value_loss: 2.0138 | lr: 1.29e-04
  Update  246 | Ep  1150 | reward:    -42.4 | mean(100):     67.0 | actor_loss: -0.0009 | value_loss: 3.3185 | lr: 1.28e-04
  Update  247 | Ep  1155 | reward:     -3.1 | mean(100):     67.7 | actor_loss: -0.0017 | value_loss: 3.5776 | lr: 1.28e-04
  Update  248 | Ep  1161 | reward:    -25.6 | mean(100):     65.6 | actor_loss: -0.0065 | value_loss: 5.1652 | lr: 1.27e-04
  Update  249 | Ep  1166 | reward:    190.4 | mean(100):     62.9 | actor_loss: -0.0040 | value_loss: 4.8453 | lr: 1.26e-04
  Update  250 | Ep  1170 | reward:     16.2 | mean(100):     61.5 | actor_loss: -0.0062 | value_loss: 3.1194 | lr: 1.25e-04
  Update  251 | Ep  1174 | reward:    -45.5 | mean(100):     57.5 | actor_loss: -0.0047 | value_loss: 3.1497 | lr: 1.24e-04
  Update  252 | Ep  1178 | reward:    -45.4 | mean(100):     55.7 | actor_loss: -0.0075 | value_loss: 2.2214 | lr: 1.24e-04
  Update  253 | Ep  1180 | reward:    134.1 | mean(100):     54.6 | actor_loss: -0.0056 | value_loss: 1.1337 | lr: 1.23e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  254 | Ep  1185 | reward:     17.1 | mean(100):     56.3 | actor_loss: -0.0037 | value_loss: 4.5970 | lr: 1.23e-04
  Update  255 | Ep  1190 | reward:    208.3 | mean(100):     58.9 | actor_loss: -0.0023 | value_loss: 4.2024 | lr: 1.22e-04
  Update  256 | Ep  1192 | reward:    116.8 | mean(100):     59.0 | actor_loss: -0.0015 | value_loss: 1.7719 | lr: 1.21e-04
  Update  257 | Ep  1196 | reward:    154.2 | mean(100):     61.3 | actor_loss: -0.0010 | value_loss: 3.2391 | lr: 1.21e-04
  Update  258 | Ep  1199 | reward:    141.0 | mean(100):     60.6 | actor_loss: -0.0035 | value_loss: 2.1021 | lr: 1.21e-04
  Update  259 | Ep  1204 | reward:    -19.7 | mean(100):     63.7 | actor_loss: -0.0041 | value_loss: 5.0967 | lr: 1.20e-04
  Update  260 | Ep  1209 | reward:    221.8 | mean(100):     64.3 | actor_loss: -0.0019 | value_loss: 3.7465 | lr: 1.19e-04
  Update  261 | Ep  1216 | reward:    -10.4 | mean(100):     64.7 | actor_loss: -0.0029 | value_loss: 4.6367 | lr: 1.19e-04
  Update  262 | Ep  1219 | reward:     26.2 | mean(100):     65.9 | actor_loss: -0.0026 | value_loss: 2.0014 | lr: 1.18e-04
  Update  263 | Ep  1225 | reward:    249.4 | mean(100):     66.6 | actor_loss: -0.0027 | value_loss: 4.2061 | lr: 1.17e-04
  Update  264 | Ep  1231 | reward:      7.4 | mean(100):     60.6 | actor_loss: -0.0058 | value_loss: 4.5324 | lr: 1.16e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  265 | Ep  1236 | reward:    256.3 | mean(100):     64.0 | actor_loss: -0.0022 | value_loss: 5.6140 | lr: 1.15e-04
  Update  266 | Ep  1239 | reward:     -2.5 | mean(100):     68.2 | actor_loss: -0.0032 | value_loss: 3.2156 | lr: 1.15e-04
  Update  267 | Ep  1241 | reward:    130.5 | mean(100):     69.4 | actor_loss: -0.0066 | value_loss: 2.9408 | lr: 1.14e-04
  Update  268 | Ep  1247 | reward:     17.0 | mean(100):     70.8 | actor_loss: -0.0082 | value_loss: 4.7328 | lr: 1.14e-04
  Update  269 | Ep  1254 | reward:    229.2 | mean(100):     72.3 | actor_loss: -0.0023 | value_loss: 7.8901 | lr: 1.13e-04
  Update  270 | Ep  1256 | reward:    132.0 | mean(100):     75.9 | actor_loss: -0.0004 | value_loss: 1.3504 | lr: 1.12e-04
  Update  271 | Ep  1261 | reward:    -71.3 | mean(100):     75.9 | actor_loss: -0.0067 | value_loss: 3.9713 | lr: 1.12e-04
  Update  272 | Ep  1265 | reward:    239.3 | mean(100):     81.8 | actor_loss: -0.0022 | value_loss: 3.4420 | lr: 1.11e-04
  Update  273 | Ep  1271 | reward:    245.8 | mean(100):     82.2 | actor_loss: -0.0043 | value_loss: 4.7565 | lr: 1.10e-04
  Update  274 | Ep  1276 | reward:    143.7 | mean(100):     86.1 | actor_loss: -0.0029 | value_loss: 5.1386 | lr: 1.09e-04
  Update  275 | Ep  1281 | reward:    146.9 | mean(100):     90.6 | actor_loss: -0.0038 | value_loss: 4.8863 | lr: 1.09e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  276 | Ep  1285 | reward:    156.6 | mean(100):     87.7 | actor_loss: -0.0036 | value_loss: 3.5008 | lr: 1.08e-04
  Update  277 | Ep  1288 | reward:    110.3 | mean(100):     86.7 | actor_loss: -0.0029 | value_loss: 2.4334 | lr: 1.07e-04
  Update  278 | Ep  1293 | reward:    196.7 | mean(100):     87.3 | actor_loss: -0.0029 | value_loss: 6.7119 | lr: 1.07e-04
  Update  279 | Ep  1295 | reward:    155.8 | mean(100):     88.4 | actor_loss: -0.0029 | value_loss: 0.5427 | lr: 1.06e-04
  Update  280 | Ep  1300 | reward:    213.5 | mean(100):     88.9 | actor_loss: -0.0009 | value_loss: 4.5952 | lr: 1.06e-04
  Update  281 | Ep  1303 | reward:    -37.1 | mean(100):     88.6 | actor_loss: -0.0012 | value_loss: 2.2798 | lr: 1.05e-04
  Update  282 | Ep  1307 | reward:    187.8 | mean(100):     93.5 | actor_loss: -0.0055 | value_loss: 4.0411 | lr: 1.05e-04
  Update  283 | Ep  1311 | reward:    233.0 | mean(100):     92.6 | actor_loss: -0.0080 | value_loss: 3.3424 | lr: 1.04e-04
  Update  284 | Ep  1316 | reward:    137.1 | mean(100):    100.7 | actor_loss: -0.0020 | value_loss: 6.8683 | lr: 1.03e-04
  Update  285 | Ep  1321 | reward:    206.9 | mean(100):    104.6 | actor_loss: -0.0042 | value_loss: 4.9959 | lr: 1.03e-04
  Update  286 | Ep  1326 | reward:    156.5 | mean(100):    104.5 | actor_loss: -0.0025 | value_loss: 5.4491 | lr: 1.02e-04
  Update  287 | Ep  1330 | reward:    205.5 | mean(100):    110.0 | actor_loss: -0.0012 | value_loss: 4.0202 | lr: 1.01e-04
  Update  288 | Ep  1333 | reward:     29.8 | mean(100):    113.2 | actor_loss: -0.0021 | value_loss: 3.8981 | lr: 1.00e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  289 | Ep  1335 | reward:    126.0 | mean(100):    112.3 | actor_loss: -0.0047 | value_loss: 0.5013 | lr: 1.00e-04
  Update  290 | Ep  1338 | reward:    199.7 | mean(100):    112.3 | actor_loss: -0.0007 | value_loss: 3.0964 | lr: 9.97e-05
  Update  291 | Ep  1340 | reward:    172.4 | mean(100):    114.4 | actor_loss: -0.0039 | value_loss: 0.9867 | lr: 9.93e-05
  Update  292 | Ep  1342 | reward:    133.7 | mean(100):    116.3 | actor_loss: -0.0019 | value_loss: 1.2898 | lr: 9.90e-05
  Update  293 | Ep  1344 | reward:    139.3 | mean(100):    114.3 | actor_loss: -0.0029 | value_loss: 0.8687 | lr: 9.87e-05
  Update  294 | Ep  1349 | reward:      8.7 | mean(100):    124.0 | actor_loss: -0.0022 | value_loss: 4.0554 | lr: 9.84e-05
  Update  295 | Ep  1351 | reward:    121.5 | mean(100):    123.8 | actor_loss: -0.0037 | value_loss: 0.4898 | lr: 9.76e-05
  Update  296 | Ep  1354 | reward:    132.8 | mean(100):    125.2 | actor_loss: -0.0078 | value_loss: 2.7876 | lr: 9.73e-05
  Update  297 | Ep  1357 | reward:    129.7 | mean(100):    123.7 | actor_loss: -0.0029 | value_loss: 4.0318 | lr: 9.69e-05
  Update  298 | Ep  1363 | reward:     32.4 | mean(100):    130.1 | actor_loss: -0.0029 | value_loss: 6.5872 | lr: 9.64e-05
  Update  299 | Ep  1365 | reward:     34.1 | mean(100):    128.4 | actor_loss: -0.0052 | value_loss: 1.3130 | lr: 9.55e-05
  Update  300 | Ep  1367 | reward:    176.6 | mean(100):    128.7 | actor_loss: -0.0056 | value_loss: 3.1348 | lr: 9.52e-05
  Update  301 | Ep  1369 | reward:    141.9 | mean(100):    131.7 | actor_loss: -0.0013 | value_loss: 0.3337 | lr: 9.49e-05
  Update  302 | Ep  1371 | reward:    138.7 | mean(100):    132.1 | actor_loss: -0.0073 | value_loss: 0.3213 | lr: 9.46e-05
  Update  303 | Ep  1373 | reward:    220.6 | mean(100):    131.1 | actor_loss: -0.0004 | value_loss: 1.5252 | lr: 9.43e-05
  Update  304 | Ep  1377 | reward:    260.7 | mean(100):    135.2 | actor_loss: -0.0054 | value_loss: 3.7131 | lr: 9.40e-05
  Update  305 | Ep  1384 | reward:     26.1 | mean(100):    142.1 | actor_loss: -0.0045 | value_loss: 7.6799 | lr: 9.34e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  306 | Ep  1387 | reward:    244.0 | mean(100):    146.3 | actor_loss: -0.0086 | value_loss: 2.2390 | lr: 9.24e-05
  Update  307 | Ep  1392 | reward:      4.0 | mean(100):    144.7 | actor_loss: -0.0032 | value_loss: 5.3814 | lr: 9.19e-05
  Update  308 | Ep  1396 | reward:    243.5 | mean(100):    143.9 | actor_loss: -0.0034 | value_loss: 3.8713 | lr: 9.12e-05
  Update  309 | Ep  1402 | reward:     17.5 | mean(100):    147.0 | actor_loss: -0.0029 | value_loss: 7.1439 | lr: 9.06e-05
  Update  310 | Ep  1406 | reward:    194.1 | mean(100):    152.3 | actor_loss: -0.0021 | value_loss: 5.8240 | lr: 8.97e-05
  Update  311 | Ep  1411 | reward:    203.7 | mean(100):    159.1 | actor_loss: -0.0028 | value_loss: 5.8095 | lr: 8.91e-05
  Update  312 | Ep  1414 | reward:    195.7 | mean(100):    159.3 | actor_loss: -0.0021 | value_loss: 1.9245 | lr: 8.83e-05
  Update  313 | Ep  1419 | reward:     -8.2 | mean(100):    162.6 | actor_loss: -0.0028 | value_loss: 5.8203 | lr: 8.79e-05
  Update  314 | Ep  1422 | reward:    231.0 | mean(100):    163.8 | actor_loss: -0.0028 | value_loss: 2.5874 | lr: 8.71e-05
  Update  315 | Ep  1427 | reward:    266.6 | mean(100):    165.5 | actor_loss: -0.0006 | value_loss: 4.2241 | lr: 8.67e-05
  Update  316 | Ep  1434 | reward:    262.3 | mean(100):    171.6 | actor_loss: -0.0019 | value_loss: 6.8653 | lr: 8.59e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  317 | Ep  1440 | reward:    229.3 | mean(100):    173.3 | actor_loss: -0.0023 | value_loss: 6.3216 | lr: 8.49e-05
  Update  318 | Ep  1446 | reward:    273.6 | mean(100):    178.7 | actor_loss: -0.0009 | value_loss: 6.9909 | lr: 8.40e-05
  Update  319 | Ep  1452 | reward:    216.5 | mean(100):    179.1 | actor_loss: -0.0037 | value_loss: 6.4703 | lr: 8.31e-05
  Update  320 | Ep  1458 | reward:    218.1 | mean(100):    187.1 | actor_loss: -0.0018 | value_loss: 6.4846 | lr: 8.22e-05
  Update  321 | Ep  1468 | reward:    212.8 | mean(100):    186.7 | actor_loss: -0.0027 | value_loss: 9.4194 | lr: 8.13e-05
  Update  322 | Ep  1474 | reward:     29.3 | mean(100):    186.1 | actor_loss: -0.0020 | value_loss: 5.2696 | lr: 7.98e-05
  Update  323 | Ep  1480 | reward:    246.8 | mean(100):    182.4 | actor_loss: -0.0025 | value_loss: 5.9953 | lr: 7.89e-05
  Update  324 | Ep  1485 | reward:    173.2 | mean(100):    184.5 | actor_loss: -0.0011 | value_loss: 5.1129 | lr: 7.80e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  325 | Ep  1490 | reward:    133.7 | mean(100):    187.8 | actor_loss: -0.0018 | value_loss: 5.0371 | lr: 7.72e-05
  Update  326 | Ep  1492 | reward:     64.9 | mean(100):    187.8 | actor_loss: -0.0031 | value_loss: 2.2821 | lr: 7.65e-05
  Update  327 | Ep  1500 | reward:     26.3 | mean(100):    185.5 | actor_loss: -0.0050 | value_loss: 8.9213 | lr: 7.62e-05
  Update  328 | Ep  1503 | reward:    131.4 | mean(100):    187.1 | actor_loss: -0.0020 | value_loss: 4.4395 | lr: 7.50e-05
  Update  329 | Ep  1509 | reward:    230.1 | mean(100):    185.8 | actor_loss: -0.0031 | value_loss: 7.2603 | lr: 7.46e-05
  Update  330 | Ep  1514 | reward:     -6.1 | mean(100):    181.2 | actor_loss: -0.0029 | value_loss: 4.1010 | lr: 7.37e-05
  Update  331 | Ep  1519 | reward:    116.4 | mean(100):    182.3 | actor_loss: -0.0016 | value_loss: 4.5052 | lr: 7.29e-05
  Update  332 | Ep  1521 | reward:    102.6 | mean(100):    181.9 | actor_loss: -0.0016 | value_loss: 2.2836 | lr: 7.22e-05
  Update  333 | Ep  1527 | reward:    253.5 | mean(100):    179.3 | actor_loss: -0.0036 | value_loss: 5.7222 | lr: 7.19e-05
  Update  334 | Ep  1532 | reward:    268.7 | mean(100):    179.3 | actor_loss: -0.0002 | value_loss: 4.2379 | lr: 7.10e-05
  Update  335 | Ep  1540 | reward:    232.1 | mean(100):    182.2 | actor_loss: -0.0016 | value_loss: 7.3402 | lr: 7.02e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  336 | Ep  1549 | reward:    256.6 | mean(100):    176.6 | actor_loss: -0.0016 | value_loss: 8.7924 | lr: 6.90e-05
  Update  337 | Ep  1554 | reward:    240.6 | mean(100):    178.6 | actor_loss: -0.0007 | value_loss: 4.6685 | lr: 6.77e-05
  Update  338 | Ep  1558 | reward:    247.6 | mean(100):    179.0 | actor_loss: -0.0011 | value_loss: 4.7079 | lr: 6.69e-05
  Update  339 | Ep  1566 | reward:    245.7 | mean(100):    182.9 | actor_loss: -0.0031 | value_loss: 8.2800 | lr: 6.63e-05
  Update  340 | Ep  1571 | reward:    243.2 | mean(100):    184.5 | actor_loss: -0.0013 | value_loss: 4.4415 | lr: 6.51e-05
  Update  341 | Ep  1576 | reward:    239.8 | mean(100):    186.9 | actor_loss: -0.0024 | value_loss: 4.5131 | lr: 6.44e-05
  Update  342 | Ep  1583 | reward:     14.2 | mean(100):    186.6 | actor_loss: -0.0059 | value_loss: 7.3180 | lr: 6.36e-05
  Update  343 | Ep  1588 | reward:    248.0 | mean(100):    185.8 | actor_loss: -0.0020 | value_loss: 4.2724 | lr: 6.26e-05
  Update  344 | Ep  1593 | reward:    258.4 | mean(100):    185.8 | actor_loss: -0.0008 | value_loss: 5.5981 | lr: 6.18e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  345 | Ep  1598 | reward:    273.4 | mean(100):    190.2 | actor_loss: -0.0020 | value_loss: 5.6990 | lr: 6.10e-05
  Update  346 | Ep  1606 | reward:    255.0 | mean(100):    192.4 | actor_loss: -0.0032 | value_loss: 8.5170 | lr: 6.03e-05
  Update  347 | Ep  1613 | reward:    249.8 | mean(100):    192.0 | actor_loss: -0.0026 | value_loss: 6.8493 | lr: 5.91e-05
  Update  348 | Ep  1617 | reward:     37.2 | mean(100):    190.7 | actor_loss: -0.0011 | value_loss: 5.0299 | lr: 5.80e-05
  Update  349 | Ep  1623 | reward:    261.6 | mean(100):    192.5 | actor_loss: -0.0025 | value_loss: 6.8480 | lr: 5.74e-05
  Update  350 | Ep  1628 | reward:    257.2 | mean(100):    193.4 | actor_loss: -0.0020 | value_loss: 5.9748 | lr: 5.65e-05
  Update  351 | Ep  1632 | reward:    231.8 | mean(100):    190.4 | actor_loss: -0.0037 | value_loss: 4.8899 | lr: 5.58e-05
  Update  352 | Ep  1637 | reward:    246.9 | mean(100):    186.3 | actor_loss: -0.0031 | value_loss: 4.8363 | lr: 5.52e-05
  Update  353 | Ep  1645 | reward:    278.3 | mean(100):    178.5 | actor_loss: -0.0034 | value_loss: 9.6761 | lr: 5.44e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  354 | Ep  1654 | reward:     35.3 | mean(100):    177.9 | actor_loss: -0.0025 | value_loss: 8.0393 | lr: 5.32e-05
  Update  355 | Ep  1661 | reward:    250.6 | mean(100):    177.7 | actor_loss: -0.0015 | value_loss: 7.1771 | lr: 5.19e-05
  Update  356 | Ep  1666 | reward:    246.8 | mean(100):    181.6 | actor_loss: -0.0032 | value_loss: 5.6446 | lr: 5.08e-05
  Update  357 | Ep  1671 | reward:    261.9 | mean(100):    182.1 | actor_loss: -0.0024 | value_loss: 4.7395 | lr: 5.01e-05
  Update  358 | Ep  1680 | reward:    227.9 | mean(100):    188.1 | actor_loss: -0.0007 | value_loss: 7.8831 | lr: 4.93e-05
  Update  359 | Ep  1689 | reward:    229.3 | mean(100):    189.8 | actor_loss: -0.0040 | value_loss: 8.0440 | lr: 4.80e-05
  Update  360 | Ep  1694 | reward:    272.3 | mean(100):    189.5 | actor_loss: -0.0061 | value_loss: 5.9154 | lr: 4.66e-05
  Update  361 | Ep  1701 | reward:    246.3 | mean(100):    190.0 | actor_loss: -0.0009 | value_loss: 7.3973 | lr: 4.59e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  362 | Ep  1705 | reward:    269.6 | mean(100):    187.8 | actor_loss: -0.0016 | value_loss: 4.3046 | lr: 4.48e-05
  Update  363 | Ep  1708 | reward:    271.5 | mean(100):    190.8 | actor_loss: -0.0031 | value_loss: 4.0173 | lr: 4.42e-05
  Update  364 | Ep  1715 | reward:    241.5 | mean(100):    192.7 | actor_loss: -0.0008 | value_loss: 7.1160 | lr: 4.38e-05
  Update  365 | Ep  1720 | reward:      5.5 | mean(100):    189.6 | actor_loss: -0.0034 | value_loss: 4.4772 | lr: 4.27e-05
  Update  366 | Ep  1724 | reward:    248.4 | mean(100):    190.9 | actor_loss: -0.0019 | value_loss: 3.8555 | lr: 4.20e-05
  Update  367 | Ep  1730 | reward:    218.7 | mean(100):    195.4 | actor_loss: -0.0012 | value_loss: 6.6181 | lr: 4.14e-05
  Update  368 | Ep  1737 | reward:    267.5 | mean(100):    192.6 | actor_loss: -0.0020 | value_loss: 6.3655 | lr: 4.05e-05
  Update  369 | Ep  1745 | reward:    257.4 | mean(100):    198.3 | actor_loss: -0.0003 | value_loss: 7.5527 | lr: 3.94e-05
  Update  370 | Ep  1753 | reward:    241.7 | mean(100):    201.0 | actor_loss: -0.0020 | value_loss: 7.2143 | lr: 3.82e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png

Solved at episode 1753 (update 370) with mean 201.0!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
