# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：54. Spiral Matrix.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-28 오후 4:23 
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        if len(matrix) == 0:
            return matrix

        rowBegin = 0
        rowEnd = len(matrix)-1
        colBegin = 0
        colEnd = len(matrix[0])-1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd+1):
                res.append(matrix[rowBegin][i])
            rowBegin+=1

            for i in range(rowBegin, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd-=1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin-1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd-=1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    res.append(matrix[i][colBegin])
            colBegin+=1
        return res

s = Solution()
print(s.spiralOrder([[1,2],[3,4]]))