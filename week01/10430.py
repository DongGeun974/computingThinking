# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10430.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 9:14
'''
import sys

data = list(map(int, sys.stdin.readline().split()))

print( (data[0] + data[1]) % data[2])
print( ((data[0] % data[2]) + (data[1] % data[2])) % data[2])
print( (data[0] * data[1]) % data[2])
print( ((data[0] % data[2]) * (data[1] % data[2])) % data[2])
