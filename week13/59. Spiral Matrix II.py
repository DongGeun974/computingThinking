# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：59. Spiral Matrix II.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오전 2:26 
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        num = 1

        while left<right and top<bottom:
            for i in range(left,right):
                matrix[top][i] = num
                num+=1
            top+=1

            for i in range(top,bottom):
                matrix[i][right-1] = num
                num+=1
            right-=1

            if not (left<right and top<bottom):
                break

            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = num
                num+=1
            bottom-=1

            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = num
                num+=1
            left+=1
        return matrix