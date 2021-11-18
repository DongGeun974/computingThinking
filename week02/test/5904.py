# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：5904.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-18 오전 10:00 
'''

# # memory over
# import sys
# sys.setrecursionlimit(10**6)
# """
#     Moo 게임
#     문제에서 조건 그대로 구현
# """
#
# def s(n):
#     if n == 0:
#         return 'moo'
#     else:
#         return s(n-1) + 'm'+'o'*(n+2) + s(n-1)
#
# # print(s(0))
# # print(s(1))
# # print(s(2))
#
# n = int(sys.stdin.readline())
# print(s(n)[n-1])

# import math
# import sys
#
# sys.setrecursionlimit(10**6)
# def s(n):
#     if n == 0:
#         return 'moo'
#
#     return  s(n - 1) + 'm'+'o'*(n + 2) + s(n-1)
#
# n = int(sys.stdin.readline())
#
# temp = 3
# answer = 0
# for i in range(1,n+1):
#     if temp < n:
#         temp = temp*2 + (i+2) +1
#     else:
#         answer = i-1
#         break
#
# print(s(answer)[n-1])

"""
    풀이
    n보다 긴 s(k)
    s(k) = s(k-1) + 'moo' + 'oooo....' >> k개 + s(k-1)
    
    l(k) = 2l(k-1)+3+k
    
    f(k, l, n)
        > f(k-1, l(k-1), n)
        > m (n=l(k-1)+1
        > o (l(k-1) +2 <= n <= l(k-1)+3+k)
        > else f(k-1, l(k-1), n-l(k-1)-3-k)
    
    주어진 n에 대해 k를 찾고
    k를 분할 
"""

import sys

n = int(sys.stdin.readline())

def length(k):
    if k == 0:
        return 3
    return 2*(length(k-1)) + 3 + k

k = 0
l = 0
for i in range(1, n):
    l = length(i)
    if l > n:
        k = i
        break
l=length(k)
# print(k)
# print(l)

def divideAndConquer(k, l, n):
    if k == 0:
        if n == 1:
            return 'm'
        else:
            return 'o'

    # l(n) = 2*(l(n-1) + 3 + k
    # l(n-1) = (l(n) - 3 - K) // 2
    l = (l - 3- k)//2

    k=k-1
    # print(k)
    # print(l)
    if n <= l:
        return divideAndConquer(k, l , n)
    elif n == l+1:
        return 'm'
    elif n >= l+3+k:
        return divideAndConquer(k,l, n - l - 3-k)
    else:
        return 'o'

print(divideAndConquer(k,l,n))