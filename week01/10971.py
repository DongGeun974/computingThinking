# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10971.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오전 11:46 
'''
import itertools
import sys

def find_path(depth, start, stop, case):
    sum = 0
    if depth == n-2:
        print(start, stop, data[start][stop])
        return int(data[start][stop])
        print('done')
    else:
        print(start, stop, data[start][stop])
        return find_path(depth+1, case[depth+1],case[depth+2], case) + int(data[start][stop])

n = int(sys.stdin.readline().split()[0])
ls = []
for i in range(n):
    ls.append(i)
data = [sys.stdin.readline().split() for i in range(n)]
all_case = itertools.permutations(ls)

for case in all_case:
    print()
    print(find_path(0,case[0],case[1], case))