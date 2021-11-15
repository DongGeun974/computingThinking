# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：13334.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오후 8:52 
'''

# import sys
#
# people = int(sys.stdin.readline())
# # homeOffice = list(list(map(int, sys.stdin.readline().split())) for _ in range(people))
# homeOffice=[]
# for _ in range(people):
#     temp = list(map(int, sys.stdin.readline().split()))
#     homeOffice.append(sorted(temp))
# distance = int(sys.stdin.readline())
#
# print(people)
# print(sorted(homeOffice))
# print(distance)

import heapq
import sys

n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)
d = int(sys.stdin.readline())

roads = []
for road in road_info:
    house, office = road
    if abs(house-office) <= d:
        road = sorted(road)
        roads.append(road)

roads.sort()
print(roads)
roads.sort(key=lambda x : x[1])
print(roads)

answer = 0
heap =[]
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] -d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap,road)
    answer = max(answer, len(heap))

print(answer)

### https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-13334-%EC%B2%A0%EB%A1%9C%ED%8C%8C%EC%9D%B4%EC%8D%AC