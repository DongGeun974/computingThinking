# -*- coding: UTF-8 -*-
'''
@Project ：week16 
@File ：2606.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-20 오후 5:24 
'''
import sys

numCom = int(sys.stdin.readline())
numPair = int(sys.stdin.readline())
graph = [[] for _ in range(numCom+1)]
for _ in range(numPair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = [1]
    visited = []
    while q:
        x = q.pop(0)
        visited.append(x)
        for i in graph[x]:
            if i not in visited and i not in q:
                q.append(i)

    return len(visited)-1

print(bfs())
