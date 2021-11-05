# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10872.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 7:15 
'''
import sys

def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

data = int(sys.stdin.readline().strip())

print(factorial(data))