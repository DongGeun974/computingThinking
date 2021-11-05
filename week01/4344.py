# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：4344.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오전 10:52 
'''
import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):

    data = list(map(int, sys.stdin.readline().split()))
    # data.remove(data[0])

    avg = sum(data[1:])/data[0]
    # print(avg)

    student = 0

    for i in data[1:]:
        if i > avg:
            student = student + 1

    # percent = round((student/data[0])*100,3)
    percent = (student / data[0]) * 100

    print("{:.3f}".format(percent)+'%')