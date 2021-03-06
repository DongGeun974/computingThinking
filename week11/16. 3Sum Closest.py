# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：16. 3Sum Closest.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 1:35 
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for idx, a in enumerate(nums):
            l, r = idx+1, len(nums)-1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if abs(target - three_sum) < abs(diff):
                    diff = target - three_sum
                if three_sum > target:
                    r -= 1
                else:
                    l += 1
            if diff == 0:
                break
        return target-diff