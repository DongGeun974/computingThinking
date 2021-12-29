# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：316. Remove Duplicate Letters.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-30 오전 2:35 
'''
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char<stack[-1] and counter[stack[-1]] >0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)