# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：11. Container With Most Water.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-18 오후 8:39 
'''
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0

        while right > left:
            max_area = max(max_area, (right-left)*min(height[left],height[right]))

            if height[left] >= height[right]:
                right-=1
            else:
                left+=1

        return max_area