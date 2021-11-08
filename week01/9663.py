# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：9663.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-06 오후 7:14 
'''
import sys

n = int(sys.stdin.readline().split()[0])

pos = [0]*n         # column
flag_a = [False]*n  # row
flag_b = [False]*(n*2 -1) # diagonal1
flag_c = [False]*(n*2 -1) # diagonal2

# def put(n):
#     for i in range(n):
#         print(f'{pos[i]:2}',end='')
#     print()

cnt = 0
def set (i, n) :
    global cnt
    for j in range(n):
        if (    not flag_a[j]
                and not flag_b[i+j]
                and not flag_c[i-j +(n-1)]):
            pos[i]=j
            if i == n-1:
                # put(n)
                cnt = cnt +1
            else:
                flag_a[j] = flag_b[j+i] = flag_c[i-j + (n-1)] = True
                set(i+1, n)
                flag_a[j] = flag_b[j+i] = flag_c[i-j + (n-1)] = False

set(0,n)
print(cnt)

