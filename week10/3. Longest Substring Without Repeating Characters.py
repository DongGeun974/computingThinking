# -*- coding: UTF-8 -*-
'''
@Project ：week10 
@File ：3. Longest Substring Without Repeating Characters.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-10 오후 4:08 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, max_len = 0,0,0
        exist = dict()

        for idx, char in enumerate(s):
            if char in exist and start <= exist[char]:
                start = exist[char] + 1
            else:
                max_len = max(max_len, idx - start + 1)
            exist[char] = idx
        return max_len