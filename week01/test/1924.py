# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1924.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-11 오전 10:00 
'''
import sys

# 성공
"""
    2007.1.1 == 월
    2007.x.y == ??
    1,3,5,7,8,10,12 >> 31일
    4,6,9,11 >> 30일
    2 >> 28일
"""

# x월 y일 입력
x,y = map(int,sys.stdin.readline().split())
# 요일
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# n월
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
month_28 = [2]

# x월
day = 0
for i in range(1, 13):
    if i == x:
        break
    else:
        if i in month_31:
            day+=31
        elif i in month_30:
            day+=30
        elif i in month_28:
            day+=28

# y일
day+=y

# 날짜계산
print(week[day%7])
