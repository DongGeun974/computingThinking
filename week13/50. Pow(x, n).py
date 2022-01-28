# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：50. Pow(x, n).py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오전 11:14 
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        return self.pow_helper(x,n)

    def pow_helper(self, x, n):
        if n == 0 :
            return 1
        half = self.pow_helper(x, n//2)
        if n % 2 == 0:
            return half*half
        else:
            return half*half*x

s = Solution()
print(s.myPow(2.0, -2))