# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2468.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 3:32 
'''
import copy

import sys

# def safe(data, minus ):
#     print(minus)
#     data_ = copy.deepcopy(data)
#     for i in range(len(data_)):
#         for j in range(len(data_)):
#             if data_[i][j] - minus > 0:
#                 data_[i][j] = 1
#                 # data_[i][j] = '□'
#             else:
#                 data_[i][j] = 0
#                 # data_[i][j] = '■'
#     for i in data_:
#         print(i)
#
# def saftyArea(_data, r ,c):
#     for i in range(r, n):
#         for j in range(c, n):
#             if _data[i][j] == 1:
#                 return 0
#             else:

from collections import deque

def bfs(a,b,h):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    queue = deque()
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny <0 or ny >=n:
                continue
            elif copy[nx][ny] == 1:
                copy[nx][ny] = 0
                queue.append((nx,ny))

n = int(input())
graph = []
for i in  range(n):
    graph.append(list(map(int, input().split())))

result = []

# water height
for k in range(101):
    copy = [ [0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > k:
                copy[i][j] = 1

    for i in range(n):
        for j in range(n):
            if copy[i][j] == 1:
                copy[i][j] =0
                bfs(i,j,k)
                cnt +=1

    result.append(cnt)
print(max(result))