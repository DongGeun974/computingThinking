# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2098.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오후 5:55 
'''

# import sys
#
# n = int(sys.stdin.readline())
# dp = [[float('inf')]* (1 << n) for _ in range(n)]
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# def dfs(x, visited):
#     if visited == (1 << n) -1:
#         if graph[x][0]:
#             return graph[x][0]
#         else:
#             return float('inf')
#     if dp[x][visited] != float('inf'):
#         return dp[x][visited]
#     for i in range(1, n):
#         if not graph[x][i]:
#             continue
#         if visited & (1 << i) :
#             continue
#         dp[x][visited] = min(dp[x][visited], dfs(i,visited | (1 << i)) + graph[x][i])
#     return dp[x][visited]
#
# print(dfs(0,1))

import sys

n = int(sys.stdin.readline())
dist = [[float('inf')] * (1 << n) for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def dfs(v,vistied):
    if vistied == (1 << n) -1:
        if graph[v][0]:
            return graph[v][0]
        else:
            return float('inf')

    if dist[v][vistied] != float('inf'):
        return dist[v][vistied]

    for i in range(1, n):
        if not graph[v][i] or vistied & (1 << i):
            continue
        dist[v][vistied] = min(dist[v][vistied], dfs(i,vistied | (1 << i)) + graph[v][i])
    return dist[v][vistied]

print(dfs(0,1))