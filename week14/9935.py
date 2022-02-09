# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：9935.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오전 2:56 
'''

import sys

target = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
lastChar = bomb[-1]
stack = []
length = len(bomb)

for char in target:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)
if answer:
    print(answer)
else:
    print("FRULA")