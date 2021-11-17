# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：12738.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-16 오후 7:22 
'''

# n = int(input())
# array = list(map(int, input().split()))
#
# def binary_search(start, end, target):
#     if start>end:
#         return start
#     mid=(start+end)//2
#
#     if total[mid]>target:
#         return binary_search(start,mid-1,target)
#     elif total[mid]==target:
#         return mid
#     else:
#         return binary_search(mid+1, end, target)
#
# total=[array[0]]
# for i in range(1, len(array)):
#     if total[-1] < array[i]:
#         total.append(array[i])
#     else:
#         total[binary_search(0, len(total)-1, array[i])] = array[i]
#
# print(len(total))

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

answer = [arr[0]]

for i in range(1, len(arr)):
    # print(answer)
    if answer[-1] < arr[i] :
        answer.append(arr[i])
    else:
        answer[lower_bound(answer, arr[i])] = arr[i]

print(len(answer))