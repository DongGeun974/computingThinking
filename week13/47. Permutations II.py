# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：47. Permutations II.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오전 8:33 
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums,[], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path + [nums[i]], res)

s = Solution()
print(s.permuteUnique([1,1,2]))