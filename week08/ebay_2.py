# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：ebay_2.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-30 오후 7:51 
'''

from itertools import product

def solution(stones, k):
    answer = ''
    prod = product(list(range(len(stones))) for _ in range(len(stones)))

    for i in prod:
        print(i)

    return answer

stones =[1, 3, 2]
k=3
print(solution(stones, k))