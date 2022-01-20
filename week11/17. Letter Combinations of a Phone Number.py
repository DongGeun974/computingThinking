# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：17. Letter Combinations of a Phone Number.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 1:47 
'''
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}

        if not digits:
            return []

        answer = ['']
        for ch in digits:
            temp = []
            for a in answer:
                for i in letter[int(ch)]:
                    temp.append(a+i)
                answer = temp

        return answer

s = Solution()
print(s.letterCombinations("23"))