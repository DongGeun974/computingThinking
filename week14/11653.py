# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：11653.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-06 오후 1:12 
'''
import sys

n = int(sys.stdin.readline())
ans = 2
while n > 1:
    if n % ans == 0:
        print(ans)
        n = n // ans
    else:
        ans+=1