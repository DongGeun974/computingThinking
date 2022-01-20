# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：9. Palindrome Number.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-15 오후 5:54 
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        if str_x[0] == '-':
            return False

        reverse_x = []
        for i in str_x:
            reverse_x.insert(0, i)
        reverse_x = int("".join(reverse_x))

        if x == reverse_x:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(10))