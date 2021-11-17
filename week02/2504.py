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

# index error
# import sys
#
# n = list(sys.stdin.readline().split()[0])
# stack = []
# answer = 0
# for i in n:
#     if i == '(' or i == '[':
#         stack.append(i)
#     else:
#         if stack and i == ')' and (stack[-1] == '(' or str(stack[-1]).isdigit()):
#             temp = stack.pop()
#             if temp == '(':
#                 stack.append(2)
#             else:
#                 while str(stack[-1]).isdigit():
#                     temp+=stack.pop()
#                 if stack[-1] == '(':
#                     stack.pop()
#                     stack.append(temp*2)
#                 else:
#                     print(0)
#                     exit()
#
#         elif stack and i == ']' and (stack[-1] == '[' or str(stack[-1]).isdigit()):
#             temp = stack.pop()
#             if temp == '[':
#                 stack.append(3)
#             else:
#                 while str(stack[-1]).isdigit():
#                     temp += stack.pop()
#                 if stack[-1] == '[':
#                     stack.pop()
#                     stack.append(temp * 3)
#                 else:
#                     print(0)
#                     exit()
#         else:
#             print(0)
#             exit()
#         # print(stack)
#         temp = 0
#         while stack and str(stack[-1]).isdigit():
#             temp += stack.pop()
#         if temp:
#             stack.append(temp)
#
# if stack and str(stack[0]).isdigit():
#     print(*stack)
# else:
#     print(0)

s= input()
stack = []
answer = 0

for x in s:
    if x == ')':
        temp = 0
        if len(stack) == 0:
            print(0)
            exit()
        while len(stack)!=0:
            top = stack.pop()
            if top=='[':
                print(0)
                exit()
            elif top =='(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2*temp)
                break
            else:
                temp += top

    elif x == ']':
        temp = 0
        if len(stack) == 0:
            print(0)
            exit()
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                print(0)
                exit()
            elif top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            else:
                temp += top

    else:
        stack.append(x)

for i in stack:
    if i == '(' or i =='[':
        print(0)
        exit()
    else:
        answer+=i

print(answer)