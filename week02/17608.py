# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：17608.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 10:14 
'''
import sys

n = int(sys.stdin.readline().split()[0])
data = list(int(sys.stdin.readline().split()[0]) for i in range(n))

standard = data[-1]

stack = []

for i in range(n):
    stack.append(data[i])

count = set()
for i in range(n):
    temp = stack.pop()
    if temp >= standard:
        standard = temp
        count.add(temp)

print(len(count))