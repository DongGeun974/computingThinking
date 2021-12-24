# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：937. Reorder Data in Log Files.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-24 오전 11:26 
'''

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for i in logs:
            if i.split()[1].isdigit():
                digit.append(i)
            else:
                letter.append(i)
        print(letter)
        letter.sort(key=lambda x:(x.split()[1:], x.split()[0]))

        list_letter = []
        for i in letter:
            list_letter.append("".join(i))
        list_digit = []
        for i in digit:
            list_digit.append("".join(i))
        return list_letter + list_digit


s = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(s.reorderLogFiles(logs))