# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：22. Generate Parentheses.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 6:57 
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def genParent(s,left,right,result):
            if left:
                genParent(s+'(', left-1, right, result)
            if right > left:
                genParent(s+')', left, right-1, result)
            if not right:
                result.append(s)
            return result
        return genParent('',n,n,[])


