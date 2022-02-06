# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：1406.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오전 1:10 
'''

import sys

str = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
tmp = []
    #L D B P
for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order == 'L':
        if str:
            tmp.append(str.pop())
    elif order == 'D':
        if tmp:
            str.append(tmp.pop())
    elif order == 'B':
        if str:
            str.pop()
    else:
        str.append(order[2])

tmp_str = ''
for i in tmp:
    tmp_str = i + tmp_str
str_str = ''
for i in str:
    str_str += i

print(str_str + tmp_str)

