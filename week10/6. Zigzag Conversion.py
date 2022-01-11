# -*- coding: UTF-8 -*-
'''
@Project ：week10 
@File ：6. Zigzag Conversion.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-10 오후 5:18 
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index_dict = dict()
        zigzag_index = 0
        down = 1
        up = -1
        move = 0

        for char in s:
            if zigzag_index == 0:
                move=down
            elif zigzag_index == numRows-1:
                move=up

            index_dict[zigzag_index] = index_dict.get(zigzag_index,'') + char
            zigzag_index += move

        return "".join(index_dict.values())

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
