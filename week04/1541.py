# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1541.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오후 8:56 
'''

# import sys
#
# arr = sys.stdin.readline().strip().split('-')
#
# result = 0
# for i in arr[0].split('+'):
#     result+= int(i)
# for i in arr[1:]:
#     for j in i.split('+'):
#         result -= int(j)
# print(result)
#


import sys

calculate = list(sys.stdin.readline().strip().split('-'))
result = 0

for i in range(len(calculate)):
    if i == 0:
        for j in map(int, calculate[i].split('+')):
            result+=j
    else:
        for j in map(int, calculate[i].split('+')):
            result-=j

print(result)