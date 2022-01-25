# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：41. First Missing Positive.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-25 오후 8:24 
'''
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1

        for num in nums:
            if num == res:
                res += 1

        return res

s = Solution()
print(s.firstMissingPositive([2,2]))