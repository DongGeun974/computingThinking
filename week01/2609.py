# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2609.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 9:27
'''
import sys

# read two number( 1 <= n <= 10,000)
data = list(map(int, sys.stdin.readline().split()))

# 최대공약수 : greatest common divisor > GCD
# 최소공배수 : least common mulitple > LCM

# list each common divisor
ls1 = []
ls2 = []

# find common divisor
def findDivisor(temp):
    ls = []
    i =2
    while temp != 1:
        while True:
            if temp%i == 0:
                ls.append(i)
                temp = int(temp/i)
                i=2
                break
            else:
                i+=1
    return ls

ls1 = findDivisor(data[0])
ls2 = findDivisor(data[1])

# find GCD
gcd = []
for i in range(len(ls1)):
    if ls1[i] in ls2:
        gcd.append(ls1[i])
        ls2.remove(ls1[i])

_gcd = 1
for i in gcd:
    _gcd*=i
print(_gcd)

# find LCM
print(int(data[0]/_gcd) * data[1])