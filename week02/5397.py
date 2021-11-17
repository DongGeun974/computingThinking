# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：5397.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-17 오전 9:29 
'''

# wrong answer, not use cursor
# import sys
#
# n = int(sys.stdin.readline())
#
# for _ in range(n):
#     password = sys.stdin.readline().split()[0]
#
#     stack = []
#     cur = 0
#
#     for x in password:
#         if x == '<' and cur > 0:
#             cur-=1
#         elif x == '>' and cur < len(stack)-1:
#             cur+=1
#         elif x == '-' and cur > 0:
#             stack.pop(cur)
#             cur-=1
#         else:
#             stack.insert(cur, x)
#             cur+=1
#
#     print(stack)

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    pw = sys.stdin.readline().split()[0]
    stack1 = []
    stack2 = []

    for x in pw:
        if x == '<':
            if stack1:
                temp = stack1.pop()
                stack2.append(temp)
        elif x == '>':
            if stack2:
                temp = stack2.pop()
                stack1.append(temp)
        elif x == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(x)

    print(''.join(stack1+list(reversed(stack2))))