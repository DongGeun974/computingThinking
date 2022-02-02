# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：68. Text Justification.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-03 오전 2:05 
'''
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, numLetter = [], [], 0
        for w in words:
            if numLetter + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - numLetter):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, numLetter = [], 0
            cur += [w]
            numLetter += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]