# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：18258.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 10:55 
'''

# input
import sys
from collections import deque

n = int(sys.stdin.readline().split()[0])
data = list(sys.stdin.readline().split() for i in range(n))

# deque
queue = deque()

for i in data:
    if len(i) == 2:
        queue.append(int(i[1]))
    else:
        if i[0] == 'pop':
            if len(queue) != 0:
                print(queue.popleft())
            else:
                print(-1)
        elif i[0] == 'front':
            if len(queue) != 0:
                print(queue[0])
            else:
                print(-1)
        elif i[0] == 'back':
            if len(queue) != 0:
                print(queue[-1])
            else:
                print(-1)

        if i[0] == 'size':
                print(len(queue))

        elif i[0] =='empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)