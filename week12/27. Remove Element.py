# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：27. Remove Element.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-20 오후 6:59 
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = [num for num in nums if num != val]
        for i in range(len(answer)):
            nums[i] = answer[i]
        nums = nums[:len(answer)]
        return len(nums)

s = Solution()
print(s.removeElement([3,2,2,3], 3))