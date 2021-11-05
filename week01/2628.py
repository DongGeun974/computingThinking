# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2628.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 5:12 
'''
import sys

def divDist(line, distance):
    result = distance

    targetIDX = 0
    length = 0
    for i in range(len(distance)):
        if sum(distance[:i+1]) > line:
            length = sum(distance[:i+1])
            break
        else:
            targetIDX = targetIDX+1

    result.insert(targetIDX, length - line)
    result.insert(targetIDX, result[targetIDX+1] - result[targetIDX])

    del result[targetIDX + 2]

    return result

# square = list(map(int, sys.stdin.readline().split()))
width, height = map(int, sys.stdin.readline().split())

width = [width]
height = [height]


line = int(sys.stdin.readline().split()[0])

for _ in range(line):
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        # height
        height = divDist(data[1], height)
    else:
        # width
        width = divDist(data[1], width)

    # print(width)
    # print(height)

print(max(width) * max(height))