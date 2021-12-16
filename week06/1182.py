# -*- coding: UTF-8 -*-
'''
@Project ：week06 
@File ：1182.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-14 오후 1:07 
'''
import itertools
import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(1,len(arr)+1):
    combi = itertools.combinations(arr, i)
    for j in combi:
        if sum(j) == s:
            res+=1
print(res)