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

import sys

# dfs
def dfs(start, next, value, visited):
    global min_value

    # all visited and travel[last][start] !=0
    # return
    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value+ travel[next][start])
        return

    # not all visited, visit all other city
    for i in range(N):
        # check visited
        if travel[next][i] != 0 and \
                i != start and \
                i not in visited:
            # input visited
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            # reach last, all pop visited
            visited.pop()


N = int(sys.stdin.readline().split()[0])
travel = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_value = float('inf')

# start 0~n-1
for i in range(N):
    dfs(i, i, 0, [i])

print(min_value)