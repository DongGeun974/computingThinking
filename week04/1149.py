# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1149.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-30 오후 3:39 
'''

import sys

n = int(sys.stdin.readline())
house = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
for i in range(1, n):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][2], house[i - 1][0]) + house[i][1]
    house[i][2] = min(house[i - 1][1], house[i - 1][0]) + house[i][2]
print(min(house[n-1]))
