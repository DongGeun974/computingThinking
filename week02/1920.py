# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1920.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-11 오후 3:56 
'''
import sys

n = int(sys.stdin.readline().strip()[0])
ls = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip()[0])
data = list(map(int, sys.stdin.readline().split()))
# print(ls)
# print(data)

def binarySearch(ls, l, r, find):
    if l==r:
        if ls[l] == find:
            return 1
        else:
            return 0

    else:
        half = (l+r)//2
        if ls[half] == find:
            return 1
        elif ls[half] > find:
            return binarySearch(ls,l, half, find)
        else:
            return binarySearch(ls, half+1, r, find)

ls.sort()

for i in data:
    print(binarySearch(ls, 0, len(ls)-1, i))
