# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：9498.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-04 오후 11:16 
'''

import sys

data = int(sys.stdin.readline())

if 90 <= data:
    print("A")
elif 80 <= data:
    print("B")
elif 70 <= data:
    print("C")
elif 60 <= data:
    print("D")
else:
    print("F")