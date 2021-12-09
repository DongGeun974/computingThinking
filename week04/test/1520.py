# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1520.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-02 오전 10:14 
'''
"""
    bottom up
        dp, 점화식
        스캔 방향이 명확할때
    top down
        recursion, memoization
    dfs로 하면서(경우의 수)
"""

import sys
sys.setrecursionlimit(10**9)
m,n = map(int, sys.stdin.readline().split())
graph = list(list(map(int,sys.stdin.readline().split())) for _ in range(m))
dp = [[-1 for i in range(n)] for j in range(m)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    if x == m-1 and y==n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx,ny)
        # for _ in dp:
        #     print(_)
        # print()
    return dp[x][y]

print(dfs(0,0))