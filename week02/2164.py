# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2164.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 11:05 
'''

# input
import collections
import sys

n = int(sys.stdin.readline().split()[0])

# deque
queue = collections.deque(list(range(n, 0, -1)))

while True:
    if len(queue) == 1:
        break
    else:
        queue.pop()
        temp = queue[-1]
        queue.insert(0,temp)
        queue.pop()

print(queue.pop())