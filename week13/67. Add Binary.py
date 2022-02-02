# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：67. Add Binary.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-03 오전 1:12 
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = 0
        num_b = 0

        for i in range(len(a)):
            num_a+= int(a[i]) * pow(2, len(a)-i-1)
        for i in range(len(b)):
            num_b+= int(b[i]) * pow(2, len(b)-i-1)

        s = num_a+num_b
        ans = str(bin(s))

        return ans[2:]

