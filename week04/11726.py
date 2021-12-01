# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：11726.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-30 오후 3:33 
'''

import sys

n = int(sys.stdin.readline())
dp = [0] * 1001
dp [0] =1
dp [1] =1
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%10007
print(dp[n]%10007)