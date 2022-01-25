# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：39. Combination Sum.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-25 오후 7:03 
'''
import itertools
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(sum, index, path):
            if sum < 0:
                return
            if sum == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(sum-candidates[i], i, path+[candidates[i]])
        dfs(target, 0, [])
        return result