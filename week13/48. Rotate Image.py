# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：48. Rotate Image.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오전 11:01 
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotate = [[] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)-1, -1, -1):
                rotate[i].append(matrix[j][i])

        for i in range(len(rotate)):
            for j in range(len(rotate)):
                matrix[i][j] = rotate[i][j]

        for i in matrix:
            print(i)

s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
