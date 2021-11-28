# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：9251.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-25 오후 9:58 
'''

# import sys
#
# sub1 = sys.stdin.readline().strip().upper()
# sub2 = sys.stdin.readline().strip().upper()
# len1 = len(sub1)
# len2 = len(sub2)
# matrix = [[0] * ( len2+1) for _ in range(len1+1)]
#
# for i in range(1, len1+1):
#     for j in range(1, len2+1):
#         if sub1[i-1] == sub2[j-1]:
#             # print(1)
#             # print(sub1[:i],i)
#             # print(sub2[:j],j)
#             # 길이는 (두 글자가 추가되기 전 가장 큰 길이 + 1)이 됨
#             matrix[i][j] = matrix[i-1][j-1] + 1
#         else:
#             # print(2)
#             # print(sub1[:i], i)
#             # print(sub2[:j], j)
#             # 기존에 주어진 문자열로 만들 수 있던 최대 길이를 갖게 됨
#             matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
#
#     # print(' ',list(range(7)))
#     # for i, k in enumerate(matrix):
#     #     print(i,k)
#
# print(matrix[-1][-1])

import sys

str1=sys.stdin.readline().strip()
str2=sys.stdin.readline().strip()

lcs = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[len(str1)][len(str2)])