Using device: cuda (rollout collection stays on CPU; batched PPO update uses cuda)
Training PPO on LunarLander-v3 (up to 2000 episodes)
  n_steps=2048  n_epochs=4  batch_size=64
  clip_eps=0.2  lr=0.0003  gamma=0.999  gae_lambda=0.98
  entropy_coef=0.01  value_coef=0.5

  Update    1 | Ep    22 | reward:   -112.3 | mean(100):   -162.2 | actor_loss: -0.0062 | value_loss: 61.3195 | lr: 3.00e-04
  Update    2 | Ep    44 | reward:   -456.6 | mean(100):   -179.3 | actor_loss: -0.0092 | value_loss: 73.7883 | lr: 2.97e-04
  Update    3 | Ep    66 | reward:    -91.0 | mean(100):   -163.9 | actor_loss: -0.0047 | value_loss: 52.2671 | lr: 2.93e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update    4 | Ep    88 | reward:   -167.4 | mean(100):   -153.7 | actor_loss: -0.0079 | value_loss: 45.6530 | lr: 2.90e-04
  Update    5 | Ep   109 | reward:   -300.6 | mean(100):   -145.6 | actor_loss: -0.0123 | value_loss: 47.4218 | lr: 2.87e-04
  Update    6 | Ep   131 | reward:    -54.2 | mean(100):   -133.8 | actor_loss: -0.0073 | value_loss: 38.2263 | lr: 2.84e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update    7 | Ep   154 | reward:    -95.3 | mean(100):   -112.0 | actor_loss: -0.0083 | value_loss: 34.7758 | lr: 2.80e-04
  Update    8 | Ep   176 | reward:    -82.7 | mean(100):   -103.5 | actor_loss: -0.0055 | value_loss: 31.8475 | lr: 2.77e-04
  Update    9 | Ep   199 | reward:    -74.8 | mean(100):    -93.3 | actor_loss: -0.0081 | value_loss: 30.7072 | lr: 2.74e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   10 | Ep   222 | reward:    -71.3 | mean(100):    -79.8 | actor_loss: -0.0077 | value_loss: 25.0616 | lr: 2.70e-04
  Update   11 | Ep   242 | reward:    -57.9 | mean(100):    -75.7 | actor_loss: -0.0078 | value_loss: 24.0302 | lr: 2.67e-04
  Update   12 | Ep   265 | reward:    -72.7 | mean(100):    -70.5 | actor_loss: -0.0062 | value_loss: 26.0099 | lr: 2.64e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   13 | Ep   286 | reward:    -73.5 | mean(100):    -65.1 | actor_loss: -0.0068 | value_loss: 22.1364 | lr: 2.60e-04
  Update   14 | Ep   306 | reward:    -54.5 | mean(100):    -61.7 | actor_loss: -0.0070 | value_loss: 23.6605 | lr: 2.57e-04
  Update   15 | Ep   326 | reward:    -81.3 | mean(100):    -60.6 | actor_loss: -0.0103 | value_loss: 22.3750 | lr: 2.54e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   16 | Ep   345 | reward:    -49.4 | mean(100):    -59.8 | actor_loss: -0.0083 | value_loss: 22.6643 | lr: 2.51e-04
  Update   17 | Ep   364 | reward:    -85.4 | mean(100):    -59.0 | actor_loss: -0.0052 | value_loss: 23.9594 | lr: 2.48e-04
  Update   18 | Ep   382 | reward:    -92.2 | mean(100):    -60.5 | actor_loss: -0.0111 | value_loss: 26.6077 | lr: 2.45e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   19 | Ep   400 | reward:   -160.5 | mean(100):    -62.6 | actor_loss: -0.0068 | value_loss: 24.6255 | lr: 2.43e-04
  Update   20 | Ep   418 | reward:    -30.2 | mean(100):    -60.2 | actor_loss: -0.0075 | value_loss: 21.3947 | lr: 2.40e-04
  Update   21 | Ep   433 | reward:     11.1 | mean(100):    -57.0 | actor_loss: -0.0046 | value_loss: 23.5677 | lr: 2.37e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   22 | Ep   451 | reward:      7.8 | mean(100):    -53.6 | actor_loss: -0.0074 | value_loss: 21.9133 | lr: 2.35e-04
  Update   23 | Ep   470 | reward:     -4.1 | mean(100):    -46.2 | actor_loss: -0.0065 | value_loss: 20.1112 | lr: 2.32e-04
  Update   24 | Ep   479 | reward:     74.4 | mean(100):    -42.4 | actor_loss: -0.0052 | value_loss: 17.3134 | lr: 2.29e-04
  Update   25 | Ep   489 | reward:    -36.0 | mean(100):    -35.5 | actor_loss: -0.0067 | value_loss: 15.7191 | lr: 2.28e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   26 | Ep   506 | reward:    -55.0 | mean(100):    -27.3 | actor_loss: -0.0055 | value_loss: 18.0283 | lr: 2.27e-04
  Update   27 | Ep   515 | reward:   -114.8 | mean(100):    -24.0 | actor_loss: -0.0079 | value_loss: 18.1789 | lr: 2.24e-04
  Update   28 | Ep   523 | reward:     -3.9 | mean(100):    -20.4 | actor_loss: -0.0059 | value_loss: 14.5174 | lr: 2.23e-04
  Update   29 | Ep   525 | reward:     28.8 | mean(100):    -17.9 | actor_loss: -0.0049 | value_loss: 10.9499 | lr: 2.22e-04
  Update   30 | Ep   533 | reward:      2.6 | mean(100):    -13.5 | actor_loss: -0.0092 | value_loss: 13.6751 | lr: 2.21e-04
  Update   31 | Ep   536 | reward:      9.8 | mean(100):    -11.2 | actor_loss: -0.0046 | value_loss: 10.7450 | lr: 2.20e-04
  Update   32 | Ep   538 | reward:    101.5 | mean(100):     -9.1 | actor_loss: -0.0023 | value_loss: 9.2208 | lr: 2.20e-04
  Update   33 | Ep   542 | reward:    -36.0 | mean(100):     -8.9 | actor_loss: -0.0057 | value_loss: 13.2309 | lr: 2.19e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   34 | Ep   547 | reward:    119.7 | mean(100):     -4.3 | actor_loss: -0.0079 | value_loss: 12.3421 | lr: 2.19e-04
  Update   35 | Ep   551 | reward:     66.7 | mean(100):     -2.7 | actor_loss: -0.0028 | value_loss: 13.0768 | lr: 2.18e-04
  Update   36 | Ep   554 | reward:   -107.4 | mean(100):     -2.7 | actor_loss: -0.0050 | value_loss: 13.8886 | lr: 2.17e-04
  Update   37 | Ep   556 | reward:    -12.0 | mean(100):     -1.8 | actor_loss: -0.0032 | value_loss: 8.1208 | lr: 2.17e-04
  Update   38 | Ep   558 | reward:    153.1 | mean(100):      0.8 | actor_loss: -0.0047 | value_loss: 7.2007 | lr: 2.17e-04
  Update   39 | Ep   560 | reward:    126.3 | mean(100):      2.1 | actor_loss: -0.0067 | value_loss: 7.0730 | lr: 2.16e-04
  Update   40 | Ep   563 | reward:    -34.9 | mean(100):      3.0 | actor_loss: -0.0091 | value_loss: 12.1605 | lr: 2.16e-04
  Update   41 | Ep   565 | reward:     75.2 | mean(100):      4.5 | actor_loss: -0.0069 | value_loss: 8.5134 | lr: 2.16e-04
  Update   42 | Ep   567 | reward:     68.9 | mean(100):      6.9 | actor_loss: -0.0049 | value_loss: 6.8553 | lr: 2.15e-04
  Update   43 | Ep   569 | reward:    114.7 | mean(100):      9.8 | actor_loss: -0.0068 | value_loss: 6.2634 | lr: 2.15e-04
  Update   44 | Ep   571 | reward:    129.8 | mean(100):     12.8 | actor_loss: -0.0023 | value_loss: 4.9411 | lr: 2.15e-04
  Update   45 | Ep   573 | reward:    124.9 | mean(100):     16.1 | actor_loss: -0.0031 | value_loss: 5.3926 | lr: 2.14e-04
  Update   46 | Ep   576 | reward:     -5.1 | mean(100):     17.6 | actor_loss: -0.0024 | value_loss: 10.7683 | lr: 2.14e-04
  Update   47 | Ep   578 | reward:    107.7 | mean(100):     20.8 | actor_loss: -0.0037 | value_loss: 5.5874 | lr: 2.14e-04
  Update   48 | Ep   580 | reward:     83.7 | mean(100):     21.9 | actor_loss: -0.0051 | value_loss: 6.6136 | lr: 2.13e-04
  Update   49 | Ep   582 | reward:    -32.2 | mean(100):     17.5 | actor_loss: -0.0073 | value_loss: 18.7508 | lr: 2.13e-04
  Update   50 | Ep   584 | reward:    126.3 | mean(100):     19.7 | actor_loss: -0.0031 | value_loss: 4.1288 | lr: 2.13e-04
  Update   51 | Ep   586 | reward:     60.1 | mean(100):     22.8 | actor_loss: -0.0018 | value_loss: 7.9705 | lr: 2.12e-04
  Update   52 | Ep   588 | reward:    118.6 | mean(100):     25.0 | actor_loss: -0.0054 | value_loss: 4.4228 | lr: 2.12e-04
  Update   53 | Ep   590 | reward:     95.6 | mean(100):     28.0 | actor_loss: -0.0038 | value_loss: 3.8787 | lr: 2.12e-04
  Update   54 | Ep   592 | reward:     71.9 | mean(100):     29.8 | actor_loss: -0.0039 | value_loss: 6.2470 | lr: 2.11e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   55 | Ep   594 | reward:     95.4 | mean(100):     31.3 | actor_loss: -0.0048 | value_loss: 8.0870 | lr: 2.11e-04
  Update   56 | Ep   596 | reward:    129.7 | mean(100):     33.8 | actor_loss: -0.0084 | value_loss: 5.2386 | lr: 2.11e-04
  Update   57 | Ep   598 | reward:      1.9 | mean(100):     34.7 | actor_loss: -0.0030 | value_loss: 5.4285 | lr: 2.11e-04
  Update   58 | Ep   600 | reward:    169.7 | mean(100):     37.8 | actor_loss: 0.0003 | value_loss: 5.2906 | lr: 2.10e-04
  Update   59 | Ep   602 | reward:    176.0 | mean(100):     40.8 | actor_loss: -0.0036 | value_loss: 4.4971 | lr: 2.10e-04
  Update   60 | Ep   604 | reward:    114.2 | mean(100):     42.7 | actor_loss: -0.0019 | value_loss: 3.5398 | lr: 2.10e-04
  Update   61 | Ep   606 | reward:    116.3 | mean(100):     45.8 | actor_loss: -0.0016 | value_loss: 4.0771 | lr: 2.09e-04
  Update   62 | Ep   608 | reward:    102.5 | mean(100):     47.3 | actor_loss: -0.0056 | value_loss: 3.3037 | lr: 2.09e-04
  Update   63 | Ep   610 | reward:    147.5 | mean(100):     49.4 | actor_loss: -0.0033 | value_loss: 3.5514 | lr: 2.09e-04
  Update   64 | Ep   612 | reward:     88.1 | mean(100):     51.7 | actor_loss: -0.0025 | value_loss: 3.4981 | lr: 2.08e-04
  Update   65 | Ep   614 | reward:    145.6 | mean(100):     54.4 | actor_loss: -0.0025 | value_loss: 5.8418 | lr: 2.08e-04
  Update   66 | Ep   616 | reward:     54.2 | mean(100):     57.4 | actor_loss: -0.0049 | value_loss: 4.9563 | lr: 2.08e-04
  Update   67 | Ep   618 | reward:     18.3 | mean(100):     58.9 | actor_loss: -0.0041 | value_loss: 5.9315 | lr: 2.08e-04
  Update   68 | Ep   620 | reward:    167.2 | mean(100):     61.5 | actor_loss: -0.0011 | value_loss: 5.2741 | lr: 2.07e-04
  Update   69 | Ep   622 | reward:     99.3 | mean(100):     63.4 | actor_loss: -0.0013 | value_loss: 4.0440 | lr: 2.07e-04
  Update   70 | Ep   624 | reward:    116.0 | mean(100):     63.8 | actor_loss: -0.0043 | value_loss: 6.4841 | lr: 2.07e-04
  Update   71 | Ep   626 | reward:    147.0 | mean(100):     64.8 | actor_loss: -0.0029 | value_loss: 6.3599 | lr: 2.06e-04
  Update   72 | Ep   628 | reward:     83.2 | mean(100):     66.7 | actor_loss: -0.0051 | value_loss: 2.9090 | lr: 2.06e-04
  Update   73 | Ep   630 | reward:    126.0 | mean(100):     69.0 | actor_loss: -0.0055 | value_loss: 4.4552 | lr: 2.06e-04
  Update   74 | Ep   632 | reward:    155.6 | mean(100):     69.8 | actor_loss: -0.0028 | value_loss: 5.5379 | lr: 2.06e-04
  Update   75 | Ep   634 | reward:    119.9 | mean(100):     71.5 | actor_loss: -0.0040 | value_loss: 2.8949 | lr: 2.05e-04
  Update   76 | Ep   636 | reward:    138.8 | mean(100):     73.6 | actor_loss: -0.0031 | value_loss: 3.2959 | lr: 2.05e-04
  Update   77 | Ep   638 | reward:     99.1 | mean(100):     73.9 | actor_loss: -0.0017 | value_loss: 2.5559 | lr: 2.05e-04
  Update   78 | Ep   640 | reward:    121.6 | mean(100):     76.4 | actor_loss: -0.0081 | value_loss: 3.0342 | lr: 2.04e-04
  Update   79 | Ep   642 | reward:     95.1 | mean(100):     79.2 | actor_loss: -0.0021 | value_loss: 2.9855 | lr: 2.04e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update   80 | Ep   644 | reward:    128.1 | mean(100):     82.1 | actor_loss: -0.0018 | value_loss: 3.5032 | lr: 2.04e-04
  Update   81 | Ep   646 | reward:    121.5 | mean(100):     83.1 | actor_loss: -0.0015 | value_loss: 8.5255 | lr: 2.03e-04
  Update   82 | Ep   648 | reward:    114.6 | mean(100):     83.7 | actor_loss: -0.0032 | value_loss: 6.3790 | lr: 2.03e-04
  Update   83 | Ep   650 | reward:    161.4 | mean(100):     86.8 | actor_loss: -0.0017 | value_loss: 3.3289 | lr: 2.03e-04
  Update   84 | Ep   652 | reward:    115.3 | mean(100):     86.4 | actor_loss: -0.0019 | value_loss: 5.6007 | lr: 2.02e-04
  Update   85 | Ep   654 | reward:    127.9 | mean(100):     90.0 | actor_loss: -0.0002 | value_loss: 4.3050 | lr: 2.02e-04
  Update   86 | Ep   656 | reward:    143.1 | mean(100):     91.3 | actor_loss: -0.0010 | value_loss: 2.8577 | lr: 2.02e-04
  Update   87 | Ep   658 | reward:     97.9 | mean(100):     90.9 | actor_loss: -0.0045 | value_loss: 2.3115 | lr: 2.02e-04
  Update   88 | Ep   660 | reward:    142.8 | mean(100):     92.6 | actor_loss: -0.0035 | value_loss: 2.8216 | lr: 2.01e-04
  Update   89 | Ep   662 | reward:    133.4 | mean(100):     94.6 | actor_loss: -0.0049 | value_loss: 3.6538 | lr: 2.01e-04
  Update   90 | Ep   664 | reward:    144.8 | mean(100):     97.5 | actor_loss: -0.0011 | value_loss: 2.7913 | lr: 2.01e-04
  Update   91 | Ep   666 | reward:    104.1 | mean(100):     95.9 | actor_loss: -0.0007 | value_loss: 4.9126 | lr: 2.00e-04
  Update   92 | Ep   668 | reward:    111.7 | mean(100):     96.3 | actor_loss: -0.0021 | value_loss: 2.4389 | lr: 2.00e-04
  Update   93 | Ep   670 | reward:    -30.9 | mean(100):     94.4 | actor_loss: -0.0010 | value_loss: 5.8629 | lr: 2.00e-04
  Update   94 | Ep   672 | reward:    124.5 | mean(100):     94.2 | actor_loss: -0.0070 | value_loss: 2.2011 | lr: 1.99e-04
  Update   95 | Ep   674 | reward:     81.7 | mean(100):     95.6 | actor_loss: -0.0009 | value_loss: 5.4846 | lr: 1.99e-04
  Update   96 | Ep   676 | reward:     92.1 | mean(100):     97.2 | actor_loss: -0.0031 | value_loss: 2.5080 | lr: 1.99e-04
  Update   97 | Ep   678 | reward:    153.9 | mean(100):     95.7 | actor_loss: -0.0035 | value_loss: 6.7900 | lr: 1.99e-04
  Update   98 | Ep   680 | reward:    -90.2 | mean(100):     93.9 | actor_loss: -0.0015 | value_loss: 6.8384 | lr: 1.98e-04
  Update   99 | Ep   683 | reward:     46.6 | mean(100):     97.5 | actor_loss: -0.0086 | value_loss: 7.2852 | lr: 1.98e-04
  Update  100 | Ep   685 | reward:    115.7 | mean(100):     97.2 | actor_loss: -0.0036 | value_loss: 3.0774 | lr: 1.98e-04
  Update  101 | Ep   687 | reward:    137.8 | mean(100):     96.6 | actor_loss: -0.0036 | value_loss: 6.4971 | lr: 1.97e-04
  Update  102 | Ep   689 | reward:     88.8 | mean(100):     94.8 | actor_loss: -0.0091 | value_loss: 5.4770 | lr: 1.97e-04
  Update  103 | Ep   691 | reward:     11.6 | mean(100):     94.0 | actor_loss: -0.0011 | value_loss: 6.0624 | lr: 1.97e-04
  Update  104 | Ep   694 | reward:    -14.8 | mean(100):     94.6 | actor_loss: -0.0035 | value_loss: 9.2343 | lr: 1.96e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  105 | Ep   696 | reward:    248.8 | mean(100):     97.6 | actor_loss: -0.0024 | value_loss: 10.0707 | lr: 1.96e-04
  Update  106 | Ep   698 | reward:     91.2 | mean(100):     99.4 | actor_loss: -0.0028 | value_loss: 5.1785 | lr: 1.96e-04
  Update  107 | Ep   701 | reward:    196.1 | mean(100):     97.8 | actor_loss: -0.0005 | value_loss: 9.0376 | lr: 1.95e-04
  Update  108 | Ep   704 | reward:    262.3 | mean(100):    101.3 | actor_loss: -0.0019 | value_loss: 11.1829 | lr: 1.95e-04
  Update  109 | Ep   707 | reward:    -56.0 | mean(100):    100.9 | actor_loss: -0.0043 | value_loss: 8.1164 | lr: 1.94e-04
  Update  110 | Ep   710 | reward:     26.6 | mean(100):    100.9 | actor_loss: -0.0022 | value_loss: 9.1742 | lr: 1.94e-04
  Update  111 | Ep   714 | reward:    237.0 | mean(100):     99.9 | actor_loss: -0.0024 | value_loss: 13.6241 | lr: 1.93e-04
  Update  112 | Ep   719 | reward:    -72.2 | mean(100):     96.6 | actor_loss: -0.0032 | value_loss: 20.2568 | lr: 1.93e-04
  Update  113 | Ep   723 | reward:    263.6 | mean(100):     97.7 | actor_loss: -0.0042 | value_loss: 14.6053 | lr: 1.92e-04
  Update  114 | Ep   727 | reward:    240.4 | mean(100):    101.0 | actor_loss: -0.0022 | value_loss: 13.2446 | lr: 1.92e-04
  Update  115 | Ep   732 | reward:    -46.3 | mean(100):     97.5 | actor_loss: -0.0044 | value_loss: 16.7670 | lr: 1.91e-04
  Update  116 | Ep   736 | reward:     -8.8 | mean(100):     97.5 | actor_loss: -0.0024 | value_loss: 16.1557 | lr: 1.90e-04
  Update  117 | Ep   739 | reward:    240.9 | mean(100):     99.8 | actor_loss: -0.0010 | value_loss: 8.6131 | lr: 1.90e-04
  Update  118 | Ep   743 | reward:    174.0 | mean(100):    100.9 | actor_loss: -0.0036 | value_loss: 12.0348 | lr: 1.89e-04
  Update  119 | Ep   747 | reward:    203.6 | mean(100):    105.8 | actor_loss: -0.0023 | value_loss: 12.7841 | lr: 1.89e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  120 | Ep   753 | reward:    199.9 | mean(100):    106.1 | actor_loss: -0.0006 | value_loss: 20.3305 | lr: 1.88e-04
  Update  121 | Ep   757 | reward:    -60.2 | mean(100):    106.8 | actor_loss: -0.0049 | value_loss: 15.5998 | lr: 1.87e-04
  Update  122 | Ep   761 | reward:      2.4 | mean(100):    104.7 | actor_loss: -0.0042 | value_loss: 10.5441 | lr: 1.86e-04
  Update  123 | Ep   767 | reward:      5.5 | mean(100):    103.7 | actor_loss: -0.0041 | value_loss: 18.5845 | lr: 1.86e-04
  Update  124 | Ep   772 | reward:    216.6 | mean(100):    106.9 | actor_loss: -0.0029 | value_loss: 15.6342 | lr: 1.85e-04
  Update  125 | Ep   777 | reward:    -87.6 | mean(100):    108.3 | actor_loss: -0.0035 | value_loss: 16.1455 | lr: 1.84e-04
  Update  126 | Ep   783 | reward:     29.9 | mean(100):    112.3 | actor_loss: -0.0037 | value_loss: 19.7614 | lr: 1.83e-04
  Update  127 | Ep   788 | reward:     14.5 | mean(100):    119.2 | actor_loss: -0.0011 | value_loss: 16.6530 | lr: 1.83e-04
  Update  128 | Ep   793 | reward:    268.7 | mean(100):    124.2 | actor_loss: -0.0026 | value_loss: 18.3426 | lr: 1.82e-04
  Update  129 | Ep   799 | reward:    252.6 | mean(100):    125.4 | actor_loss: -0.0013 | value_loss: 19.6145 | lr: 1.81e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  130 | Ep   804 | reward:    -14.3 | mean(100):    122.0 | actor_loss: -0.0043 | value_loss: 17.6584 | lr: 1.80e-04
  Update  131 | Ep   810 | reward:    262.4 | mean(100):    122.6 | actor_loss: -0.0028 | value_loss: 17.9594 | lr: 1.79e-04
  Update  132 | Ep   816 | reward:    -19.5 | mean(100):    124.4 | actor_loss: -0.0021 | value_loss: 21.0362 | lr: 1.78e-04
  Update  133 | Ep   822 | reward:    224.4 | mean(100):    128.6 | actor_loss: -0.0030 | value_loss: 17.8090 | lr: 1.78e-04
  Update  134 | Ep   826 | reward:     52.7 | mean(100):    124.0 | actor_loss: -0.0057 | value_loss: 15.8186 | lr: 1.77e-04
  Update  135 | Ep   830 | reward:    273.3 | mean(100):    127.6 | actor_loss: -0.0031 | value_loss: 16.0119 | lr: 1.76e-04
  Update  136 | Ep   835 | reward:    216.3 | mean(100):    130.6 | actor_loss: -0.0023 | value_loss: 19.3431 | lr: 1.75e-04
  Update  137 | Ep   840 | reward:     -3.3 | mean(100):    128.1 | actor_loss: -0.0022 | value_loss: 19.2178 | lr: 1.75e-04
  Update  138 | Ep   844 | reward:    234.4 | mean(100):    133.7 | actor_loss: -0.0022 | value_loss: 14.5440 | lr: 1.74e-04
  Update  139 | Ep   849 | reward:    247.4 | mean(100):    136.8 | actor_loss: -0.0039 | value_loss: 16.6116 | lr: 1.73e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  140 | Ep   853 | reward:    175.7 | mean(100):    135.9 | actor_loss: -0.0017 | value_loss: 22.6584 | lr: 1.73e-04
  Update  141 | Ep   859 | reward:    268.7 | mean(100):    139.5 | actor_loss: -0.0034 | value_loss: 19.5168 | lr: 1.72e-04
  Update  142 | Ep   865 | reward:    249.6 | mean(100):    145.0 | actor_loss: -0.0006 | value_loss: 19.2547 | lr: 1.71e-04
  Update  143 | Ep   869 | reward:     -5.1 | mean(100):    147.4 | actor_loss: -0.0021 | value_loss: 14.4234 | lr: 1.70e-04
  Update  144 | Ep   874 | reward:    251.2 | mean(100):    155.4 | actor_loss: -0.0015 | value_loss: 16.9599 | lr: 1.70e-04
  Update  145 | Ep   879 | reward:    274.6 | mean(100):    163.4 | actor_loss: -0.0032 | value_loss: 17.1734 | lr: 1.69e-04
  Update  146 | Ep   886 | reward:    254.3 | mean(100):    161.0 | actor_loss: -0.0024 | value_loss: 23.2929 | lr: 1.68e-04
  Update  147 | Ep   892 | reward:    262.2 | mean(100):    164.0 | actor_loss: -0.0053 | value_loss: 21.9477 | lr: 1.67e-04
  Update  148 | Ep   898 | reward:    224.4 | mean(100):    166.1 | actor_loss: -0.0061 | value_loss: 21.6951 | lr: 1.66e-04
  Update  149 | Ep   905 | reward:    249.1 | mean(100):    168.2 | actor_loss: -0.0031 | value_loss: 23.2976 | lr: 1.65e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  150 | Ep   911 | reward:    247.0 | mean(100):    174.2 | actor_loss: -0.0058 | value_loss: 21.4928 | lr: 1.64e-04
  Update  151 | Ep   916 | reward:     35.9 | mean(100):    176.3 | actor_loss: -0.0044 | value_loss: 16.6071 | lr: 1.63e-04
  Update  152 | Ep   922 | reward:    227.3 | mean(100):    183.6 | actor_loss: -0.0012 | value_loss: 21.6693 | lr: 1.63e-04
  Update  153 | Ep   928 | reward:    273.2 | mean(100):    191.5 | actor_loss: -0.0033 | value_loss: 20.2496 | lr: 1.62e-04
  Update  154 | Ep   936 | reward:    284.8 | mean(100):    193.8 | actor_loss: -0.0075 | value_loss: 27.5463 | lr: 1.61e-04
  Update  155 | Ep   942 | reward:    237.6 | mean(100):    193.6 | actor_loss: -0.0022 | value_loss: 25.4494 | lr: 1.60e-04
  Update  156 | Ep   949 | reward:     50.4 | mean(100):    184.5 | actor_loss: -0.0010 | value_loss: 25.8050 | lr: 1.59e-04
  Update  157 | Ep   956 | reward:    273.0 | mean(100):    194.7 | actor_loss: -0.0025 | value_loss: 23.5164 | lr: 1.58e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  158 | Ep   963 | reward:     15.6 | mean(100):    194.6 | actor_loss: -0.0031 | value_loss: 22.0496 | lr: 1.57e-04
  Update  159 | Ep   967 | reward:    257.0 | mean(100):    196.5 | actor_loss: -0.0016 | value_loss: 14.5747 | lr: 1.56e-04
  Update  160 | Ep   970 | reward:    199.0 | mean(100):    196.4 | actor_loss: -0.0026 | value_loss: 13.8477 | lr: 1.55e-04
  Update  161 | Ep   978 | reward:    285.8 | mean(100):    192.6 | actor_loss: -0.0004 | value_loss: 24.3693 | lr: 1.54e-04
  Update  162 | Ep   986 | reward:    264.0 | mean(100):    195.3 | actor_loss: -0.0015 | value_loss: 26.9183 | lr: 1.53e-04
  Update  163 | Ep   993 | reward:     23.3 | mean(100):    193.6 | actor_loss: -0.0036 | value_loss: 23.5305 | lr: 1.52e-04
  Update  164 | Ep  1000 | reward:    260.6 | mean(100):    191.1 | actor_loss: -0.0048 | value_loss: 24.0035 | lr: 1.51e-04
  Update  165 | Ep  1007 | reward:    266.8 | mean(100):    196.0 | actor_loss: -0.0036 | value_loss: 24.8308 | lr: 1.50e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  166 | Ep  1013 | reward:    269.5 | mean(100):    194.2 | actor_loss: -0.0013 | value_loss: 19.8350 | lr: 1.49e-04
  Update  167 | Ep  1020 | reward:     22.7 | mean(100):    196.8 | actor_loss: -0.0016 | value_loss: 21.5283 | lr: 1.48e-04
  Update  168 | Ep  1028 | reward:      7.8 | mean(100):    192.7 | actor_loss: -0.0017 | value_loss: 24.9687 | lr: 1.47e-04
  Update  169 | Ep  1036 | reward:    -44.7 | mean(100):    188.0 | actor_loss: -0.0043 | value_loss: 26.0683 | lr: 1.46e-04
  Update  170 | Ep  1043 | reward:      4.6 | mean(100):    189.1 | actor_loss: -0.0044 | value_loss: 23.6491 | lr: 1.45e-04
  Update  171 | Ep  1050 | reward:    240.0 | mean(100):    194.0 | actor_loss: -0.0060 | value_loss: 22.9822 | lr: 1.44e-04
  Update  172 | Ep  1058 | reward:    263.2 | mean(100):    187.5 | actor_loss: -0.0047 | value_loss: 26.3317 | lr: 1.42e-04
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
  Update  173 | Ep  1065 | reward:    268.8 | mean(100):    189.9 | actor_loss: -0.0027 | value_loss: 21.1809 | lr: 1.41e-04
  Update  174 | Ep  1073 | reward:    241.5 | mean(100):    190.5 | actor_loss: -0.0071 | value_loss: 24.4912 | lr: 1.40e-04
  Update  175 | Ep  1080 | reward:    259.3 | mean(100):    194.8 | actor_loss: -0.0032 | value_loss: 21.1404 | lr: 1.39e-04
  Update  176 | Ep  1087 | reward:    284.6 | mean(100):    197.0 | actor_loss: -0.0026 | value_loss: 22.3306 | lr: 1.38e-04
  Update  177 | Ep  1094 | reward:    274.9 | mean(100):    204.1 | actor_loss: -0.0002 | value_loss: 21.9397 | lr: 1.37e-04

Solved at episode 1094 (update 177) with mean 204.1!
  Plot saved to: /home/vijay/Documents/work3/logs/rewards_4.png
