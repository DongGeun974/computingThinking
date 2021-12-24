# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：819. Most Common Word.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-24 오전 11:26 
'''
import re
from collections import Counter
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]
s= Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(s.mostCommonWord(paragraph, banned))
