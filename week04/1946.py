# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1946.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-27 오전 1:28 
'''
import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))
    arr.sort()

    first = arr[0]
    cnt =1
    for i in range(1,len(arr)):
        if first[1] > arr[i][1]:
            # print(first, arr[i])
            cnt+=1
            first=arr[i]

    print(cnt)