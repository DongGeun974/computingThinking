# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：11053.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-13 오후 8:17 
'''

# wrong answer
# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = list(map(int, sys.stdin.readline().split()))
#
# seq = []
#
# for i in range(len(data)):
#     if len(seq) == 0:
#         seq.append(data[i])
#         continue
#     if data[i] in seq:
#         continue
#
#     if seq[-1] < data[i]:
#         seq.append(data[i])
#     else:
#         start = 0
#         end = len(seq) - 1
#         idx = 0
#         while start <= end:
#             mid = (start + end) // 2
#             if seq[mid] < data[i]:
#                 idx = mid
#                 start = mid+1
#             else:
#                 end = mid
#         # seq.insert(idx , data[i])
#         seq[idx+1] = data[i]
#     # print(seq)
#
# print(len(seq))

# input

# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = list(map(int, sys.stdin.readline().split()))
# temp = []
#
# # lower_bound
# def lower_bound(a, x):
#     lo = 0
#     hi = len(a)-1
#     while lo<hi:
#         mid = (lo+hi) // 2
#         if x <= a[mid] :
#             hi = mid
#         else:
#             lo = mid+1
#     return lo
#
# temp.append(data[0])
#
# # dont get exactly subsequence
# for i in range(1,len(data)):
#     if data[i] in temp:
#         continue
#     if temp[-1] < data[i]:
#         temp.append(data[i])
#     else:
#         idx = lower_bound(temp, data[i])
#         print(idx)
#         temp[idx] = data[i]
#     # print(temp)
#
# print(len(temp))

import sys

def lower_bound(arr, x):
    start = 0
    end = len(arr)-1
    # print('start,end', start, end)
    while start<end:
        mid = (start + end) // 2
        if arr[mid] >= x :
            end = mid
        else:
            start = mid+1

    return start

n = int(sys.stdin.readline())
arr = list(list(map(int, sys.stdin.readline().split())))
# print(arr)
# print(lower_bound(arr, 40))

answer = []

for i in arr:
    # print(answer)
    if answer :
        if i in answer:
            continue
        if answer[-1] < i:
            answer.append(i)
        else:
            # print(answer, i)
            idx = lower_bound(answer, i)
            # print(idx)
            answer[idx] = i
    else:
        answer.append(i)

print(len(answer))