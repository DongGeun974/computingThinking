# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：69. Sqrt(x).py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-03 오전 2:14 
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        i = 1
        while i*i <= x:
            i+=1
        return i-1

s = Solution()
print(s.mySqrt(8))
