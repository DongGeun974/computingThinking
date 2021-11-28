# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：9249.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-28 오전 10:59 
'''

import sys

sub1 = sys.stdin.readline()
sub2 = sys.stdin.readline()
dp = [ [0] * (len(sub2)+1) for _ in range(len(sub1)+1)]

for i in range(len(sub1)+1):
    for j in range(len(sub2)+1):
        if i == 0 or j == 0:
            dp[i][j] =0
        elif sub1[i-1] == sub2[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = 0

ans = 0
idx = 0
for i in range(len(dp)):
    if ans < max(dp[i]):
        ans = max(dp[i])
        idx = i

print(ans)
print(sub2[idx-ans+1:idx+1])