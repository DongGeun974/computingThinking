# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10989.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 9:56 
'''

# this way is memory over

# import sys
#
#
# def counting(ls):
#
#     max_ = 10000
#
#     n = len(ls)
#     f = [0] * (max_+1)
#     b = [0] * n
#
#     for i in range(n):
#         f[ls[i]] += 1
#     for i in range(1, max_+1):
#         f[i] += f[i -1]
#     for i in range(n-1, -1, -1):
#         f[ls[i]] -= 1
#         b[f[ls[i]]] = ls[i]
#     for i in range(n):
#         ls[i] = b[i]
#
# n = int(sys.stdin.readline().split()[0])
# ls = []
# for i in range(n):
#     ls.append(int(sys.stdin.readline().split()[0]))
#
# counting(ls)
#
# for i in ls:
#     print(i)

# input n
import sys

n = int(sys.stdin.readline().split()[0])

# make statistical table
count = [0] * 10001

# input data and count data, this way is reduce memory
for i in range(n):
    temp = int(sys.stdin.readline().split()[0])
    count[temp]+=1

# print table
for i in range(len(count)):
    if count[i] != 0:
        # if exist many element
        for j in range(count[i]):
            print(i)
