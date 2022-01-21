# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：28. Implement strStr().py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-21 오후 3:01 
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle:
            return 0

        for i in range(len(haystack)-len(needle)+1):
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("", ""))
print(s.strStr("abc","c"))