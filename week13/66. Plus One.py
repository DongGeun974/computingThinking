# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：66. Plus One.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-03 오전 12:59 
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10,(len(digits) -1 -i))
        return [int(i) for i in str(num+1)]