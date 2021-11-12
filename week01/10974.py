# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10974.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오전 10:22 
'''

# input n
import itertools
import sys

n = int(sys.stdin.readline().split()[0])
for i in itertools.permutations([i for i in range(1, n+1)]):
    print(*i)