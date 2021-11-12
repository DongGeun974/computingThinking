# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2468.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 3:32 
'''
import copy



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

import sys
from collections import deque

input = sys.stdin.readline

# bfs
def bfs(x, y, safe_area):
    # make queue
    queue = deque()
    # put start point
    queue.append((x, y))
    # put visited start point
    visited[x][y] = 1

    while queue:
        # queue pop
        x, y = queue.popleft()

        # check adjacent point(left, right, up, down)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if nx, ny are in square
            if 0 <= nx < N and 0 <= ny < N:
                # if safe, not visited
                if graph[nx][ny] >= safe_area and visited[nx][ny] == 0:
                    # check visited
                    visited[nx][ny] = 1
                    # put queue
                    queue.append((nx, ny))


# input n and data
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

graph_min = min(map(min, graph))
graph_max = max(map(max, graph))

# for adjacent
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# why?
# max_safe_area = graph_min
max_safe_area = 0

# for all case by safe
for safe_area in range(graph_min, graph_max+1):
    # initialize visited
    visited = [[0] * N for _ in range(N)]
    # for check area
    temp = 0
    # check all point
    for i in range(N):
        for j in range(N):
            # if safe and not visited
            if graph[i][j] >= safe_area and visited[i][j] == 0:
                bfs(i,j,safe_area)
                temp+=1

    if temp > max_safe_area:
        max_safe_area = temp
print(max_safe_area)
