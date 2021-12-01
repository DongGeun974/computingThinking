# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：2662.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-01 오후 7:24 
'''

import sys

n, m = map(int, sys.stdin.readline().split())
byInvestment = [[0 for _ in range(m+1)]]

for _ in range(n):
    byInvestment.append(list(map(int, sys.stdin.readline().split())))

table = [[0 for _ in range(m+1)] for _ in range(n+1)]
pos = [[[0 for  _ in range(m+1)] for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        table[i][j] = max(table[i][j-1], byInvestment[i][j])
        if table[i][j] == byInvestment[i][j]:
            pos[i][j][j] = i
        else:
            pos[i][j] = pos[i][j].copy()
    for k in range(1, i+1):
        if table[i][j] < table[k][j-1] + byInvestment[i-k][j]:
            table[i][j] = table[k][j-1] + byInvestment[i-k][j]
            pos[i][j] = pos[k][j-1].copy()
            pos[i][j][j] = i-k

print(table[-1][-1])
print(*pos[-1][-1][1:])