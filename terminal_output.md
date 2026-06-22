Using device: cuda (rollout collection stays on CPU; batched PPO update uses cuda)
Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    21 | reward:    -34.9 | mean(100):   -193.8 | actor_loss: -0.0055 | value_loss: 32.4345 | lr: 3.00e-04
  Update    2 | Ep    42 | reward:    -55.2 | mean(100):   -187.4 | actor_loss: -0.0069 | value_loss: 29.1005 | lr: 2.97e-04
  Update    3 | Ep    65 | reward:   -127.8 | mean(100):   -172.4 | actor_loss: -0.0067 | value_loss: 26.4931 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    4 | Ep    86 | reward:   -175.4 | mean(100):   -165.1 | actor_loss: -0.0094 | value_loss: 23.3037 | lr: 2.90e-04
  Update    5 | Ep   107 | reward:   -293.7 | mean(100):   -158.7 | actor_loss: -0.0113 | value_loss: 23.9532 | lr: 2.87e-04
  Update    6 | Ep   131 | reward:    -47.6 | mean(100):   -132.3 | actor_loss: -0.0068 | value_loss: 19.3577 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    7 | Ep   154 | reward:   -114.0 | mean(100):   -114.1 | actor_loss: -0.0058 | value_loss: 16.4234 | lr: 2.80e-04
  Update    8 | Ep   175 | reward:   -107.3 | mean(100):   -104.7 | actor_loss: -0.0104 | value_loss: 16.7350 | lr: 2.77e-04
  Update    9 | Ep   195 | reward:    -61.2 | mean(100):    -84.5 | actor_loss: -0.0096 | value_loss: 14.6962 | lr: 2.74e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   10 | Ep   214 | reward:    -46.5 | mean(100):    -75.3 | actor_loss: -0.0051 | value_loss: 15.2929 | lr: 2.71e-04
  Update   11 | Ep   232 | reward:    -76.4 | mean(100):    -71.0 | actor_loss: -0.0102 | value_loss: 13.8784 | lr: 2.68e-04
  Update   12 | Ep   251 | reward:    -28.5 | mean(100):    -64.0 | actor_loss: -0.0045 | value_loss: 15.0432 | lr: 2.65e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   13 | Ep   268 | reward:    -31.9 | mean(100):    -51.9 | actor_loss: -0.0104 | value_loss: 13.0900 | lr: 2.62e-04
  Update   14 | Ep   276 | reward:    -45.1 | mean(100):    -48.5 | actor_loss: -0.0072 | value_loss: 9.3044 | lr: 2.60e-04
  Update   15 | Ep   293 | reward:     11.3 | mean(100):    -43.2 | actor_loss: -0.0045 | value_loss: 14.2913 | lr: 2.59e-04
  Update   16 | Ep   309 | reward:    -13.2 | mean(100):    -35.2 | actor_loss: -0.0047 | value_loss: 11.6409 | lr: 2.56e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   17 | Ep   318 | reward:    130.3 | mean(100):    -28.4 | actor_loss: -0.0085 | value_loss: 8.9974 | lr: 2.54e-04
  Update   18 | Ep   323 | reward:     -8.8 | mean(100):    -26.6 | actor_loss: -0.0071 | value_loss: 9.4983 | lr: 2.52e-04
  Update   19 | Ep   331 | reward:    -97.1 | mean(100):    -24.7 | actor_loss: -0.0055 | value_loss: 11.9374 | lr: 2.52e-04
  Update   20 | Ep   335 | reward:     17.2 | mean(100):    -21.9 | actor_loss: -0.0070 | value_loss: 8.2345 | lr: 2.50e-04
  Update   21 | Ep   340 | reward:    -78.6 | mean(100):    -21.0 | actor_loss: -0.0052 | value_loss: 8.1561 | lr: 2.50e-04
  Update   22 | Ep   342 | reward:     55.1 | mean(100):    -19.0 | actor_loss: -0.0110 | value_loss: 6.4409 | lr: 2.49e-04
  Update   23 | Ep   344 | reward:    -43.7 | mean(100):    -20.4 | actor_loss: -0.0048 | value_loss: 5.9645 | lr: 2.49e-04
  Update   24 | Ep   346 | reward:     62.3 | mean(100):    -17.6 | actor_loss: -0.0055 | value_loss: 4.1863 | lr: 2.48e-04
  Update   25 | Ep   348 | reward:    101.3 | mean(100):    -16.2 | actor_loss: -0.0084 | value_loss: 4.5979 | lr: 2.48e-04
  Update   26 | Ep   350 | reward:     75.2 | mean(100):    -15.6 | actor_loss: -0.0033 | value_loss: 4.5642 | lr: 2.48e-04
  Update   27 | Ep   352 | reward:     82.3 | mean(100):    -14.2 | actor_loss: -0.0072 | value_loss: 3.7468 | lr: 2.47e-04
  Update   28 | Ep   355 | reward:    -88.1 | mean(100):    -17.2 | actor_loss: -0.0052 | value_loss: 5.9914 | lr: 2.47e-04
  Update   29 | Ep   358 | reward:     46.9 | mean(100):    -17.5 | actor_loss: -0.0044 | value_loss: 4.0587 | lr: 2.47e-04
  Update   30 | Ep   360 | reward:     30.4 | mean(100):    -17.7 | actor_loss: -0.0044 | value_loss: 3.0723 | lr: 2.46e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   31 | Ep   363 | reward:   -145.9 | mean(100):    -18.7 | actor_loss: -0.0021 | value_loss: 5.7378 | lr: 2.46e-04
  Update   32 | Ep   365 | reward:   -170.5 | mean(100):    -20.3 | actor_loss: -0.0047 | value_loss: 4.1014 | lr: 2.46e-04
  Update   33 | Ep   367 | reward:     93.4 | mean(100):    -19.4 | actor_loss: -0.0071 | value_loss: 3.2173 | lr: 2.45e-04
  Update   34 | Ep   369 | reward:   -182.4 | mean(100):    -21.3 | actor_loss: -0.0054 | value_loss: 3.8348 | lr: 2.45e-04
  Update   35 | Ep   371 | reward:    -74.2 | mean(100):    -21.5 | actor_loss: -0.0029 | value_loss: 2.6183 | lr: 2.45e-04
  Update   36 | Ep   373 | reward:    -16.8 | mean(100):    -22.5 | actor_loss: -0.0083 | value_loss: 2.6899 | lr: 2.44e-04
  Update   37 | Ep   375 | reward:     30.7 | mean(100):    -22.0 | actor_loss: -0.0070 | value_loss: 3.1209 | lr: 2.44e-04
  Update   38 | Ep   377 | reward:     26.0 | mean(100):    -19.7 | actor_loss: -0.0053 | value_loss: 3.2895 | lr: 2.44e-04
  Update   39 | Ep   379 | reward:    -19.5 | mean(100):    -19.8 | actor_loss: -0.0076 | value_loss: 2.3154 | lr: 2.43e-04
  Update   40 | Ep   381 | reward:    -94.1 | mean(100):    -21.1 | actor_loss: -0.0033 | value_loss: 3.9715 | lr: 2.43e-04
  Update   41 | Ep   383 | reward:      0.1 | mean(100):    -21.6 | actor_loss: -0.0064 | value_loss: 3.4147 | lr: 2.43e-04
  Update   42 | Ep   385 | reward:     62.2 | mean(100):    -20.5 | actor_loss: -0.0076 | value_loss: 1.8935 | lr: 2.43e-04
  Update   43 | Ep   387 | reward:    -40.7 | mean(100):    -20.6 | actor_loss: -0.0111 | value_loss: 2.4775 | lr: 2.42e-04
  Update   44 | Ep   389 | reward:     60.0 | mean(100):    -19.7 | actor_loss: -0.0052 | value_loss: 2.3939 | lr: 2.42e-04
  Update   45 | Ep   391 | reward:    -61.7 | mean(100):    -19.7 | actor_loss: -0.0076 | value_loss: 2.8672 | lr: 2.42e-04
  Update   46 | Ep   393 | reward:    -76.3 | mean(100):    -19.5 | actor_loss: -0.0036 | value_loss: 2.5476 | lr: 2.41e-04
  Update   47 | Ep   395 | reward:    166.3 | mean(100):    -16.5 | actor_loss: -0.0065 | value_loss: 3.2212 | lr: 2.41e-04
  Update   48 | Ep   397 | reward:    162.7 | mean(100):    -13.4 | actor_loss: -0.0104 | value_loss: 3.5149 | lr: 2.41e-04
  Update   49 | Ep   400 | reward:    163.1 | mean(100):     -9.3 | actor_loss: -0.0030 | value_loss: 5.4534 | lr: 2.40e-04
  Update   50 | Ep   402 | reward:    240.0 | mean(100):     -7.0 | actor_loss: -0.0021 | value_loss: 3.7934 | lr: 2.40e-04
  Update   51 | Ep   405 | reward:    173.4 | mean(100):     -3.7 | actor_loss: -0.0057 | value_loss: 5.2012 | lr: 2.40e-04
  Update   52 | Ep   408 | reward:    186.4 | mean(100):     -0.3 | actor_loss: -0.0021 | value_loss: 5.3730 | lr: 2.39e-04
  Update   53 | Ep   412 | reward:     -6.9 | mean(100):      1.5 | actor_loss: -0.0029 | value_loss: 5.9927 | lr: 2.39e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   54 | Ep   415 | reward:   -215.5 | mean(100):      0.2 | actor_loss: -0.0066 | value_loss: 6.3214 | lr: 2.38e-04
  Update   55 | Ep   418 | reward:    219.2 | mean(100):      2.3 | actor_loss: -0.0000 | value_loss: 5.3705 | lr: 2.38e-04
  Update   56 | Ep   422 | reward:    -29.4 | mean(100):      6.6 | actor_loss: -0.0062 | value_loss: 5.7808 | lr: 2.37e-04
  Update   57 | Ep   425 | reward:    184.3 | mean(100):     12.8 | actor_loss: -0.0013 | value_loss: 7.7083 | lr: 2.37e-04
  Update   58 | Ep   428 | reward:    189.3 | mean(100):     20.9 | actor_loss: -0.0044 | value_loss: 5.6623 | lr: 2.36e-04
  Update   59 | Ep   432 | reward:    210.1 | mean(100):     29.0 | actor_loss: -0.0046 | value_loss: 7.1930 | lr: 2.36e-04
  Update   60 | Ep   436 | reward:   -183.4 | mean(100):     31.3 | actor_loss: -0.0035 | value_loss: 8.3067 | lr: 2.35e-04
  Update   61 | Ep   440 | reward:    173.1 | mean(100):     36.5 | actor_loss: -0.0032 | value_loss: 7.3771 | lr: 2.35e-04
  Update   62 | Ep   443 | reward:   -152.6 | mean(100):     36.9 | actor_loss: -0.0021 | value_loss: 6.5931 | lr: 2.34e-04
  Update   63 | Ep   447 | reward:    191.1 | mean(100):     44.3 | actor_loss: -0.0006 | value_loss: 6.8641 | lr: 2.34e-04
  Update   64 | Ep   451 | reward:      0.3 | mean(100):     49.9 | actor_loss: -0.0050 | value_loss: 7.8723 | lr: 2.33e-04
  Update   65 | Ep   455 | reward:    203.3 | mean(100):     60.5 | actor_loss: -0.0004 | value_loss: 6.8634 | lr: 2.32e-04
  Update   66 | Ep   459 | reward:    256.0 | mean(100):     70.0 | actor_loss: -0.0025 | value_loss: 7.5514 | lr: 2.32e-04
  Update   67 | Ep   463 | reward:    233.2 | mean(100):     77.8 | actor_loss: -0.0035 | value_loss: 7.2534 | lr: 2.31e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   68 | Ep   468 | reward:    192.4 | mean(100):     85.5 | actor_loss: -0.0039 | value_loss: 8.3029 | lr: 2.31e-04
  Update   69 | Ep   472 | reward:    206.6 | mean(100):     96.2 | actor_loss: -0.0012 | value_loss: 6.7981 | lr: 2.30e-04
  Update   70 | Ep   474 | reward:    153.4 | mean(100):    101.7 | actor_loss: -0.0030 | value_loss: 6.9724 | lr: 2.29e-04
  Update   71 | Ep   479 | reward:    203.8 | mean(100):    106.5 | actor_loss: -0.0027 | value_loss: 6.4498 | lr: 2.29e-04
  Update   72 | Ep   482 | reward:    225.1 | mean(100):    111.9 | actor_loss: -0.0032 | value_loss: 6.7007 | lr: 2.28e-04
  Update   73 | Ep   485 | reward:    206.3 | mean(100):    116.7 | actor_loss: -0.0015 | value_loss: 5.3498 | lr: 2.28e-04
  Update   74 | Ep   490 | reward:   -203.5 | mean(100):    116.3 | actor_loss: -0.0034 | value_loss: 8.7123 | lr: 2.27e-04
  Update   75 | Ep   494 | reward:    182.3 | mean(100):    123.1 | actor_loss: -0.0016 | value_loss: 6.4245 | lr: 2.26e-04
  Update   76 | Ep   499 | reward:     -8.1 | mean(100):    120.9 | actor_loss: -0.0023 | value_loss: 6.5283 | lr: 2.26e-04
  Update   77 | Ep   503 | reward:   -120.1 | mean(100):    123.3 | actor_loss: -0.0026 | value_loss: 7.3039 | lr: 2.25e-04
  Update   78 | Ep   507 | reward:    194.0 | mean(100):    126.7 | actor_loss: -0.0020 | value_loss: 5.8913 | lr: 2.25e-04
  Update   79 | Ep   511 | reward:    223.8 | mean(100):    132.0 | actor_loss: -0.0023 | value_loss: 6.3524 | lr: 2.24e-04
  Update   80 | Ep   515 | reward:    171.3 | mean(100):    141.9 | actor_loss: -0.0014 | value_loss: 7.8395 | lr: 2.23e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   81 | Ep   519 | reward:    152.3 | mean(100):    142.9 | actor_loss: -0.0007 | value_loss: 7.8103 | lr: 2.23e-04
  Update   82 | Ep   523 | reward:    234.9 | mean(100):    148.0 | actor_loss: -0.0044 | value_loss: 7.6726 | lr: 2.22e-04
  Update   83 | Ep   527 | reward:    223.2 | mean(100):    145.9 | actor_loss: -0.0023 | value_loss: 7.1589 | lr: 2.22e-04
  Update   84 | Ep   532 | reward:    229.5 | mean(100):    147.3 | actor_loss: -0.0027 | value_loss: 6.6905 | lr: 2.21e-04
  Update   85 | Ep   536 | reward:    137.8 | mean(100):    153.2 | actor_loss: -0.0028 | value_loss: 6.6174 | lr: 2.20e-04
  Update   86 | Ep   542 | reward:    253.1 | mean(100):    154.6 | actor_loss: -0.0058 | value_loss: 7.5747 | lr: 2.20e-04
  Update   87 | Ep   548 | reward:    239.8 | mean(100):    156.5 | actor_loss: -0.0007 | value_loss: 7.5626 | lr: 2.19e-04
  Update   88 | Ep   553 | reward:    -58.3 | mean(100):    153.6 | actor_loss: -0.0032 | value_loss: 7.0834 | lr: 2.18e-04
  Update   89 | Ep   558 | reward:     -5.1 | mean(100):    154.6 | actor_loss: -0.0010 | value_loss: 7.9351 | lr: 2.17e-04
  Update   90 | Ep   563 | reward:    199.7 | mean(100):    153.1 | actor_loss: -0.0022 | value_loss: 8.2810 | lr: 2.16e-04
  Update   91 | Ep   568 | reward:   -215.2 | mean(100):    154.7 | actor_loss: -0.0037 | value_loss: 9.0889 | lr: 2.16e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   92 | Ep   573 | reward:    256.8 | mean(100):    153.9 | actor_loss: -0.0070 | value_loss: 8.7063 | lr: 2.15e-04
  Update   93 | Ep   578 | reward:    242.8 | mean(100):    154.7 | actor_loss: -0.0011 | value_loss: 6.7899 | lr: 2.14e-04
  Update   94 | Ep   582 | reward:    237.0 | mean(100):    157.1 | actor_loss: -0.0060 | value_loss: 6.9648 | lr: 2.13e-04
  Update   95 | Ep   586 | reward:     21.1 | mean(100):    158.4 | actor_loss: -0.0034 | value_loss: 8.3334 | lr: 2.13e-04
  Update   96 | Ep   589 | reward:    170.6 | mean(100):    162.7 | actor_loss: -0.0015 | value_loss: 6.1941 | lr: 2.12e-04
  Update   97 | Ep   593 | reward:    240.8 | mean(100):    163.6 | actor_loss: -0.0047 | value_loss: 5.4626 | lr: 2.12e-04
  Update   98 | Ep   599 | reward:    219.0 | mean(100):    163.7 | actor_loss: -0.0029 | value_loss: 7.5359 | lr: 2.11e-04
  Update   99 | Ep   604 | reward:    250.2 | mean(100):    167.2 | actor_loss: -0.0026 | value_loss: 6.9433 | lr: 2.10e-04
  Update  100 | Ep   609 | reward:    -23.6 | mean(100):    160.7 | actor_loss: -0.0061 | value_loss: 6.2275 | lr: 2.09e-04
  Update  101 | Ep   613 | reward:    222.1 | mean(100):    160.4 | actor_loss: -0.0033 | value_loss: 6.7675 | lr: 2.09e-04
  Update  102 | Ep   620 | reward:    -71.0 | mean(100):    154.9 | actor_loss: -0.0102 | value_loss: 7.8322 | lr: 2.08e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  103 | Ep   624 | reward:    200.8 | mean(100):    152.8 | actor_loss: -0.0035 | value_loss: 5.1418 | lr: 2.07e-04
  Update  104 | Ep   628 | reward:    147.0 | mean(100):    155.1 | actor_loss: -0.0033 | value_loss: 7.9461 | lr: 2.06e-04
  Update  105 | Ep   633 | reward:    -18.8 | mean(100):    149.5 | actor_loss: -0.0010 | value_loss: 7.8395 | lr: 2.06e-04
  Update  106 | Ep   637 | reward:    -29.1 | mean(100):    147.0 | actor_loss: -0.0046 | value_loss: 6.9010 | lr: 2.05e-04
  Update  107 | Ep   643 | reward:    212.9 | mean(100):    145.7 | actor_loss: -0.0027 | value_loss: 7.6461 | lr: 2.04e-04
  Update  108 | Ep   649 | reward:   -111.3 | mean(100):    136.7 | actor_loss: -0.0058 | value_loss: 9.6714 | lr: 2.04e-04
  Update  109 | Ep   652 | reward:    214.1 | mean(100):    137.3 | actor_loss: -0.0027 | value_loss: 5.0645 | lr: 2.03e-04
  Update  110 | Ep   659 | reward:   -152.4 | mean(100):    130.0 | actor_loss: -0.0036 | value_loss: 9.3354 | lr: 2.02e-04
  Update  111 | Ep   666 | reward:    220.4 | mean(100):    126.5 | actor_loss: -0.0042 | value_loss: 8.0054 | lr: 2.01e-04
  Update  112 | Ep   672 | reward:   -173.1 | mean(100):    122.6 | actor_loss: -0.0021 | value_loss: 9.5465 | lr: 2.00e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  113 | Ep   677 | reward:    264.9 | mean(100):    127.0 | actor_loss: -0.0055 | value_loss: 8.3027 | lr: 1.99e-04
  Update  114 | Ep   685 | reward:    -90.0 | mean(100):    121.8 | actor_loss: -0.0015 | value_loss: 9.8832 | lr: 1.98e-04
  Update  115 | Ep   692 | reward:    -78.3 | mean(100):    121.9 | actor_loss: -0.0009 | value_loss: 9.1954 | lr: 1.97e-04
  Update  116 | Ep   700 | reward:    189.7 | mean(100):    118.7 | actor_loss: -0.0024 | value_loss: 8.6276 | lr: 1.96e-04
  Update  117 | Ep   707 | reward:   -223.2 | mean(100):    115.1 | actor_loss: -0.0033 | value_loss: 9.2934 | lr: 1.95e-04
  Update  118 | Ep   714 | reward:    -29.5 | mean(100):    111.8 | actor_loss: -0.0035 | value_loss: 8.5005 | lr: 1.94e-04
  Update  119 | Ep   720 | reward:    248.8 | mean(100):    120.1 | actor_loss: -0.0029 | value_loss: 7.7976 | lr: 1.93e-04
  Update  120 | Ep   727 | reward:    -33.5 | mean(100):    111.1 | actor_loss: -0.0013 | value_loss: 9.3132 | lr: 1.92e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  121 | Ep   734 | reward:    244.8 | mean(100):    110.8 | actor_loss: -0.0038 | value_loss: 8.4818 | lr: 1.91e-04
  Update  122 | Ep   741 | reward:    160.3 | mean(100):    112.3 | actor_loss: -0.0042 | value_loss: 8.5857 | lr: 1.90e-04
  Update  123 | Ep   748 | reward:    233.5 | mean(100):    110.5 | actor_loss: -0.0038 | value_loss: 10.2485 | lr: 1.89e-04
  Update  124 | Ep   755 | reward:    -37.5 | mean(100):    113.2 | actor_loss: -0.0054 | value_loss: 9.1273 | lr: 1.88e-04
  Update  125 | Ep   762 | reward:    256.6 | mean(100):    114.0 | actor_loss: -0.0029 | value_loss: 8.0853 | lr: 1.87e-04
  Update  126 | Ep   768 | reward:   -229.8 | mean(100):    108.2 | actor_loss: -0.0079 | value_loss: 9.7811 | lr: 1.86e-04
  Update  127 | Ep   775 | reward:    206.0 | mean(100):    102.4 | actor_loss: -0.0039 | value_loss: 8.9586 | lr: 1.85e-04
  Update  128 | Ep   781 | reward:    -45.9 | mean(100):     92.4 | actor_loss: -0.0077 | value_loss: 8.2463 | lr: 1.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  129 | Ep   787 | reward:      8.9 | mean(100):     92.5 | actor_loss: -0.0030 | value_loss: 9.4942 | lr: 1.83e-04
  Update  130 | Ep   793 | reward:    190.8 | mean(100):     94.3 | actor_loss: -0.0015 | value_loss: 9.1472 | lr: 1.82e-04
  Update  131 | Ep   799 | reward:    -78.3 | mean(100):     96.5 | actor_loss: -0.0049 | value_loss: 8.4791 | lr: 1.81e-04
  Update  132 | Ep   806 | reward:    -55.5 | mean(100):     91.1 | actor_loss: -0.0044 | value_loss: 8.3103 | lr: 1.80e-04
  Update  133 | Ep   811 | reward:    -86.8 | mean(100):     92.3 | actor_loss: -0.0068 | value_loss: 7.7866 | lr: 1.79e-04
  Update  134 | Ep   816 | reward:   -165.4 | mean(100):     90.1 | actor_loss: -0.0063 | value_loss: 6.8539 | lr: 1.78e-04
  Update  135 | Ep   822 | reward:    -24.4 | mean(100):     84.7 | actor_loss: -0.0045 | value_loss: 6.8501 | lr: 1.78e-04
  Update  136 | Ep   826 | reward:    209.6 | mean(100):     90.2 | actor_loss: -0.0014 | value_loss: 4.6967 | lr: 1.77e-04
  Update  137 | Ep   831 | reward:    222.3 | mean(100):     98.2 | actor_loss: -0.0012 | value_loss: 5.6879 | lr: 1.76e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  138 | Ep   837 | reward:    -48.5 | mean(100):    100.2 | actor_loss: -0.0033 | value_loss: 6.7048 | lr: 1.75e-04
  Update  139 | Ep   844 | reward:    -54.2 | mean(100):    104.0 | actor_loss: -0.0037 | value_loss: 8.6815 | lr: 1.74e-04
  Update  140 | Ep   850 | reward:    -98.8 | mean(100):    103.9 | actor_loss: -0.0076 | value_loss: 8.2458 | lr: 1.73e-04
  Update  141 | Ep   855 | reward:   -133.5 | mean(100):    101.8 | actor_loss: -0.0007 | value_loss: 6.8758 | lr: 1.72e-04
  Update  142 | Ep   864 | reward:    -41.3 | mean(100):     97.0 | actor_loss: -0.0044 | value_loss: 8.7780 | lr: 1.72e-04
  Update  143 | Ep   869 | reward:    237.7 | mean(100):    104.3 | actor_loss: -0.0047 | value_loss: 6.1077 | lr: 1.70e-04
  Update  144 | Ep   876 | reward:    -92.6 | mean(100):    112.9 | actor_loss: -0.0034 | value_loss: 8.0378 | lr: 1.70e-04
  Update  145 | Ep   882 | reward:    182.8 | mean(100):    120.0 | actor_loss: -0.0031 | value_loss: 8.1775 | lr: 1.69e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  146 | Ep   889 | reward:    -11.0 | mean(100):    125.3 | actor_loss: -0.0037 | value_loss: 9.0738 | lr: 1.68e-04
  Update  147 | Ep   894 | reward:    176.6 | mean(100):    125.1 | actor_loss: -0.0020 | value_loss: 7.5755 | lr: 1.67e-04
  Update  148 | Ep   900 | reward:    -38.5 | mean(100):    129.5 | actor_loss: -0.0023 | value_loss: 8.0131 | lr: 1.66e-04
  Update  149 | Ep   907 | reward:    197.9 | mean(100):    126.3 | actor_loss: -0.0042 | value_loss: 9.4837 | lr: 1.65e-04
  Update  150 | Ep   912 | reward:      8.3 | mean(100):    124.5 | actor_loss: -0.0052 | value_loss: 8.7436 | lr: 1.64e-04
  Update  151 | Ep   919 | reward:    -37.2 | mean(100):    119.8 | actor_loss: -0.0051 | value_loss: 9.3362 | lr: 1.63e-04
  Update  152 | Ep   926 | reward:    -56.8 | mean(100):    120.0 | actor_loss: -0.0041 | value_loss: 7.9716 | lr: 1.62e-04
  Update  153 | Ep   934 | reward:    251.5 | mean(100):    112.4 | actor_loss: -0.0051 | value_loss: 8.6206 | lr: 1.61e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  154 | Ep   941 | reward:    -96.7 | mean(100):    112.9 | actor_loss: -0.0030 | value_loss: 7.3918 | lr: 1.60e-04
  Update  155 | Ep   947 | reward:   -242.8 | mean(100):    112.0 | actor_loss: -0.0029 | value_loss: 10.1087 | lr: 1.59e-04
  Update  156 | Ep   955 | reward:    263.5 | mean(100):    119.6 | actor_loss: -0.0026 | value_loss: 7.9293 | lr: 1.58e-04
  Update  157 | Ep   963 | reward:    227.5 | mean(100):    124.7 | actor_loss: -0.0027 | value_loss: 7.5700 | lr: 1.57e-04
  Update  158 | Ep   971 | reward:    224.4 | mean(100):    122.5 | actor_loss: -0.0036 | value_loss: 7.1997 | lr: 1.56e-04
  Update  159 | Ep   979 | reward:   -135.7 | mean(100):    114.3 | actor_loss: -0.0033 | value_loss: 8.9345 | lr: 1.54e-04
  Update  160 | Ep   986 | reward:    -15.6 | mean(100):    103.6 | actor_loss: -0.0048 | value_loss: 8.3829 | lr: 1.53e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  161 | Ep   991 | reward:    250.8 | mean(100):    102.8 | actor_loss: -0.0053 | value_loss: 6.0947 | lr: 1.52e-04
  Update  162 | Ep   997 | reward:    -11.4 | mean(100):     98.3 | actor_loss: -0.0054 | value_loss: 9.5868 | lr: 1.51e-04
  Update  163 | Ep  1005 | reward:    248.8 | mean(100):    100.1 | actor_loss: -0.0045 | value_loss: 7.6789 | lr: 1.50e-04
  Update  164 | Ep  1012 | reward:    -62.9 | mean(100):    103.8 | actor_loss: -0.0039 | value_loss: 7.0355 | lr: 1.49e-04
  Update  165 | Ep  1017 | reward:    235.5 | mean(100):    108.1 | actor_loss: -0.0058 | value_loss: 7.3387 | lr: 1.48e-04
  Update  166 | Ep  1020 | reward:    202.3 | mean(100):    113.1 | actor_loss: -0.0032 | value_loss: 7.9816 | lr: 1.47e-04
  Update  167 | Ep  1026 | reward:    262.0 | mean(100):    119.4 | actor_loss: -0.0031 | value_loss: 7.7347 | lr: 1.47e-04
  Update  168 | Ep  1031 | reward:    180.2 | mean(100):    126.1 | actor_loss: -0.0028 | value_loss: 8.5498 | lr: 1.46e-04
  Update  169 | Ep  1037 | reward:    290.8 | mean(100):    125.8 | actor_loss: -0.0085 | value_loss: 8.1510 | lr: 1.45e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  170 | Ep  1041 | reward:    248.5 | mean(100):    123.6 | actor_loss: -0.0070 | value_loss: 6.7266 | lr: 1.44e-04
  Update  171 | Ep  1047 | reward:    197.7 | mean(100):    125.9 | actor_loss: -0.0033 | value_loss: 7.3800 | lr: 1.44e-04
  Update  172 | Ep  1054 | reward:    242.1 | mean(100):    128.7 | actor_loss: -0.0060 | value_loss: 6.9038 | lr: 1.43e-04
  Update  173 | Ep  1062 | reward:    234.5 | mean(100):    127.4 | actor_loss: -0.0033 | value_loss: 10.3732 | lr: 1.42e-04
  Update  174 | Ep  1069 | reward:    247.4 | mean(100):    127.8 | actor_loss: -0.0111 | value_loss: 8.4701 | lr: 1.41e-04
  Update  175 | Ep  1075 | reward:    162.6 | mean(100):    133.2 | actor_loss: -0.0047 | value_loss: 7.0708 | lr: 1.40e-04
  Update  176 | Ep  1080 | reward:    251.8 | mean(100):    138.7 | actor_loss: -0.0017 | value_loss: 6.4469 | lr: 1.39e-04
  Update  177 | Ep  1087 | reward:    257.6 | mean(100):    150.4 | actor_loss: -0.0027 | value_loss: 7.5154 | lr: 1.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  178 | Ep  1092 | reward:     -1.3 | mean(100):    150.5 | actor_loss: -0.0026 | value_loss: 7.3620 | lr: 1.37e-04
  Update  179 | Ep  1098 | reward:    262.3 | mean(100):    160.3 | actor_loss: -0.0039 | value_loss: 6.3813 | lr: 1.36e-04
  Update  180 | Ep  1105 | reward:    173.3 | mean(100):    162.9 | actor_loss: -0.0077 | value_loss: 7.4270 | lr: 1.35e-04
  Update  181 | Ep  1111 | reward:    213.1 | mean(100):    164.8 | actor_loss: -0.0032 | value_loss: 7.9475 | lr: 1.34e-04
  Update  182 | Ep  1117 | reward:    225.2 | mean(100):    165.3 | actor_loss: -0.0038 | value_loss: 8.3083 | lr: 1.33e-04
  Update  183 | Ep  1124 | reward:    259.4 | mean(100):    168.9 | actor_loss: -0.0008 | value_loss: 7.7900 | lr: 1.32e-04
  Update  184 | Ep  1129 | reward:    250.7 | mean(100):    165.3 | actor_loss: -0.0015 | value_loss: 5.9156 | lr: 1.31e-04
  Update  185 | Ep  1135 | reward:    220.4 | mean(100):    170.1 | actor_loss: -0.0055 | value_loss: 6.5205 | lr: 1.31e-04
  Update  186 | Ep  1140 | reward:    245.8 | mean(100):    171.9 | actor_loss: -0.0022 | value_loss: 7.9827 | lr: 1.30e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  187 | Ep  1147 | reward:     24.1 | mean(100):    174.7 | actor_loss: -0.0027 | value_loss: 7.2570 | lr: 1.29e-04
  Update  188 | Ep  1152 | reward:    253.0 | mean(100):    173.4 | actor_loss: -0.0048 | value_loss: 7.9388 | lr: 1.28e-04
  Update  189 | Ep  1157 | reward:    225.6 | mean(100):    174.0 | actor_loss: -0.0046 | value_loss: 7.3418 | lr: 1.27e-04
  Update  190 | Ep  1163 | reward:    251.7 | mean(100):    180.3 | actor_loss: -0.0035 | value_loss: 7.5899 | lr: 1.26e-04
  Update  191 | Ep  1170 | reward:    210.7 | mean(100):    186.8 | actor_loss: -0.0033 | value_loss: 7.1450 | lr: 1.26e-04
  Update  192 | Ep  1178 | reward:     -5.2 | mean(100):    185.9 | actor_loss: -0.0018 | value_loss: 7.3042 | lr: 1.24e-04
  Update  193 | Ep  1185 | reward:     -0.6 | mean(100):    184.2 | actor_loss: -0.0030 | value_loss: 7.8313 | lr: 1.23e-04
  Update  194 | Ep  1192 | reward:    264.7 | mean(100):    185.8 | actor_loss: -0.0052 | value_loss: 8.1255 | lr: 1.22e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  195 | Ep  1199 | reward:    227.6 | mean(100):    183.4 | actor_loss: -0.0038 | value_loss: 7.0087 | lr: 1.21e-04
  Update  196 | Ep  1205 | reward:     20.0 | mean(100):    185.9 | actor_loss: -0.0026 | value_loss: 7.6153 | lr: 1.20e-04
  Update  197 | Ep  1212 | reward:    244.7 | mean(100):    187.3 | actor_loss: -0.0026 | value_loss: 7.1896 | lr: 1.19e-04
  Update  198 | Ep  1218 | reward:    201.2 | mean(100):    192.0 | actor_loss: -0.0050 | value_loss: 7.9350 | lr: 1.18e-04
  Update  199 | Ep  1224 | reward:    -31.2 | mean(100):    188.0 | actor_loss: -0.0047 | value_loss: 6.9304 | lr: 1.17e-04
  Update  200 | Ep  1230 | reward:    205.8 | mean(100):    186.9 | actor_loss: -0.0029 | value_loss: 7.8136 | lr: 1.16e-04
  Update  201 | Ep  1236 | reward:    227.9 | mean(100):    185.4 | actor_loss: -0.0024 | value_loss: 6.8348 | lr: 1.15e-04
  Update  202 | Ep  1243 | reward:    244.6 | mean(100):    189.4 | actor_loss: -0.0018 | value_loss: 6.4747 | lr: 1.15e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  203 | Ep  1249 | reward:    262.4 | mean(100):    191.4 | actor_loss: -0.0023 | value_loss: 6.5793 | lr: 1.14e-04
  Update  204 | Ep  1257 | reward:    247.2 | mean(100):    195.1 | actor_loss: -0.0040 | value_loss: 8.7002 | lr: 1.13e-04
  Update  205 | Ep  1265 | reward:    263.0 | mean(100):    194.3 | actor_loss: -0.0024 | value_loss: 8.1025 | lr: 1.11e-04
  Update  206 | Ep  1273 | reward:    231.0 | mean(100):    194.7 | actor_loss: -0.0058 | value_loss: 7.7103 | lr: 1.10e-04
  Update  207 | Ep  1278 | reward:    255.1 | mean(100):    195.3 | actor_loss: -0.0017 | value_loss: 6.6342 | lr: 1.09e-04
  Update  208 | Ep  1284 | reward:    245.7 | mean(100):    197.4 | actor_loss: -0.0007 | value_loss: 5.6008 | lr: 1.08e-04
  Update  209 | Ep  1290 | reward:    232.1 | mean(100):    200.2 | actor_loss: -0.0017 | value_loss: 6.8101 | lr: 1.07e-04

Solved at episode 1290 (update 209) with mean 200.2!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
