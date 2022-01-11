# -*- coding: UTF-8 -*-
'''
@Project ：week10 
@File ：4. Median of Two Sorted Arrays.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-10 오후 5:00 
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        array.sort()
        median = len(nums1) + len(nums2)
        if median % 2 == 0:
            return (array[median // 2 -1] + array[median // 2]) / 2
        else:
            return array[median // 2] / 1

s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))
