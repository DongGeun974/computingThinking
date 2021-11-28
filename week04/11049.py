# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：11049.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오전 11:23 
'''

# # wrong answer
# import sys
#
# n = int(sys.stdin.readline())
# matrix = [[]]
#
# for _ in range(n):
#     x, y = map(int,sys.stdin.readline().split())
#     matrix.append([x,y])
#
# dp = [[0] * (n+1) for _ in range(n+1)  ]
#
# # 대각선대로 진행되어야 하는데, 이 코드는 위에서부터 아래로 진행
# for i in range(1,n+1):
#     for j in range(i, n+1):
#         if i==j:
#             dp[i][j] = 0
#             continue
#         elif i +1 == j:
#             dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
#             continue
#         else:
#             dp[i][j] = float('inf')
#             # print(i, j)
#             for k in range(1, j-i+1):
#                 # print(i,k,'  ', k+1, j)
#                 # print('곱셈 횟수',matrix[i][0] , matrix[k][1] , matrix[j][1])
#                 # print(dp[i][k] , dp[k+1][j])
#                 # print(matrix[i][0] * matrix[k][0] * matrix[j][1])
#                 dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
#
# for i in dp:
#     print(i)

# import sys
#
# n = int(sys.stdin.readline())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, sys.stdin.readline().split())))
# dp = [[0 for _ in range(n)] for _ in range(n)]
#
# for diagonal in range(1, n):
#     for i in range(0, n-diagonal):
#         j = i+diagonal
#         # print(diagonal, i, j)
#         if diagonal == 1:
#             dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
#             continue
#
#         dp[i][j] = float('inf')
#         for k in range(i,j):
#             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
#
# print(dp[0][n-1])
#
# # for i in dp:
# #     print(i)

import sys

n = int(sys.stdin.readline())
matrices = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
dp = [[0] * n for _ in range(n)]

for diagonal in range(1,n):
    for i in range(0, n-diagonal):
        j = i+diagonal
        if diagonal == 1:
            dp[i][j] = matrices[i][0] * matrices[i][1] * matrices[j][1]
            continue
        dp[i][j] = float('inf')
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]  + matrices[i][0] * matrices[k][1] * matrices[j][1])

print(dp[0][n-1])