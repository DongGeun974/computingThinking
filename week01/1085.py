# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1085.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-04 오후 11:22 
'''
import sys

def dist(target, standard):
    if target < standard/2:
        return target
    elif target < standard:
        return standard-target
    else:
        return target-standard
# false : check limit in problem, float and int type

data = list(map(int,sys.stdin.readline().split()))

print(min(dist(data[0], data[2]), dist(data[1], data[3])))