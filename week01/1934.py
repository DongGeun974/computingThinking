# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1934.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오후 9:51
'''

# input number of test case
import sys
testCase = int(sys.stdin.readline().split()[0])

# input data
data = [ sys.stdin.readline().split() for i in range(testCase)]

# find greatest common divisor
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

# for each case
for case in data:
    divisor =gcd(int(case[1]), int(case[0]))
    print(int(int(case[0])/divisor)  * int(case[1]))