# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2470.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-13 오후 7:04 
'''

# time over
# import copy
# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = sorted(list(map(int, sys.stdin.readline().split())))
#
# answer = float('inf')
#
# l1, l2 = 0, 0
#
# for i in range(len(data)):
#     std = data[i]
#
#     temp = copy.deepcopy(data)
#     temp.remove(std)
#
#     start = 0
#     end = len(temp) -1
#
#     while start <= end:
#         mid = (start+end)//2
#         if answer >= abs(std + temp[mid]):
#             answer = abs(std + temp[mid])
#             l1, l2 = std, temp[mid]
#             start = mid+1
#         else:
#             end = mid-1
#
# # print(answer)
# print(*sorted([l1, l2]))

# input and sort

# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = sorted(list(map(int, sys.stdin.readline().split())))
#
# # minimum
# answer = float('inf')
#
# for i in range(len(data)-1):
#     start = i+1
#     end = n-1
#
#     # binary search
#     while start <= end:
#         mid = (start + end) // 2
#         temp = data[i] + data[mid]
#
#         if abs(temp)  < answer:
#             idx1, idx2 , answer = i, mid, abs(temp)
#         if temp < 0:
#             start=mid+1
#         else:
#             end=mid-1
#
#
# print(data[idx1], data[idx2])
#







n = int(input())
arr = sorted(list(map(int,input().split())))
max_min = float('inf')
idx1, idx2 = 0,0
# print(arr)
for i in range(n-1):
    start = i+1
    end = len(arr)-1

    while start <= end:
        mid = (start+end)//2
        tem = arr[mid] + arr[i]
        # print('i', i)
        # print('mid', mid)

        if abs(tem) < max_min:
            idx1, idx2, max_min = i, mid, abs(tem)
            # print('result : ', i, mid)

        if tem > 0:
            end = mid-1
        else:
            start=mid+1

print(arr[idx1], arr[idx2])

