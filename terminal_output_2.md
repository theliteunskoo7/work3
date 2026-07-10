Using device: cuda (rollout collection stays on CPU; batched PPO update uses cuda)
Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    20 | reward:   -258.7 | mean(100):   -175.7 | actor_loss: -0.0062 | value_loss: 63.5907 | lr: 3.00e-04
  Update    2 | Ep    42 | reward:   -248.8 | mean(100):   -194.5 | actor_loss: -0.0160 | value_loss: 81.8322 | lr: 2.97e-04
  Update    3 | Ep    64 | reward:   -157.3 | mean(100):   -177.2 | actor_loss: -0.0091 | value_loss: 54.2153 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update    4 | Ep    85 | reward:    -80.5 | mean(100):   -160.7 | actor_loss: -0.0104 | value_loss: 41.3712 | lr: 2.90e-04
  Update    5 | Ep   105 | reward:    -80.2 | mean(100):   -149.0 | actor_loss: -0.0051 | value_loss: 37.3521 | lr: 2.87e-04
  Update    6 | Ep   127 | reward:   -102.9 | mean(100):   -131.4 | actor_loss: -0.0076 | value_loss: 34.3487 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update    7 | Ep   148 | reward:   -114.5 | mean(100):   -100.9 | actor_loss: -0.0075 | value_loss: 29.1862 | lr: 2.81e-04
  Update    8 | Ep   169 | reward:    -80.2 | mean(100):    -83.2 | actor_loss: -0.0047 | value_loss: 25.5747 | lr: 2.78e-04
  Update    9 | Ep   189 | reward:    -39.2 | mean(100):    -74.1 | actor_loss: -0.0066 | value_loss: 22.4361 | lr: 2.75e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   10 | Ep   209 | reward:    -80.6 | mean(100):    -64.7 | actor_loss: -0.0060 | value_loss: 22.8338 | lr: 2.72e-04
  Update   11 | Ep   229 | reward:    -53.5 | mean(100):    -55.8 | actor_loss: -0.0047 | value_loss: 22.8111 | lr: 2.69e-04
  Update   12 | Ep   249 | reward:    -36.4 | mean(100):    -50.9 | actor_loss: -0.0044 | value_loss: 25.1018 | lr: 2.66e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   13 | Ep   269 | reward:    -54.5 | mean(100):    -52.9 | actor_loss: -0.0055 | value_loss: 24.3123 | lr: 2.63e-04
  Update   14 | Ep   288 | reward:    -22.6 | mean(100):    -55.7 | actor_loss: -0.0066 | value_loss: 25.0203 | lr: 2.60e-04
  Update   15 | Ep   298 | reward:    -57.6 | mean(100):    -54.7 | actor_loss: -0.0070 | value_loss: 17.3931 | lr: 2.57e-04
  Update   16 | Ep   317 | reward:    -67.6 | mean(100):    -52.1 | actor_loss: -0.0053 | value_loss: 21.6500 | lr: 2.55e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   17 | Ep   337 | reward:    -18.6 | mean(100):    -50.9 | actor_loss: -0.0058 | value_loss: 20.1489 | lr: 2.52e-04
  Update   18 | Ep   356 | reward:    -40.6 | mean(100):    -48.6 | actor_loss: -0.0045 | value_loss: 20.8356 | lr: 2.49e-04
  Update   19 | Ep   370 | reward:    -44.0 | mean(100):    -44.4 | actor_loss: -0.0056 | value_loss: 18.9511 | lr: 2.47e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   20 | Ep   387 | reward:    -12.3 | mean(100):    -34.6 | actor_loss: -0.0057 | value_loss: 18.2392 | lr: 2.44e-04
  Update   21 | Ep   403 | reward:    -44.2 | mean(100):    -31.5 | actor_loss: -0.0057 | value_loss: 19.7195 | lr: 2.42e-04
  Update   22 | Ep   412 | reward:     25.4 | mean(100):    -30.1 | actor_loss: -0.0052 | value_loss: 14.8309 | lr: 2.40e-04
  Update   23 | Ep   414 | reward:     14.3 | mean(100):    -28.1 | actor_loss: -0.0015 | value_loss: 10.8020 | lr: 2.38e-04
  Update   24 | Ep   423 | reward:     75.3 | mean(100):    -24.8 | actor_loss: -0.0064 | value_loss: 14.6791 | lr: 2.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   25 | Ep   425 | reward:    118.0 | mean(100):    -23.2 | actor_loss: -0.0038 | value_loss: 9.8207 | lr: 2.37e-04
  Update   26 | Ep   442 | reward:    -38.5 | mean(100):    -18.3 | actor_loss: -0.0067 | value_loss: 17.1227 | lr: 2.36e-04
  Update   27 | Ep   451 | reward:    138.5 | mean(100):    -13.1 | actor_loss: -0.0045 | value_loss: 12.3962 | lr: 2.34e-04
  Update   28 | Ep   461 | reward:      4.9 | mean(100):     -8.6 | actor_loss: -0.0042 | value_loss: 14.9915 | lr: 2.32e-04
  Update   29 | Ep   469 | reward:    -24.5 | mean(100):     -8.3 | actor_loss: -0.0077 | value_loss: 15.9212 | lr: 2.31e-04
  Update   30 | Ep   477 | reward:     -9.0 | mean(100):     -7.2 | actor_loss: -0.0028 | value_loss: 15.0069 | lr: 2.30e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   31 | Ep   486 | reward:     30.5 | mean(100):     -9.0 | actor_loss: -0.0037 | value_loss: 16.4314 | lr: 2.28e-04
  Update   32 | Ep   491 | reward:    -14.9 | mean(100):     -6.3 | actor_loss: -0.0071 | value_loss: 11.4648 | lr: 2.27e-04
  Update   33 | Ep   500 | reward:    -42.4 | mean(100):     -3.7 | actor_loss: -0.0033 | value_loss: 13.9056 | lr: 2.26e-04
  Update   34 | Ep   509 | reward:    -24.6 | mean(100):     -1.5 | actor_loss: -0.0074 | value_loss: 14.5964 | lr: 2.25e-04
  Update   35 | Ep   515 | reward:    -56.4 | mean(100):     -1.2 | actor_loss: -0.0036 | value_loss: 12.1984 | lr: 2.24e-04
  Update   36 | Ep   520 | reward:     22.3 | mean(100):      1.4 | actor_loss: -0.0053 | value_loss: 10.1330 | lr: 2.23e-04
  Update   37 | Ep   528 | reward:      6.6 | mean(100):     -0.8 | actor_loss: -0.0041 | value_loss: 13.5980 | lr: 2.22e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   38 | Ep   536 | reward:    -21.7 | mean(100):     -0.7 | actor_loss: -0.0064 | value_loss: 10.5241 | lr: 2.21e-04
  Update   39 | Ep   542 | reward:    -48.2 | mean(100):      1.3 | actor_loss: -0.0069 | value_loss: 11.6459 | lr: 2.20e-04
  Update   40 | Ep   544 | reward:     66.3 | mean(100):      3.8 | actor_loss: -0.0060 | value_loss: 6.7513 | lr: 2.19e-04
  Update   41 | Ep   551 | reward:     28.2 | mean(100):      5.0 | actor_loss: -0.0054 | value_loss: 12.2957 | lr: 2.18e-04
  Update   42 | Ep   553 | reward:    141.1 | mean(100):      7.5 | actor_loss: -0.0036 | value_loss: 8.1713 | lr: 2.17e-04
  Update   43 | Ep   556 | reward:     69.6 | mean(100):     10.7 | actor_loss: -0.0039 | value_loss: 8.4000 | lr: 2.17e-04
  Update   44 | Ep   558 | reward:   -196.4 | mean(100):      8.4 | actor_loss: -0.0038 | value_loss: 12.5317 | lr: 2.17e-04
  Update   45 | Ep   560 | reward:     68.3 | mean(100):     10.6 | actor_loss: -0.0031 | value_loss: 6.8404 | lr: 2.16e-04
  Update   46 | Ep   562 | reward:    114.0 | mean(100):     11.8 | actor_loss: -0.0020 | value_loss: 6.4526 | lr: 2.16e-04
  Update   47 | Ep   564 | reward:    128.9 | mean(100):     15.0 | actor_loss: -0.0068 | value_loss: 6.5569 | lr: 2.16e-04
  Update   48 | Ep   566 | reward:    148.3 | mean(100):     18.2 | actor_loss: -0.0030 | value_loss: 7.4507 | lr: 2.15e-04
  Update   49 | Ep   568 | reward:    138.9 | mean(100):     20.2 | actor_loss: -0.0026 | value_loss: 7.9203 | lr: 2.15e-04
  Update   50 | Ep   572 | reward:     44.3 | mean(100):     22.1 | actor_loss: -0.0047 | value_loss: 10.8066 | lr: 2.15e-04
  Update   51 | Ep   574 | reward:     91.6 | mean(100):     24.1 | actor_loss: -0.0051 | value_loss: 4.9983 | lr: 2.14e-04
  Update   52 | Ep   576 | reward:    152.9 | mean(100):     26.7 | actor_loss: -0.0035 | value_loss: 5.7337 | lr: 2.14e-04
  Update   53 | Ep   579 | reward:     11.6 | mean(100):     29.1 | actor_loss: -0.0026 | value_loss: 7.7761 | lr: 2.14e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   54 | Ep   581 | reward:    123.4 | mean(100):     32.1 | actor_loss: -0.0071 | value_loss: 4.7428 | lr: 2.13e-04
  Update   55 | Ep   583 | reward:    101.5 | mean(100):     35.0 | actor_loss: -0.0068 | value_loss: 6.1565 | lr: 2.13e-04
  Update   56 | Ep   585 | reward:     66.3 | mean(100):     38.8 | actor_loss: -0.0049 | value_loss: 5.6704 | lr: 2.13e-04
  Update   57 | Ep   587 | reward:     23.6 | mean(100):     39.2 | actor_loss: -0.0064 | value_loss: 5.5547 | lr: 2.12e-04
  Update   58 | Ep   589 | reward:    162.2 | mean(100):     41.3 | actor_loss: -0.0046 | value_loss: 4.9632 | lr: 2.12e-04
  Update   59 | Ep   591 | reward:    106.4 | mean(100):     43.4 | actor_loss: -0.0014 | value_loss: 4.7337 | lr: 2.12e-04
  Update   60 | Ep   593 | reward:      4.7 | mean(100):     44.5 | actor_loss: -0.0031 | value_loss: 8.2750 | lr: 2.11e-04
  Update   61 | Ep   595 | reward:     88.1 | mean(100):     46.5 | actor_loss: -0.0045 | value_loss: 4.8998 | lr: 2.11e-04
  Update   62 | Ep   597 | reward:    144.4 | mean(100):     49.0 | actor_loss: -0.0031 | value_loss: 5.6568 | lr: 2.11e-04
  Update   63 | Ep   599 | reward:   -137.9 | mean(100):     47.2 | actor_loss: -0.0074 | value_loss: 11.0663 | lr: 2.10e-04
  Update   64 | Ep   601 | reward:    101.3 | mean(100):     50.4 | actor_loss: -0.0064 | value_loss: 5.1065 | lr: 2.10e-04
  Update   65 | Ep   603 | reward:   -159.4 | mean(100):     50.4 | actor_loss: -0.0026 | value_loss: 13.9977 | lr: 2.10e-04
  Update   66 | Ep   605 | reward:    153.3 | mean(100):     52.6 | actor_loss: -0.0076 | value_loss: 5.5813 | lr: 2.10e-04
  Update   67 | Ep   607 | reward:    102.5 | mean(100):     54.2 | actor_loss: -0.0051 | value_loss: 6.0852 | lr: 2.09e-04
  Update   68 | Ep   609 | reward:     66.7 | mean(100):     54.8 | actor_loss: -0.0070 | value_loss: 5.9440 | lr: 2.09e-04
  Update   69 | Ep   611 | reward:     38.7 | mean(100):     56.3 | actor_loss: -0.0039 | value_loss: 3.9985 | lr: 2.09e-04
  Update   70 | Ep   615 | reward:     64.6 | mean(100):     53.6 | actor_loss: -0.0034 | value_loss: 17.6108 | lr: 2.08e-04
  Update   71 | Ep   618 | reward:   -104.3 | mean(100):     53.1 | actor_loss: -0.0022 | value_loss: 12.8583 | lr: 2.08e-04
  Update   72 | Ep   620 | reward:     90.6 | mean(100):     53.0 | actor_loss: -0.0014 | value_loss: 9.5549 | lr: 2.07e-04
  Update   73 | Ep   624 | reward:    -57.0 | mean(100):     51.7 | actor_loss: -0.0037 | value_loss: 17.4017 | lr: 2.07e-04
  Update   74 | Ep   626 | reward:     94.7 | mean(100):     53.0 | actor_loss: -0.0061 | value_loss: 4.9670 | lr: 2.06e-04
  Update   75 | Ep   628 | reward:     95.9 | mean(100):     55.0 | actor_loss: -0.0052 | value_loss: 5.5853 | lr: 2.06e-04
  Update   76 | Ep   630 | reward:    159.5 | mean(100):     56.8 | actor_loss: -0.0053 | value_loss: 11.6461 | lr: 2.06e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update   77 | Ep   632 | reward:     99.8 | mean(100):     56.7 | actor_loss: -0.0103 | value_loss: 7.4464 | lr: 2.06e-04
  Update   78 | Ep   634 | reward:     88.3 | mean(100):     58.3 | actor_loss: -0.0038 | value_loss: 6.5462 | lr: 2.05e-04
  Update   79 | Ep   637 | reward:    127.1 | mean(100):     59.2 | actor_loss: -0.0071 | value_loss: 13.6827 | lr: 2.05e-04
  Update   80 | Ep   639 | reward:    122.7 | mean(100):     60.8 | actor_loss: -0.0072 | value_loss: 3.5286 | lr: 2.04e-04
  Update   81 | Ep   641 | reward:    106.3 | mean(100):     62.0 | actor_loss: -0.0047 | value_loss: 4.4848 | lr: 2.04e-04
  Update   82 | Ep   643 | reward:     74.6 | mean(100):     62.7 | actor_loss: -0.0017 | value_loss: 4.1766 | lr: 2.04e-04
  Update   83 | Ep   645 | reward:     79.6 | mean(100):     63.3 | actor_loss: -0.0040 | value_loss: 3.8620 | lr: 2.04e-04
  Update   84 | Ep   647 | reward:    -75.5 | mean(100):     62.9 | actor_loss: -0.0109 | value_loss: 9.6887 | lr: 2.03e-04
  Update   85 | Ep   649 | reward:    150.5 | mean(100):     63.7 | actor_loss: -0.0036 | value_loss: 5.3545 | lr: 2.03e-04
  Update   86 | Ep   651 | reward:    119.8 | mean(100):     65.5 | actor_loss: -0.0032 | value_loss: 3.5497 | lr: 2.03e-04
  Update   87 | Ep   653 | reward:    150.6 | mean(100):     64.9 | actor_loss: -0.0028 | value_loss: 3.6079 | lr: 2.02e-04
  Update   88 | Ep   655 | reward:     93.2 | mean(100):     65.7 | actor_loss: -0.0036 | value_loss: 4.1961 | lr: 2.02e-04
  Update   89 | Ep   657 | reward:    104.7 | mean(100):     66.3 | actor_loss: 0.0001 | value_loss: 4.8759 | lr: 2.02e-04
  Update   90 | Ep   659 | reward:    105.0 | mean(100):     68.8 | actor_loss: -0.0018 | value_loss: 2.9877 | lr: 2.01e-04
  Update   91 | Ep   661 | reward:     86.3 | mean(100):     68.4 | actor_loss: -0.0035 | value_loss: 3.3559 | lr: 2.01e-04
  Update   92 | Ep   663 | reward:     18.4 | mean(100):     68.1 | actor_loss: -0.0078 | value_loss: 5.9323 | lr: 2.01e-04
  Update   93 | Ep   665 | reward:    216.8 | mean(100):     69.4 | actor_loss: -0.0040 | value_loss: 7.5488 | lr: 2.01e-04
  Update   94 | Ep   667 | reward:    147.7 | mean(100):     70.5 | actor_loss: -0.0013 | value_loss: 3.2374 | lr: 2.00e-04
  Update   95 | Ep   670 | reward:    243.7 | mean(100):     73.5 | actor_loss: -0.0019 | value_loss: 8.7036 | lr: 2.00e-04
  Update   96 | Ep   672 | reward:    -16.7 | mean(100):     73.0 | actor_loss: -0.0072 | value_loss: 6.2493 | lr: 1.99e-04
  Update   97 | Ep   674 | reward:     94.0 | mean(100):     73.1 | actor_loss: -0.0041 | value_loss: 2.2656 | lr: 1.99e-04
  Update   98 | Ep   676 | reward:    208.8 | mean(100):     73.2 | actor_loss: -0.0040 | value_loss: 6.2239 | lr: 1.99e-04
  Update   99 | Ep   680 | reward:    106.5 | mean(100):     70.6 | actor_loss: -0.0056 | value_loss: 9.8210 | lr: 1.99e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  100 | Ep   682 | reward:    173.0 | mean(100):     71.6 | actor_loss: -0.0019 | value_loss: 9.5566 | lr: 1.98e-04
  Update  101 | Ep   684 | reward:    116.2 | mean(100):     71.6 | actor_loss: -0.0012 | value_loss: 2.8881 | lr: 1.98e-04
  Update  102 | Ep   686 | reward:     96.7 | mean(100):     72.7 | actor_loss: -0.0024 | value_loss: 3.5662 | lr: 1.97e-04
  Update  103 | Ep   689 | reward:     57.3 | mean(100):     72.3 | actor_loss: -0.0016 | value_loss: 8.7975 | lr: 1.97e-04
  Update  104 | Ep   692 | reward:    187.9 | mean(100):     72.2 | actor_loss: -0.0029 | value_loss: 10.5982 | lr: 1.97e-04
  Update  105 | Ep   694 | reward:    112.9 | mean(100):     73.1 | actor_loss: -0.0022 | value_loss: 2.6127 | lr: 1.96e-04
  Update  106 | Ep   697 | reward:     93.0 | mean(100):     72.6 | actor_loss: -0.0019 | value_loss: 9.0649 | lr: 1.96e-04
  Update  107 | Ep   699 | reward:    132.0 | mean(100):     75.5 | actor_loss: -0.0022 | value_loss: 3.1838 | lr: 1.95e-04
  Update  108 | Ep   701 | reward:    117.6 | mean(100):     74.7 | actor_loss: -0.0057 | value_loss: 2.1071 | lr: 1.95e-04
  Update  109 | Ep   703 | reward:    137.7 | mean(100):     75.9 | actor_loss: -0.0032 | value_loss: 5.5657 | lr: 1.95e-04
  Update  110 | Ep   705 | reward:     88.8 | mean(100):     76.3 | actor_loss: -0.0029 | value_loss: 3.1269 | lr: 1.95e-04
  Update  111 | Ep   708 | reward:    206.5 | mean(100):     80.6 | actor_loss: -0.0038 | value_loss: 10.1438 | lr: 1.94e-04
  Update  112 | Ep   710 | reward:    108.8 | mean(100):     81.2 | actor_loss: -0.0026 | value_loss: 2.2910 | lr: 1.94e-04
  Update  113 | Ep   712 | reward:    115.4 | mean(100):     83.7 | actor_loss: -0.0032 | value_loss: 2.3313 | lr: 1.93e-04
  Update  114 | Ep   714 | reward:    107.9 | mean(100):     87.7 | actor_loss: -0.0035 | value_loss: 2.3236 | lr: 1.93e-04
  Update  115 | Ep   716 | reward:    109.5 | mean(100):     90.4 | actor_loss: -0.0028 | value_loss: 2.3766 | lr: 1.93e-04
  Update  116 | Ep   718 | reward:    124.0 | mean(100):     92.5 | actor_loss: -0.0022 | value_loss: 2.9987 | lr: 1.93e-04
  Update  117 | Ep   720 | reward:    193.1 | mean(100):     93.7 | actor_loss: -0.0013 | value_loss: 5.5624 | lr: 1.92e-04
  Update  118 | Ep   722 | reward:    114.9 | mean(100):     98.7 | actor_loss: -0.0018 | value_loss: 5.8351 | lr: 1.92e-04
  Update  119 | Ep   724 | reward:    -75.7 | mean(100):     99.2 | actor_loss: -0.0083 | value_loss: 7.0201 | lr: 1.92e-04
  Update  120 | Ep   727 | reward:    195.7 | mean(100):    102.0 | actor_loss: -0.0018 | value_loss: 7.8972 | lr: 1.91e-04
  Update  121 | Ep   730 | reward:    192.3 | mean(100):    102.6 | actor_loss: -0.0039 | value_loss: 7.4913 | lr: 1.91e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  122 | Ep   732 | reward:    115.9 | mean(100):    102.4 | actor_loss: 0.0005 | value_loss: 6.1275 | lr: 1.90e-04
  Update  123 | Ep   734 | reward:    109.9 | mean(100):    103.5 | actor_loss: -0.0044 | value_loss: 3.8722 | lr: 1.90e-04
  Update  124 | Ep   736 | reward:    103.0 | mean(100):    105.0 | actor_loss: -0.0028 | value_loss: 4.8381 | lr: 1.90e-04
  Update  125 | Ep   738 | reward:     95.6 | mean(100):    103.7 | actor_loss: -0.0058 | value_loss: 6.2200 | lr: 1.90e-04
  Update  126 | Ep   740 | reward:     83.4 | mean(100):    103.0 | actor_loss: -0.0016 | value_loss: 2.7900 | lr: 1.89e-04
  Update  127 | Ep   742 | reward:    118.5 | mean(100):    103.1 | actor_loss: -0.0040 | value_loss: 3.0582 | lr: 1.89e-04
  Update  128 | Ep   744 | reward:     84.4 | mean(100):    103.5 | actor_loss: -0.0042 | value_loss: 2.1612 | lr: 1.89e-04
  Update  129 | Ep   746 | reward:    113.3 | mean(100):    104.5 | actor_loss: -0.0044 | value_loss: 2.3299 | lr: 1.88e-04
  Update  130 | Ep   748 | reward:    -23.5 | mean(100):    105.0 | actor_loss: -0.0085 | value_loss: 4.9999 | lr: 1.88e-04
  Update  131 | Ep   750 | reward:     87.0 | mean(100):    102.3 | actor_loss: -0.0018 | value_loss: 5.8481 | lr: 1.88e-04
  Update  132 | Ep   752 | reward:    104.3 | mean(100):    103.3 | actor_loss: -0.0022 | value_loss: 5.4887 | lr: 1.87e-04
  Update  133 | Ep   754 | reward:     -4.7 | mean(100):    101.7 | actor_loss: -0.0031 | value_loss: 5.1695 | lr: 1.87e-04
  Update  134 | Ep   757 | reward:    213.4 | mean(100):    100.6 | actor_loss: -0.0051 | value_loss: 10.7872 | lr: 1.87e-04
  Update  135 | Ep   760 | reward:     92.2 | mean(100):    100.9 | actor_loss: -0.0031 | value_loss: 9.4308 | lr: 1.86e-04
  Update  136 | Ep   762 | reward:     98.0 | mean(100):    100.2 | actor_loss: -0.0025 | value_loss: 2.7798 | lr: 1.86e-04
  Update  137 | Ep   764 | reward:    -17.8 | mean(100):    100.1 | actor_loss: -0.0062 | value_loss: 5.7911 | lr: 1.86e-04
  Update  138 | Ep   767 | reward:     89.5 | mean(100):     98.7 | actor_loss: -0.0060 | value_loss: 9.0210 | lr: 1.85e-04
  Update  139 | Ep   770 | reward:    182.1 | mean(100):     98.8 | actor_loss: -0.0013 | value_loss: 8.7020 | lr: 1.85e-04
  Update  140 | Ep   772 | reward:    106.8 | mean(100):     99.8 | actor_loss: -0.0029 | value_loss: 2.0809 | lr: 1.84e-04
  Update  141 | Ep   774 | reward:    115.9 | mean(100):     98.7 | actor_loss: -0.0015 | value_loss: 6.8872 | lr: 1.84e-04
  Update  142 | Ep   777 | reward:     72.3 | mean(100):    100.7 | actor_loss: -0.0025 | value_loss: 8.3422 | lr: 1.84e-04
  Update  143 | Ep   781 | reward:    -26.3 | mean(100):     99.4 | actor_loss: -0.0008 | value_loss: 12.6457 | lr: 1.83e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  144 | Ep   783 | reward:    138.1 | mean(100):     99.3 | actor_loss: -0.0020 | value_loss: 3.3572 | lr: 1.83e-04
  Update  145 | Ep   785 | reward:    124.1 | mean(100):     99.9 | actor_loss: -0.0015 | value_loss: 5.5725 | lr: 1.83e-04
  Update  146 | Ep   787 | reward:    150.9 | mean(100):    100.1 | actor_loss: -0.0050 | value_loss: 4.1616 | lr: 1.82e-04
  Update  147 | Ep   789 | reward:    -11.2 | mean(100):    100.4 | actor_loss: -0.0005 | value_loss: 4.2608 | lr: 1.82e-04
  Update  148 | Ep   791 | reward:    128.2 | mean(100):    101.6 | actor_loss: -0.0014 | value_loss: 3.2102 | lr: 1.82e-04
  Update  149 | Ep   794 | reward:     91.3 | mean(100):     99.8 | actor_loss: -0.0018 | value_loss: 8.3436 | lr: 1.81e-04
  Update  150 | Ep   798 | reward:    211.2 | mean(100):    100.8 | actor_loss: -0.0022 | value_loss: 12.2751 | lr: 1.81e-04
  Update  151 | Ep   800 | reward:    116.1 | mean(100):    101.1 | actor_loss: -0.0025 | value_loss: 2.5158 | lr: 1.80e-04
  Update  152 | Ep   802 | reward:    134.2 | mean(100):    102.4 | actor_loss: 0.0005 | value_loss: 4.2859 | lr: 1.80e-04
  Update  153 | Ep   804 | reward:    226.3 | mean(100):    102.8 | actor_loss: -0.0015 | value_loss: 5.8427 | lr: 1.80e-04
  Update  154 | Ep   807 | reward:    -47.3 | mean(100):     98.2 | actor_loss: -0.0051 | value_loss: 10.1199 | lr: 1.79e-04
  Update  155 | Ep   809 | reward:    118.0 | mean(100):     97.4 | actor_loss: -0.0018 | value_loss: 3.3113 | lr: 1.79e-04
  Update  156 | Ep   811 | reward:    111.5 | mean(100):     97.2 | actor_loss: -0.0012 | value_loss: 3.0586 | lr: 1.79e-04
  Update  157 | Ep   814 | reward:    180.1 | mean(100):     98.9 | actor_loss: -0.0024 | value_loss: 7.6368 | lr: 1.78e-04
  Update  158 | Ep   816 | reward:    -11.9 | mean(100):     97.7 | actor_loss: -0.0033 | value_loss: 4.6501 | lr: 1.78e-04
  Update  159 | Ep   819 | reward:    -31.6 | mean(100):     94.2 | actor_loss: -0.0049 | value_loss: 8.0057 | lr: 1.78e-04
  Update  160 | Ep   821 | reward:    155.3 | mean(100):     93.2 | actor_loss: -0.0052 | value_loss: 4.4554 | lr: 1.77e-04
  Update  161 | Ep   826 | reward:    -39.0 | mean(100):     91.4 | actor_loss: 0.0000 | value_loss: 12.6127 | lr: 1.77e-04
  Update  162 | Ep   830 | reward:    -36.6 | mean(100):     90.7 | actor_loss: -0.0046 | value_loss: 10.9853 | lr: 1.76e-04
  Update  163 | Ep   832 | reward:     93.4 | mean(100):     92.0 | actor_loss: -0.0034 | value_loss: 2.9630 | lr: 1.75e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  164 | Ep   834 | reward:     -7.8 | mean(100):     91.0 | actor_loss: -0.0009 | value_loss: 5.0440 | lr: 1.75e-04
  Update  165 | Ep   836 | reward:    140.8 | mean(100):     92.9 | actor_loss: -0.0027 | value_loss: 4.3726 | lr: 1.75e-04
  Update  166 | Ep   839 | reward:    239.3 | mean(100):     97.3 | actor_loss: -0.0012 | value_loss: 9.4205 | lr: 1.75e-04
  Update  167 | Ep   841 | reward:    132.0 | mean(100):     97.6 | actor_loss: -0.0042 | value_loss: 3.2754 | lr: 1.74e-04
  Update  168 | Ep   843 | reward:     88.9 | mean(100):     97.8 | actor_loss: -0.0021 | value_loss: 3.4442 | lr: 1.74e-04
  Update  169 | Ep   845 | reward:     94.2 | mean(100):     98.2 | actor_loss: -0.0031 | value_loss: 2.2337 | lr: 1.74e-04
  Update  170 | Ep   847 | reward:    134.8 | mean(100):     98.9 | actor_loss: -0.0033 | value_loss: 3.4734 | lr: 1.73e-04
  Update  171 | Ep   849 | reward:     86.3 | mean(100):    101.9 | actor_loss: -0.0012 | value_loss: 4.8750 | lr: 1.73e-04
  Update  172 | Ep   852 | reward:    234.6 | mean(100):    103.7 | actor_loss: -0.0029 | value_loss: 8.2443 | lr: 1.73e-04
  Update  173 | Ep   854 | reward:    216.0 | mean(100):    105.9 | actor_loss: -0.0019 | value_loss: 4.2832 | lr: 1.72e-04
  Update  174 | Ep   856 | reward:     86.5 | mean(100):    107.4 | actor_loss: -0.0009 | value_loss: 2.5548 | lr: 1.72e-04
  Update  175 | Ep   861 | reward:      8.7 | mean(100):    105.2 | actor_loss: -0.0021 | value_loss: 11.7625 | lr: 1.72e-04
  Update  176 | Ep   865 | reward:    249.2 | mean(100):    109.4 | actor_loss: -0.0025 | value_loss: 11.5121 | lr: 1.71e-04
  Update  177 | Ep   867 | reward:     99.6 | mean(100):    108.9 | actor_loss: -0.0023 | value_loss: 5.6906 | lr: 1.70e-04
  Update  178 | Ep   869 | reward:     99.8 | mean(100):    108.6 | actor_loss: -0.0024 | value_loss: 3.0024 | lr: 1.70e-04
  Update  179 | Ep   871 | reward:    244.2 | mean(100):    109.1 | actor_loss: -0.0021 | value_loss: 6.5962 | lr: 1.70e-04
  Update  180 | Ep   873 | reward:    103.1 | mean(100):    110.3 | actor_loss: -0.0024 | value_loss: 3.2867 | lr: 1.69e-04
  Update  181 | Ep   877 | reward:    111.3 | mean(100):    110.1 | actor_loss: -0.0032 | value_loss: 10.0250 | lr: 1.69e-04
  Update  182 | Ep   879 | reward:      3.5 | mean(100):    110.4 | actor_loss: -0.0024 | value_loss: 5.0633 | lr: 1.68e-04
  Update  183 | Ep   881 | reward:     15.4 | mean(100):    112.1 | actor_loss: -0.0060 | value_loss: 4.9108 | lr: 1.68e-04
  Update  184 | Ep   883 | reward:    102.2 | mean(100):    110.7 | actor_loss: -0.0047 | value_loss: 4.0542 | lr: 1.68e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  185 | Ep   885 | reward:    128.9 | mean(100):    109.8 | actor_loss: -0.0058 | value_loss: 3.1761 | lr: 1.68e-04
  Update  186 | Ep   887 | reward:     98.3 | mean(100):    108.6 | actor_loss: -0.0078 | value_loss: 2.0868 | lr: 1.67e-04
  Update  187 | Ep   889 | reward:    242.2 | mean(100):    111.1 | actor_loss: -0.0025 | value_loss: 5.2391 | lr: 1.67e-04
  Update  188 | Ep   891 | reward:    103.1 | mean(100):    111.0 | actor_loss: -0.0041 | value_loss: 2.1839 | lr: 1.67e-04
  Update  189 | Ep   893 | reward:    136.0 | mean(100):    110.9 | actor_loss: -0.0020 | value_loss: 4.3928 | lr: 1.66e-04
  Update  190 | Ep   896 | reward:    226.0 | mean(100):    112.3 | actor_loss: -0.0012 | value_loss: 7.5530 | lr: 1.66e-04
  Update  191 | Ep   901 | reward:    122.9 | mean(100):    107.3 | actor_loss: -0.0053 | value_loss: 9.1671 | lr: 1.66e-04
  Update  192 | Ep   904 | reward:     15.1 | mean(100):    104.0 | actor_loss: -0.0025 | value_loss: 6.8837 | lr: 1.65e-04
  Update  193 | Ep   906 | reward:     86.2 | mean(100):    105.0 | actor_loss: 0.0006 | value_loss: 2.3448 | lr: 1.64e-04
  Update  194 | Ep   908 | reward:    129.9 | mean(100):    106.5 | actor_loss: -0.0032 | value_loss: 3.5190 | lr: 1.64e-04
  Update  195 | Ep   911 | reward:    -35.7 | mean(100):    106.3 | actor_loss: -0.0018 | value_loss: 9.0219 | lr: 1.64e-04
  Update  196 | Ep   914 | reward:     43.2 | mean(100):    103.1 | actor_loss: -0.0046 | value_loss: 5.7847 | lr: 1.63e-04
  Update  197 | Ep   919 | reward:     20.8 | mean(100):    103.4 | actor_loss: -0.0040 | value_loss: 8.5457 | lr: 1.63e-04
  Update  198 | Ep   921 | reward:     89.7 | mean(100):    101.5 | actor_loss: -0.0048 | value_loss: 4.4035 | lr: 1.62e-04
  Update  199 | Ep   923 | reward:     41.8 | mean(100):    101.9 | actor_loss: -0.0049 | value_loss: 4.6828 | lr: 1.62e-04
  Update  200 | Ep   925 | reward:    126.7 | mean(100):    102.0 | actor_loss: -0.0013 | value_loss: 4.1154 | lr: 1.62e-04
  Update  201 | Ep   927 | reward:      2.3 | mean(100):    102.0 | actor_loss: -0.0028 | value_loss: 4.6670 | lr: 1.61e-04
  Update  202 | Ep   929 | reward:     12.5 | mean(100):    100.1 | actor_loss: -0.0057 | value_loss: 4.3080 | lr: 1.61e-04
  Update  203 | Ep   933 | reward:    117.5 | mean(100):     99.0 | actor_loss: -0.0059 | value_loss: 7.3729 | lr: 1.61e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  204 | Ep   937 | reward:     50.5 | mean(100):     97.1 | actor_loss: -0.0065 | value_loss: 8.1525 | lr: 1.60e-04
  Update  205 | Ep   944 | reward:    161.1 | mean(100):     89.4 | actor_loss: -0.0030 | value_loss: 13.4457 | lr: 1.59e-04
  Update  206 | Ep   947 | reward:     36.6 | mean(100):     88.3 | actor_loss: -0.0042 | value_loss: 5.5720 | lr: 1.58e-04
  Update  207 | Ep   949 | reward:    118.5 | mean(100):     88.9 | actor_loss: -0.0052 | value_loss: 4.4356 | lr: 1.58e-04
  Update  208 | Ep   951 | reward:    106.3 | mean(100):     88.2 | actor_loss: -0.0006 | value_loss: 3.3172 | lr: 1.58e-04
  Update  209 | Ep   958 | reward:     32.0 | mean(100):     79.0 | actor_loss: -0.0006 | value_loss: 14.2890 | lr: 1.57e-04
  Update  210 | Ep   965 | reward:     55.0 | mean(100):     72.5 | actor_loss: -0.0022 | value_loss: 11.9027 | lr: 1.56e-04
  Update  211 | Ep   974 | reward:     38.0 | mean(100):     65.4 | actor_loss: -0.0038 | value_loss: 15.5054 | lr: 1.55e-04
  Update  212 | Ep   976 | reward:    186.4 | mean(100):     66.2 | actor_loss: -0.0046 | value_loss: 3.9077 | lr: 1.54e-04
  Update  213 | Ep   978 | reward:     30.5 | mean(100):     65.3 | actor_loss: -0.0053 | value_loss: 3.7524 | lr: 1.54e-04
  Update  214 | Ep   982 | reward:     24.3 | mean(100):     65.8 | actor_loss: -0.0029 | value_loss: 6.3709 | lr: 1.53e-04
  Update  215 | Ep   984 | reward:    105.5 | mean(100):     65.9 | actor_loss: -0.0033 | value_loss: 3.0120 | lr: 1.53e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  216 | Ep   989 | reward:     21.8 | mean(100):     61.5 | actor_loss: -0.0066 | value_loss: 8.6241 | lr: 1.52e-04
  Update  217 | Ep   991 | reward:      5.1 | mean(100):     60.4 | actor_loss: -0.0015 | value_loss: 3.5701 | lr: 1.52e-04
  Update  218 | Ep   993 | reward:    -10.7 | mean(100):     60.0 | actor_loss: -0.0054 | value_loss: 5.5993 | lr: 1.51e-04
  Update  219 | Ep   995 | reward:     24.8 | mean(100):     60.9 | actor_loss: -0.0030 | value_loss: 3.4803 | lr: 1.51e-04
  Update  220 | Ep  1002 | reward:     21.3 | mean(100):     59.1 | actor_loss: -0.0022 | value_loss: 9.2949 | lr: 1.51e-04
  Update  221 | Ep  1004 | reward:    101.7 | mean(100):     59.1 | actor_loss: -0.0051 | value_loss: 3.6585 | lr: 1.50e-04
  Update  222 | Ep  1008 | reward:    110.8 | mean(100):     57.2 | actor_loss: -0.0065 | value_loss: 6.0831 | lr: 1.49e-04
  Update  223 | Ep  1012 | reward:    185.1 | mean(100):     56.5 | actor_loss: -0.0034 | value_loss: 8.8979 | lr: 1.49e-04
  Update  224 | Ep  1014 | reward:    125.0 | mean(100):     57.5 | actor_loss: -0.0054 | value_loss: 3.2977 | lr: 1.48e-04
  Update  225 | Ep  1016 | reward:     98.6 | mean(100):     59.2 | actor_loss: -0.0034 | value_loss: 2.6341 | lr: 1.48e-04
  Update  226 | Ep  1018 | reward:    148.0 | mean(100):     61.6 | actor_loss: -0.0025 | value_loss: 2.6146 | lr: 1.48e-04
  Update  227 | Ep  1020 | reward:    146.8 | mean(100):     64.5 | actor_loss: -0.0052 | value_loss: 2.9016 | lr: 1.47e-04
  Update  228 | Ep  1022 | reward:    163.2 | mean(100):     64.3 | actor_loss: -0.0022 | value_loss: 5.0611 | lr: 1.47e-04
  Update  229 | Ep  1024 | reward:    106.4 | mean(100):     65.3 | actor_loss: -0.0023 | value_loss: 2.2936 | lr: 1.47e-04
  Update  230 | Ep  1026 | reward:    177.4 | mean(100):     66.0 | actor_loss: -0.0037 | value_loss: 3.8072 | lr: 1.46e-04
  Update  231 | Ep  1028 | reward:    177.5 | mean(100):     68.0 | actor_loss: -0.0050 | value_loss: 2.9384 | lr: 1.46e-04
  Update  232 | Ep  1030 | reward:    130.1 | mean(100):     70.6 | actor_loss: -0.0054 | value_loss: 2.1475 | lr: 1.46e-04
  Update  233 | Ep  1032 | reward:     76.0 | mean(100):     73.6 | actor_loss: -0.0047 | value_loss: 5.8165 | lr: 1.45e-04
  Update  234 | Ep  1034 | reward:    171.7 | mean(100):     76.9 | actor_loss: -0.0049 | value_loss: 6.3671 | lr: 1.45e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  235 | Ep  1037 | reward:    172.0 | mean(100):     82.0 | actor_loss: -0.0017 | value_loss: 9.5499 | lr: 1.45e-04
  Update  236 | Ep  1040 | reward:     26.8 | mean(100):     86.9 | actor_loss: -0.0070 | value_loss: 9.7378 | lr: 1.44e-04
  Update  237 | Ep  1044 | reward:    278.5 | mean(100):     95.2 | actor_loss: -0.0061 | value_loss: 14.3735 | lr: 1.44e-04
  Update  238 | Ep  1048 | reward:    125.0 | mean(100):    100.2 | actor_loss: -0.0048 | value_loss: 11.4390 | lr: 1.43e-04
  Update  239 | Ep  1053 | reward:     14.8 | mean(100):    105.1 | actor_loss: -0.0037 | value_loss: 17.4206 | lr: 1.43e-04
  Update  240 | Ep  1057 | reward:    258.1 | mean(100):    111.4 | actor_loss: -0.0014 | value_loss: 10.8056 | lr: 1.42e-04
  Update  241 | Ep  1064 | reward:    235.2 | mean(100):    120.3 | actor_loss: -0.0037 | value_loss: 20.8442 | lr: 1.41e-04
  Update  242 | Ep  1070 | reward:     33.8 | mean(100):    131.3 | actor_loss: -0.0023 | value_loss: 18.0570 | lr: 1.40e-04
  Update  243 | Ep  1074 | reward:     75.7 | mean(100):    138.0 | actor_loss: -0.0033 | value_loss: 11.2644 | lr: 1.39e-04
  Update  244 | Ep  1082 | reward:    -51.9 | mean(100):    142.4 | actor_loss: -0.0022 | value_loss: 25.5821 | lr: 1.39e-04
  Update  245 | Ep  1089 | reward:    266.1 | mean(100):    154.9 | actor_loss: -0.0051 | value_loss: 23.2084 | lr: 1.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  246 | Ep  1097 | reward:    278.7 | mean(100):    159.6 | actor_loss: -0.0020 | value_loss: 28.1762 | lr: 1.37e-04
  Update  247 | Ep  1105 | reward:     70.2 | mean(100):    169.7 | actor_loss: -0.0031 | value_loss: 27.8451 | lr: 1.35e-04
  Update  248 | Ep  1112 | reward:    225.8 | mean(100):    181.5 | actor_loss: -0.0038 | value_loss: 21.5388 | lr: 1.34e-04
  Update  249 | Ep  1118 | reward:     20.9 | mean(100):    186.3 | actor_loss: -0.0027 | value_loss: 19.1871 | lr: 1.33e-04
  Update  250 | Ep  1124 | reward:    284.2 | mean(100):    195.6 | actor_loss: -0.0012 | value_loss: 20.5604 | lr: 1.32e-04
  Update  251 | Ep  1133 | reward:     31.5 | mean(100):    191.6 | actor_loss: -0.0074 | value_loss: 39.6382 | lr: 1.31e-04
  Update  252 | Ep  1138 | reward:     59.8 | mean(100):    191.9 | actor_loss: -0.0018 | value_loss: 18.3927 | lr: 1.30e-04
  Update  253 | Ep  1147 | reward:    255.7 | mean(100):    184.3 | actor_loss: -0.0036 | value_loss: 26.0887 | lr: 1.29e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  254 | Ep  1156 | reward:    239.6 | mean(100):    183.7 | actor_loss: -0.0018 | value_loss: 24.4440 | lr: 1.28e-04
  Update  255 | Ep  1165 | reward:     62.2 | mean(100):    179.7 | actor_loss: -0.0021 | value_loss: 24.4036 | lr: 1.27e-04
  Update  256 | Ep  1170 | reward:    275.3 | mean(100):    178.1 | actor_loss: -0.0016 | value_loss: 15.6014 | lr: 1.25e-04
  Update  257 | Ep  1179 | reward:    268.3 | mean(100):    179.4 | actor_loss: -0.0021 | value_loss: 28.6107 | lr: 1.24e-04
  Update  258 | Ep  1188 | reward:    265.8 | mean(100):    181.4 | actor_loss: -0.0049 | value_loss: 29.8093 | lr: 1.23e-04
  Update  259 | Ep  1191 | reward:     34.2 | mean(100):    182.5 | actor_loss: -0.0039 | value_loss: 8.3609 | lr: 1.22e-04
  Update  260 | Ep  1199 | reward:    251.9 | mean(100):    183.6 | actor_loss: -0.0021 | value_loss: 26.8193 | lr: 1.21e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  261 | Ep  1206 | reward:    188.1 | mean(100):    184.8 | actor_loss: -0.0036 | value_loss: 22.4911 | lr: 1.20e-04
  Update  262 | Ep  1211 | reward:    139.5 | mean(100):    175.8 | actor_loss: -0.0068 | value_loss: 14.3298 | lr: 1.19e-04
  Update  263 | Ep  1219 | reward:    288.1 | mean(100):    173.3 | actor_loss: -0.0025 | value_loss: 21.9373 | lr: 1.18e-04
  Update  264 | Ep  1227 | reward:     69.8 | mean(100):    173.0 | actor_loss: -0.0016 | value_loss: 23.1598 | lr: 1.17e-04
  Update  265 | Ep  1233 | reward:    269.4 | mean(100):    177.0 | actor_loss: -0.0013 | value_loss: 23.4157 | lr: 1.16e-04
  Update  266 | Ep  1241 | reward:    275.3 | mean(100):    181.1 | actor_loss: -0.0041 | value_loss: 25.3493 | lr: 1.15e-04
  Update  267 | Ep  1248 | reward:    269.5 | mean(100):    185.8 | actor_loss: -0.0037 | value_loss: 22.1206 | lr: 1.14e-04
  Update  268 | Ep  1256 | reward:     37.9 | mean(100):    189.1 | actor_loss: -0.0023 | value_loss: 26.6614 | lr: 1.13e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
  Update  269 | Ep  1262 | reward:     55.3 | mean(100):    194.0 | actor_loss: -0.0021 | value_loss: 16.6117 | lr: 1.12e-04
  Update  270 | Ep  1267 | reward:    255.5 | mean(100):    197.4 | actor_loss: -0.0040 | value_loss: 16.3279 | lr: 1.11e-04
  Update  271 | Ep  1273 | reward:    286.6 | mean(100):    197.0 | actor_loss: -0.0018 | value_loss: 17.2521 | lr: 1.10e-04
  Update  272 | Ep  1276 | reward:     54.0 | mean(100):    197.6 | actor_loss: -0.0018 | value_loss: 12.9577 | lr: 1.09e-04
  Update  273 | Ep  1283 | reward:    276.1 | mean(100):    203.8 | actor_loss: -0.0021 | value_loss: 19.7667 | lr: 1.09e-04

Solved at episode 1283 (update 273) with mean 203.8!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_2.png
