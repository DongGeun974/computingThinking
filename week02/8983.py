# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：8983.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-13 오후 11:43 
'''

# 동물 기준, 사대 binary search
# 사대, 동물, 사정거리 입력
import sys

gun_pos, animal, gun_range = map(int,sys.stdin.readline().split())
list_gun_pos = sorted(list(sys.stdin.readline().split()))
list_animal = list(list(map(int,sys.stdin.readline().split())) for i in range(animal))

answer = 0

for i in range(len(list_animal)):
    x = list_animal[i][0]
    y = list_animal[i][1]
    start = 0
    if (x - y) > 0:
        start = x - y
    end = y + x
    # print(x,y, start, end)

