# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2869.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 1:13 
'''
import sys
from math import ceil


def snail(start, go, back, goal):
    now = start + go
    if now >= goal:
        return 1
    else:
        now = now - back
        return snail(now, go, back,goal) + 1

data = list(map(int, sys.stdin.readline().split()))

# add to solve RecursionError, fix to logic(need to ceil)
day = ceil((data[2]-data[0]) / (data[0] - data[1]))
start = (data[2]-data[0])

print(day + snail(start, data[0], data[1], data[2]))


