# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2562.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 10:07 
'''

# fail : thoroughly and surely read problem

import sys

# data = sys.stdin.readlines()
arr = []

for i in range(9):
    arr.append(int(sys.stdin.readline()))

print(max(arr))
print(arr.index(max(arr))+1)
