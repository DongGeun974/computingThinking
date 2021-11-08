# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1914.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 8:33 
'''
import sys

def hanoi(group, x, y):
    if group > 1:
        hanoi(group-1, x, 6-x-y)
    print(x, y)
    if group > 1:
        hanoi(group-1, 6-x-y, y)

# def cnt(group, x, y):
#     count_ = 0
#
#     if group <= 1:
#         return 1
#
#     count_ = count_ + cnt(group-1, x, 6-x-y)
#     count_ = count_ + 1
#     count_ = count_ + cnt(group-1, 6-x-y, y)
#
#     return count_

    # 2^n-1
    # 2 ** n -1

data = int(sys.stdin.readline())

# print(cnt(data,1,3))
print(pow(2, data)-1)
if data <21:
    hanoi(data,1,3)