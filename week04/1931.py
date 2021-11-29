# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1931.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-26 오후 11:24 
'''

# import sys
#
# n = int(sys.stdin.readline())
# meeting = []
# for i in range(n):
#     meeting.append(list(map(int, sys.stdin.readline().split())))
# meeting.sort(key=lambda x : (x[1], x[0]))
#
# cnt = 1
# end_time = meeting[0][1]
#
# for i in range(1, n):
#     if meeting[i][0] >= end_time:
#         cnt += 1
#         end_time=meeting[i][1]
#
# print(cnt)


import sys

n = int(sys.stdin.readline())
meeting = sorted(list(list(map(int, sys.stdin.readline().split())) for _ in range(n)), key=lambda x:(x[1], x[0]))
ans = 1
end_time = meeting[0][1]

for i in range(1, len(meeting)):
    if meeting[i][0] >= end_time:
        ans+=1
        end_time = meeting[i][1]
print(ans)