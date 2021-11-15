# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2493.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 10:31 
'''

# # time over, stack is always sorted
# import sys
#
# n = int(sys.stdin.readline().split()[0])
# data = list(map(int, sys.stdin.readline().split()))
#
# answer = []
# lower = []
# for i in range(len(data)-1, -1,-1):
#     temp = data.pop()
#     receive = -1
#     print('i',i)
#     for j in range(i-1, -1,-1):
#         print('j',j)
#         if data[j] > temp:
#             receive = j
#
#             answer.insert(0,receive+1)
#             break
#         else:
#             lower.append(j)
#
#     print()
#     if receive == -1:
#         answer.insert(0,0)
#
# print(*answer)

import sys

n = int(sys.stdin.readline().split()[0])
tower = list(list(map(int, sys.stdin.readline().split())))
stack = []
answer = []
for i in range(len(tower)):
    while stack:
        if stack[-1][1] > tower[i]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, tower[i]])

print(*answer)
