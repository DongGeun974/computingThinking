# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：8958.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 10:15 
'''
import sys

testCase = int(sys.stdin.readline())

for i in range(testCase):

    data =  sys.stdin.readline().split()[0].split('X')
    res = 0
    for item in data:
        j = len(item)
        # print(int((j*(j+1))/2))
        res = res + (int((j*(j+1))/2))
    print(res)

