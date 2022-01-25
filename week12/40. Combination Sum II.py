# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：40. Combination Sum II.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-25 오후 8:14 
'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(sorted(candidates), target, 0, [], result)
        return result

    def dfs(self, nums, target, idx, path, ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)