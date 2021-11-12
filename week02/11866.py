# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：11866.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 11:13 
'''

import collections
import sys

number, k = map(int, sys.stdin.readline().split())

target = k-1
answer = []
queue = collections.deque(list(range(1, number+1)))
while len(answer) < number:
    if queue[target] not in answer:
        answer.append(queue[target])
        queue.remove(queue[target])
        target-=1
        if len(queue) !=0 :
            target=(target+k)%len(queue)
    else:
        target=(target+1)%len(queue)
print('<',end='')
print(str(answer).replace('[','').replace(']',''),end='')
print('>')