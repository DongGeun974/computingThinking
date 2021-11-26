# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1904.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오후 5:35 
'''

"""
    이전 결과에 00와 1을 추가
    
    n=5 일때,
    
    n=3 >> 001, 100, 111, 3개
    n=4 >> 0011, 0000, 1001, 1100, 1111, 5개
    
    3의 경우에 00 추가
    00001, 00100, 10000
    00111, 11100
    3의 경우에 1 추가
    11001, 10011, 11111
    
    4의 경우에 1추가
    10011, 00111, 10000, 00001, 11001, 11111
    
    n-2일때, 맨 뒤에 00 추가
    n-1일때, 맨 앞에 1 추가
    
    f(n) = f(n-2) + f(n-1)
"""

import sys

n = int(sys.stdin.readline())

memo = [0] * (n+1)
if n == 1:
    memo[1] = 1
    print(memo[1])
elif n == 2:
    memo[2] = 2
    print(memo[2])
else:
    memo[1] = 1
    memo[2] = 2
    for i in range(3,n+1):
        memo[i]=(memo[i-1] + memo[i-2])%15746
    print(memo[n]%15746)
