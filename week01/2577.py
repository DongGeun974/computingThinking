# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2577.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 11:09 
'''
import sys

res = 1

for _ in range(3):
    data = int(sys.stdin.readline())
    res =res * data

for i in range(10):
    print(str(res).count(str(i)))