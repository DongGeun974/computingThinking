# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：9084.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오후 8:15 
'''

import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    num_coin = int(sys.stdin.readline())
    arr_coin = list(map(int, sys.stdin.readline().split()))
    count = int(sys.stdin.readline())

    dp = [0] * (count+1)
    dp[0] = 1

    # print(list(range(count+1)))
    for i in range(num_coin):
        # print(dp)
        for j in range(1, count+1):
            # print(j,arr_coin[i])
            if j - arr_coin[i] >= 0:
                dp[j] += dp[j-arr_coin[i]]
    # print(dp)
    print(dp[count])