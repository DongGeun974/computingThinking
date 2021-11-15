# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2261.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-14 오후 8:04 
'''
import sys

"""
    가로축에서 가장 짧은 거리의 두 점 구하기
        x 정렬
            거리 비교하면서 이분 탐색(히스토그램, 왼쪽-오른쪽-가운데)
            거리 = 제일 큰 값 - 제일 작은 값 
                >> 최소거리
        세로축에서 가장 짧은 거리의 두 점 구하기
            y 정렬
                거리 = 제일 큰 값 - 제일 작은 값
                거리 비교하면서 이분 탐색
    두 점이 같으면, 가장 가까운 두점    

    해결방법:
        포인트 클래스
            두 점 간 거리 메소드 작성
        x 축 정렬
        분할 정복시, 원소가 1개만 남을 경우는 탐색하지 못함
            현재 분할 된 구간의 점의 개수가 3개 이하면 
            점의 개수가 2 또는 3일떄 거리 측정
        분할 구간 내 두 점의 최솟값이 전체의 최소값 보장 못함

        가장 가까운 두 점이 왼쪽
        가장 가까운 두 점이 오른쪽
        가장 가까운 두 점이 오른쪽과 왼쪽 하나씩
            중앙선을 기준으로 d만큼 떨어진 지역 = band
                y 기준 정렬한 뒤 아래서부터 자기보다 위에 있는 점끼리 비교

    ...?
"""

# # wrong answer
# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = list(list(map(int, sys.stdin.readline().split())) for i in range(n))
# data.sort()
#
# def point_distance(a,b):
#     return (a[0] - b[0]) ** 2 + (a[1] -b[1]) ** 2
#
# # for i in range(len(data) -1):
# #     print(point_distance(data[i], data[i+1]))
#
# def binarySearch(ls, start, end):
#     # x축 기준 같은 선
#     if start == end:
#         return float('inf')
#     else:
#         # 왼쪽, 오른쪽 영역에서 가장 작은 x 거리 구하기
#         mid = (start+end)//2
#         dist = min(binarySearch(ls,start,mid), binarySearch(ls,mid+1, end))
#         target_list = []
#
#         # 가운데에서 mid만큼 왼쪽으로 떨어진 점 구하기
#         for i in range(mid, start-1, -1):
#             if (data[i][0] - data[mid][0]) ** 2 < dist:
#                 target_list.append(data[i])
#             else:
#                 break
#         # 가운데에서 mid만큼 오른쪽으로 떨어진 점 구하기
#         for i in range(mid+1, end+1):
#             if (data[i][0] - data[mid][0]) ** 2 < dist:
#                 target_list.append(data[i])
#             else:
#                 break
#
#         # 가운데 영역(후보군) y축으로 정렬
#         data.sort(key=lambda x:x[1])
#
#         # 후보군에서 가장 짧은 y 거리 구하기(완전탐색)
#         for i in range(len(target_list)-1):
#             for j in range(i+1, len(target_list)):
#                 # y 거리가 최소거리보다 짧으면
#                 if (data[i][1] - data[j][1]) ** 2 < dist:
#                     min_dist = point_distance(data[i], data[j])
#                     dist=min(dist, min_dist)
#                 else:
#                     break
#
#         return dist
#
# # if len(data) != len(list(set(data))):
# #     print(0)
# # else:
# #     print(binarySearch(data,0,len(data)-1))
#
# print(binarySearch(data,0,len(data)-1))

import sys

n = int(sys.stdin.readline().split()[0])
sorted_location = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    sorted_location.append((x,y))
sorted_location.sort()

def get_dist(a,b):
    return (a[0] - b[0]) ** 2 + (a[1] -b[1]) ** 2

def solution(l,r):
    if l == r:
        return float('inf')
    else:
        m = (l+r)//2
        min_dist = min(solution(l,m), solution(m+1, r))
        target_list = []

        for i in range(m,l-1,-1):
            if (sorted_location[i][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[i])
            else:
                break
        for i in range(m+1, r+1):
            if (sorted_location[i][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[i])
            else:
                break

        target_list.sort(key=lambda x:x[1])

        for i in range(len(target_list) -1):
            for j in range(i+1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_dist:
                    dist = get_dist(target_list[i], target_list[j])
                    min_dist = min(min_dist, dist)
                else:
                    break

        return min_dist

if len(sorted_location) != len(set(sorted_location)):
    print(0)
else:
    print(solution(0, len(sorted_location)-1))