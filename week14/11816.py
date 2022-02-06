# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：11816.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-06 오후 1:23 
'''

import sys

n = sys.stdin.readline().split()[0]
ans = 0
if n[0] == '0':
    if n[1] == 'x':
        # 16
        n = n[2:]
        for i in range(len(n)):
            temp = n[i]
            if temp == 'a':
                temp = 10
            elif temp == 'b':
                temp = 11
            elif temp == 'c':
                temp = 12
            elif temp == 'd':
                temp = 13
            elif temp == 'e':
                temp = 14
            elif temp == 'f':
                temp = 15
            ans += int(temp)*pow(16, len(n)-i-1)
        print(ans)
    elif len(n) != 1:
        # 8
        n = n[1:]
        for i in range(len(n)):
            ans += int(n[i]) * pow(8, len(n) - i-1)
        print(ans)
    else:
        print(0)
else:
    print(n)