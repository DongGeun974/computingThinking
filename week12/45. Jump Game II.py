# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：45. Jump Game II.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-26 오후 2:56 
'''
import math
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curEnd, curFarthest = 0, 0, 0
        for i in range(len(nums)-1):
            curFarthest = max(curFarthest, i+nums[i])
            if i == curEnd:
                jumps+=1
                curEnd=curFarthest

        return jumps

s = Solution()
print(s.jump([2,3,1,1,4]))