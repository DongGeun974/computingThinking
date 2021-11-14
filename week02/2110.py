# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2110.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-11 오후 10:49 
'''

# input
import sys

n, c = map(int, sys.stdin.readline().split())
data = list(int(sys.stdin.readline().split()[0]) for i in range(n))
data.sort()

# set distacne
end = data[-1]-data[0]
start = 1
result = 0

# use binary search
while start <= end:
    mid = (start+end) // 2
    current = data[0]
    cnt = 1

    for i in range(len(data)):
        if data[i] >= current+mid:
            cnt+=1
            current= data[i]

    if cnt >= c:
        result =mid
        start = mid+1
    else:
        end = mid-1


print(result)