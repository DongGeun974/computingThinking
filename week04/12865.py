# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：12865.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오후 10:59 
'''

# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# arr = [[0,0]]
# for _ in range(n):
#     weight, value = map(int, sys.stdin.readline().split())
#     arr.append([weight, value])
#
# matrix = [[0] * (k+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         w=arr[i][0]
#         v=arr[i][1]
#
#         if j < w:
#             # print(j, w)
#             matrix[i][j] = matrix[i-1][j]
#         else:
#             # print(j, i-1, j-w, v )
#             # print(matrix[i-1][j], matrix[i-1][j-w]+v)
#             matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w]+v)
#
#     #     for _ in matrix:
#     #         print(_)
#     #     print()
#     # print()
# print(matrix[n][k])


import sys

n,k = map(int, sys.stdin.readline().split())
items = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
dp = [[0] *(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight, value = items[i-1][0], items[i-1][1]
    for j in range(1,k+1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[-1][-1])