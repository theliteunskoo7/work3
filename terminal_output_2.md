Using device: cpu (rollout collection stays on CPU; batched PPO update uses cpu)
Training PPO on CartPole-v1 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gae_lambda=0.95
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    97 | reward:     21.0 | mean(100):     21.1 | actor_loss: -0.0186 | value_loss: 7.6748 | lr: 3.00e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    2 | Ep   169 | reward:     18.0 | mean(100):     26.1 | actor_loss: -0.0247 | value_loss: 8.7203 | lr: 2.85e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    3 | Ep   211 | reward:     71.0 | mean(100):     36.2 | actor_loss: -0.0199 | value_loss: 10.9685 | lr: 2.75e-04
  Update    4 | Ep   232 | reward:    107.0 | mean(100):     50.1 | actor_loss: -0.0116 | value_loss: 12.9742 | lr: 2.68e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update    5 | Ep   241 | reward:     92.0 | mean(100):     68.2 | actor_loss: -0.0048 | value_loss: 14.4373 | lr: 2.65e-04
  Update    6 | Ep   250 | reward:    122.0 | mean(100):     84.5 | actor_loss: -0.0009 | value_loss: 14.1995 | lr: 2.64e-04
  Update    7 | Ep   263 | reward:    119.0 | mean(100):    100.3 | actor_loss: -0.0076 | value_loss: 13.4296 | lr: 2.62e-04
  Update    8 | Ep   270 | reward:    428.0 | mean(100):    117.4 | actor_loss: -0.0004 | value_loss: 14.1349 | lr: 2.61e-04
  Update    9 | Ep   276 | reward:    168.0 | mean(100):    133.7 | actor_loss: -0.0010 | value_loss: 14.0616 | lr: 2.59e-04
  Update   10 | Ep   284 | reward:    327.0 | mean(100):    150.1 | actor_loss: -0.0006 | value_loss: 13.5422 | lr: 2.59e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   11 | Ep   292 | reward:    155.0 | mean(100):    166.3 | actor_loss: -0.0083 | value_loss: 13.3162 | lr: 2.57e-04
  Update   12 | Ep   297 | reward:    459.0 | mean(100):    181.7 | actor_loss: -0.0022 | value_loss: 13.6139 | lr: 2.56e-04
  Update   13 | Ep   304 | reward:    178.0 | mean(100):    196.0 | actor_loss: -0.0031 | value_loss: 13.0890 | lr: 2.55e-04
  Update   14 | Ep   311 | reward:    202.0 | mean(100):    211.1 | actor_loss: -0.0068 | value_loss: 12.9542 | lr: 2.54e-04
  Update   15 | Ep   317 | reward:    249.0 | mean(100):    223.1 | actor_loss: -0.0039 | value_loss: 12.7002 | lr: 2.53e-04
  Update   16 | Ep   322 | reward:    329.0 | mean(100):    234.2 | actor_loss: -0.0034 | value_loss: 12.6184 | lr: 2.52e-04
  Update   17 | Ep   326 | reward:    500.0 | mean(100):    249.6 | actor_loss: 0.0008 | value_loss: 12.5986 | lr: 2.52e-04
  Update   18 | Ep   330 | reward:    308.0 | mean(100):    263.3 | actor_loss: -0.0012 | value_loss: 12.4369 | lr: 2.51e-04
  Update   19 | Ep   334 | reward:    352.0 | mean(100):    272.1 | actor_loss: 0.0001 | value_loss: 12.2099 | lr: 2.50e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   20 | Ep   341 | reward:    409.0 | mean(100):    278.2 | actor_loss: -0.0014 | value_loss: 11.5305 | lr: 2.50e-04
  Update   21 | Ep   352 | reward:    187.0 | mean(100):    276.4 | actor_loss: -0.0094 | value_loss: 10.8950 | lr: 2.49e-04
  Update   22 | Ep   361 | reward:    157.0 | mean(100):    282.2 | actor_loss: -0.0077 | value_loss: 10.9801 | lr: 2.47e-04
  Update   23 | Ep   368 | reward:    203.0 | mean(100):    284.9 | actor_loss: -0.0058 | value_loss: 11.0316 | lr: 2.46e-04
  Update   24 | Ep   373 | reward:    268.0 | mean(100):    290.6 | actor_loss: -0.0061 | value_loss: 11.2275 | lr: 2.45e-04
  Update   25 | Ep   381 | reward:    187.0 | mean(100):    286.4 | actor_loss: -0.0024 | value_loss: 10.7205 | lr: 2.44e-04
  Update   26 | Ep   387 | reward:    222.0 | mean(100):    289.2 | actor_loss: -0.0030 | value_loss: 10.8308 | lr: 2.43e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   27 | Ep   396 | reward:    229.0 | mean(100):    281.9 | actor_loss: -0.0040 | value_loss: 10.4465 | lr: 2.42e-04
  Update   28 | Ep   404 | reward:    252.0 | mean(100):    278.4 | actor_loss: -0.0004 | value_loss: 10.3790 | lr: 2.41e-04
  Update   29 | Ep   413 | reward:    231.0 | mean(100):    271.5 | actor_loss: -0.0035 | value_loss: 10.1820 | lr: 2.39e-04
  Update   30 | Ep   426 | reward:    172.0 | mean(100):    246.8 | actor_loss: -0.0100 | value_loss: 9.9774 | lr: 2.38e-04
  Update   31 | Ep   434 | reward:    211.0 | mean(100):    231.3 | actor_loss: -0.0048 | value_loss: 10.0657 | lr: 2.36e-04
  Update   32 | Ep   440 | reward:    500.0 | mean(100):    235.5 | actor_loss: -0.0009 | value_loss: 10.0453 | lr: 2.35e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   33 | Ep   446 | reward:    185.0 | mean(100):    240.4 | actor_loss: -0.0048 | value_loss: 9.9312 | lr: 2.34e-04
  Update   34 | Ep   456 | reward:    200.0 | mean(100):    239.7 | actor_loss: -0.0015 | value_loss: 9.7212 | lr: 2.33e-04
  Update   35 | Ep   461 | reward:    500.0 | mean(100):    246.2 | actor_loss: -0.0032 | value_loss: 9.7883 | lr: 2.32e-04
  Update   36 | Ep   466 | reward:    322.0 | mean(100):    251.0 | actor_loss: -0.0035 | value_loss: 9.6700 | lr: 2.31e-04
  Update   37 | Ep   472 | reward:    500.0 | mean(100):    249.1 | actor_loss: -0.0054 | value_loss: 9.5337 | lr: 2.30e-04
  Update   38 | Ep   480 | reward:    500.0 | mean(100):    248.3 | actor_loss: -0.0018 | value_loss: 9.4061 | lr: 2.29e-04
  Update   39 | Ep   486 | reward:    500.0 | mean(100):    250.8 | actor_loss: -0.0025 | value_loss: 9.3250 | lr: 2.28e-04
  Update   40 | Ep   491 | reward:    235.0 | mean(100):    254.7 | actor_loss: -0.0027 | value_loss: 9.2516 | lr: 2.27e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   41 | Ep   497 | reward:    500.0 | mean(100):    263.1 | actor_loss: -0.0021 | value_loss: 9.1322 | lr: 2.26e-04
  Update   42 | Ep   503 | reward:    290.0 | mean(100):    268.2 | actor_loss: -0.0027 | value_loss: 9.0558 | lr: 2.25e-04
  Update   43 | Ep   511 | reward:    259.0 | mean(100):    269.9 | actor_loss: -0.0031 | value_loss: 9.0003 | lr: 2.25e-04
  Update   44 | Ep   515 | reward:    500.0 | mean(100):    278.7 | actor_loss: -0.0007 | value_loss: 8.7963 | lr: 2.23e-04
  Update   45 | Ep   524 | reward:    214.0 | mean(100):    286.1 | actor_loss: -0.0048 | value_loss: 8.8465 | lr: 2.23e-04
  Update   46 | Ep   530 | reward:    500.0 | mean(100):    292.9 | actor_loss: -0.0005 | value_loss: 8.6629 | lr: 2.21e-04
  Update   47 | Ep   536 | reward:    194.0 | mean(100):    296.7 | actor_loss: -0.0021 | value_loss: 8.5656 | lr: 2.20e-04
  Update   48 | Ep   545 | reward:    193.0 | mean(100):    283.9 | actor_loss: -0.0021 | value_loss: 8.6672 | lr: 2.20e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   49 | Ep   552 | reward:    248.0 | mean(100):    289.0 | actor_loss: -0.0002 | value_loss: 8.4517 | lr: 2.18e-04
  Update   50 | Ep   561 | reward:    144.0 | mean(100):    282.4 | actor_loss: -0.0022 | value_loss: 8.5143 | lr: 2.17e-04
  Update   51 | Ep   570 | reward:    151.0 | mean(100):    270.7 | actor_loss: -0.0046 | value_loss: 8.3981 | lr: 2.16e-04
  Update   52 | Ep   582 | reward:    161.0 | mean(100):    259.2 | actor_loss: -0.0030 | value_loss: 8.6908 | lr: 2.15e-04
  Update   53 | Ep   592 | reward:    157.0 | mean(100):    243.8 | actor_loss: -0.0027 | value_loss: 8.3976 | lr: 2.13e-04
  Update   54 | Ep   602 | reward:    201.0 | mean(100):    231.9 | actor_loss: -0.0023 | value_loss: 8.3395 | lr: 2.11e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   55 | Ep   613 | reward:    205.0 | mean(100):    220.4 | actor_loss: -0.0019 | value_loss: 8.3935 | lr: 2.10e-04
  Update   56 | Ep   622 | reward:    238.0 | mean(100):    215.9 | actor_loss: -0.0097 | value_loss: 8.1552 | lr: 2.08e-04
  Update   57 | Ep   630 | reward:    195.0 | mean(100):    210.3 | actor_loss: -0.0007 | value_loss: 7.9781 | lr: 2.07e-04
  Update   58 | Ep   638 | reward:    251.0 | mean(100):    205.6 | actor_loss: -0.0023 | value_loss: 7.9032 | lr: 2.06e-04
  Update   59 | Ep   647 | reward:    218.0 | mean(100):    206.9 | actor_loss: -0.0023 | value_loss: 7.9887 | lr: 2.04e-04
  Update   60 | Ep   655 | reward:    281.0 | mean(100):    204.0 | actor_loss: -0.0001 | value_loss: 7.7809 | lr: 2.03e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   61 | Ep   663 | reward:    312.0 | mean(100):    207.2 | actor_loss: -0.0033 | value_loss: 7.7362 | lr: 2.02e-04
  Update   62 | Ep   670 | reward:    217.0 | mean(100):    211.9 | actor_loss: -0.0014 | value_loss: 7.5554 | lr: 2.01e-04
  Update   63 | Ep   677 | reward:    200.0 | mean(100):    218.9 | actor_loss: -0.0024 | value_loss: 7.4731 | lr: 1.99e-04
  Update   64 | Ep   682 | reward:    500.0 | mean(100):    226.8 | actor_loss: -0.0034 | value_loss: 7.0679 | lr: 1.98e-04
  Update   65 | Ep   686 | reward:    500.0 | mean(100):    238.8 | actor_loss: -0.0012 | value_loss: 6.8088 | lr: 1.98e-04
  Update   66 | Ep   692 | reward:    197.0 | mean(100):    248.3 | actor_loss: -0.0028 | value_loss: 7.1047 | lr: 1.97e-04
  Update   67 | Ep   698 | reward:    166.0 | mean(100):    253.0 | actor_loss: -0.0027 | value_loss: 7.1132 | lr: 1.96e-04
  Update   68 | Ep   706 | reward:    191.0 | mean(100):    257.1 | actor_loss: -0.0008 | value_loss: 7.3987 | lr: 1.95e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   69 | Ep   714 | reward:    185.0 | mean(100):    262.2 | actor_loss: -0.0018 | value_loss: 7.3309 | lr: 1.94e-04
  Update   70 | Ep   722 | reward:    200.0 | mean(100):    265.5 | actor_loss: -0.0027 | value_loss: 7.3671 | lr: 1.93e-04
  Update   71 | Ep   730 | reward:    346.0 | mean(100):    265.8 | actor_loss: -0.0020 | value_loss: 7.2497 | lr: 1.92e-04
  Update   72 | Ep   736 | reward:    286.0 | mean(100):    270.1 | actor_loss: -0.0022 | value_loss: 6.6996 | lr: 1.90e-04
  Update   73 | Ep   741 | reward:    410.0 | mean(100):    276.2 | actor_loss: -0.0060 | value_loss: 6.3753 | lr: 1.90e-04
  Update   74 | Ep   745 | reward:    500.0 | mean(100):    287.0 | actor_loss: -0.0014 | value_loss: 6.0369 | lr: 1.89e-04
  Update   75 | Ep   749 | reward:    405.0 | mean(100):    295.7 | actor_loss: -0.0024 | value_loss: 5.9466 | lr: 1.88e-04
  Update   76 | Ep   754 | reward:    500.0 | mean(100):    304.0 | actor_loss: -0.0005 | value_loss: 6.1390 | lr: 1.88e-04
  Update   77 | Ep   762 | reward:    335.0 | mean(100):    304.4 | actor_loss: -0.0070 | value_loss: 6.9815 | lr: 1.87e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   78 | Ep   767 | reward:    500.0 | mean(100):    305.4 | actor_loss: -0.0024 | value_loss: 6.0512 | lr: 1.86e-04
  Update   79 | Ep   771 | reward:    500.0 | mean(100):    311.1 | actor_loss: -0.0023 | value_loss: 5.6163 | lr: 1.85e-04
  Update   80 | Ep   776 | reward:    500.0 | mean(100):    318.1 | actor_loss: -0.0027 | value_loss: 5.8564 | lr: 1.84e-04
  Update   81 | Ep   780 | reward:    444.0 | mean(100):    323.0 | actor_loss: -0.0009 | value_loss: 5.4478 | lr: 1.84e-04
  Update   82 | Ep   784 | reward:    500.0 | mean(100):    326.2 | actor_loss: -0.0005 | value_loss: 5.3776 | lr: 1.83e-04
  Update   83 | Ep   788 | reward:    500.0 | mean(100):    329.4 | actor_loss: -0.0008 | value_loss: 5.2997 | lr: 1.82e-04
  Update   84 | Ep   793 | reward:     18.0 | mean(100):    336.0 | actor_loss: -0.0019 | value_loss: 5.5728 | lr: 1.82e-04
  Update   85 | Ep   797 | reward:    500.0 | mean(100):    341.5 | actor_loss: -0.0015 | value_loss: 5.1509 | lr: 1.81e-04
  Update   86 | Ep   803 | reward:    297.0 | mean(100):    344.2 | actor_loss: -0.0060 | value_loss: 5.7712 | lr: 1.80e-04
  Update   87 | Ep   808 | reward:     34.0 | mean(100):    352.6 | actor_loss: -0.0027 | value_loss: 5.4262 | lr: 1.80e-04
  Update   88 | Ep   812 | reward:    500.0 | mean(100):    361.8 | actor_loss: -0.0020 | value_loss: 4.9190 | lr: 1.79e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update   89 | Ep   816 | reward:    500.0 | mean(100):    371.9 | actor_loss: -0.0028 | value_loss: 4.8422 | lr: 1.78e-04
  Update   90 | Ep   820 | reward:    500.0 | mean(100):    381.1 | actor_loss: -0.0020 | value_loss: 4.7717 | lr: 1.78e-04
  Update   91 | Ep   824 | reward:    500.0 | mean(100):    389.5 | actor_loss: -0.0022 | value_loss: 4.7000 | lr: 1.77e-04
  Update   92 | Ep   828 | reward:    500.0 | mean(100):    401.4 | actor_loss: -0.0011 | value_loss: 4.6278 | lr: 1.76e-04
  Update   93 | Ep   832 | reward:    500.0 | mean(100):    408.5 | actor_loss: 0.0007 | value_loss: 4.5613 | lr: 1.76e-04
  Update   94 | Ep   837 | reward:    500.0 | mean(100):    411.5 | actor_loss: -0.0014 | value_loss: 4.8733 | lr: 1.75e-04
  Update   95 | Ep   841 | reward:    500.0 | mean(100):    420.1 | actor_loss: -0.0009 | value_loss: 4.4143 | lr: 1.74e-04
  Update   96 | Ep   845 | reward:    500.0 | mean(100):    420.1 | actor_loss: -0.0005 | value_loss: 4.3457 | lr: 1.74e-04
  Update   97 | Ep   849 | reward:    500.0 | mean(100):    419.7 | actor_loss: -0.0012 | value_loss: 4.2733 | lr: 1.73e-04
  Update   98 | Ep   853 | reward:    500.0 | mean(100):    423.2 | actor_loss: -0.0009 | value_loss: 4.2069 | lr: 1.73e-04
  Update   99 | Ep   858 | reward:    293.0 | mean(100):    424.3 | actor_loss: -0.0070 | value_loss: 4.6495 | lr: 1.72e-04
  Update  100 | Ep   864 | reward:    241.0 | mean(100):    429.9 | actor_loss: -0.0075 | value_loss: 5.1275 | lr: 1.71e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  101 | Ep   868 | reward:    493.0 | mean(100):    433.3 | actor_loss: -0.0011 | value_loss: 4.0066 | lr: 1.70e-04
  Update  102 | Ep   872 | reward:    500.0 | mean(100):    430.9 | actor_loss: -0.0026 | value_loss: 3.9413 | lr: 1.70e-04
  Update  103 | Ep   877 | reward:    500.0 | mean(100):    434.9 | actor_loss: -0.0031 | value_loss: 4.4315 | lr: 1.69e-04
  Update  104 | Ep   881 | reward:    500.0 | mean(100):    435.5 | actor_loss: -0.0014 | value_loss: 3.8143 | lr: 1.68e-04
  Update  105 | Ep   885 | reward:    500.0 | mean(100):    432.6 | actor_loss: -0.0023 | value_loss: 3.7500 | lr: 1.68e-04
  Update  106 | Ep   889 | reward:    500.0 | mean(100):    432.6 | actor_loss: -0.0011 | value_loss: 3.6889 | lr: 1.67e-04
  Update  107 | Ep   893 | reward:    500.0 | mean(100):    437.4 | actor_loss: 0.0002 | value_loss: 3.6261 | lr: 1.67e-04
  Update  108 | Ep   897 | reward:    500.0 | mean(100):    437.4 | actor_loss: -0.0001 | value_loss: 3.5654 | lr: 1.66e-04
  Update  109 | Ep   901 | reward:    500.0 | mean(100):    445.4 | actor_loss: -0.0017 | value_loss: 3.5051 | lr: 1.65e-04
  Update  110 | Ep   908 | reward:    137.0 | mean(100):    437.8 | actor_loss: -0.0040 | value_loss: 5.3352 | lr: 1.65e-04
  Update  111 | Ep   912 | reward:    500.0 | mean(100):    437.8 | actor_loss: -0.0012 | value_loss: 3.3875 | lr: 1.64e-04
  Update  112 | Ep   916 | reward:    500.0 | mean(100):    440.1 | actor_loss: -0.0024 | value_loss: 3.3285 | lr: 1.63e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  113 | Ep   920 | reward:    500.0 | mean(100):    440.1 | actor_loss: -0.0015 | value_loss: 3.2735 | lr: 1.63e-04
  Update  114 | Ep   924 | reward:    449.0 | mean(100):    439.6 | actor_loss: -0.0040 | value_loss: 3.2177 | lr: 1.62e-04
  Update  115 | Ep   929 | reward:    500.0 | mean(100):    433.4 | actor_loss: -0.0005 | value_loss: 3.8560 | lr: 1.61e-04
  Update  116 | Ep   934 | reward:    229.0 | mean(100):    427.4 | actor_loss: -0.0034 | value_loss: 3.8268 | lr: 1.61e-04
  Update  117 | Ep   946 | reward:     77.0 | mean(100):    390.4 | actor_loss: -0.0083 | value_loss: 8.2495 | lr: 1.60e-04
  Update  118 | Ep   952 | reward:    174.0 | mean(100):    383.3 | actor_loss: -0.0032 | value_loss: 4.3542 | lr: 1.58e-04
  Update  119 | Ep   957 | reward:    443.0 | mean(100):    382.7 | actor_loss: -0.0043 | value_loss: 3.7566 | lr: 1.57e-04
  Update  120 | Ep   961 | reward:    227.0 | mean(100):    388.4 | actor_loss: -0.0014 | value_loss: 3.0708 | lr: 1.56e-04
  Update  121 | Ep   965 | reward:    500.0 | mean(100):    394.8 | actor_loss: -0.0011 | value_loss: 3.0595 | lr: 1.56e-04
  Update  122 | Ep   969 | reward:    500.0 | mean(100):    395.5 | actor_loss: -0.0027 | value_loss: 3.0569 | lr: 1.55e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  123 | Ep   973 | reward:    500.0 | mean(100):    397.3 | actor_loss: -0.0021 | value_loss: 3.0548 | lr: 1.55e-04
  Update  124 | Ep   978 | reward:    185.0 | mean(100):    395.4 | actor_loss: -0.0059 | value_loss: 3.8076 | lr: 1.54e-04
  Update  125 | Ep   982 | reward:    500.0 | mean(100):    395.4 | actor_loss: -0.0007 | value_loss: 3.0681 | lr: 1.53e-04
  Update  126 | Ep   986 | reward:    500.0 | mean(100):    397.3 | actor_loss: -0.0016 | value_loss: 3.0570 | lr: 1.53e-04
  Update  127 | Ep   990 | reward:    500.0 | mean(100):    397.3 | actor_loss: -0.0020 | value_loss: 3.0673 | lr: 1.52e-04
  Update  128 | Ep   995 | reward:    500.0 | mean(100):    389.5 | actor_loss: -0.0042 | value_loss: 3.7435 | lr: 1.51e-04
  Update  129 | Ep   999 | reward:    500.0 | mean(100):    387.7 | actor_loss: -0.0002 | value_loss: 3.0335 | lr: 1.51e-04
  Update  130 | Ep  1003 | reward:    500.0 | mean(100):    391.1 | actor_loss: -0.0011 | value_loss: 3.0834 | lr: 1.50e-04
  Update  131 | Ep  1007 | reward:    260.0 | mean(100):    399.2 | actor_loss: -0.0022 | value_loss: 3.0726 | lr: 1.50e-04
  Update  132 | Ep  1011 | reward:    500.0 | mean(100):    398.8 | actor_loss: -0.0023 | value_loss: 3.0899 | lr: 1.49e-04
  Update  133 | Ep  1016 | reward:    500.0 | mean(100):    393.3 | actor_loss: -0.0031 | value_loss: 3.8346 | lr: 1.48e-04
  Update  134 | Ep  1021 | reward:    133.0 | mean(100):    388.0 | actor_loss: -0.0032 | value_loss: 3.8247 | lr: 1.48e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  135 | Ep  1028 | reward:    203.0 | mean(100):    377.7 | actor_loss: -0.0041 | value_loss: 5.2937 | lr: 1.47e-04
  Update  136 | Ep  1034 | reward:    334.0 | mean(100):    372.6 | actor_loss: -0.0043 | value_loss: 4.4267 | lr: 1.46e-04
  Update  137 | Ep  1040 | reward:    500.0 | mean(100):    381.7 | actor_loss: -0.0044 | value_loss: 4.5865 | lr: 1.45e-04
  Update  138 | Ep  1044 | reward:    500.0 | mean(100):    397.5 | actor_loss: -0.0026 | value_loss: 3.0966 | lr: 1.44e-04
  Update  139 | Ep  1049 | reward:    500.0 | mean(100):    406.7 | actor_loss: -0.0059 | value_loss: 3.6824 | lr: 1.43e-04
  Update  140 | Ep  1053 | reward:    500.0 | mean(100):    412.0 | actor_loss: -0.0028 | value_loss: 2.9283 | lr: 1.43e-04
  Update  141 | Ep  1057 | reward:    500.0 | mean(100):    413.6 | actor_loss: 0.0003 | value_loss: 3.0916 | lr: 1.42e-04
  Update  142 | Ep  1061 | reward:    500.0 | mean(100):    415.1 | actor_loss: -0.0034 | value_loss: 3.0963 | lr: 1.41e-04
  Update  143 | Ep  1065 | reward:    500.0 | mean(100):    415.1 | actor_loss: -0.0006 | value_loss: 3.0641 | lr: 1.41e-04
  Update  144 | Ep  1069 | reward:    500.0 | mean(100):    415.1 | actor_loss: -0.0031 | value_loss: 3.1317 | lr: 1.40e-04
  Update  145 | Ep  1073 | reward:    500.0 | mean(100):    415.1 | actor_loss: 0.0002 | value_loss: 3.1121 | lr: 1.40e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  146 | Ep  1077 | reward:    500.0 | mean(100):    417.0 | actor_loss: -0.0008 | value_loss: 3.0516 | lr: 1.39e-04
  Update  147 | Ep  1081 | reward:    500.0 | mean(100):    420.2 | actor_loss: -0.0020 | value_loss: 3.0438 | lr: 1.38e-04
  Update  148 | Ep  1085 | reward:    500.0 | mean(100):    418.1 | actor_loss: -0.0030 | value_loss: 3.1018 | lr: 1.38e-04
  Update  149 | Ep  1089 | reward:    290.0 | mean(100):    416.1 | actor_loss: 0.0005 | value_loss: 3.0369 | lr: 1.37e-04
  Update  150 | Ep  1093 | reward:    500.0 | mean(100):    423.8 | actor_loss: -0.0017 | value_loss: 3.1107 | lr: 1.37e-04
  Update  151 | Ep  1098 | reward:    358.0 | mean(100):    419.5 | actor_loss: -0.0031 | value_loss: 3.7899 | lr: 1.36e-04
  Update  152 | Ep  1103 | reward:    320.0 | mean(100):    413.7 | actor_loss: -0.0037 | value_loss: 3.7449 | lr: 1.35e-04
  Update  153 | Ep  1107 | reward:    500.0 | mean(100):    414.8 | actor_loss: -0.0006 | value_loss: 3.0344 | lr: 1.35e-04
  Update  154 | Ep  1112 | reward:    134.0 | mean(100):    415.8 | actor_loss: -0.0014 | value_loss: 3.8586 | lr: 1.34e-04
  Update  155 | Ep  1116 | reward:    500.0 | mean(100):    415.9 | actor_loss: -0.0061 | value_loss: 3.0605 | lr: 1.33e-04
  Update  156 | Ep  1120 | reward:    500.0 | mean(100):    414.8 | actor_loss: -0.0014 | value_loss: 3.0161 | lr: 1.33e-04
  Update  157 | Ep  1124 | reward:    500.0 | mean(100):    420.4 | actor_loss: -0.0016 | value_loss: 3.0891 | lr: 1.32e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  158 | Ep  1128 | reward:    500.0 | mean(100):    430.7 | actor_loss: -0.0006 | value_loss: 3.0899 | lr: 1.31e-04
  Update  159 | Ep  1133 | reward:    158.0 | mean(100):    432.9 | actor_loss: -0.0043 | value_loss: 3.8379 | lr: 1.31e-04
  Update  160 | Ep  1137 | reward:    500.0 | mean(100):    443.6 | actor_loss: -0.0002 | value_loss: 3.0990 | lr: 1.30e-04
  Update  161 | Ep  1141 | reward:    391.0 | mean(100):    444.4 | actor_loss: -0.0012 | value_loss: 3.0636 | lr: 1.29e-04
  Update  162 | Ep  1145 | reward:    500.0 | mean(100):    442.2 | actor_loss: -0.0050 | value_loss: 3.0315 | lr: 1.29e-04
  Update  163 | Ep  1151 | reward:    259.0 | mean(100):    439.4 | actor_loss: -0.0021 | value_loss: 4.4234 | lr: 1.28e-04
  Update  164 | Ep  1155 | reward:    500.0 | mean(100):    439.4 | actor_loss: -0.0009 | value_loss: 3.1045 | lr: 1.27e-04
  Update  165 | Ep  1159 | reward:    500.0 | mean(100):    439.5 | actor_loss: -0.0016 | value_loss: 3.0976 | lr: 1.27e-04
  Update  166 | Ep  1163 | reward:    500.0 | mean(100):    435.0 | actor_loss: -0.0015 | value_loss: 3.0995 | lr: 1.26e-04
  Update  167 | Ep  1167 | reward:    500.0 | mean(100):    435.0 | actor_loss: -0.0015 | value_loss: 3.1114 | lr: 1.26e-04
  Update  168 | Ep  1171 | reward:    500.0 | mean(100):    435.0 | actor_loss: -0.0001 | value_loss: 3.1018 | lr: 1.25e-04
  Update  169 | Ep  1175 | reward:    500.0 | mean(100):    436.9 | actor_loss: -0.0004 | value_loss: 3.1062 | lr: 1.24e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  170 | Ep  1179 | reward:    500.0 | mean(100):    433.5 | actor_loss: -0.0031 | value_loss: 3.1025 | lr: 1.24e-04
  Update  171 | Ep  1183 | reward:    500.0 | mean(100):    436.6 | actor_loss: -0.0019 | value_loss: 3.1042 | lr: 1.23e-04
  Update  172 | Ep  1188 | reward:    125.0 | mean(100):    429.9 | actor_loss: -0.0035 | value_loss: 3.8465 | lr: 1.23e-04
  Update  173 | Ep  1192 | reward:    500.0 | mean(100):    429.0 | actor_loss: -0.0036 | value_loss: 3.0972 | lr: 1.22e-04
  Update  174 | Ep  1197 | reward:    220.0 | mean(100):    424.6 | actor_loss: -0.0044 | value_loss: 3.8664 | lr: 1.21e-04
  Update  175 | Ep  1201 | reward:    500.0 | mean(100):    430.0 | actor_loss: -0.0009 | value_loss: 3.0893 | lr: 1.20e-04
  Update  176 | Ep  1205 | reward:    500.0 | mean(100):    433.1 | actor_loss: -0.0021 | value_loss: 3.0425 | lr: 1.20e-04
  Update  177 | Ep  1209 | reward:    500.0 | mean(100):    433.1 | actor_loss: -0.0005 | value_loss: 3.0609 | lr: 1.19e-04
  Update  178 | Ep  1213 | reward:    500.0 | mean(100):    439.6 | actor_loss: -0.0011 | value_loss: 3.0630 | lr: 1.19e-04
  Update  179 | Ep  1217 | reward:    500.0 | mean(100):    442.8 | actor_loss: -0.0006 | value_loss: 3.0738 | lr: 1.18e-04
  Update  180 | Ep  1221 | reward:    500.0 | mean(100):    445.6 | actor_loss: -0.0001 | value_loss: 3.0676 | lr: 1.17e-04
  Update  181 | Ep  1225 | reward:    500.0 | mean(100):    450.4 | actor_loss: -0.0009 | value_loss: 3.1065 | lr: 1.17e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  182 | Ep  1229 | reward:    500.0 | mean(100):    454.0 | actor_loss: -0.0003 | value_loss: 3.1071 | lr: 1.16e-04
  Update  183 | Ep  1234 | reward:    500.0 | mean(100):    451.4 | actor_loss: -0.0019 | value_loss: 3.8641 | lr: 1.16e-04
  Update  184 | Ep  1239 | reward:    500.0 | mean(100):    443.1 | actor_loss: -0.0028 | value_loss: 3.7256 | lr: 1.15e-04
  Update  185 | Ep  1244 | reward:    500.0 | mean(100):    442.9 | actor_loss: -0.0047 | value_loss: 3.8563 | lr: 1.14e-04
  Update  186 | Ep  1248 | reward:    500.0 | mean(100):    445.7 | actor_loss: -0.0011 | value_loss: 3.1072 | lr: 1.13e-04
  Update  187 | Ep  1252 | reward:    500.0 | mean(100):    452.9 | actor_loss: -0.0009 | value_loss: 3.0997 | lr: 1.13e-04
  Update  188 | Ep  1256 | reward:    500.0 | mean(100):    450.1 | actor_loss: 0.0001 | value_loss: 3.0771 | lr: 1.12e-04
  Update  189 | Ep  1260 | reward:    500.0 | mean(100):    451.3 | actor_loss: -0.0019 | value_loss: 3.1004 | lr: 1.12e-04
  Update  190 | Ep  1266 | reward:     25.0 | mean(100):    445.8 | actor_loss: -0.0042 | value_loss: 4.4722 | lr: 1.11e-04
  Update  191 | Ep  1271 | reward:     32.0 | mean(100):    437.2 | actor_loss: -0.0028 | value_loss: 3.7731 | lr: 1.10e-04
  Update  192 | Ep  1275 | reward:    500.0 | mean(100):    437.1 | actor_loss: -0.0004 | value_loss: 3.0880 | lr: 1.09e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  193 | Ep  1279 | reward:    500.0 | mean(100):    440.5 | actor_loss: -0.0006 | value_loss: 3.0826 | lr: 1.09e-04
  Update  194 | Ep  1283 | reward:    295.0 | mean(100):    438.5 | actor_loss: -0.0029 | value_loss: 3.0737 | lr: 1.08e-04
  Update  195 | Ep  1288 | reward:    500.0 | mean(100):    440.3 | actor_loss: -0.0037 | value_loss: 3.4391 | lr: 1.08e-04
  Update  196 | Ep  1292 | reward:    485.0 | mean(100):    443.1 | actor_loss: -0.0036 | value_loss: 3.0659 | lr: 1.07e-04
  Update  197 | Ep  1296 | reward:    464.0 | mean(100):    449.0 | actor_loss: -0.0007 | value_loss: 3.0348 | lr: 1.06e-04
  Update  198 | Ep  1300 | reward:    500.0 | mean(100):    450.4 | actor_loss: -0.0030 | value_loss: 2.9837 | lr: 1.06e-04
  Update  199 | Ep  1304 | reward:    347.0 | mean(100):    449.1 | actor_loss: -0.0035 | value_loss: 3.0353 | lr: 1.05e-04
  Update  200 | Ep  1308 | reward:    500.0 | mean(100):    449.1 | actor_loss: -0.0013 | value_loss: 3.0582 | lr: 1.04e-04
  Update  201 | Ep  1312 | reward:    500.0 | mean(100):    449.1 | actor_loss: -0.0003 | value_loss: 3.0393 | lr: 1.04e-04
  Update  202 | Ep  1316 | reward:    500.0 | mean(100):    449.1 | actor_loss: -0.0026 | value_loss: 3.0727 | lr: 1.03e-04
  Update  203 | Ep  1320 | reward:    500.0 | mean(100):    449.1 | actor_loss: -0.0013 | value_loss: 3.0820 | lr: 1.03e-04
  Update  204 | Ep  1324 | reward:    500.0 | mean(100):    449.1 | actor_loss: -0.0014 | value_loss: 3.0712 | lr: 1.02e-04
  Update  205 | Ep  1329 | reward:    330.0 | mean(100):    441.6 | actor_loss: -0.0038 | value_loss: 3.7983 | lr: 1.01e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  206 | Ep  1333 | reward:    500.0 | mean(100):    447.6 | actor_loss: -0.0004 | value_loss: 3.0665 | lr: 1.01e-04
  Update  207 | Ep  1337 | reward:    500.0 | mean(100):    451.1 | actor_loss: -0.0016 | value_loss: 3.0763 | lr: 1.00e-04
  Update  208 | Ep  1342 | reward:    368.0 | mean(100):    455.2 | actor_loss: -0.0024 | value_loss: 3.8491 | lr: 9.94e-05
  Update  209 | Ep  1346 | reward:    500.0 | mean(100):    453.1 | actor_loss: -0.0011 | value_loss: 3.0616 | lr: 9.87e-05
  Update  210 | Ep  1350 | reward:    500.0 | mean(100):    453.1 | actor_loss: -0.0010 | value_loss: 3.0740 | lr: 9.81e-05
  Update  211 | Ep  1354 | reward:    500.0 | mean(100):    455.5 | actor_loss: -0.0033 | value_loss: 3.0754 | lr: 9.75e-05
  Update  212 | Ep  1358 | reward:    500.0 | mean(100):    455.5 | actor_loss: -0.0007 | value_loss: 3.0986 | lr: 9.69e-05
  Update  213 | Ep  1362 | reward:    500.0 | mean(100):    456.8 | actor_loss: -0.0032 | value_loss: 3.0863 | lr: 9.63e-05
  Update  214 | Ep  1366 | reward:    500.0 | mean(100):    465.4 | actor_loss: -0.0027 | value_loss: 3.0912 | lr: 9.57e-05
  Update  215 | Ep  1371 | reward:    500.0 | mean(100):    469.4 | actor_loss: -0.0038 | value_loss: 3.8027 | lr: 9.51e-05
  Update  216 | Ep  1375 | reward:    500.0 | mean(100):    469.5 | actor_loss: -0.0005 | value_loss: 3.0827 | lr: 9.43e-05
  Update  217 | Ep  1380 | reward:    500.0 | mean(100):    463.4 | actor_loss: -0.0037 | value_loss: 3.6493 | lr: 9.37e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  218 | Ep  1384 | reward:    500.0 | mean(100):    465.4 | actor_loss: -0.0026 | value_loss: 3.0782 | lr: 9.30e-05
  Update  219 | Ep  1388 | reward:    500.0 | mean(100):    470.3 | actor_loss: -0.0001 | value_loss: 3.0887 | lr: 9.24e-05
  Update  220 | Ep  1392 | reward:    500.0 | mean(100):    470.5 | actor_loss: -0.0017 | value_loss: 3.0922 | lr: 9.18e-05
  Update  221 | Ep  1396 | reward:    500.0 | mean(100):    470.9 | actor_loss: -0.0002 | value_loss: 3.0836 | lr: 9.12e-05
  Update  222 | Ep  1400 | reward:    500.0 | mean(100):    469.4 | actor_loss: -0.0028 | value_loss: 3.0844 | lr: 9.06e-05
  Update  223 | Ep  1404 | reward:    500.0 | mean(100):    470.9 | actor_loss: -0.0024 | value_loss: 3.0914 | lr: 9.00e-05
  Update  224 | Ep  1410 | reward:     65.0 | mean(100):    460.0 | actor_loss: -0.0087 | value_loss: 4.6022 | lr: 8.94e-05
  Update  225 | Ep  1414 | reward:    500.0 | mean(100):    460.0 | actor_loss: -0.0005 | value_loss: 3.0811 | lr: 8.85e-05
  Update  226 | Ep  1419 | reward:    500.0 | mean(100):    455.2 | actor_loss: -0.0010 | value_loss: 3.6742 | lr: 8.79e-05
  Update  227 | Ep  1423 | reward:    500.0 | mean(100):    455.2 | actor_loss: -0.0024 | value_loss: 3.0853 | lr: 8.71e-05
  Update  228 | Ep  1427 | reward:    500.0 | mean(100):    459.3 | actor_loss: -0.0022 | value_loss: 3.0835 | lr: 8.65e-05
  Update  229 | Ep  1431 | reward:    370.0 | mean(100):    461.5 | actor_loss: -0.0019 | value_loss: 3.0830 | lr: 8.59e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  230 | Ep  1436 | reward:    500.0 | mean(100):    456.7 | actor_loss: -0.0005 | value_loss: 3.6198 | lr: 8.53e-05
  Update  231 | Ep  1440 | reward:    203.0 | mean(100):    453.7 | actor_loss: -0.0021 | value_loss: 3.0798 | lr: 8.46e-05
  Update  232 | Ep  1444 | reward:    500.0 | mean(100):    457.4 | actor_loss: -0.0008 | value_loss: 3.0859 | lr: 8.40e-05
  Update  233 | Ep  1448 | reward:    174.0 | mean(100):    454.2 | actor_loss: -0.0015 | value_loss: 3.0777 | lr: 8.34e-05
  Update  234 | Ep  1452 | reward:    500.0 | mean(100):    454.6 | actor_loss: -0.0015 | value_loss: 3.0864 | lr: 8.28e-05
  Update  235 | Ep  1456 | reward:    500.0 | mean(100):    454.6 | actor_loss: -0.0012 | value_loss: 3.0841 | lr: 8.22e-05
  Update  236 | Ep  1463 | reward:    500.0 | mean(100):    439.3 | actor_loss: -0.0058 | value_loss: 5.0606 | lr: 8.16e-05
  Update  237 | Ep  1469 | reward:    353.0 | mean(100):    434.2 | actor_loss: -0.0024 | value_loss: 4.5617 | lr: 8.05e-05
  Update  238 | Ep  1473 | reward:    500.0 | mean(100):    434.2 | actor_loss: -0.0008 | value_loss: 3.0862 | lr: 7.96e-05
  Update  239 | Ep  1477 | reward:    500.0 | mean(100):    433.8 | actor_loss: -0.0011 | value_loss: 3.0863 | lr: 7.90e-05
  Update  240 | Ep  1482 | reward:    202.0 | mean(100):    431.3 | actor_loss: -0.0030 | value_loss: 3.8475 | lr: 7.84e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  241 | Ep  1486 | reward:    500.0 | mean(100):    431.3 | actor_loss: -0.0003 | value_loss: 3.0879 | lr: 7.77e-05
  Update  242 | Ep  1490 | reward:    500.0 | mean(100):    431.3 | actor_loss: -0.0006 | value_loss: 3.0858 | lr: 7.71e-05
  Update  243 | Ep  1494 | reward:    500.0 | mean(100):    431.3 | actor_loss: -0.0002 | value_loss: 3.0784 | lr: 7.65e-05
  Update  244 | Ep  1498 | reward:    500.0 | mean(100):    430.1 | actor_loss: -0.0014 | value_loss: 3.0813 | lr: 7.59e-05
  Update  245 | Ep  1502 | reward:    500.0 | mean(100):    433.0 | actor_loss: -0.0004 | value_loss: 3.0880 | lr: 7.53e-05
  Update  246 | Ep  1506 | reward:    500.0 | mean(100):    434.5 | actor_loss: -0.0002 | value_loss: 3.0835 | lr: 7.47e-05
  Update  247 | Ep  1510 | reward:    500.0 | mean(100):    443.9 | actor_loss: -0.0021 | value_loss: 3.0813 | lr: 7.41e-05
  Update  248 | Ep  1514 | reward:    500.0 | mean(100):    443.9 | actor_loss: -0.0002 | value_loss: 3.0809 | lr: 7.35e-05
  Update  249 | Ep  1518 | reward:    500.0 | mean(100):    448.7 | actor_loss: -0.0001 | value_loss: 3.0971 | lr: 7.29e-05
  Update  250 | Ep  1522 | reward:    500.0 | mean(100):    448.7 | actor_loss: -0.0006 | value_loss: 3.0865 | lr: 7.23e-05
  Update  251 | Ep  1526 | reward:    500.0 | mean(100):    448.7 | actor_loss: -0.0024 | value_loss: 3.0810 | lr: 7.17e-05
  Update  252 | Ep  1531 | reward:    256.0 | mean(100):    443.0 | actor_loss: -0.0044 | value_loss: 3.8579 | lr: 7.11e-05
  Update  253 | Ep  1535 | reward:    500.0 | mean(100):    447.8 | actor_loss: -0.0023 | value_loss: 3.0786 | lr: 7.04e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  254 | Ep  1539 | reward:    500.0 | mean(100):    447.8 | actor_loss: -0.0009 | value_loss: 3.0910 | lr: 6.98e-05
  Update  255 | Ep  1545 | reward:    500.0 | mean(100):    443.5 | actor_loss: -0.0019 | value_loss: 4.6167 | lr: 6.92e-05
  Update  256 | Ep  1549 | reward:    500.0 | mean(100):    446.7 | actor_loss: -0.0012 | value_loss: 3.0888 | lr: 6.83e-05
  Update  257 | Ep  1553 | reward:    500.0 | mean(100):    446.7 | actor_loss: -0.0010 | value_loss: 3.0952 | lr: 6.77e-05
  Update  258 | Ep  1559 | reward:    203.0 | mean(100):    441.9 | actor_loss: -0.0057 | value_loss: 4.6175 | lr: 6.71e-05
  Update  259 | Ep  1563 | reward:    500.0 | mean(100):    451.4 | actor_loss: -0.0009 | value_loss: 3.0792 | lr: 6.62e-05
  Update  260 | Ep  1567 | reward:    500.0 | mean(100):    457.2 | actor_loss: -0.0001 | value_loss: 3.0662 | lr: 6.56e-05
  Update  261 | Ep  1572 | reward:    500.0 | mean(100):    453.6 | actor_loss: -0.0016 | value_loss: 3.7793 | lr: 6.50e-05
  Update  262 | Ep  1577 | reward:    500.0 | mean(100):    450.5 | actor_loss: -0.0006 | value_loss: 3.6412 | lr: 6.42e-05
  Update  263 | Ep  1581 | reward:    500.0 | mean(100):    454.8 | actor_loss: -0.0013 | value_loss: 3.0986 | lr: 6.34e-05
  Update  264 | Ep  1585 | reward:    500.0 | mean(100):    455.3 | actor_loss: -0.0010 | value_loss: 3.0960 | lr: 6.28e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  265 | Ep  1589 | reward:    500.0 | mean(100):    455.3 | actor_loss: -0.0013 | value_loss: 3.0993 | lr: 6.22e-05
  Update  266 | Ep  1594 | reward:    500.0 | mean(100):    447.8 | actor_loss: -0.0022 | value_loss: 3.8553 | lr: 6.16e-05
  Update  267 | Ep  1598 | reward:    500.0 | mean(100):    449.0 | actor_loss: -0.0020 | value_loss: 3.0909 | lr: 6.09e-05
  Update  268 | Ep  1605 | reward:    500.0 | mean(100):    432.4 | actor_loss: -0.0063 | value_loss: 5.2096 | lr: 6.03e-05
  Update  269 | Ep  1609 | reward:    500.0 | mean(100):    432.4 | actor_loss: -0.0001 | value_loss: 3.0957 | lr: 5.92e-05
  Update  270 | Ep  1613 | reward:    500.0 | mean(100):    430.0 | actor_loss: -0.0019 | value_loss: 3.0789 | lr: 5.86e-05
  Update  271 | Ep  1617 | reward:    326.0 | mean(100):    428.3 | actor_loss: -0.0025 | value_loss: 3.0888 | lr: 5.80e-05
  Update  272 | Ep  1621 | reward:    500.0 | mean(100):    428.3 | actor_loss: -0.0031 | value_loss: 3.0921 | lr: 5.74e-05
  Update  273 | Ep  1625 | reward:    500.0 | mean(100):    428.3 | actor_loss: -0.0017 | value_loss: 3.0919 | lr: 5.68e-05
  Update  274 | Ep  1629 | reward:    500.0 | mean(100):    432.8 | actor_loss: -0.0005 | value_loss: 3.0900 | lr: 5.62e-05
  Update  275 | Ep  1633 | reward:    500.0 | mean(100):    435.3 | actor_loss: -0.0020 | value_loss: 3.0875 | lr: 5.56e-05
  Update  276 | Ep  1637 | reward:    500.0 | mean(100):    435.3 | actor_loss: -0.0001 | value_loss: 3.0881 | lr: 5.50e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  277 | Ep  1641 | reward:    500.0 | mean(100):    442.1 | actor_loss: -0.0005 | value_loss: 3.0858 | lr: 5.44e-05
  Update  278 | Ep  1645 | reward:    500.0 | mean(100):    446.4 | actor_loss: -0.0004 | value_loss: 3.0852 | lr: 5.38e-05
  Update  279 | Ep  1649 | reward:    500.0 | mean(100):    446.4 | actor_loss: -0.0016 | value_loss: 3.0818 | lr: 5.32e-05
  Update  280 | Ep  1653 | reward:    500.0 | mean(100):    446.4 | actor_loss: -0.0010 | value_loss: 3.0860 | lr: 5.26e-05
  Update  281 | Ep  1657 | reward:    355.0 | mean(100):    451.5 | actor_loss: -0.0025 | value_loss: 3.0954 | lr: 5.20e-05
  Update  282 | Ep  1661 | reward:    500.0 | mean(100):    455.5 | actor_loss: -0.0002 | value_loss: 3.0872 | lr: 5.14e-05
  Update  283 | Ep  1665 | reward:    221.0 | mean(100):    455.2 | actor_loss: -0.0035 | value_loss: 3.0836 | lr: 5.08e-05
  Update  284 | Ep  1669 | reward:    500.0 | mean(100):    458.4 | actor_loss: -0.0010 | value_loss: 3.0854 | lr: 5.02e-05
  Update  285 | Ep  1673 | reward:    500.0 | mean(100):    460.3 | actor_loss: -0.0001 | value_loss: 3.0852 | lr: 4.96e-05
  Update  286 | Ep  1677 | reward:    500.0 | mean(100):    465.1 | actor_loss: 0.0001 | value_loss: 3.0817 | lr: 4.90e-05
  Update  287 | Ep  1681 | reward:    500.0 | mean(100):    465.1 | actor_loss: -0.0000 | value_loss: 3.0867 | lr: 4.84e-05
  Update  288 | Ep  1685 | reward:    500.0 | mean(100):    463.8 | actor_loss: -0.0004 | value_loss: 3.0888 | lr: 4.78e-05
  Update  289 | Ep  1689 | reward:    500.0 | mean(100):    463.8 | actor_loss: -0.0007 | value_loss: 3.0902 | lr: 4.72e-05
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
  Update  290 | Ep  1693 | reward:    500.0 | mean(100):    471.2 | actor_loss: -0.0008 | value_loss: 3.0863 | lr: 4.66e-05
  Update  291 | Ep  1697 | reward:    500.0 | mean(100):    468.4 | actor_loss: -0.0020 | value_loss: 3.0822 | lr: 4.60e-05
  Update  292 | Ep  1701 | reward:    353.0 | mean(100):    477.3 | actor_loss: -0.0035 | value_loss: 3.0913 | lr: 4.54e-05

Solved at episode 1701 (update 292) with mean 477.3!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards.png
