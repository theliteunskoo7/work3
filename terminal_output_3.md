Using device: cuda (rollout collection stays on CPU; batched PPO update uses cuda)
Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    21 | reward:   -287.3 | mean(100):   -211.1 | actor_loss: -0.0075 | value_loss: 75.0204 | lr: 3.00e-04
  Update    2 | Ep    42 | reward:   -220.4 | mean(100):   -182.0 | actor_loss: -0.0051 | value_loss: 58.5388 | lr: 2.97e-04
  Update    3 | Ep    64 | reward:    -79.9 | mean(100):   -160.0 | actor_loss: -0.0038 | value_loss: 45.5627 | lr: 2.94e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update    4 | Ep    88 | reward:    -84.4 | mean(100):   -142.1 | actor_loss: -0.0084 | value_loss: 38.1739 | lr: 2.90e-04
  Update    5 | Ep   109 | reward:   -106.1 | mean(100):   -126.2 | actor_loss: -0.0080 | value_loss: 30.1184 | lr: 2.87e-04
  Update    6 | Ep   132 | reward:    -76.2 | mean(100):   -101.9 | actor_loss: -0.0058 | value_loss: 36.3086 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update    7 | Ep   155 | reward:    -87.4 | mean(100):    -89.9 | actor_loss: -0.0053 | value_loss: 31.0963 | lr: 2.80e-04
  Update    8 | Ep   177 | reward:   -103.2 | mean(100):    -81.6 | actor_loss: -0.0053 | value_loss: 28.1857 | lr: 2.77e-04
  Update    9 | Ep   197 | reward:    -41.3 | mean(100):    -76.6 | actor_loss: -0.0086 | value_loss: 25.5536 | lr: 2.73e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   10 | Ep   220 | reward:    -12.5 | mean(100):    -67.8 | actor_loss: -0.0093 | value_loss: 24.6942 | lr: 2.70e-04
  Update   11 | Ep   237 | reward:     29.5 | mean(100):    -59.4 | actor_loss: -0.0065 | value_loss: 23.1738 | lr: 2.67e-04
  Update   12 | Ep   257 | reward:     -1.8 | mean(100):    -46.8 | actor_loss: -0.0048 | value_loss: 22.0697 | lr: 2.64e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   13 | Ep   274 | reward:    -18.9 | mean(100):    -42.2 | actor_loss: -0.0052 | value_loss: 23.4159 | lr: 2.61e-04
  Update   14 | Ep   294 | reward:    -32.7 | mean(100):    -35.4 | actor_loss: -0.0051 | value_loss: 24.3125 | lr: 2.59e-04
  Update   15 | Ep   304 | reward:     -8.0 | mean(100):    -32.6 | actor_loss: -0.0064 | value_loss: 24.6280 | lr: 2.56e-04
  Update   16 | Ep   326 | reward:     15.0 | mean(100):    -30.4 | actor_loss: -0.0080 | value_loss: 21.5856 | lr: 2.54e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   17 | Ep   343 | reward:     -6.9 | mean(100):    -28.3 | actor_loss: -0.0103 | value_loss: 25.4936 | lr: 2.51e-04
  Update   18 | Ep   351 | reward:     -2.9 | mean(100):    -29.7 | actor_loss: -0.0035 | value_loss: 17.8433 | lr: 2.49e-04
  Update   19 | Ep   361 | reward:    -29.3 | mean(100):    -27.4 | actor_loss: -0.0072 | value_loss: 15.4552 | lr: 2.47e-04
  Update   20 | Ep   374 | reward:    -46.8 | mean(100):    -24.0 | actor_loss: -0.0042 | value_loss: 23.9999 | lr: 2.46e-04
  Update   21 | Ep   376 | reward:      8.1 | mean(100):    -22.5 | actor_loss: -0.0086 | value_loss: 12.8777 | lr: 2.44e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   22 | Ep   384 | reward:    -32.5 | mean(100):    -22.0 | actor_loss: -0.0080 | value_loss: 20.5253 | lr: 2.44e-04
  Update   23 | Ep   392 | reward:     -8.6 | mean(100):    -20.6 | actor_loss: -0.0100 | value_loss: 19.5030 | lr: 2.42e-04
  Update   24 | Ep   402 | reward:     32.0 | mean(100):    -16.2 | actor_loss: -0.0076 | value_loss: 18.5962 | lr: 2.41e-04
  Update   25 | Ep   407 | reward:     70.2 | mean(100):    -14.5 | actor_loss: -0.0050 | value_loss: 14.8075 | lr: 2.40e-04
  Update   26 | Ep   425 | reward:    -19.3 | mean(100):    -10.7 | actor_loss: -0.0041 | value_loss: 20.5376 | lr: 2.39e-04
  Update   27 | Ep   428 | reward:     17.5 | mean(100):    -11.5 | actor_loss: -0.0073 | value_loss: 15.6025 | lr: 2.36e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   28 | Ep   436 | reward:     29.8 | mean(100):     -6.0 | actor_loss: -0.0031 | value_loss: 13.7579 | lr: 2.36e-04
  Update   29 | Ep   444 | reward:    -10.1 | mean(100):     -4.9 | actor_loss: -0.0063 | value_loss: 14.5860 | lr: 2.35e-04
  Update   30 | Ep   448 | reward:     16.1 | mean(100):     -2.2 | actor_loss: -0.0048 | value_loss: 12.8792 | lr: 2.33e-04
  Update   31 | Ep   450 | reward:    -16.0 | mean(100):     -2.5 | actor_loss: -0.0042 | value_loss: 8.8869 | lr: 2.33e-04
  Update   32 | Ep   456 | reward:    -36.3 | mean(100):     -4.5 | actor_loss: -0.0057 | value_loss: 17.8587 | lr: 2.32e-04
  Update   33 | Ep   460 | reward:     86.7 | mean(100):     -3.9 | actor_loss: -0.0109 | value_loss: 11.0935 | lr: 2.32e-04
  Update   34 | Ep   465 | reward:   -197.9 | mean(100):     -5.5 | actor_loss: -0.0039 | value_loss: 16.8125 | lr: 2.31e-04
  Update   35 | Ep   469 | reward:     -0.7 | mean(100):     -3.2 | actor_loss: -0.0050 | value_loss: 9.6127 | lr: 2.30e-04
  Update   36 | Ep   473 | reward:    -12.1 | mean(100):     -1.8 | actor_loss: -0.0068 | value_loss: 10.7061 | lr: 2.30e-04
  Update   37 | Ep   476 | reward:     38.0 | mean(100):     -1.3 | actor_loss: -0.0056 | value_loss: 9.0908 | lr: 2.29e-04
  Update   38 | Ep   478 | reward:    123.7 | mean(100):      2.0 | actor_loss: -0.0032 | value_loss: 6.7519 | lr: 2.29e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   39 | Ep   487 | reward:     25.7 | mean(100):     -0.3 | actor_loss: -0.0028 | value_loss: 21.2063 | lr: 2.28e-04
  Update   40 | Ep   491 | reward:    -46.0 | mean(100):      0.1 | actor_loss: -0.0040 | value_loss: 11.2440 | lr: 2.27e-04
  Update   41 | Ep   494 | reward:     -6.7 | mean(100):      1.0 | actor_loss: -0.0036 | value_loss: 12.4401 | lr: 2.26e-04
  Update   42 | Ep   499 | reward:    -39.4 | mean(100):      0.5 | actor_loss: -0.0045 | value_loss: 15.2222 | lr: 2.26e-04
  Update   43 | Ep   504 | reward:    207.3 | mean(100):      3.6 | actor_loss: -0.0026 | value_loss: 12.0366 | lr: 2.25e-04
  Update   44 | Ep   508 | reward:    -26.5 | mean(100):      3.6 | actor_loss: -0.0032 | value_loss: 10.1289 | lr: 2.24e-04
  Update   45 | Ep   510 | reward:     95.7 | mean(100):      6.4 | actor_loss: -0.0035 | value_loss: 5.1439 | lr: 2.24e-04
  Update   46 | Ep   512 | reward:    129.3 | mean(100):      7.6 | actor_loss: -0.0066 | value_loss: 8.1512 | lr: 2.23e-04
  Update   47 | Ep   515 | reward:   -133.7 | mean(100):      6.1 | actor_loss: -0.0053 | value_loss: 13.3548 | lr: 2.23e-04
  Update   48 | Ep   517 | reward:    133.2 | mean(100):      8.6 | actor_loss: -0.0023 | value_loss: 5.3651 | lr: 2.23e-04
  Update   49 | Ep   519 | reward:    133.5 | mean(100):     11.7 | actor_loss: -0.0067 | value_loss: 4.9355 | lr: 2.22e-04
  Update   50 | Ep   521 | reward:     74.2 | mean(100):     12.6 | actor_loss: -0.0038 | value_loss: 8.7208 | lr: 2.22e-04
  Update   51 | Ep   523 | reward:     -4.5 | mean(100):     13.9 | actor_loss: -0.0043 | value_loss: 7.1710 | lr: 2.22e-04
  Update   52 | Ep   526 | reward:    -62.2 | mean(100):     16.6 | actor_loss: -0.0044 | value_loss: 10.7664 | lr: 2.22e-04
  Update   53 | Ep   529 | reward:     -1.9 | mean(100):     17.1 | actor_loss: -0.0051 | value_loss: 9.3188 | lr: 2.21e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   54 | Ep   532 | reward:    -28.1 | mean(100):     14.4 | actor_loss: -0.0090 | value_loss: 10.9606 | lr: 2.21e-04
  Update   55 | Ep   534 | reward:    135.6 | mean(100):     17.2 | actor_loss: -0.0030 | value_loss: 5.2937 | lr: 2.20e-04
  Update   56 | Ep   537 | reward:    199.6 | mean(100):     20.0 | actor_loss: -0.0071 | value_loss: 11.7598 | lr: 2.20e-04
  Update   57 | Ep   539 | reward:    132.9 | mean(100):     22.2 | actor_loss: -0.0051 | value_loss: 4.2050 | lr: 2.19e-04
  Update   58 | Ep   541 | reward:    126.0 | mean(100):     22.9 | actor_loss: -0.0048 | value_loss: 4.3063 | lr: 2.19e-04
  Update   59 | Ep   543 | reward:    123.6 | mean(100):     24.0 | actor_loss: -0.0025 | value_loss: 6.1791 | lr: 2.19e-04
  Update   60 | Ep   546 | reward:    228.9 | mean(100):     27.4 | actor_loss: -0.0055 | value_loss: 12.7096 | lr: 2.19e-04
  Update   61 | Ep   548 | reward:     81.8 | mean(100):     28.4 | actor_loss: -0.0056 | value_loss: 7.2217 | lr: 2.18e-04
  Update   62 | Ep   550 | reward:     77.0 | mean(100):     31.1 | actor_loss: -0.0022 | value_loss: 11.1304 | lr: 2.18e-04
  Update   63 | Ep   552 | reward:    129.9 | mean(100):     33.9 | actor_loss: -0.0041 | value_loss: 4.1882 | lr: 2.17e-04
  Update   64 | Ep   554 | reward:    109.9 | mean(100):     37.4 | actor_loss: -0.0032 | value_loss: 4.1555 | lr: 2.17e-04
  Update   65 | Ep   557 | reward:    212.8 | mean(100):     40.8 | actor_loss: -0.0045 | value_loss: 11.4144 | lr: 2.17e-04
  Update   66 | Ep   559 | reward:     81.0 | mean(100):     43.5 | actor_loss: -0.0058 | value_loss: 5.1958 | lr: 2.16e-04
  Update   67 | Ep   561 | reward:    126.1 | mean(100):     44.7 | actor_loss: -0.0037 | value_loss: 6.8112 | lr: 2.16e-04
  Update   68 | Ep   564 | reward:    131.9 | mean(100):     47.3 | actor_loss: -0.0029 | value_loss: 12.8148 | lr: 2.16e-04
  Update   69 | Ep   566 | reward:    113.6 | mean(100):     51.6 | actor_loss: -0.0038 | value_loss: 6.3784 | lr: 2.15e-04
  Update   70 | Ep   568 | reward:   -122.3 | mean(100):     51.3 | actor_loss: -0.0049 | value_loss: 10.0520 | lr: 2.15e-04
  Update   71 | Ep   570 | reward:    122.3 | mean(100):     52.2 | actor_loss: -0.0038 | value_loss: 3.4575 | lr: 2.15e-04
  Update   72 | Ep   573 | reward:    228.7 | mean(100):     55.5 | actor_loss: -0.0054 | value_loss: 8.9802 | lr: 2.15e-04
  Update   73 | Ep   575 | reward:    100.7 | mean(100):     56.8 | actor_loss: -0.0031 | value_loss: 4.1247 | lr: 2.14e-04
  Update   74 | Ep   577 | reward:    107.5 | mean(100):     56.8 | actor_loss: -0.0029 | value_loss: 3.7929 | lr: 2.14e-04
  Update   75 | Ep   579 | reward:     29.0 | mean(100):     57.7 | actor_loss: -0.0015 | value_loss: 8.1196 | lr: 2.13e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   76 | Ep   581 | reward:     89.6 | mean(100):     62.1 | actor_loss: -0.0029 | value_loss: 7.2161 | lr: 2.13e-04
  Update   77 | Ep   583 | reward:     94.7 | mean(100):     64.8 | actor_loss: -0.0050 | value_loss: 3.4011 | lr: 2.13e-04
  Update   78 | Ep   585 | reward:     77.1 | mean(100):     67.6 | actor_loss: -0.0013 | value_loss: 7.0618 | lr: 2.13e-04
  Update   79 | Ep   588 | reward:   -122.5 | mean(100):     72.5 | actor_loss: -0.0083 | value_loss: 10.2011 | lr: 2.12e-04
  Update   80 | Ep   592 | reward:    208.9 | mean(100):     75.5 | actor_loss: -0.0025 | value_loss: 11.3810 | lr: 2.12e-04
  Update   81 | Ep   595 | reward:    208.8 | mean(100):     81.6 | actor_loss: -0.0028 | value_loss: 10.9023 | lr: 2.11e-04
  Update   82 | Ep   597 | reward:    117.0 | mean(100):     83.2 | actor_loss: -0.0076 | value_loss: 6.5340 | lr: 2.11e-04
  Update   83 | Ep   602 | reward:    -28.6 | mean(100):     84.9 | actor_loss: -0.0008 | value_loss: 15.8965 | lr: 2.10e-04
  Update   84 | Ep   605 | reward:    123.0 | mean(100):     87.8 | actor_loss: -0.0015 | value_loss: 8.8011 | lr: 2.10e-04
  Update   85 | Ep   609 | reward:    -13.8 | mean(100):     88.8 | actor_loss: -0.0035 | value_loss: 11.9358 | lr: 2.09e-04
  Update   86 | Ep   611 | reward:    104.2 | mean(100):     89.0 | actor_loss: -0.0020 | value_loss: 5.4131 | lr: 2.09e-04
  Update   87 | Ep   614 | reward:     -8.4 | mean(100):     87.9 | actor_loss: -0.0034 | value_loss: 9.6063 | lr: 2.08e-04
  Update   88 | Ep   618 | reward:    194.8 | mean(100):     92.8 | actor_loss: -0.0021 | value_loss: 14.6521 | lr: 2.08e-04
  Update   89 | Ep   621 | reward:     -9.8 | mean(100):     93.2 | actor_loss: -0.0017 | value_loss: 7.9694 | lr: 2.07e-04
  Update   90 | Ep   624 | reward:      0.5 | mean(100):     93.0 | actor_loss: -0.0008 | value_loss: 8.5880 | lr: 2.07e-04
  Update   91 | Ep   626 | reward:     78.4 | mean(100):     94.1 | actor_loss: -0.0042 | value_loss: 2.3040 | lr: 2.06e-04
  Update   92 | Ep   629 | reward:    -25.9 | mean(100):     95.5 | actor_loss: -0.0049 | value_loss: 7.0668 | lr: 2.06e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update   93 | Ep   631 | reward:    100.7 | mean(100):     98.2 | actor_loss: -0.0036 | value_loss: 4.0553 | lr: 2.06e-04
  Update   94 | Ep   634 | reward:     90.1 | mean(100):    100.2 | actor_loss: -0.0014 | value_loss: 8.4845 | lr: 2.05e-04
  Update   95 | Ep   637 | reward:    202.4 | mean(100):     99.8 | actor_loss: -0.0050 | value_loss: 8.0628 | lr: 2.05e-04
  Update   96 | Ep   640 | reward:     80.9 | mean(100):    101.2 | actor_loss: -0.0025 | value_loss: 7.9176 | lr: 2.04e-04
  Update   97 | Ep   642 | reward:     82.6 | mean(100):    101.5 | actor_loss: -0.0023 | value_loss: 1.9792 | lr: 2.04e-04
  Update   98 | Ep   645 | reward:    176.1 | mean(100):    103.5 | actor_loss: -0.0038 | value_loss: 7.3483 | lr: 2.04e-04
  Update   99 | Ep   647 | reward:    195.8 | mean(100):    104.5 | actor_loss: -0.0019 | value_loss: 4.9801 | lr: 2.03e-04
  Update  100 | Ep   649 | reward:    140.7 | mean(100):    104.6 | actor_loss: -0.0044 | value_loss: 3.2015 | lr: 2.03e-04
  Update  101 | Ep   652 | reward:    203.9 | mean(100):    105.3 | actor_loss: -0.0015 | value_loss: 9.6175 | lr: 2.03e-04
  Update  102 | Ep   654 | reward:     46.2 | mean(100):    105.3 | actor_loss: -0.0027 | value_loss: 4.4767 | lr: 2.02e-04
  Update  103 | Ep   656 | reward:     58.7 | mean(100):    105.8 | actor_loss: -0.0033 | value_loss: 4.5431 | lr: 2.02e-04
  Update  104 | Ep   658 | reward:    119.6 | mean(100):    104.6 | actor_loss: -0.0032 | value_loss: 2.4804 | lr: 2.02e-04
  Update  105 | Ep   661 | reward:    154.8 | mean(100):    104.8 | actor_loss: -0.0018 | value_loss: 8.3391 | lr: 2.01e-04
  Update  106 | Ep   663 | reward:     94.7 | mean(100):    106.0 | actor_loss: -0.0020 | value_loss: 2.1493 | lr: 2.01e-04
  Update  107 | Ep   665 | reward:    108.8 | mean(100):    104.5 | actor_loss: -0.0037 | value_loss: 1.9143 | lr: 2.01e-04
  Update  108 | Ep   667 | reward:    -58.7 | mean(100):    102.6 | actor_loss: -0.0047 | value_loss: 5.0596 | lr: 2.00e-04
  Update  109 | Ep   670 | reward:    144.1 | mean(100):    106.0 | actor_loss: -0.0007 | value_loss: 13.6377 | lr: 2.00e-04
  Update  110 | Ep   672 | reward:    107.0 | mean(100):    108.2 | actor_loss: -0.0017 | value_loss: 5.8646 | lr: 1.99e-04
  Update  111 | Ep   676 | reward:    131.0 | mean(100):    107.5 | actor_loss: -0.0030 | value_loss: 17.2108 | lr: 1.99e-04
  Update  112 | Ep   678 | reward:    135.6 | mean(100):    108.1 | actor_loss: -0.0014 | value_loss: 9.2686 | lr: 1.99e-04
  Update  113 | Ep   681 | reward:    181.9 | mean(100):    109.8 | actor_loss: -0.0018 | value_loss: 9.2957 | lr: 1.98e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  114 | Ep   686 | reward:    179.4 | mean(100):    108.3 | actor_loss: -0.0020 | value_loss: 15.7677 | lr: 1.98e-04
  Update  115 | Ep   690 | reward:    213.9 | mean(100):    114.5 | actor_loss: -0.0028 | value_loss: 14.7344 | lr: 1.97e-04
  Update  116 | Ep   692 | reward:     92.6 | mean(100):    113.6 | actor_loss: -0.0022 | value_loss: 9.6811 | lr: 1.96e-04
  Update  117 | Ep   696 | reward:     -3.0 | mean(100):    114.0 | actor_loss: -0.0019 | value_loss: 13.3006 | lr: 1.96e-04
  Update  118 | Ep   698 | reward:     60.0 | mean(100):    112.0 | actor_loss: -0.0043 | value_loss: 6.8092 | lr: 1.96e-04
  Update  119 | Ep   700 | reward:     90.8 | mean(100):    114.4 | actor_loss: -0.0017 | value_loss: 2.2346 | lr: 1.95e-04
  Update  120 | Ep   703 | reward:    -28.9 | mean(100):    114.1 | actor_loss: -0.0017 | value_loss: 8.8250 | lr: 1.95e-04
  Update  121 | Ep   706 | reward:    213.1 | mean(100):    116.4 | actor_loss: -0.0025 | value_loss: 7.3776 | lr: 1.95e-04
  Update  122 | Ep   709 | reward:    102.8 | mean(100):    114.8 | actor_loss: -0.0067 | value_loss: 9.4656 | lr: 1.94e-04
  Update  123 | Ep   711 | reward:    100.6 | mean(100):    116.3 | actor_loss: -0.0012 | value_loss: 2.4171 | lr: 1.94e-04
  Update  124 | Ep   713 | reward:    133.9 | mean(100):    117.9 | actor_loss: -0.0043 | value_loss: 2.5633 | lr: 1.93e-04
  Update  125 | Ep   715 | reward:     23.7 | mean(100):    117.4 | actor_loss: -0.0019 | value_loss: 3.8729 | lr: 1.93e-04
  Update  126 | Ep   717 | reward:    125.5 | mean(100):    117.3 | actor_loss: -0.0031 | value_loss: 5.0614 | lr: 1.93e-04
  Update  127 | Ep   719 | reward:    132.0 | mean(100):    116.9 | actor_loss: -0.0009 | value_loss: 2.6756 | lr: 1.92e-04
  Update  128 | Ep   721 | reward:    144.3 | mean(100):    117.6 | actor_loss: -0.0039 | value_loss: 3.0249 | lr: 1.92e-04
  Update  129 | Ep   723 | reward:    110.1 | mean(100):    119.6 | actor_loss: -0.0011 | value_loss: 2.6129 | lr: 1.92e-04
  Update  130 | Ep   726 | reward:     22.0 | mean(100):    120.9 | actor_loss: -0.0069 | value_loss: 8.3638 | lr: 1.92e-04
  Update  131 | Ep   728 | reward:    144.4 | mean(100):    120.4 | actor_loss: -0.0024 | value_loss: 2.8522 | lr: 1.91e-04
  Update  132 | Ep   730 | reward:    105.4 | mean(100):    121.9 | actor_loss: -0.0034 | value_loss: 2.1104 | lr: 1.91e-04
  Update  133 | Ep   732 | reward:    122.5 | mean(100):    121.8 | actor_loss: -0.0025 | value_loss: 4.4951 | lr: 1.90e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  134 | Ep   734 | reward:     94.0 | mean(100):    120.3 | actor_loss: -0.0039 | value_loss: 5.8125 | lr: 1.90e-04
  Update  135 | Ep   737 | reward:     99.3 | mean(100):    117.0 | actor_loss: -0.0038 | value_loss: 10.2467 | lr: 1.90e-04
  Update  136 | Ep   739 | reward:    116.3 | mean(100):    115.4 | actor_loss: -0.0028 | value_loss: 2.9941 | lr: 1.89e-04
  Update  137 | Ep   741 | reward:    125.0 | mean(100):    116.2 | actor_loss: -0.0033 | value_loss: 2.9606 | lr: 1.89e-04
  Update  138 | Ep   743 | reward:     83.9 | mean(100):    115.3 | actor_loss: -0.0055 | value_loss: 4.5821 | lr: 1.89e-04
  Update  139 | Ep   747 | reward:    -41.5 | mean(100):    112.5 | actor_loss: -0.0028 | value_loss: 9.8144 | lr: 1.89e-04
  Update  140 | Ep   749 | reward:    117.6 | mean(100):    113.1 | actor_loss: -0.0012 | value_loss: 3.9328 | lr: 1.88e-04
  Update  141 | Ep   752 | reward:    -17.1 | mean(100):    109.9 | actor_loss: -0.0059 | value_loss: 7.9518 | lr: 1.88e-04
  Update  142 | Ep   754 | reward:     -7.6 | mean(100):    109.1 | actor_loss: -0.0045 | value_loss: 4.9357 | lr: 1.87e-04
  Update  143 | Ep   757 | reward:    127.7 | mean(100):    106.9 | actor_loss: -0.0047 | value_loss: 8.5993 | lr: 1.87e-04
  Update  144 | Ep   759 | reward:     97.9 | mean(100):    106.8 | actor_loss: -0.0027 | value_loss: 2.5054 | lr: 1.86e-04
  Update  145 | Ep   761 | reward:     61.2 | mean(100):    104.9 | actor_loss: -0.0017 | value_loss: 3.6860 | lr: 1.86e-04
  Update  146 | Ep   763 | reward:      8.4 | mean(100):    104.5 | actor_loss: -0.0026 | value_loss: 4.5361 | lr: 1.86e-04
  Update  147 | Ep   765 | reward:    122.2 | mean(100):    104.7 | actor_loss: -0.0042 | value_loss: 2.5842 | lr: 1.86e-04
  Update  148 | Ep   767 | reward:     93.0 | mean(100):    106.4 | actor_loss: -0.0040 | value_loss: 2.1354 | lr: 1.85e-04
  Update  149 | Ep   772 | reward:   -105.3 | mean(100):     98.9 | actor_loss: -0.0038 | value_loss: 15.7052 | lr: 1.85e-04
  Update  150 | Ep   774 | reward:    110.6 | mean(100):     98.2 | actor_loss: -0.0029 | value_loss: 2.5293 | lr: 1.84e-04
  Update  151 | Ep   776 | reward:    104.1 | mean(100):     99.7 | actor_loss: -0.0052 | value_loss: 2.3598 | lr: 1.84e-04
  Update  152 | Ep   778 | reward:    105.0 | mean(100):     98.3 | actor_loss: -0.0019 | value_loss: 1.9209 | lr: 1.84e-04
  Update  153 | Ep   780 | reward:     95.7 | mean(100):     97.2 | actor_loss: -0.0051 | value_loss: 1.9717 | lr: 1.83e-04
  Update  154 | Ep   783 | reward:    202.9 | mean(100):    101.4 | actor_loss: -0.0021 | value_loss: 9.8838 | lr: 1.83e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  155 | Ep   785 | reward:     94.6 | mean(100):    100.2 | actor_loss: -0.0031 | value_loss: 2.2294 | lr: 1.83e-04
  Update  156 | Ep   787 | reward:    120.9 | mean(100):     99.8 | actor_loss: -0.0013 | value_loss: 5.0657 | lr: 1.82e-04
  Update  157 | Ep   789 | reward:    212.8 | mean(100):     99.3 | actor_loss: -0.0014 | value_loss: 4.3170 | lr: 1.82e-04
  Update  158 | Ep   791 | reward:    124.7 | mean(100):     98.2 | actor_loss: -0.0027 | value_loss: 1.8194 | lr: 1.82e-04
  Update  159 | Ep   794 | reward:    172.2 | mean(100):     97.3 | actor_loss: -0.0009 | value_loss: 9.5829 | lr: 1.81e-04
  Update  160 | Ep   797 | reward:    129.7 | mean(100):    100.0 | actor_loss: -0.0031 | value_loss: 8.2716 | lr: 1.81e-04
  Update  161 | Ep   799 | reward:    224.0 | mean(100):    101.9 | actor_loss: -0.0017 | value_loss: 4.4575 | lr: 1.80e-04
  Update  162 | Ep   801 | reward:     80.3 | mean(100):    101.1 | actor_loss: -0.0031 | value_loss: 8.4356 | lr: 1.80e-04
  Update  163 | Ep   803 | reward:    202.1 | mean(100):    103.3 | actor_loss: -0.0008 | value_loss: 5.3052 | lr: 1.80e-04
  Update  164 | Ep   806 | reward:    211.1 | mean(100):    103.7 | actor_loss: -0.0018 | value_loss: 7.8985 | lr: 1.80e-04
  Update  165 | Ep   808 | reward:     -2.0 | mean(100):    103.1 | actor_loss: -0.0065 | value_loss: 7.9556 | lr: 1.79e-04
  Update  166 | Ep   810 | reward:    204.9 | mean(100):    104.0 | actor_loss: -0.0010 | value_loss: 5.5906 | lr: 1.79e-04
  Update  167 | Ep   814 | reward:    -13.1 | mean(100):    103.0 | actor_loss: -0.0053 | value_loss: 10.4599 | lr: 1.78e-04
  Update  168 | Ep   818 | reward:    116.9 | mean(100):    103.4 | actor_loss: -0.0065 | value_loss: 9.7078 | lr: 1.78e-04
  Update  169 | Ep   825 | reward:     -3.6 | mean(100):     95.3 | actor_loss: -0.0067 | value_loss: 21.2374 | lr: 1.77e-04
  Update  170 | Ep   833 | reward:    -50.9 | mean(100):     90.4 | actor_loss: -0.0044 | value_loss: 23.7224 | lr: 1.76e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  171 | Ep   838 | reward:    221.4 | mean(100):     92.3 | actor_loss: -0.0038 | value_loss: 10.7824 | lr: 1.75e-04
  Update  172 | Ep   842 | reward:      4.9 | mean(100):     89.2 | actor_loss: -0.0046 | value_loss: 9.9616 | lr: 1.74e-04
  Update  173 | Ep   846 | reward:    -25.8 | mean(100):     86.5 | actor_loss: -0.0051 | value_loss: 10.6541 | lr: 1.74e-04
  Update  174 | Ep   851 | reward:     90.6 | mean(100):     85.5 | actor_loss: -0.0042 | value_loss: 14.8787 | lr: 1.73e-04
  Update  175 | Ep   857 | reward:     26.1 | mean(100):     83.1 | actor_loss: -0.0013 | value_loss: 16.8115 | lr: 1.72e-04
  Update  176 | Ep   860 | reward:    147.2 | mean(100):     80.5 | actor_loss: -0.0037 | value_loss: 8.1066 | lr: 1.71e-04
  Update  177 | Ep   862 | reward:    135.4 | mean(100):     79.6 | actor_loss: -0.0019 | value_loss: 5.0776 | lr: 1.71e-04
  Update  178 | Ep   869 | reward:     -4.1 | mean(100):     80.4 | actor_loss: -0.0017 | value_loss: 19.8169 | lr: 1.71e-04
  Update  179 | Ep   874 | reward:    112.1 | mean(100):     82.2 | actor_loss: -0.0048 | value_loss: 12.4028 | lr: 1.70e-04
  Update  180 | Ep   880 | reward:    -21.0 | mean(100):     75.3 | actor_loss: -0.0053 | value_loss: 14.7081 | lr: 1.69e-04
  Update  181 | Ep   884 | reward:    -77.9 | mean(100):     67.9 | actor_loss: -0.0072 | value_loss: 10.9713 | lr: 1.68e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  182 | Ep   891 | reward:    -17.3 | mean(100):     63.6 | actor_loss: -0.0026 | value_loss: 18.0617 | lr: 1.67e-04
  Update  183 | Ep   900 | reward:    238.3 | mean(100):     56.4 | actor_loss: -0.0019 | value_loss: 26.8866 | lr: 1.66e-04
  Update  184 | Ep   904 | reward:      0.3 | mean(100):     52.2 | actor_loss: -0.0029 | value_loss: 8.3224 | lr: 1.65e-04
  Update  185 | Ep   908 | reward:    120.2 | mean(100):     48.8 | actor_loss: -0.0056 | value_loss: 8.3129 | lr: 1.64e-04
  Update  186 | Ep   912 | reward:      0.3 | mean(100):     42.7 | actor_loss: -0.0025 | value_loss: 7.4031 | lr: 1.64e-04
  Update  187 | Ep   917 | reward:    -33.9 | mean(100):     39.1 | actor_loss: -0.0062 | value_loss: 11.8337 | lr: 1.63e-04
  Update  188 | Ep   923 | reward:     -1.3 | mean(100):     37.6 | actor_loss: -0.0015 | value_loss: 10.8316 | lr: 1.62e-04
  Update  189 | Ep   929 | reward:     16.7 | mean(100):     37.4 | actor_loss: -0.0054 | value_loss: 10.2649 | lr: 1.62e-04
  Update  190 | Ep   934 | reward:    -65.2 | mean(100):     38.8 | actor_loss: -0.0018 | value_loss: 11.8264 | lr: 1.61e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  191 | Ep   936 | reward:    123.9 | mean(100):     40.1 | actor_loss: -0.0054 | value_loss: 3.4058 | lr: 1.60e-04
  Update  192 | Ep   941 | reward:    -16.5 | mean(100):     40.5 | actor_loss: -0.0021 | value_loss: 10.0000 | lr: 1.60e-04
  Update  193 | Ep   944 | reward:    -13.7 | mean(100):     39.3 | actor_loss: -0.0062 | value_loss: 5.3686 | lr: 1.59e-04
  Update  194 | Ep   949 | reward:     20.5 | mean(100):     40.7 | actor_loss: -0.0020 | value_loss: 9.5391 | lr: 1.58e-04
  Update  195 | Ep   951 | reward:    112.9 | mean(100):     42.5 | actor_loss: -0.0026 | value_loss: 2.6123 | lr: 1.58e-04
  Update  196 | Ep   956 | reward:    283.3 | mean(100):     46.0 | actor_loss: -0.0108 | value_loss: 12.7332 | lr: 1.57e-04
  Update  197 | Ep   959 | reward:    -17.1 | mean(100):     50.7 | actor_loss: -0.0044 | value_loss: 7.8728 | lr: 1.57e-04
  Update  198 | Ep   967 | reward:      8.0 | mean(100):     51.3 | actor_loss: -0.0018 | value_loss: 17.6787 | lr: 1.56e-04
  Update  199 | Ep   973 | reward:     40.4 | mean(100):     51.0 | actor_loss: -0.0057 | value_loss: 11.7967 | lr: 1.55e-04
  Update  200 | Ep   978 | reward:    190.8 | mean(100):     58.1 | actor_loss: -0.0027 | value_loss: 16.5059 | lr: 1.54e-04
  Update  201 | Ep   987 | reward:     32.5 | mean(100):     65.1 | actor_loss: -0.0026 | value_loss: 22.2562 | lr: 1.53e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  202 | Ep   992 | reward:    222.9 | mean(100):     68.3 | actor_loss: -0.0028 | value_loss: 15.0827 | lr: 1.52e-04
  Update  203 | Ep   998 | reward:     -3.0 | mean(100):     67.8 | actor_loss: -0.0017 | value_loss: 11.9324 | lr: 1.51e-04
  Update  204 | Ep  1008 | reward:     57.5 | mean(100):     65.4 | actor_loss: -0.0034 | value_loss: 19.8827 | lr: 1.50e-04
  Update  205 | Ep  1014 | reward:      1.8 | mean(100):     68.8 | actor_loss: -0.0026 | value_loss: 15.2006 | lr: 1.49e-04
  Update  206 | Ep  1022 | reward:    258.2 | mean(100):     77.4 | actor_loss: -0.0045 | value_loss: 22.0219 | lr: 1.48e-04
  Update  207 | Ep  1026 | reward:    129.2 | mean(100):     81.0 | actor_loss: -0.0044 | value_loss: 9.7872 | lr: 1.47e-04
  Update  208 | Ep  1028 | reward:    239.4 | mean(100):     83.6 | actor_loss: -0.0023 | value_loss: 6.7386 | lr: 1.46e-04
  Update  209 | Ep  1035 | reward:     -8.4 | mean(100):     81.8 | actor_loss: -0.0038 | value_loss: 13.3915 | lr: 1.46e-04
  Update  210 | Ep  1039 | reward:      3.0 | mean(100):     81.9 | actor_loss: -0.0018 | value_loss: 10.6026 | lr: 1.45e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  211 | Ep  1045 | reward:     14.7 | mean(100):     86.2 | actor_loss: -0.0076 | value_loss: 22.3877 | lr: 1.44e-04
  Update  212 | Ep  1052 | reward:    -46.6 | mean(100):     83.9 | actor_loss: -0.0046 | value_loss: 18.2843 | lr: 1.43e-04
  Update  213 | Ep  1058 | reward:     -1.5 | mean(100):     88.8 | actor_loss: -0.0046 | value_loss: 17.5740 | lr: 1.42e-04
  Update  214 | Ep  1065 | reward:     21.1 | mean(100):     89.2 | actor_loss: -0.0035 | value_loss: 19.7819 | lr: 1.41e-04
  Update  215 | Ep  1069 | reward:    263.4 | mean(100):     95.8 | actor_loss: -0.0027 | value_loss: 12.9012 | lr: 1.40e-04
  Update  216 | Ep  1076 | reward:    311.6 | mean(100):     97.9 | actor_loss: -0.0021 | value_loss: 23.6234 | lr: 1.40e-04
  Update  217 | Ep  1083 | reward:     -5.6 | mean(100):     98.2 | actor_loss: -0.0063 | value_loss: 20.9692 | lr: 1.39e-04
  Update  218 | Ep  1089 | reward:    186.9 | mean(100):    100.0 | actor_loss: -0.0058 | value_loss: 16.7682 | lr: 1.38e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  219 | Ep  1094 | reward:    262.4 | mean(100):     99.8 | actor_loss: -0.0019 | value_loss: 12.2557 | lr: 1.37e-04
  Update  220 | Ep  1100 | reward:    223.6 | mean(100):    106.9 | actor_loss: -0.0027 | value_loss: 15.3453 | lr: 1.36e-04
  Update  221 | Ep  1106 | reward:    268.0 | mean(100):    113.8 | actor_loss: -0.0032 | value_loss: 19.8576 | lr: 1.35e-04
  Update  222 | Ep  1112 | reward:     42.3 | mean(100):    120.9 | actor_loss: -0.0038 | value_loss: 17.0697 | lr: 1.34e-04
  Update  223 | Ep  1118 | reward:    232.6 | mean(100):    126.6 | actor_loss: -0.0032 | value_loss: 19.1463 | lr: 1.33e-04
  Update  224 | Ep  1124 | reward:    191.6 | mean(100):    134.7 | actor_loss: -0.0031 | value_loss: 19.6097 | lr: 1.32e-04
  Update  225 | Ep  1133 | reward:    286.1 | mean(100):    136.5 | actor_loss: -0.0066 | value_loss: 21.2664 | lr: 1.31e-04
  Update  226 | Ep  1141 | reward:     -1.7 | mean(100):    143.9 | actor_loss: -0.0044 | value_loss: 22.0041 | lr: 1.30e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  227 | Ep  1146 | reward:    219.1 | mean(100):    142.7 | actor_loss: -0.0032 | value_loss: 11.3660 | lr: 1.29e-04
  Update  228 | Ep  1153 | reward:     20.6 | mean(100):    145.6 | actor_loss: -0.0039 | value_loss: 16.3632 | lr: 1.28e-04
  Update  229 | Ep  1160 | reward:    -33.4 | mean(100):    146.3 | actor_loss: -0.0031 | value_loss: 18.1382 | lr: 1.27e-04
  Update  230 | Ep  1166 | reward:    244.8 | mean(100):    145.0 | actor_loss: -0.0024 | value_loss: 12.8555 | lr: 1.26e-04
  Update  231 | Ep  1173 | reward:    260.2 | mean(100):    142.4 | actor_loss: -0.0037 | value_loss: 22.1722 | lr: 1.25e-04
  Update  232 | Ep  1177 | reward:    247.6 | mean(100):    147.7 | actor_loss: -0.0030 | value_loss: 12.2103 | lr: 1.24e-04
  Update  233 | Ep  1185 | reward:    243.2 | mean(100):    145.4 | actor_loss: -0.0024 | value_loss: 16.4498 | lr: 1.23e-04
  Update  234 | Ep  1190 | reward:    258.7 | mean(100):    151.8 | actor_loss: -0.0045 | value_loss: 15.9500 | lr: 1.22e-04
  Update  235 | Ep  1197 | reward:     10.4 | mean(100):    150.7 | actor_loss: -0.0036 | value_loss: 18.5558 | lr: 1.21e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  236 | Ep  1202 | reward:    239.6 | mean(100):    148.7 | actor_loss: -0.0049 | value_loss: 13.0560 | lr: 1.20e-04
  Update  237 | Ep  1210 | reward:    -22.6 | mean(100):    144.4 | actor_loss: -0.0011 | value_loss: 21.3769 | lr: 1.20e-04
  Update  238 | Ep  1216 | reward:     29.3 | mean(100):    140.9 | actor_loss: -0.0039 | value_loss: 16.1573 | lr: 1.18e-04
  Update  239 | Ep  1221 | reward:    256.3 | mean(100):    140.2 | actor_loss: -0.0044 | value_loss: 15.6480 | lr: 1.18e-04
  Update  240 | Ep  1224 | reward:    122.3 | mean(100):    139.0 | actor_loss: -0.0041 | value_loss: 7.4581 | lr: 1.17e-04
  Update  241 | Ep  1228 | reward:    253.8 | mean(100):    146.6 | actor_loss: -0.0030 | value_loss: 15.1110 | lr: 1.16e-04
  Update  242 | Ep  1233 | reward:    222.2 | mean(100):    151.8 | actor_loss: -0.0014 | value_loss: 15.5014 | lr: 1.16e-04
  Update  243 | Ep  1239 | reward:    244.3 | mean(100):    153.8 | actor_loss: -0.0017 | value_loss: 15.4618 | lr: 1.15e-04
  Update  244 | Ep  1247 | reward:      0.9 | mean(100):    164.2 | actor_loss: -0.0019 | value_loss: 23.1360 | lr: 1.14e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
  Update  245 | Ep  1253 | reward:    229.8 | mean(100):    171.0 | actor_loss: -0.0023 | value_loss: 17.8719 | lr: 1.13e-04
  Update  246 | Ep  1258 | reward:    264.8 | mean(100):    170.0 | actor_loss: -0.0019 | value_loss: 11.2930 | lr: 1.12e-04
  Update  247 | Ep  1263 | reward:    247.3 | mean(100):    176.7 | actor_loss: -0.0041 | value_loss: 16.3375 | lr: 1.11e-04
  Update  248 | Ep  1266 | reward:    179.0 | mean(100):    181.8 | actor_loss: -0.0055 | value_loss: 12.2215 | lr: 1.11e-04
  Update  249 | Ep  1269 | reward:    252.5 | mean(100):    184.6 | actor_loss: -0.0073 | value_loss: 9.0563 | lr: 1.10e-04
  Update  250 | Ep  1275 | reward:    219.7 | mean(100):    185.5 | actor_loss: -0.0049 | value_loss: 18.1835 | lr: 1.10e-04
  Update  251 | Ep  1279 | reward:    242.7 | mean(100):    183.5 | actor_loss: -0.0017 | value_loss: 12.5478 | lr: 1.09e-04
  Update  252 | Ep  1281 | reward:     93.8 | mean(100):    186.8 | actor_loss: -0.0028 | value_loss: 4.7619 | lr: 1.08e-04
  Update  253 | Ep  1284 | reward:    284.0 | mean(100):    189.5 | actor_loss: -0.0050 | value_loss: 9.7594 | lr: 1.08e-04
  Update  254 | Ep  1290 | reward:    246.5 | mean(100):    191.1 | actor_loss: -0.0029 | value_loss: 15.0079 | lr: 1.07e-04
  Update  255 | Ep  1296 | reward:    222.0 | mean(100):    195.9 | actor_loss: -0.0028 | value_loss: 16.7413 | lr: 1.06e-04
  Update  256 | Ep  1302 | reward:    245.4 | mean(100):    206.3 | actor_loss: -0.0013 | value_loss: 16.3299 | lr: 1.06e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png

Solved at episode 1302 (update 256) with mean 206.3!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_3.png
