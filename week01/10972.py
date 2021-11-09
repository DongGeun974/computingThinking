# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10972.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-09 오후 1:21 
'''

# input n
# import itertools
# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = tuple(map(int, sys.stdin.readline().split()))
#
# # permutation
# # handle all case >> time over
# all_case = itertools.permutations(range(1,n+1))
#
# # each case
# chk = False
# for case in all_case:
#     if chk:
#         print(case)
#         exit()
#     if (case == data):
#         chk=True
#
# print('-1')

# input n and data
import sys

n = int(sys.stdin.readline().split()[0])
data = list(map(int, sys.stdin.readline().split()))

# find swap index
idx = 0
for i in range(n-1,0,-1):
    if data[i-1] < data[i]:
        idx = i-1
        break

for i in range(n-1, 0, -1):
    if data[idx] < data[i]:
        # swap
        data[idx], data[i] = data[i], data[idx]
        # sort
        data = data[:idx+1] + sorted(data[idx+1:])
        # print each element
        print(*data)
        exit()

# if data is last
print(-1)