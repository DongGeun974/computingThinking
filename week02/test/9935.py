# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：9935.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-18 오전 10:09 
'''

"""
    문자열 폭발
    stack
    풀이
        하나씩 스택에 추가
        스택 길이가 폭탄 길이보다 크면
            스택과 폭탄 비교
"""

# # time over
# import sys
#
# target = sys.stdin.readline().split()[0]
# boom = list(sys.stdin.readline().split()[0])
#
# # print(type(target))
# # print(boom)
#
# stack1 = []
# stack2 = []
#
# before = len(target)
# after = before+1
# while before != after:
#     before = len(target)
#     cur = 0
#     for i in target:
#         if i in boom[cur%len(boom)]:
#             cur+=1
#             stack2.append(i)
#         else:
#             stack1.append(i)
#     target = ''.join(stack1)
#     stack1=[]
#     stack2=[]
#     after = len(target)
#     # print(after)
#
# if target:
#     print(target)
# else:
#     print('FRULA')


import sys

target = sys.stdin.readline().strip()
# boom = list(sys.stdin.readline().split()[0])
boom = sys.stdin.readline().strip()

stack = []

# 한 문자마다 판단
for x in target:
    # 임의의 문자가 boom의 마지막 글자와 같으면
    if x == boom[-1]:
        stack.append(x)
        if len(stack) >= len(boom):
            if stack[len(stack)-len(boom):] == list(boom):
                del stack[len(stack)-len(boom):]
    else:
        stack.append(x)

if stack:
    print(''.join(stack))
else:
    print('FRULA')
