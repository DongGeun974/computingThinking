# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2588.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-04 오후 5:00 
'''

# faster
import sys
item1 = int(sys.stdin.readline())
item2 = int(sys.stdin.readline())
i=10
for _ in range(len(str(item1))):
    print(item1 * int(((item2 % i) / (i/10))))
    i = i *10
print(item1*item2)