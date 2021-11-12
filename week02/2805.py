# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2805.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-11 오후 5:04 
'''

import copy

# 가장 큰 나무에서 m 직전까지의 h값 구한 후 1씩 증가
# h = 1
#
# max_h = max(data)
#
# while h < max_h-m:
#     h*=2
#
# h//=2
# # print('h', h)
#
# for i in range(len(data)):
#     if data[i] <= h:
#         data[i]=0
#     else:
#         data[i]-=h
#
# # print(data)
# add_h = 0
# for i in range(max(data)+1):
#     if sum(data) <= m:
#         add_h = i
#         # print('i', i)
#         # print(sum(data))
#         break
#     else:
#         for i in range(len(data)):
#             if data[i] <= 1:
#                 data[i] = 0
#             else:
#                 data[i] -= 1
#
# print(h+add_h)

# 자른 후 모든 배열의 합 구하기
# while sum(data) > m:
#     temp = copy.deepcopy(data)
#     if h == 0:
#         h+=1
#     for i in range(len(temp)):
#         if temp[i] <= h:
#             temp[i]=0
#         else:
#             temp[i]-=h
#     if sum(temp) < m:
#         break
#     h = h*2
#
# for j in range(len(data)):
#     if data[j] <= h//2:
#         data[j] = 0
#     else:
#         data[j] -= h//2
#
# for i in range(h//2, max(data) +1):
#     for j in range(len(data)):
#         if data[j] <= 1:
#             data[j]=0
#         else:
#             data[j]-=1
#     print(data)
#     if sum(data) <= m:
#         print(i)

# input n ,m

import sys

n,m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

def binarySearch(l, r, target):
    global max_height
    half = (l+r)//2

    if l > r:
        return half

    sum = 0

    for i in range(len(data)):
        if data[i] <= half:
            sum+=0
        else:
            sum+=data[i]-half


    if sum == target:
        return half
    elif sum < target:
        return binarySearch(l, half-1, target)
    else:
        # max_height = half
        return binarySearch(half+1, r, target)

    # if sum < m:
    #     return binarySearch(l, half-1, target)
    # elif sum >= m:
    #     return binarySearch(half+1, r, target)
max_height = 0
print(binarySearch(1, max(data), m))