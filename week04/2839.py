# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2839.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-29 오후 2:11 
'''

import sys

n = int(sys.stdin.readline())
dp = [float('inf')] * 5001
dp[3] = dp[5] = 1
for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
if dp[n] != float('inf'):
    print(dp[n])
else:
    print(-1)