# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1202.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-02 오전 11:05 
'''

import heapq
import sys

n, k = map(int, sys.stdin.readline().split())

jewelryList = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
bagList = [int(sys.stdin.readline()) for _ in range(k)]
jewelryList.sort()
bagList.sort()

result = 0
temp = []

for currentBag in bagList:
    while jewelryList and currentBag >= jewelryList[0][0]:
        heapq.heappush(temp, -jewelryList[0][1])
        heapq.heappop(jewelryList)
    if temp:
        result+=heapq.heappop(temp)
    elif not jewelryList:
        break
print(-result)