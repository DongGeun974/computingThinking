# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：561. Array Partition I.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-26 오후 9:59 
'''
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        anwser = 0
        for i in range(len(nums)):
            if i%2 == 0:
                anwser+=nums[i]
        return anwser

s = Solution()
nums = [6,2,6,5,1,2]
print(s.arrayPairSum(nums))