# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1003.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-30 오후 3:10 
'''

# # time over
# def fibo(n):
#     global zero, one
#     if n == 0 :
#         zero+=1
#     elif n == 1:
#         one+=1
#     else:
#         fibo(n-1)
#         fibo(n-2)
#
# import sys
#
# for _ in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     one = 0
#     zero = 0
#     fibo(n)
#     print(zero, one)
#

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0 :
        print('1 0')
        continue
    if n == 1 :
        print('0 1')
        continue
    zero = [0] * (n+1)
    one = [0] * (n+1)
    zero[0] = 1
    one[1] = 1
    for i in range(2,n+1) :
        zero[i] += zero[i-2] + zero[i-1]
        one[i] += one[i-1] + one[i-2]
    print(zero[n], one[n])
