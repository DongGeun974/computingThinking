# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2812.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오후 1:06 
'''
# import sys
#
# n,k =map(int, sys.stdin.readline().split())
# num = str(sys.stdin.readline().split()[0])
#
# stack = []
#
# for i in num:
#     if len(stack) == 0:
#         stack.append(int(i))
#     else:
#         for j in range(len(stack)-1,-1,-1):
#             if stack[j] < int(i) and k > 0:
#                 stack.pop()
#                 k-=1
#             else:
#                 break
#         stack.append(int(i))
#
# for j in range(len(stack) - 2, -1, -1):
#     if stack[j] >= stack[j+1] and k > 0:
#         stack.pop()
#         k -= 1
#
#
# stack=map(str, stack)
# print(''.join(stack))

import sys

n, k = map(int, sys.stdin.readline().split())
num = str(sys.stdin.readline().split()[0])
K = k
stack = []

for i in num:
    # if len(stack) == 0:
    #     stack.append(int(i))
    # else:
    for j in range(len(stack) - 1, -1, -1):
        if  stack and stack[j] < int(i) and k > 0:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(int(i))

# for j in range(len(stack) - 2, -1, -1):
#     if stack[j] >= stack[j + 1] and k > 0:
#         stack.pop()
#         k -= 1

# thanks to Kim
stack = stack[:n-K]
print(''.join(map(str, stack)))