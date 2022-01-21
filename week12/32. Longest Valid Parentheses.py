# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：32. Longest Valid Parentheses.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-21 오후 4:12 
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                    length = i - (stack[-1] if stack else -1)
                    res = max(res, length)
                else:
                    stack.append(i)

        return res

s =Solution()
print(s.longestValidParentheses(")()())"))