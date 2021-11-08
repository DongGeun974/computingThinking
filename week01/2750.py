# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2750.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-06 오후 9:49 
'''
import sys

def bubble(ls):
    n = len(ls)

    for i in range(n-1):
        # if exist exchange, check is True
        check = True

        #start path
        for j in range(0,(n-1)-i):
            if ls[j] > ls[j+1] :
                ls[j],ls[j+1] = ls[j+1],ls[j]
                check = False
                # print(ls)
        # if check is True, no exchange, no need to calculating
        if check:
            break
        # print()

def select(ls):
    n = len(ls)

    for i in range(n-1):
        minimum = i
        for j in range(i+1,n):
            if ls[minimum] > ls[j]:
                minimum=j
            # print(ls)
        # print()
        ls[i], ls[minimum] = ls[minimum] , ls[i]

def insert(ls):
    n = len(ls)
    for i in range(1,n):
        for j in range(0,i):
            if ls[j] > ls[i]:
                ls[j], ls[i] = ls[i], ls[j]

# sys.stdin = open('input', 'r')

n = int(sys.stdin.readline().split()[0])
ls = []
for i in range(n):
    ls.append(int(sys.stdin.readline().split()[0]))

insert(ls)

for i in ls:
    print(i)