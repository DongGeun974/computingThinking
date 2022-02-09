# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：2231.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-08 오전 1:12 
'''

import sys

n = int(sys.stdin.readline())
result = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))
    result= i+sum(a)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)