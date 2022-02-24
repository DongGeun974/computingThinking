# -*- coding: UTF-8 -*-
'''
@Project ：week16 
@File ：1303.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-21 오전 2:55 
'''
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(m)]
visited = [[0]*n for _ in range(m)]
for i in range(m):
    graph[i] = list(sys.stdin.readline().strip())

white = 0
blue = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, color):
    global white, blue
    q = [[x,y]]
    visited[x][y] = 1
    cnt = 1
    while q:
        _x, _y = q.pop(0)
        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]
            if 0 <= nx < m and 0 <= ny < n :
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    cnt +=1
                    q.append([nx,ny])
                    visited[nx][ny] = 1
    if color == 'W':
        white+=pow(cnt,2)
    else:
        blue+=pow(cnt,2)

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j,graph[i][j])

print(white, blue)