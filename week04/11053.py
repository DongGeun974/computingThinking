# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：11053.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오후 5:29 
'''

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j] +1)

print(max(result))