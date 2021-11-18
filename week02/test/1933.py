# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1933.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-18 오전 10:19 
'''
import sys

"""
    스카이라인
"""

num_building = int(sys.stdin.readline())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(num_building))

print(arr)