# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2579.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-02 오전 10:00 
'''
"""
    dp(n) 정의
        
    문제에 조건으로 점화식 도출
"""
import sys

n = int(sys.stdin.readline())
step = list(int(sys.stdin.readline()) for _ in range(n))
dp = [0] *(301)
dp[0] = step[0]

if n >1:
    dp[1] = max(step[0]+step[1], step[1])
    if n >2 :
        dp[2] = max(step[0] + step[2], step[1] + step[2])

        for i in range(3,n):
            dp[i] = max(step[i]+dp[i-2], step[i]+step[i-1]+dp[i-3])

print(dp[n-1])