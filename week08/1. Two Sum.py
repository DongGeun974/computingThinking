# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：1. Two Sum.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-25 오후 1:39 
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

nums = [3,2,4]
target = 6
s = Solution()
print(s.twoSum(nums, target))