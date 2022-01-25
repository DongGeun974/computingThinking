# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：36. Valid Sudoku.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-23 오전 1:54 
'''
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_check = []
            col_check = []
            for j in range(len(board)):
                row = board[i][j]
                col = board[j][i]
                if row != '.' and row in row_check:
                    return False
                else:
                    row_check.append(row)
                if col != '.' and col in col_check:
                    return False
                else:
                    col_check.append(col)
        for i in range(0,len(board),3):
            check = []
            for j in range(0,len(board),3):
                check = []
                for x in range(3):
                    for y in range(3):
                        data = board[i+x][j+y]
                        if data != '.' and data in check:
                            return False
                        else:
                            check.append(data)
        return True
