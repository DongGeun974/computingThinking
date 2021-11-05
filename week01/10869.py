# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10869.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-04 오후 4:55 
'''

# std input
# data = list(map(int, input().split()))

# faster
import sys

data = list(map(int, sys.stdin.readline().split()))

print(data[0] + data[1])
print(data[0] - data[1])
print(data[0] * data[1])
print(int(data[0] / data[1]))
print(data[0] % data[1])
