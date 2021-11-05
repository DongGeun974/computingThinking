# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2675.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 11:35 
'''
import sys

testCase = int(sys.stdin.readline().split()[0])

for _ in range(testCase):

    data = sys.stdin.readline().split()

    for i in list(data[1]):
        print(i * int(data[0]), end="")

    print()