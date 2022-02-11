# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：2343.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 10:56 
'''

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l = max(arr)
r = sum(arr)
ans = sys.maxsize

while l <= r:
    mid = (r+l) // 2
    cnt = 0
    sum = 0
    for i in range(len(arr)):
        if sum+arr[i] > mid:
            cnt += 1
            sum = 0
        sum+=arr[i]
    if sum:
        cnt+=1

    if cnt > m:
        l=mid+1
    else:
        ans=min(ans,mid)
        r=mid-1
print(ans)