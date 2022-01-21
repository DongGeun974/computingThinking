# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：34. Find First and Last Position of Element in Sorted Array.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-21 오후 4:32 
'''
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l1 = []
        if target not in nums:
            return [-1,-1]

        for i in nums:
            if i == target:
                l1.append(nums.index(i))
                l1.append(nums.index(i)+nums.count(i)-1)
                return l1

s = Solution()
print(s.searchRange([2,2], 2))