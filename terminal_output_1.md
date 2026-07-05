Using device: cuda (rollout collection stays on CPU; batched PPO update uses cuda)
Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    22 | reward:    -85.4 | mean(100):   -191.1 | actor_loss: -0.0100 | value_loss: 72.8860 | lr: 3.00e-04
  Update    2 | Ep    44 | reward:   -117.8 | mean(100):   -171.9 | actor_loss: -0.0104 | value_loss: 59.2986 | lr: 2.97e-04
  Update    3 | Ep    67 | reward:   -129.6 | mean(100):   -158.2 | actor_loss: -0.0059 | value_loss: 52.2863 | lr: 2.93e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update    4 | Ep    89 | reward:    -88.2 | mean(100):   -148.0 | actor_loss: -0.0056 | value_loss: 45.9013 | lr: 2.90e-04
  Update    5 | Ep   110 | reward:   -297.3 | mean(100):   -136.2 | actor_loss: -0.0068 | value_loss: 42.3694 | lr: 2.87e-04
  Update    6 | Ep   131 | reward:   -113.3 | mean(100):   -120.4 | actor_loss: -0.0103 | value_loss: 45.2964 | lr: 2.83e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update    7 | Ep   153 | reward:    -44.7 | mean(100):   -109.9 | actor_loss: -0.0081 | value_loss: 30.8679 | lr: 2.80e-04
  Update    8 | Ep   176 | reward:   -268.2 | mean(100):   -106.4 | actor_loss: -0.0071 | value_loss: 45.5094 | lr: 2.77e-04
  Update    9 | Ep   195 | reward:    -70.3 | mean(100):   -101.2 | actor_loss: -0.0084 | value_loss: 30.0132 | lr: 2.74e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   10 | Ep   216 | reward:      7.8 | mean(100):    -92.1 | actor_loss: -0.0093 | value_loss: 28.4454 | lr: 2.71e-04
  Update   11 | Ep   237 | reward:    -20.8 | mean(100):    -83.1 | actor_loss: -0.0061 | value_loss: 28.0170 | lr: 2.68e-04
  Update   12 | Ep   259 | reward:    -86.8 | mean(100):    -81.2 | actor_loss: -0.0089 | value_loss: 24.2663 | lr: 2.64e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   13 | Ep   281 | reward:    -16.4 | mean(100):    -64.1 | actor_loss: -0.0068 | value_loss: 22.2779 | lr: 2.61e-04
  Update   14 | Ep   301 | reward:    -29.0 | mean(100):    -51.5 | actor_loss: -0.0044 | value_loss: 19.7989 | lr: 2.58e-04
  Update   15 | Ep   319 | reward:    -34.2 | mean(100):    -41.0 | actor_loss: -0.0051 | value_loss: 19.3196 | lr: 2.55e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   16 | Ep   338 | reward:    -25.6 | mean(100):    -30.2 | actor_loss: -0.0058 | value_loss: 19.9708 | lr: 2.52e-04
  Update   17 | Ep   352 | reward:    -11.1 | mean(100):    -25.1 | actor_loss: -0.0055 | value_loss: 28.3584 | lr: 2.49e-04
  Update   18 | Ep   356 | reward:    -59.7 | mean(100):    -23.9 | actor_loss: -0.0045 | value_loss: 18.3028 | lr: 2.47e-04
  Update   19 | Ep   365 | reward:      0.9 | mean(100):    -18.9 | actor_loss: -0.0047 | value_loss: 18.3535 | lr: 2.47e-04
  Update   20 | Ep   374 | reward:     73.7 | mean(100):    -15.7 | actor_loss: -0.0072 | value_loss: 17.7341 | lr: 2.45e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   21 | Ep   381 | reward:      5.9 | mean(100):    -11.4 | actor_loss: -0.0060 | value_loss: 18.6204 | lr: 2.44e-04
  Update   22 | Ep   391 | reward:     33.7 | mean(100):     -9.6 | actor_loss: -0.0040 | value_loss: 16.0137 | lr: 2.43e-04
  Update   23 | Ep   399 | reward:     74.3 | mean(100):     -8.2 | actor_loss: -0.0046 | value_loss: 20.8549 | lr: 2.41e-04
  Update   24 | Ep   406 | reward:     42.3 | mean(100):     -5.9 | actor_loss: -0.0069 | value_loss: 17.2029 | lr: 2.40e-04
  Update   25 | Ep   413 | reward:     12.2 | mean(100):     -3.0 | actor_loss: -0.0058 | value_loss: 16.2754 | lr: 2.39e-04
  Update   26 | Ep   428 | reward:    -10.0 | mean(100):      0.9 | actor_loss: -0.0092 | value_loss: 20.4793 | lr: 2.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   27 | Ep   434 | reward:     25.0 | mean(100):      2.7 | actor_loss: -0.0042 | value_loss: 14.9874 | lr: 2.36e-04
  Update   28 | Ep   436 | reward:     -0.3 | mean(100):      3.8 | actor_loss: -0.0017 | value_loss: 10.6131 | lr: 2.35e-04
  Update   29 | Ep   438 | reward:     83.0 | mean(100):      5.0 | actor_loss: -0.0057 | value_loss: 8.6869 | lr: 2.35e-04
  Update   30 | Ep   441 | reward:    115.2 | mean(100):      5.9 | actor_loss: -0.0045 | value_loss: 12.0464 | lr: 2.34e-04
  Update   31 | Ep   443 | reward:     74.0 | mean(100):      7.0 | actor_loss: -0.0047 | value_loss: 8.7171 | lr: 2.34e-04
  Update   32 | Ep   445 | reward:    142.7 | mean(100):     10.1 | actor_loss: -0.0040 | value_loss: 6.9576 | lr: 2.34e-04
  Update   33 | Ep   450 | reward:    -41.6 | mean(100):     13.0 | actor_loss: -0.0088 | value_loss: 15.3712 | lr: 2.33e-04
  Update   34 | Ep   452 | reward:      2.5 | mean(100):     13.9 | actor_loss: -0.0083 | value_loss: 6.4961 | lr: 2.32e-04
  Update   35 | Ep   454 | reward:    -18.0 | mean(100):     15.7 | actor_loss: -0.0056 | value_loss: 6.5855 | lr: 2.32e-04
  Update   36 | Ep   456 | reward:    124.7 | mean(100):     17.3 | actor_loss: -0.0024 | value_loss: 5.8835 | lr: 2.32e-04
  Update   37 | Ep   458 | reward:      4.6 | mean(100):     18.3 | actor_loss: -0.0051 | value_loss: 7.3704 | lr: 2.32e-04
  Update   38 | Ep   460 | reward:    -78.6 | mean(100):     18.0 | actor_loss: -0.0068 | value_loss: 9.5964 | lr: 2.31e-04
  Update   39 | Ep   462 | reward:    117.9 | mean(100):     20.0 | actor_loss: -0.0016 | value_loss: 4.5494 | lr: 2.31e-04
  Update   40 | Ep   464 | reward:    105.3 | mean(100):     22.8 | actor_loss: -0.0056 | value_loss: 5.6422 | lr: 2.31e-04
  Update   41 | Ep   466 | reward:     56.0 | mean(100):     24.8 | actor_loss: -0.0026 | value_loss: 5.6586 | lr: 2.30e-04
  Update   42 | Ep   468 | reward:    114.8 | mean(100):     26.0 | actor_loss: -0.0038 | value_loss: 7.5390 | lr: 2.30e-04
  Update   43 | Ep   470 | reward:    -82.4 | mean(100):     26.4 | actor_loss: -0.0059 | value_loss: 7.7574 | lr: 2.30e-04
  Update   44 | Ep   472 | reward:     44.6 | mean(100):     26.3 | actor_loss: -0.0028 | value_loss: 5.2323 | lr: 2.29e-04
  Update   45 | Ep   474 | reward:     15.6 | mean(100):     26.9 | actor_loss: -0.0049 | value_loss: 5.2937 | lr: 2.29e-04
  Update   46 | Ep   477 | reward:    -62.9 | mean(100):     25.7 | actor_loss: -0.0006 | value_loss: 9.6209 | lr: 2.29e-04
  Update   47 | Ep   479 | reward:     40.7 | mean(100):     25.1 | actor_loss: -0.0041 | value_loss: 6.0058 | lr: 2.28e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   48 | Ep   481 | reward:      4.7 | mean(100):     25.4 | actor_loss: -0.0083 | value_loss: 5.1887 | lr: 2.28e-04
  Update   49 | Ep   483 | reward:    -97.8 | mean(100):     23.3 | actor_loss: -0.0047 | value_loss: 11.1322 | lr: 2.28e-04
  Update   50 | Ep   485 | reward:     63.4 | mean(100):     24.9 | actor_loss: -0.0045 | value_loss: 4.1388 | lr: 2.28e-04
  Update   51 | Ep   487 | reward:    120.4 | mean(100):     25.9 | actor_loss: -0.0027 | value_loss: 10.1563 | lr: 2.27e-04
  Update   52 | Ep   489 | reward:     31.0 | mean(100):     26.0 | actor_loss: 0.0010 | value_loss: 8.8848 | lr: 2.27e-04
  Update   53 | Ep   491 | reward:     82.0 | mean(100):     24.6 | actor_loss: -0.0055 | value_loss: 8.4397 | lr: 2.27e-04
  Update   54 | Ep   493 | reward:     93.6 | mean(100):     26.5 | actor_loss: -0.0049 | value_loss: 6.5035 | lr: 2.26e-04
  Update   55 | Ep   495 | reward:     65.3 | mean(100):     29.4 | actor_loss: -0.0085 | value_loss: 4.2847 | lr: 2.26e-04
  Update   56 | Ep   497 | reward:    169.0 | mean(100):     32.5 | actor_loss: -0.0040 | value_loss: 7.0964 | lr: 2.26e-04
  Update   57 | Ep   499 | reward:    146.5 | mean(100):     34.1 | actor_loss: -0.0018 | value_loss: 5.1700 | lr: 2.25e-04
  Update   58 | Ep   501 | reward:    124.4 | mean(100):     35.9 | actor_loss: -0.0039 | value_loss: 4.3912 | lr: 2.25e-04
  Update   59 | Ep   503 | reward:    126.5 | mean(100):     38.7 | actor_loss: -0.0036 | value_loss: 4.6384 | lr: 2.25e-04
  Update   60 | Ep   505 | reward:     61.6 | mean(100):     38.9 | actor_loss: -0.0036 | value_loss: 3.9521 | lr: 2.25e-04
  Update   61 | Ep   507 | reward:     93.1 | mean(100):     40.1 | actor_loss: -0.0048 | value_loss: 3.3293 | lr: 2.24e-04
  Update   62 | Ep   509 | reward:     80.8 | mean(100):     41.3 | actor_loss: -0.0050 | value_loss: 4.3575 | lr: 2.24e-04
  Update   63 | Ep   511 | reward:      3.9 | mean(100):     42.5 | actor_loss: -0.0007 | value_loss: 4.2591 | lr: 2.24e-04
  Update   64 | Ep   513 | reward:     66.5 | mean(100):     43.5 | actor_loss: -0.0027 | value_loss: 3.1960 | lr: 2.23e-04
  Update   65 | Ep   515 | reward:     92.4 | mean(100):     44.3 | actor_loss: -0.0013 | value_loss: 3.4179 | lr: 2.23e-04
  Update   66 | Ep   517 | reward:     67.7 | mean(100):     46.2 | actor_loss: -0.0030 | value_loss: 2.8212 | lr: 2.23e-04
  Update   67 | Ep   519 | reward:    135.6 | mean(100):     48.3 | actor_loss: -0.0020 | value_loss: 4.3736 | lr: 2.22e-04
  Update   68 | Ep   521 | reward:    -60.9 | mean(100):     49.0 | actor_loss: -0.0058 | value_loss: 9.9399 | lr: 2.22e-04
  Update   69 | Ep   524 | reward:    225.6 | mean(100):     52.5 | actor_loss: -0.0046 | value_loss: 12.7000 | lr: 2.22e-04
  Update   70 | Ep   527 | reward:    202.4 | mean(100):     59.2 | actor_loss: -0.0033 | value_loss: 13.3727 | lr: 2.21e-04
  Update   71 | Ep   531 | reward:    234.7 | mean(100):     66.0 | actor_loss: -0.0025 | value_loss: 14.8118 | lr: 2.21e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   72 | Ep   533 | reward:     80.6 | mean(100):     67.8 | actor_loss: -0.0034 | value_loss: 7.9443 | lr: 2.20e-04
  Update   73 | Ep   535 | reward:    238.0 | mean(100):     70.9 | actor_loss: -0.0018 | value_loss: 9.7583 | lr: 2.20e-04
  Update   74 | Ep   538 | reward:    212.3 | mean(100):     76.2 | actor_loss: -0.0017 | value_loss: 11.7512 | lr: 2.20e-04
  Update   75 | Ep   541 | reward:    177.3 | mean(100):     81.5 | actor_loss: -0.0026 | value_loss: 13.5897 | lr: 2.19e-04
  Update   76 | Ep   544 | reward:    231.5 | mean(100):     86.7 | actor_loss: -0.0029 | value_loss: 14.7911 | lr: 2.19e-04
  Update   77 | Ep   547 | reward:    173.9 | mean(100):     90.1 | actor_loss: -0.0015 | value_loss: 11.3583 | lr: 2.18e-04
  Update   78 | Ep   549 | reward:    164.9 | mean(100):     92.4 | actor_loss: 0.0000 | value_loss: 5.4106 | lr: 2.18e-04
  Update   79 | Ep   552 | reward:    259.2 | mean(100):     98.0 | actor_loss: -0.0028 | value_loss: 12.0368 | lr: 2.18e-04
  Update   80 | Ep   556 | reward:    203.1 | mean(100):    103.7 | actor_loss: -0.0018 | value_loss: 14.1422 | lr: 2.17e-04
  Update   81 | Ep   558 | reward:    172.7 | mean(100):    106.0 | actor_loss: -0.0024 | value_loss: 9.1369 | lr: 2.17e-04
  Update   82 | Ep   562 | reward:    199.1 | mean(100):    112.8 | actor_loss: -0.0010 | value_loss: 16.4903 | lr: 2.16e-04
  Update   83 | Ep   565 | reward:    224.1 | mean(100):    115.5 | actor_loss: -0.0007 | value_loss: 11.1995 | lr: 2.16e-04
  Update   84 | Ep   568 | reward:    208.1 | mean(100):    120.3 | actor_loss: -0.0005 | value_loss: 11.7479 | lr: 2.15e-04
  Update   85 | Ep   571 | reward:     48.0 | mean(100):    124.1 | actor_loss: -0.0015 | value_loss: 10.2078 | lr: 2.15e-04
  Update   86 | Ep   575 | reward:    208.9 | mean(100):    131.1 | actor_loss: -0.0015 | value_loss: 14.8230 | lr: 2.14e-04
  Update   87 | Ep   579 | reward:    202.9 | mean(100):    137.9 | actor_loss: -0.0023 | value_loss: 15.3289 | lr: 2.14e-04
  Update   88 | Ep   583 | reward:    229.8 | mean(100):    147.8 | actor_loss: -0.0014 | value_loss: 15.0979 | lr: 2.13e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update   89 | Ep   588 | reward:    265.4 | mean(100):    158.5 | actor_loss: -0.0018 | value_loss: 19.6440 | lr: 2.13e-04
  Update   90 | Ep   592 | reward:    200.0 | mean(100):    167.0 | actor_loss: -0.0025 | value_loss: 15.8278 | lr: 2.12e-04
  Update   91 | Ep   596 | reward:    230.8 | mean(100):    173.7 | actor_loss: -0.0038 | value_loss: 17.3763 | lr: 2.11e-04
  Update   92 | Ep   601 | reward:    249.6 | mean(100):    177.2 | actor_loss: -0.0013 | value_loss: 20.3744 | lr: 2.11e-04
  Update   93 | Ep   606 | reward:    221.5 | mean(100):    181.5 | actor_loss: -0.0015 | value_loss: 18.3050 | lr: 2.10e-04
  Update   94 | Ep   610 | reward:    191.9 | mean(100):    186.7 | actor_loss: -0.0031 | value_loss: 15.2691 | lr: 2.09e-04
  Update   95 | Ep   615 | reward:    263.0 | mean(100):    193.8 | actor_loss: -0.0041 | value_loss: 20.0912 | lr: 2.08e-04
  Update   96 | Ep   619 | reward:    187.1 | mean(100):    199.3 | actor_loss: -0.0030 | value_loss: 18.0053 | lr: 2.08e-04
  Update   97 | Ep   624 | reward:    200.4 | mean(100):    199.2 | actor_loss: -0.0050 | value_loss: 22.1989 | lr: 2.07e-04
  Update   98 | Ep   630 | reward:    228.3 | mean(100):    197.1 | actor_loss: -0.0038 | value_loss: 21.5633 | lr: 2.06e-04
  Update   99 | Ep   635 | reward:    247.0 | mean(100):    196.8 | actor_loss: -0.0024 | value_loss: 22.0867 | lr: 2.06e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
  Update  100 | Ep   641 | reward:    231.6 | mean(100):    196.5 | actor_loss: -0.0018 | value_loss: 22.1057 | lr: 2.05e-04
  Update  101 | Ep   646 | reward:    231.4 | mean(100):    194.0 | actor_loss: -0.0046 | value_loss: 21.5210 | lr: 2.04e-04
  Update  102 | Ep   651 | reward:    199.9 | mean(100):    196.2 | actor_loss: -0.0019 | value_loss: 19.2607 | lr: 2.03e-04
  Update  103 | Ep   655 | reward:    270.2 | mean(100):    197.7 | actor_loss: -0.0047 | value_loss: 18.8400 | lr: 2.02e-04
  Update  104 | Ep   661 | reward:    265.1 | mean(100):    195.9 | actor_loss: -0.0041 | value_loss: 23.1619 | lr: 2.02e-04
  Update  105 | Ep   665 | reward:    267.1 | mean(100):    197.4 | actor_loss: -0.0024 | value_loss: 18.5774 | lr: 2.01e-04
  Update  106 | Ep   670 | reward:    206.5 | mean(100):    196.5 | actor_loss: -0.0045 | value_loss: 17.6312 | lr: 2.00e-04
  Update  107 | Ep   675 | reward:    222.9 | mean(100):    199.0 | actor_loss: -0.0027 | value_loss: 19.2198 | lr: 1.99e-04
  Update  108 | Ep   679 | reward:    236.0 | mean(100):    202.3 | actor_loss: -0.0048 | value_loss: 14.9852 | lr: 1.99e-04

Solved at episode 679 (update 108) with mean 202.3!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_1.png
