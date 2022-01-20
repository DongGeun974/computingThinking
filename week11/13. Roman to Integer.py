# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：13. Roman to Integer.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-18 오후 10:13 
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman2value = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
                       'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        value = 0
        temp = ''
        cursor = 0

        while cursor < len(s):
            if (cursor+1)!=len(s) and s[cursor]+s[cursor+1] in roman2value:
                value += roman2value[s[cursor]+s[cursor+1]]
                cursor+=2
            else:
                value += roman2value[s[cursor]]
                cursor+=1

        return value