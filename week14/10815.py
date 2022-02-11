# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：10815.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 9:38 
'''

import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

card.sort()

for i in target:
    left, right = 0, len(card)-1
    flag = False
    while left <= right:
        mid = (left+right)//2
        if card[mid] == i:
            flag = True
            break
        elif card[mid] < i:
            left = mid +1
        else:
            right = mid-1
    if flag:
        print(1, end=' ')
    else:
        print(0, end=' ')