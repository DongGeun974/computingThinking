# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：70. Climbing Stairs.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-03 오전 2:20 
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        # print(dp)
        return dp[n]

s = Solution()
print(s.climbStairs(4))