# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：52. N-Queens II.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오후 3:33 
'''

class Solution:
    res = 0

    def totalNQueens(self, n: int) -> int:
        self.dfs([-1] * n, 0, [])
        return self.res

    def dfs(self, nums, index, path):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = '.' * len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + 'Q' + tmp[i + 1:]])

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True