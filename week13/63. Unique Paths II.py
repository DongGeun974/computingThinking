# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：63. Unique Paths II.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오후 3:29 
'''
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))