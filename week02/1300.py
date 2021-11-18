# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1300.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-17 오후 1:41 
'''

# memory over
# import bisect
# import sys
#
# n = int(sys.stdin.readline())
# target = int(sys.stdin.readline())
# matrix = list(list((i+1)*(j+1) for j in range(n)) for i in range(n))
# print(sys.getsizeof(matrix))
# for i in matrix:
#     print(i)
# arr = []
#
# for i in matrix:
#     arr+=i
# arr.sort()
# # print(arr)
#
# print(arr[target])

n, k = int(input()), int(input())
start, end = 1, k

while start <= end:
    # print(start)
    # print(end)
    mid = (start+end)//2
    # print('mid',mid)
    temp = 0

    # counting sort
    for i in range(1,n+1):
        temp+=min(mid//i, n)
    #     print('temp',temp)
    # print('temp', temp)

    if temp >= k:
        answer = mid
        end = mid-1
    else:
        start = mid+1
    # print()

print(answer)