# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2309.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 10:55 
'''
import sys

# input data
data = [int(sys.stdin.readline().split()[0]) for i in range(9)]

# sum of all data
total = sum(data)
data.sort()


# check each data(i)
for i in range(9):
    # check next data(j)
    for j in range(i+1, 9):
        # calculate
        if 100 == total - data[i] - data[j]:
            num1, num2 = data[i], data[j]
            data.remove(num1)
            data.remove(num2)
            # stop loop
            for i in data:
                print(i)
            break
    # if answer, stop loop
    if len(data) < 9 :
        break