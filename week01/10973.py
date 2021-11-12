# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10973.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오전 9:13 
'''

# input n and data
import sys

n = int(sys.stdin.readline().split()[0])
data = list(map(int, sys.stdin.readline().split()))

# find index to exchange
idx = 0
for i in range(n-1,0,-1):
    if data[i-1] > data[i]:
        idx= i-1
        break

for i in range(n-1, 0, -1):
    if data[idx] > data[i]:
        data[idx], data[i] = data[i], data[idx]
        data = data[:idx+1] + sorted(data[idx+1:], reverse=True)
        print(*data)
        exit()
print(-1)