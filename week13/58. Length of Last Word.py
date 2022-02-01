# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：58. Length of Last Word.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오전 2:20 
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])