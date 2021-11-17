# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1493.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-17 오후 4:06 
'''

import sys

length, width, height = map(int, sys.stdin.readline().split())
type_cube = int(sys.stdin.readline())
cube_arr = sorted(list(list(map(int,sys.stdin.readline().split())) for _ in range(type_cube)),reverse=True)

# total_vol = length*width*height
#
# for i in range(len(cube_arr)-1,-1,-1):
#     cube_size = 2 ** cube_arr[i][0]
#     cube_num = cube_arr[i][1]
#     cube_vol = cube_size ** 3
#
#     min_dist = min(length, width, height)
#
#     if cube_size > min_dist:
#         continue
#     else:
#         # print(min_dist)
#         # print(cube_size)
#         temp = 0
#         if total_vol // cube_vol > cube_num:
#             temp = cube_vol*cube_num
#         else:
#             temp= total_vol//cube_vol
#
#
# def find_cube(l,w,h, n):
#     if n == -1:
#         return 0
#     min_dist = min(l,w,h)
#     cube_size = 2**n
#
#     if cube_size > min_dist:
#         return 0
#
#     find_cube(l-cube_size, w, h,n-1)
#     find_cube(l-cube_size,w-cube_size,h,n-1)
#     find_cube(cube_size,cube_size,h-cube_size,n-1)
#

volume = length*width*height
ans = 0
before = 0

for w, cnt in cube_arr:
    before <<=3
    v = 2**w        # cube length
    maxCnt = (length//v) * (width//v) * (height//v) - before
    maxCnt = min(cnt, maxCnt)
    ans+= maxCnt
    before+=maxCnt

if before == volume:
    print(ans)
else:
    print(-1)

