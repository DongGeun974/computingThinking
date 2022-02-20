# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：2447.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-12 오후 10:24 
'''
import sys
sys.setrecursionlimit(10**6)

def paint_star(LEN):
    div3 = LEN//3
    if LEN==3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*']*3
        return
    paint_star(div3)
    for i in range(0,LEN, div3):
        for j in range(0, LEN, div3):
            if i != div3 or j != div3:
                for k in range(div3):
                    g[i+k][j:j+div3] = g[k][:div3]

n = int(sys.stdin.readline())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()