# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：10971.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-08 오전 11:46 
'''

# all permutations

# import itertools
# import sys
#
# def find_path(depth, start, stop, case):
#     sum = 0
#     if depth == n-2:
#         print(start, stop, data[start][stop])
#         return int(data[start][stop])
#         print('done')
#     else:
#         print(start, stop, data[start][stop])
#         return find_path(depth+1, case[depth+1],case[depth+2], case) + int(data[start][stop])
#
# n = int(sys.stdin.readline().split()[0])
# ls = []
# for i in range(n):
#     ls.append(i)
# data = [sys.stdin.readline().split() for i in range(n)]
# all_case = itertools.permutations(ls)
#
# for case in all_case:
#     print()
#     sum = find_path(0,case[0],case[1], case)
#     print( case[-1], case[0], data[case[-1]][case[0]])
#     print(sum + int(data[case[-1]][case[0]]))

# n-1 permutation

# import itertools
# import sys
#
# def find_path(depth, start, stop, case):
#     if int(data[start][stop]) == 0 :
#         return 10000000
#     else:
#         if depth == n-2:
#             print(start, stop, data[start][stop])
#             return int(data[start][stop])
#             print('done')
#         else:
#             print(start, stop, data[start][stop])
#             return find_path(depth+1, case[depth],case[depth+1], case) + int(data[start][stop])
#
# n = int(sys.stdin.readline().split()[0])
# ls = []
# for i in range(1, n):
#     ls.append(i)
# data = [sys.stdin.readline().split() for i in range(n)]
# all_case = itertools.permutations(ls)
#
# for case in all_case:
#     print()
#     sum = find_path(0,0,case[0], case)
#     print( case[-1],0, data[case[-1]][0])
#     print(sum + int(data[case[-1]][0]))


import itertools
import sys

def find_path(depth, start, stop, case):

    if depth == n-2:
        # print(start, stop, data[start][stop])
        if int(data[start][stop]) == 0 :
            return float('inf')
        else:
            return int(data[start][stop])
    else:
        # print(start, stop, data[start][stop])
        if int(data[start][stop]) == 0 :
            return find_path(depth+1, case[depth],case[depth+1], case) +float('inf')
        else:
            return find_path(depth+1, case[depth],case[depth+1], case) + int(data[start][stop])


n = int(sys.stdin.readline().split()[0])
ls = []
for i in range(1, n):
    ls.append(i)
data = [sys.stdin.readline().split() for i in range(n)]
all_case = itertools.permutations(ls)

answer = float('inf')

for case in all_case:
    # print()
    sum = find_path(0,0,case[0], case) + int(data[case[-1]][0])
    # print( case[-1],0, data[case[-1]][0])
    if sum < answer : answer = sum
    # print(sum)

print(answer)
