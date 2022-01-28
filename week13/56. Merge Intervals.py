# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：56. Merge Intervals.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오후 5:25 
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # intervals.sort(key=lambda x:(x[1], x[0]))
        intervals.sort()
        while intervals:
            start, end = intervals.pop(0)
            while intervals and end >= intervals[0][0]:
                _, _end = intervals.pop(0)
                end = max(end, _end)
            res.append([start, end])
        return res

s = Solution()
print(s.merge([[1,4],[2,3]]))