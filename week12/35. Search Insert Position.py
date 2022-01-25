# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：35. Search Insert Position.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-22 오후 11:59 
'''
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return left

s = Solution()
print(s.searchInsert([1,3],2))