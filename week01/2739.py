# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2739.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 9:48 
'''
import sys

data = int(sys.stdin.readline())

for i in range(9):
    print(str(data) +' * ' + str(i+1) +' = ' + str(data*(i+1)))