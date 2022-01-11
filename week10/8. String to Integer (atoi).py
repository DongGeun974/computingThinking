# -*- coding: UTF-8 -*-
'''
@Project ：week10 
@File ：8. String to Integer (atoi).py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-10 오후 10:01 
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        flag = False
        array = []
        for i in s:
            if i == '-':
                flag = True
            elif i.isdigit():
                array.append(i)
            elif i.isalpha():
                break

        if not array:
            return 0

        num = int("".join(array))

        if flag:
            num = -num

        if -pow(2,31) > num:
            num = 2 ** 31 * -1
        if num >pow(2, 31)-1:
            num = 2 ** 31 -1

        return num

s = Solution()
print(s.myAtoi("-91283472332"))