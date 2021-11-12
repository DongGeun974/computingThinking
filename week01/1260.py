# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1260.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오후 10:55 
'''

# input n, m, v and data
import sys

n, m ,v = map(int, sys.stdin.readline().split())
N = []
matrix =[[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    matrix[temp[0]][temp[1]] = matrix[temp[1]][temp[0]] = 1
    N.append(temp[0])
    N.append(temp[1])
N = list(set(N))

# for dfs
visited = []

def dfs(v):
    print(v)
    visited.append(v)
    for i in N:
        if i not in visited and  matrix[v][i] != 0:
            visited.append(i)
            dfs(i)
            visited.pop()

dfs(v)