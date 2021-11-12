# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：10828.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 12:47 
'''

# input
import sys

n = int(sys.stdin.readline().split()[0])
data = list(sys.stdin.readline().split() for i in range(n))
# print(data)

# stack
stack = []

for i in data:
    if len(i) == 2:
        stack.append(int(i[1]))
    else:
        command = i[0]
        if command == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif command ==  'size':
            print(len(stack))
        elif command == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])

