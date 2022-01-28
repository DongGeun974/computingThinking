# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：46. Permutations.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오전 8:14 
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(node, visited):
            print(node)
            if len(visited) == len(nums):
                print(visited)
                result.append(visited)
                return
            for i in nums:
                if i not in visited:
                    dfs(i, visited+[i])

        # for i in nums:
        dfs(nums[-1], [])

        return result

s = Solution()
print(s.permute([1,2,3]))