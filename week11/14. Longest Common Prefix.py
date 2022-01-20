# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：14. Longest Common Prefix.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-18 오후 10:24 
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''

        strs.sort(reverse=True)

        for idx, ch in enumerate(strs[0]):
            flag = False
            for i in range(1, len(strs)):
                if not strs[i]:
                    flag = True
                    break
                if idx < len(strs[i]):
                    if ch != strs[i][idx]:
                        flag = True
                        break
                else:
                    flag = True
                    break
            if flag:
                break
            answer+=ch

        return answer

s = Solution()
print(s.longestCommonPrefix(["","b"]))