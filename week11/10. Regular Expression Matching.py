# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：10. Regular Expression Matching.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-15 오후 6:03 
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       if p == '':
            return s == ''
       if len(p) == 1:
            return len(s) == 1 and (s == p or p == '.')
       if p[1] != '*':
            if s == '':
                return False
            return (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:],p[1:])
       while s and (p[0] == s[0] or p[0] == '.'):
            if self.isMatch(s,p[2:]):
                return True
            s = s[1:]
       return self.isMatch(s, p[2:])