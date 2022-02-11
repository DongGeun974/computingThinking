# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：10974.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 7:39 
'''

import sys

n = int(sys.stdin.readline())
arr = list(range(1,n+1))

result = []
def dfs(visited):
    if len(visited) == n:
        result.append(visited)
    for i in arr:
        if i not in visited:
            dfs(visited+[i])
dfs([])

for i in result:
    print(' '.join(list(map(str, i))))