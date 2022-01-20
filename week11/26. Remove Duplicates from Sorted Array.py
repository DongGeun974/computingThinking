# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：26. Remove Duplicates from Sorted Array.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 8:54 
'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        change_idx = 1
        for i in range(len(nums)):
            if i != 0 and nums[i-1] != nums[i]:
                nums[change_idx] = nums[i]
                change_idx+=1
        return change_idx

s = Solution()
s.removeDuplicates([0,1,1,2,3,4,4,4,4,4,5,6,7,8,9,11])  # 11
s.removeDuplicates([0,1,2,3,4,5]) # 6
s.removeDuplicates([-1]) # 1


