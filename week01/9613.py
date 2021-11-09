# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：9613.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 10:36 
'''

import sys

# for greatest common divisor
def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

# input test case
testCase = int(sys.stdin.readline().split()[0])

# input data
data = []
for _ in range(testCase):
    data.append(list(map(int, sys.stdin.readline().split())))

# for each case
for case in data:
    sum = 0
    for i in range(1, len(case)):
        for j in range(i+1, len(case)):
            sum+=gcd(case[i], case[j])
    print(sum)