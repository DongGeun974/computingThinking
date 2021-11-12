# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1182.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오후 2:30 
'''

# input n and data
import itertools
import sys

n, x = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

temp = 0
sum_ = 0

for i in range(1, n+1):
    perm = itertools.combinations(data, i)
    for case in perm:
        if sum(case) == x:
            temp+=1
print(temp)
