# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2253.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오후 7:55 
'''
import sys

n,m = map(int, sys.stdin.readline().split())
stone = set()
for i in range(m):
    stone.add(int(sys.stdin.readline()))
dp = [[float('inf')] * (int((2*n) ** 0.5)+2) for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    if i in stone:
        continue
    for j in range(1, int((2*i) ** 0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

if min(dp[n]) == float('inf'):
    print(-1)
else:
    print(min(dp[n]))