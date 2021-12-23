# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：125. Valid Palindrome.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-24 오전 1:10 
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        buf = ""
        for ch in s:
            if ch.isdigit() or ch.isalpha():
                buf+=ch.upper()
        length = len(buf.upper())
        for i in range(length // 2):
            if buf[i] != buf[length-i-1]:
                return False
        return True

s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))