# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：64. Minimum Path Sum.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오후 3:59 
'''
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid[0]), len(grid)
        dp = [[0]*r for _ in range(c)]
        dp[0][0] = grid[0][0]
        for i in range(1,r):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1,c):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1,c):
            for j in range(1,r):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]]))

