# -*- coding: UTF-8 -*-
'''
@Project ：week06 
@File ：3584.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-15 오후 3:16 
'''

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    parent = [0] * (n+1)

    for i in range(n-1):
        p, c = map(int, sys.stdin.readline().split())
        parent[c] = p

    a,b = map(int, sys.stdin.readline().split())
    a_list = [0,a]
    b_list = [0,b]

    while parent[a]:
        a_list.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_list.append(parent[b])
        b = parent[b]

    cnt = 1
    while a_list[-cnt] == b_list[-cnt]:
        cnt += 1

    print(a_list[-cnt+1])