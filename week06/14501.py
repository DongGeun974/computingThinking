# -*- coding: UTF-8 -*-
'''
@Project ：week06 
@File ：14501.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-13 오후 11:29 
'''

import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(len(arr)):
    dp[i] = max(dp[i - 1], dp[i])
    cost, val = arr[i]
    if (i + cost) <= (n):
        dp[i+cost] = max(dp[i+cost], dp[i] + val)

print(max(dp))