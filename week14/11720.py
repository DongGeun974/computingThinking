# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：11720.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-06 오후 1:18 
'''

import sys

_ = sys.stdin.readline()
ans = 0
for i in sys.stdin.readline().split()[0]:
    ans += int(i)
print(ans)