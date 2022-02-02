# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：62. Unique Paths.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오후 2:48 
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        dp = [[0]*n for _ in range(m)]
        for i in range(1,m):
            dp[i][0] = 1
        for i in range(1,n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(3,7))