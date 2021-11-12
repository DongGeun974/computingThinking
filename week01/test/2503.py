# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2503.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-11 오전 10:18 
'''
import itertools
import sys

# 실패
"""
    숫자 야구
    서로 다른 세 숫자로 구성
    입력 : 질문 한 수
        민혁이가 질문 숫자, 스트라이크, 볼
    출력 : 가능성 있는 경우의 수 총 개수
"""

# 입력 n, data
# n = int(sys.stdin.readline().split()[0])
# data = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
#
# # 후보군 줄이기
# number = [1,2,3,4,5,6,7,8,9]
# cadinate = set()
# for i in range(len(data)):
#     if data[i][1] != 0 or data[i][2] != 0:
#         temp = list(str(data[i][0]))
#         for i in temp:
#             cadinate.add(i)
#
# cadinate=sorted(list(cadinate))
# print(cadinate)
#
# print(data)
#
# 모든 경우의 수
# ls = list(range(1,10))
# perms = itertools.permutations(ls, 3)
#
# for perm in perms:
#     case = list(perm)

# 각 데이터의 경우의 수 구하기
# all_case_set = set()
# for i in range(len(data)):
#     case = list(str(data[i][0]))        # ['a', 'b', 'c']
#     strike = data[i][1]
#     ball = data[i][2]
#     sum = strike+ball
#
#     temp = ['0','0','0']
#
#     if sum == 1:
#         # 숫자 2개 처리
#         case_list =
#     elif sum == 2:
#         # 숫자 1개 처리
#     elif sum == 3:


# 각 자리수 후보
# first = set()
# second = set()
# third = set()
#
# for i in range(len(data)):
#     case = list(str(data[i][0]))
#     strike = data[i][1]
#     ball = data[i][2]
#
#     if strike == 1:
#         first.add(case[0])
#         second.add(case[1])
#         third.add(case[2])
#     elif strike == 2:

# 입력 n, data

ls = list(range(1, 10))
per = []
answer = []


def permutation():
    if len(answer) == 3:
        per.append(list(answer))
        return

    for i in range(1, 10):
        if i not in answer:
            answer.append(i)
            permutation()
            answer.pop()


n = int(sys.stdin.readline().split()[0])
data = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

permutation()       # == itertools.permutations(9,3)
# print(len(per))

for i in data:

    data_temp = list(map(int, str(i[0])))
    # print(data_temp)
    # print(type(data_temp))
    remove_temp = []

    remove= 0
    for j in range(len(per)):
        strike = 0
        ball = 0
        j-=remove
        for index in range(3):
            if data_temp[index] == per[j][index]:
                strike+=1
            if data_temp[index] in per[j]:
                ball+=1
            ball -= strike
        # print('strike : ', strike, 'ball : ', ball)
        if i[1] != strike or i[2] != ball:
            # print('delete : ',case)
            per.remove(per[j])
            remove+=1
        # print()
    # print(per)

    # print()
    # print()
print(len(per))