# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：344. Reverse String.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-24 오전 2:17 
'''


class Solution:
    def reverseString(self, s) -> None:
        s[:] = s[::-1]
        print(s)

s= Solution()

print(s.reverseString(["h","e","l","l","o"]))