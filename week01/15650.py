# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：15650.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-10 오후 4:21 
'''
import sys

n, m = map(int, sys.stdin.readline().split())

visited = []

def combination(ls,x):
    if len(visited) == m:
        print(*visited)
        return

    for i in range(1+x, n+1):
        if i not in visited:
            visited.append(i)
            combination(ls,i)
            visited.pop()

combination(range(1, n+1) , 0)