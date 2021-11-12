# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：9095.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오후 5:41 
'''

# input testCase
# import sys
# testCase = int(sys.stdin.readline().split()[0])
#
# # input data
# data = list(int(sys.stdin.readline().split()[0]) for i in range(testCase))
import sys


def sumCase(x):
    if x < 0:
        return 0
    elif x <= 1:
        return 1
    return sumCase(x-1) + sumCase(x-2) + sumCase(x-3)

T = int(sys.stdin.readline().split()[0])
for i in range(T):
    n = int(sys.stdin.readline().split()[0])
    print(sumCase(n))