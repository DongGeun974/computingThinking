# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：55. Jump Game.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오후 4:55 
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True