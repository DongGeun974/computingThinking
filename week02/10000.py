# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：10000.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오전 10:19 
'''

import sys

n = int(sys.stdin.readline().split()[0])
point = []
for _ in range(n):
    x, r = list(map(int, sys.stdin.readline().split()))
    # 원의 왼쪽, 왼쪽 좌표, 상태, 지름의 합
    point.append(["{", x - r, 0, 0])
    # 원의 오른쪽
    point.append([")", x + r, 0, 0])

point.sort(key=lambda x: (x[1], x[0]))
print(point)

stack = []
answer = 1

for i in range(len(point)):
    print()
    print(point[i])
    print(stack)
    if point[i][0] == "{":
        if stack:
            # 맨 뒤와 x 시작 좌표가 같거나 이어지는 거리가 같으면
            if stack[-1][1] == point[i][1] or stack[-1][3] == point[i][1]:
                # 이어져 있음 표시 >> [2]=1
                stack[-1][2] = 1
            else:
                stack[-1][2] = 0
        stack.append(point[i])
    else:
        half = stack.pop()
        if stack and stack[-1][2] == 1:
            stack[-1][3] = point[i][1]
        if half[2] == 1 and half[3] == point[i][1]:
            answer += 1
        answer += 1

print(answer)

# import sys
#
# n = int(sys.stdin.readline())
# arr = []
# for _ in range(n):
#     x, r = map(int, sys.stdin.readline().split())
#     arr.append([0, x - r, 0])
#     arr.append([1, x + r, 0])
#
# # arr = sorted(sorted(arr,key=lambda x:x[0]), key=lambda x:x[1])
# arr.sort(key=lambda x: (x[1], -x[0]))
# print(arr)
# stack = []
# answer = 1
#
# for i in range(len(arr)):
#     if arr[i][0] == 0:
#         stack.append(arr[i])
#     else:
#
#