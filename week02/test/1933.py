# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1933.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-18 오전 10:19 
'''

import heapq
import sys

"""
    스카이라인
"""

num_building = int(sys.stdin.readline())

arr = []

for i in range(num_building):
    r, h, l = map(int, sys.stdin.readline().split())
    arr.append([r,-h,l])
    arr.append([l, 0, 0])

arr.sort()

# result : [start, height]
# hq : [-height, end]
result = [[0,0]]
hq = [[0, float('inf')]]

for r, negH, l in arr:
    while hq[0][1] <= r :
        heapq.heappop(hq)
    if negH:
        heapq.heappush(hq, [negH, l])
    if result[-1][1] != -hq[0][0]:
        result.append([r, -hq[0][0]])
    # print(r, negH, l , result, hq)

result.pop(0)
for i in result:
    print(*i,end=' ')
# print(*result)