# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：1654.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 11:44 
'''

import sys

k, n = map(int, sys.stdin.readline().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline()))

sum_arr = sum(arr)
max_arr = max(arr)
print(sum_arr,max_arr, sum_arr/n)