# -*- coding: UTF-8 -*-
'''
@Project ：week12 
@File ：38. Count and Say.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-25 오후 6:46 
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count+=1
                else:
                    temp += str(count)+let
                    let = l
                    count=1
            temp += str(count)+let
            s = temp
            print(s)

        return s

s =Solution()
print(s.countAndSay(4))