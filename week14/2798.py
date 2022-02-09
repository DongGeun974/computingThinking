# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：2798.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-08 오전 1:35 
'''

import sys

n, m = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
ls.sort(reverse=True)

max_ = 0

for i in range(len(ls)-2):
    for j in range(i+1,len(ls)-1):
        for k in range(j+1, len(ls)):
            if ls[i]+ls[j]+ls[k] == m:
                print(m)
                exit()
            if ls[i]+ls[j]+ls[k] < m:
                max_ = max(max_, ls[i]+ls[j]+ls[k])
print(max_)