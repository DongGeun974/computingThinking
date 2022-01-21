# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：29. Divide Two Integers.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-21 오후 3:11 
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = True

        abs_end, abs_sor = abs(dividend), abs(divisor)

        answer = abs_end // abs_sor

        if flag:
            answer = -answer

        if answer > pow(2,31) -1:
            return pow(2,31) -1
        elif answer < -pow(2,31):
            return -pow(2,31)

        return answer