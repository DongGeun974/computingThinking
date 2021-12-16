# -*- coding: UTF-8 -*-
'''
@Project ：week06 
@File ：13458.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-09 오후 10:18 
'''

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
ans = len(arr)
for i in range(len(arr)):
    arr[i] = arr[i] -b if arr[i] -b >0 else 0
    ans += (arr[i]//c)
    arr[i]%=c
    if arr[i] != 0 : ans+=1
print(ans)