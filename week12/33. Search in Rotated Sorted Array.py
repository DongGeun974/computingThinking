# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：33. Search in Rotated Sorted Array.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-21 오후 4:27 
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        return nums.index(target)

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))