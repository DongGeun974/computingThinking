# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：6588.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 11:12 
'''

# input data
import sys

data = []
while True:
    temp = int(sys.stdin.readline().split()[0])
    if temp == 0:
        break
    data.append(temp)

# use 에라토스테네스의 체
max_ = max(data)
prime = [ i for i in range(2, max_+1)]
for i in range(len(prime)):
    if prime[i] == -1:
        continue
    for j in range(i+1,len(prime)):
        if prime[j] == -1:
            continue
        if prime[j] % prime[i] == 0:
            prime[j] = -1

# find answer
for i in data:
    for j in range(max_):
        if prime[j] == -1:
            continue
        if i//2 in prime:
            print(i, '=', (i//2), '+', (i//2))
            break
        if (i - prime[j]) in prime:
            print(i, '=', (prime[j]) , '+', (i-prime[j]))
            break
        if  j == max_//2:
            print("Goldbach's conjecture is wrong.")
            break