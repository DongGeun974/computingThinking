# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：15. 3Sum.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-26 오후 3:08 
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left+=1
                elif sum > 0:
                    right-=1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1

                    left+=1
                    right-=1

        return answer


nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))
