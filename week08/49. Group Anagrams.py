# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：49. Group Anagrams.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-25 오후 1:37 
'''
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for item in strs:
            answer["".join(sorted(item))].append(item)
        return list(answer.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s= Solution()
print(s.groupAnagrams(strs))