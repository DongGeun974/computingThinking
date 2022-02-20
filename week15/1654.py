# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：1654.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 11:44 
'''

import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in lan:
        line+=i//mid
    if line >= n:
        start = mid+1
    else:
        end = mid-1
print(end)