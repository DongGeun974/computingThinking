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
import sys

n = int(sys.stdin.readline().split()[0])
data = list(map(int, sys.stdin.readline().split()))
temp = []

# lower_bound
def lower_bound(a, x):
    lo = 0
    hi = len(a)-1
    while lo<hi:
        mid = (lo+hi) // 2
        if x < a[mid] :
            hi = mid
        else:
            lo = mid+1
    return lo

temp.append(data[0])

for i in range(1,len(data)):
    if data[i] in temp:
        continue
    if temp[-1] < data[i]:
        temp.append(data[i])
    else:
        idx = lower_bound(temp, data[i])
        # print(idx)
        temp[idx] = data[i]
    # print(temp)

print(len(temp))