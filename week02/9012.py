# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：9012.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 1:04 
'''

# input
import sys

n = int(sys.stdin.readline().split()[0])
data = list(list(sys.stdin.readline().split()[0]) for i in range(n))
# data = list(list(sys.stdin.readline().split()[0].replace('()','')) for i in range(n))

for case in data:
    flag = True
    stack = []
    for i in case:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                print("NO")
                flag=False
                break
            else:
                check = stack.pop()
                # print(check)
                if check != "(":
                    print("NO")
                    flag=False
                    break
    if flag and len(stack) == 0:
        print("YES")
    elif flag and len(stack)!=0:
        print("NO")


