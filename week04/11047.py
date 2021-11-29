# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：11047.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오후 8:45 
'''

# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# coin = []
# for i in range(n):
#     temp = int(sys.stdin.readline())
#     if temp <= k:
#         coin.append(temp)
# cnt = 0
# while k:
#     if not coin:
#         break
#     bigest= coin.pop()
#     while bigest > k:
#         bigest =coin.pop()
#     cnt += k//bigest
#     k %= bigest
#
# print(cnt)
#


import sys

n, target = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0

while target:
    if coins[-1] > target:
        coins.pop()
        continue
    big = coins.pop()
    cnt += target//big
    target %= big

print(cnt)
