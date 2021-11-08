# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1074.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-06 오후 8:32 
'''
import sys


def z(n, r, c):
    global ls, cnt
    if n == 1:
        ls[r].insert(c, cnt)
        cnt += 1
        ls[r].insert(c+1, cnt)
        cnt += 1
        ls[r+1].insert(c, cnt)
        cnt += 1
        ls[r+1].insert(c+1, cnt)
        cnt += 1
    else:
        z(n - 1, r - (2 ** (n -1)), c - (2 ** (n -1)))
        z(n - 1, r - (2 ** (n-1)), c)
        z(n - 1, r , c - (2 ** (n -1)))
        z(n - 1, r , c )


data = list(map(int, sys.stdin.readline().split()))

pow_n = 2**data[0]

ls = [[] for _ in range(pow_n)]

cnt = 0

z(data[0],pow_n-2,pow_n-2)

print(ls[data[1]][data[2]])