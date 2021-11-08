# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10989.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 9:56 
'''
import sys


def counting(ls):

    max_ = 10000

    n = len(ls)
    f = [0] * (max_+1)
    b = [0] * n

    for i in range(n):
        f[ls[i]] += 1
    for i in range(1, max_+1):
        f[i] += f[i -1]
    for i in range(n-1, -1, -1):
        f[ls[i]] -= 1
        b[f[ls[i]]] = ls[i]
    for i in range(n):
        ls[i] = b[i]

n = int(sys.stdin.readline().split()[0])
ls = []
for i in range(n):
    ls.append(int(sys.stdin.readline().split()[0]))

counting(ls)

for i in ls:
    print(i)
