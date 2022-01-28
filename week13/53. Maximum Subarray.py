# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：53. Maximum Subarray.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오후 3:35 
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

s = Solution()
print(s.maxSubArray( [-2,1,-3,4, -1,2,1,-5,4]))