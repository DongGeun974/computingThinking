# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：6603.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-11 오전 10 :09
'''



# 성공
"""
    집합에서 고를 수 있는 모든 경우의 수
    입력 : 여러 개 테스트 케이스
        첫번째 k, 다음 k개는 집합 s
        입력의 마지막 0
    출력 : 각 테스트 케이스마다 수를 고르는 방법 출력
"""
import itertools
import sys

answer =[]
def recursion(ls, index):
    if len(answer) == 6:
        print(* answer)

    for i in range(index, 51):
        if i in ls and i not in answer:
            answer.append(i)
            recursion(ls,i)
            answer.pop()

# 테스트 케이스 입력
while True:
    data = list(map(int,sys.stdin.readline().split()))
    # k
    k = data[0]
    if k == 0:
        break
    # s
    s = data[1:]

    # 순열 사용(모든 경우의 수) == fales
    # 로또는 1,2,3 과 3,2,1이 같은 경우, 즉 순서 상관 없음
    # 조합 사용
    combis = recursion(s,0)

    print()
#
# # 테스트 케이스 입력
# while True:
#     data = list(map(int,sys.stdin.readline().split()))
#     # k
#     k = data[0]
#     if k == 0:
#         break
#     # s
#     s = data[1:]
#
#     # 순열 사용(모든 경우의 수) == fales
#     # 로또는 1,2,3 과 3,2,1이 같은 경우, 즉 순서 상관 없음
#     # 조합 사용
#     combis = itertools.combinations(s, 6)
#     for combi in combis:
#         print(*combi)
#
#     print()
