# -*- coding: UTF-8 -*-
'''
@Project ：week10 
@File ：7. Reverse Integer.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-10 오후 7:57 
'''

class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = abs(x)

        x = str(x)
        array = []

        for i in x:
            array.insert(0, i)

        x = int("".join(array))

        if flag:
            x = -x

        if -pow(2,31) > x or x >pow(2, 31)-1:
            return 0

        return x

s = Solution()
print(s.reverse(1534236469))