# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：6603.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 7:46 
'''

import sys

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=" ")
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i+1, depth+1)

combi = [0 for i in range(13)]

while True:
    s = list(map(int, sys.stdin.readline().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0,0)

    print()