# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1629.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 11:49 
'''

# input
import sys

a, b, c = map(int, sys.stdin.readline().split())

# define function
def multiple(a, b, c):
    if b ==1:
        return a%c
    return (a*(multiple(a, b//2, c)))%c

print(multiple(a,b,c))