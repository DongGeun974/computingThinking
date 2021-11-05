# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2753.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-04 오후 11:19 
'''

import sys

data = int(sys.stdin.readline())

if data % 400 == 0:
    print("1")
elif data % 4 == 0 and data % 100 != 0:
    print("1")
else:
    print("0")