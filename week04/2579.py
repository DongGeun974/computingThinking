# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2579.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-30 오후 4:08 
'''

import sys

n = int(sys.stdin.readline())
step = list(int(sys.stdin.readline()) for _ in range(n))
if n == 1:
    print(step[0])
    exit()
if n == 2:
    print(step[0] + step[1])
    exit()
dp = [0] * (n+1)
dp[0] = step[0]
dp[1] = max(step[0] + step[1], step[1])
dp[2] = max(step[0] + step [2], step[1] + step[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i] + step[i-1])

print(dp[n-1])