# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：10773.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 12:56 
'''

# input
import sys

n = int(sys.stdin.readline().split()[0])

data = []
for i in range(n):
    data.append(int(sys.stdin.readline().split()[0]))

stack = []
for i in data:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))