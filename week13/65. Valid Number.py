# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：65. Valid Number.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오후 4:12 
'''


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char == 'E':
                char = 'e'
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char=='.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit =True
            else:
                return False
        return met_digit