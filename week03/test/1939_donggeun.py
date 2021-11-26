# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：1939_donggeun.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오전 10:38 
'''

import sys
from collections import deque

"""
    최대 중량 찾기
    
    최소, 최대에서 가능한 이분탐색
    bfs에서 중간값을 기준으로 
    
    사냥꾼 : decision algorithm
    그래프 탐색을 하면서 찾음
"""

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([end, weight])
    graph[end].append([start, weight])

start_island, end_island = map(int, sys.stdin.readline().split())

min_weight , max_weight = 1, 10000000000

def bfs(mid_weight): # 3
    queue = deque()
    queue.append(start_island)
    visited = set()
    visited.add(start_island)

    while queue:
        start = queue.popleft()
        for end, weight in graph[start]:
            if end not in visited and weight >= mid_weight:
                visited.add(end)
                queue.append(end)

    if end_island in visited:
        return True
    else:
        return False

result = min_weight

while min_weight <= max_weight:
    mid_weight = (min_weight + max_weight)//2
    if bfs(mid_weight): # 3
        result = mid_weight
        min_weight = mid_weight+1
    else:
        max_weight = mid_weight-1

print(result)