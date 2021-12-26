# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：238. Product of Array Except Self.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-26 오후 10:12 
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out =[]
        p=1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p=1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i]*p
            p = p*nums[i]
        return out
s=Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))