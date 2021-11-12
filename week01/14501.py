# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：14501.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오전 10:25 
'''

# input n and data
import sys

n = int(sys.stdin.readline().split()[0])
data = [ list(map(int, sys.stdin.readline().split())) for i in range(n)]
T, P = [], []
for i in data:
    T.append(i[0])
    P.append(i[1])

# set max
maxMoney = 0




print(T)
print(P)