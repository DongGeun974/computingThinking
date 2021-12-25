# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：42. Trapping Rain Water.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-25 오후 1:40 
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # stack =[]
        # answer = 0
        #
        # for i in range(len(height)):
        #     while stack and height[i] > height[stack[-1]]:
        #         top = stack.pop()
        #
        #         if not len(stack):
        #             break
        #
        #         distance = i - stack[-1] -1
        #         waters = min(height[i], height[stack[-1]]) - height[top]
        #         answer += distance*waters
        #     stack.append(i)
        #
        # return answer

        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(right_max, height[right])

            print()

            if left_max <= right_max:
                print('l', left, left_max)
                print(left_max - height[left])
                volume += left_max - height[left]
                left+=1
            else:
                print('r', right, right_max)
                print(right_max - height[right])
                volume += right_max - height[right]
                right-=1

        return volume

s = Solution()
height = [4, 2, 0, 3, 2, 5]
print(s.trap(height))