# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1978.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 2:09 
'''

# 에라토스테네스의 체
# prime = list(range(2,1001))
# for i in prime:
#     if i != -1:
#         for j in prime[prime.index(i)+1:]:
#             if j % i == 0 :
#                 prime[prime.index(j)] = -1
#
# print(prime)
import sys

num = int(sys.stdin.readline().split()[0])
data = list(map(int, sys.stdin.readline().split()))
data.sort()

maxNum = data[-1]

prime = list(range(2,maxNum+1))
for i in prime:
    if i != -1:
        for j in prime[prime.index(i)+1:]:
            if j % i == 0 :
                prime[prime.index(j)] = -1

cnt = 0
for i in data:
    if i in prime:
        cnt=cnt+1

print(cnt)