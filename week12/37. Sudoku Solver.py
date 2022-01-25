# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：37. Sudoku Solver.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-25 오후 6:18 
'''
from typing import List

class Solution:
    boardSize = 9

    def numOnRow(self, pBoard, pRow, pCol, pNumber):
        for c in range(Solution.boardSize):
            if c != pCol and pBoard[pRow][c] == pNumber:
                return True
        return False

    def numOnCol(self, pBoard, pRow, pCol, pNumber):
        for r in range(Solution.boardSize):
            if r != pRow and pBoard[r][pCol] == pNumber:
                return True
        return False

    def numInThreeCube(self, pBoard, pRow, pCol, pNumber):
        threeCubeRow = pRow - pRow%3
        threeCubeCol = pCol - pCol%3
        for r in range(threeCubeRow, threeCubeRow+3):
            for c in range(threeCubeCol, threeCubeCol+3):
                if pRow != r and pCol != c and pBoard[r][c] == pNumber:
                    return True
        return False

    def validateCell(self,pBoard, pRow, pCol, pNumber):
        return (not Solution.numOnRow(self, pBoard, pRow, pCol, pNumber) and
                not Solution.numOnCol(self, pBoard, pRow, pCol, pNumber) and
                not Solution.numInThreeCube(self, pBoard, pRow, pCol, pNumber))

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(self.boardSize):
            for c in range(self.boardSize):
                if board[r][c] == '.':
                    for x in range(1, self.boardSize+1):
                        if Solution.validateCell(self, board, r, c, str(x)) == True:
                            board[r][c] = str(x)
                            if Solution.solveSudoku(self, board):
                                return True
                            else:
                                board[r][c] = '.'
                    return False
        return True