# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：11728.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오전 1:00 
'''
import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ia = 0
ib = 0
res = []
while ia < n and ib < m:
    if a[ia] == b[ib]:
        res.append(str(a[ia]))
        res.append(str(b[ib]))
        ia+=1
        ib+=1
    elif a[ia] > b[ib]:
        res.append(str(b[ib]))
        ib+=1
    else:
        res.append(str(a[ia]))
        ia+=1

if ia < n:
    res += list(map(str,a[ia:]))

if ib < m:
    res += list(map(str,b[ib:]))

print(' '.join(res))