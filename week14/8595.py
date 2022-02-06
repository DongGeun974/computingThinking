# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：8595.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-06 오후 1:36 
'''

import sys

_ = sys.stdin.readline()
ans = 0
tmp = ''

for ch in sys.stdin.readline().split()[0]:
    if ch.isalpha():
        if tmp != '':
            ans += int(tmp)
            tmp = ''
    else:
        tmp+=ch
if tmp != '':
    ans+=int(tmp)

print(ans)