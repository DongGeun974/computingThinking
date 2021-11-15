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

gun_pos, animal, gun_range = map(int, sys.stdin.readline().split())
list_gun_pos = sorted(list(map(int, sys.stdin.readline().split())))
list_animal = list(list(map(int, sys.stdin.readline().split())) for i in range(animal))

answer = 0

for i in range(len(list_animal)):
    # 동물 사냥 가능 x 축
    x = list_animal[i][0]
    y = list_animal[i][1]
    animal_start = 0
    if (x - gun_range) > 0:
        animal_start = x - gun_range
    animal_end = x+gun_range

    # 사대 binary search
    gun_start = 0
    gun_end = len(list_gun_pos) - 1

    while gun_start <= gun_end:
        # print(list_animal[i])
        # print('animal range : ', animal_start, animal_end)
        # print('gun range : ', gun_range)
        mid = (gun_start + gun_end) // 2
        # print('gun pos' , list_gun_pos[mid])
        # 사대가 동물의 범위 안에 있는지, 해당 사대에서 총의 범위가 되는지
        if list_gun_pos[mid] >= animal_start \
                and list_gun_pos[mid] <= animal_end\
                and abs(list_gun_pos[mid] - x) + y <= gun_range:
            # print(x, y)
            answer += 1
            # print('answer')
            break
        # 사대가 동물의 범위에 없을때, 사대가 있어도 범위가 안될 때
        if list_gun_pos[mid] < animal_start or (list_gun_pos[mid] - x) <=0:
            gun_start = mid + 1
        elif list_gun_pos[mid] > animal_end or (list_gun_pos[mid] - x) >0:
            gun_end = mid - 1

    # print()
print(answer)
