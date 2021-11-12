# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：15649.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오후 3:34 
'''
# success
# import itertools
# import sys
#
# n,m= map(int, sys.stdin.readline().split())
# pers = itertools.permutations(range(1,n+1), m)
# for per in pers:
#     print(*per)

# success to dfs
import sys

n, m = map(int, sys.stdin.readline().split())
visited = []

def permutation(ls):
    if len(visited) == m:
        # print('visit is full ' ,visited)
        print(*visited)
        return

    # print('visit : ', visited, 'and x is' , x)
    for i in range(len(ls)):
        if not ls[i] in visited:
            visited.append(ls[i])
            permutation(ls)
            visited.pop()

permutation(range(1, n+1))
