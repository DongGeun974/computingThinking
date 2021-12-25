# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：5. Longest Palindromic Substring.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-25 오후 1:39 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left : int, right : int) -> str:
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        if len(s) < 2 or s == s[::-1]:
            return  s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)

        return result

st = "babad"
s = Solution()
print(s.longestPalindrome(st))