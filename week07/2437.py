# -*- coding: UTF-8 -*-
'''
@Project ：week07 
@File ：2437.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-16 오후 4:31 
'''

import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

target = 1
for i in arr:
    if target < i:
        break
    target +=i
print(target)