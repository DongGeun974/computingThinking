# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：1269.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오전 12:42 
'''

import sys

n, m = map(int,sys.stdin.readline().split())

a = sorted(list(map(int,sys.stdin.readline().split())))
b = sorted(list(map(int,sys.stdin.readline().split())))

idx_a = 0
idx_b = 0
cnt = 0

while idx_a < n and idx_b < m:
    if a[idx_a] == b[idx_b]:
        cnt+=1
        idx_a+=1
        idx_b+=1
    elif a[idx_a] > b[idx_b]:
        idx_b+=1
    else:
        idx_a+=1

print(n+m - (2*cnt))

# count = 0
# if len(a) < len(b):
#     for i in a:
#         if i in b:
#             count+=1
# else:
#     for i in b:
#         if i in a:
#             count+=1
#
# print(n+m - (2*count))