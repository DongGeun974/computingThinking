# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2309.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 10:55 
'''
import sys

data = [int(sys.stdin.readline().split()[0]) for i in range(9)]
total = sum(data)
data.sort()

for i in range(9):
    for j in range(i+1, 9):
        if 100 == total - data[i] - data[j]:
            num1, num2 = data[i], data[j]

            data.remove(num1)
            data.remove(num2)

            for i in data:
                print(i)
            break
    if len(data) < 9 :
        break