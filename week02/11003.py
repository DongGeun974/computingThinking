# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：11003.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-17 오후 7:54 
'''

import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
q =deque()
ans = []

for i in range(n):
    # print((arr[i], i))
    while q and q[-1][0] > arr[i]:
        q.pop()
    while q and q[0][1] < i-l+1:
        q.popleft()
    q.append((arr[i], i))
    # print(q)
    print(q[0][0], end=' ')
