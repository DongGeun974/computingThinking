# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1065.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 4:45 
'''
import sys

data = int(sys.stdin.readline().split()[0])

if data < 111:
    print(min(99, data)) # max 99
else:
    default = 99

    for i in range(111, data+1):
        arr = list(map(int, str(i)))
        diff1 = arr[0] - arr[1]
        diff2 = arr[1] - arr[2]
        if diff1 == diff2:
            default = default + 1

    print(default)