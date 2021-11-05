# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10950.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 9:52 
'''
import sys

testCase = int(sys.stdin.readline())

for i in range(testCase):
    data = list(map(int, sys.stdin.readline().split()))
    print(data[0] + data[1])