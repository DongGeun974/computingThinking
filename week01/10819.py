# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10819.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 11:46 
'''
import itertools
import sys

# input n and data
n = int(sys.stdin.readline().split()[0])
data = list(map(int, sys.stdin.readline().split()))

# get all case of permutation
all_case = itertools.permutations(data)

answer = 0

# calculate
for i in all_case:
    sum = 0
    for j in range(n-1):
        sum+=abs(i[j] - i[j+1])
    answer = max(answer,sum)

print(answer)
