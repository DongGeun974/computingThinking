# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：57. Insert Interval.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-29 오후 10:29 
'''
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, n = [], newInterval
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                res.append(i)
            elif n[1] < i[0]:
                res.append(n)
                return res + intervals[index:]
            else:
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        res.append(n)
        return res

s = Solution()
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))