# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2908.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 11:48 
'''
import sys

data = sys.stdin.readline().split()

num = []

for string in data:
    # revList = list(string).reverse()
    # reverse() dont have return
    # if want to return, use reversed()
    num.append(int(string[::-1]))

print(max(num))