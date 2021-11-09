# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1476.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-09 오전 10:02 
'''

# input E, S, M (1<=E<=15, 1<=S<=28, 1<=M<=19)
import sys

data = list(map(int, sys.stdin.readline().split()))

# find answer
i = 1
while True:
    # if E, S, M is max, need to % operator
    if (i) % 15 == data[0] % 15 \
            and (i) % 28 == data[1] % 28 \
            and (i) % 19 == data[2] % 19:
        break
    else:
        i+=1
print(i)
