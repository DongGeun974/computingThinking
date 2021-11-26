# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2748.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오후 3:11 
'''

# import sys
#
# n = int(sys.stdin.readline())
#
# memo = [0] * (n+2)
#
# def dp(n):
#     if n == 1:
#         memo[n] = 1
#         return memo[n]
#     elif n == 2:
#         memo[n] = 1
#         return memo[n]
#     elif memo[n] != 0:
#         return memo[n]
#     else:
#         memo[n] = dp(n-1)+dp(n-2)
#         return memo[n]
#
# print(dp(n))


import sys

n = int(sys.stdin.readline())
if n == 1 or n == 2:
    print(1)
    exit()

memo = [0] * (n+1)

memo[1] = memo[2] =1

for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]
    # print(memo)

print(memo[n])