# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：20. Valid Parentheses.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-28 오후 6:54 
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == ')' and stack[-1] != '(':
                    return False
                elif s[i] == '}' and stack[-1] != '{':
                    return False
                elif s[i] == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()

        if stack:
            return False

        return True

s = Solution()
print(s.isValid("{[]}"))