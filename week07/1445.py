# -*- coding: UTF-8 -*-
'''
@Project ：week07 
@File ：1445.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-16 오후 8:08 
'''

import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
forest = [list(sys.stdin.readline().strip()) for _ in range(n)]
check = [[0]*m for _ in range(n)]
dist = [[1e9] * m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
G = 2500
q =[]

def out(x,y):
    return x<0 or x >= n or y < 0 or y >=m

def dijkstra():
    while q:
        d, x, y = heappop(q)
        if forest[x][y] == 'F':
            print(dist[x][y]//G, dist[x][y]%G)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if out(nx,ny):
                continue
            nd = d+ check[nx][ny]
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heappush(q, (nd, nx, ny))

for i in range(n):
    for j in range(m):
        if forest[i][j] == 'S':
            heappush(q, (0,i,j))
            dist[i][j] = 0
        elif forest[i][j] == 'g':
            check[i][j] = G
            for k in range(4):
                ni,nj = i+dx[k], j+dy[k]
                if not out(ni, nj) and forest[ni][nj] == '.':
                    check[i][j]=1

dijkstra()

for i in dist:
    print(i)