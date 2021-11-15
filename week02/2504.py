# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2504.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오전 10:39 
'''

"""
    temp 사용, append할 때 temp 초기화
"""
# wrong answer
# import sys
#
# data = list(sys.stdin.readline().split()[0])
# stack = []
# answer = 0
# for i in range(len(data)):
#     if data[i] == '(' or data[i] == '[':
#         answer+=temp
#         temp=0
#         stack.append(data[i])
#     else:
#         if data[i] == ')' and stack[-1] == '(':
#             if temp==0:
#                 temp=2
#                 stack.pop()
#             else:
#                 temp*=2
#                 stack.pop()
#         elif data[i] == ']' and stack[-1] == '[' :
#             if temp==0:
#                 temp=3
#                 stack.pop()
#             else:
#                 temp*=3
#                 stack.pop()
#         else:
#             print('bad')
#             print(0)
#             exit()
#     print()
# answer+=temp
# print(answer)

s = input()
stack = []
for i in s:
    if i in ['(', '[']:
        stack.append(i)
    else:
        if stack and i == ')':
            if len(stack) > 1 and str(stack[-1]).isdigit():
                n = stack.pop() * 2
                stack.pop()
                stack.append(n)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                stack.append('-')
                break

        elif stack and i == ']':
            if len(stack) > 1 and str(stack[-1]).isdigit():
                n = stack.pop() * 3
                stack.pop()
                stack.append(n)
            elif stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                stack.append('-')
                break

        else:
            stack.append('-')
            break
    if len(stack) > 1 and str(stack[-1]).isdigit() and str(stack[-2]).isdigit():
        stack.append(stack.pop() + stack.pop())
    # print(stack)

if len(stack) == 1 and str(stack[-1]).isdigit():
    print(stack.pop())
else:
    print(0)
