# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10871.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 9:57 
'''
import sys

data = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

for i in range(data[0]):
    if arr[i] < data[1]:
        print(str(arr[i]) + ' ',end='')