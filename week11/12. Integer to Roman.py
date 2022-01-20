# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：12. Integer to Roman.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-18 오후 9:47 
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        value2roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                       9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        answer = ""

        while num!=0:
            for value in value2roman:
                if num-value >= 0:
                    answer+=value2roman[value]
                    num = num-value
                    break

        return answer