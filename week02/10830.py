# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：10830.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-14 오후 6:45 
'''
import sys

def mul_matrix(n, a,b):
    temp = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += (a[i][k]* b[k][j])%1000
            temp[i].append(sum)
    return temp

def pow_matrix(n,a,b):
    # print(b)
    if b == 1:
        return a
    if b % 2 == 0:
        left = pow_matrix(n,a,b//2)
        # print('1',left)
        return mul_matrix(n,left,left)
    else:
        left = pow_matrix(n,a,b//2)
        # print('2', left)
        return mul_matrix(n, mul_matrix(n,left,left), a)

n, b = map(int, sys.stdin.readline().split())
a = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
# print(n , a, b)

answer = pow_matrix(n , a, b)
for i in answer:
    for j in i:
        print(j%1000 , end=' ')
    print()