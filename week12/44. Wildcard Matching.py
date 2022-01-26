# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：44. Wildcard Matching.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-26 오전 11:29 
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True

        for i in range(1,len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]