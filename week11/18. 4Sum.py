# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：18. 4Sum.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 4:19 
'''
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, a in enumerate(nums):
            if idx > 0 and a == nums[idx-1]:
                continue
            l1, r = idx+1, len(nums)-1
            while l1 < r:
                l2, r= l1+1, len(nums)-1
                while l2 < r:
                    four_sum = a + nums[l1] + nums[l2] + nums[r]
                    if four_sum > target:
                        r-=1
                    elif four_sum < target:
                        l2+=1
                    else:
                        res.append([a,nums[l1],nums[l2],nums[r]])
                        l2+=1
                        while nums[l2] == nums[l2-1] and l2<r:
                            l2+=1
                l1+=1
                while nums[l1] == nums[l1-1] and l1 < r:
                    l1+=1
        return res
