# -*- coding: UTF-8 -*-
'''
@Project ：week06 
@File ：3020.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-14 오후 11:06 
'''
import sys

n, h = map(int, sys.stdin.readline().split())
down = [0] * (h+1)
up = [0] * (h+1)

min_conut = n
range_count = 0

for i in range(n):
    if i % 2 == 0:
        down[int(sys.stdin.readline())] +=1
    else:
        up[int(sys.stdin.readline())] += 1

for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, h+1):
    if min_conut > (down[i] + up[h-i+1]):
        min_conut = (down[i] + up[h-i+1])
        range_count = 1
    elif min_conut == (down[i] + up[h-i+1]):
        range_count +=1

print(min_conut, range_count)