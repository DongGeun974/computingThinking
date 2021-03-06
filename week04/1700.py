# -*- coding: UTF-8 -*-
'''
@Project ：week04 
@File ：1700.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-27 오전 1:38 
'''

# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# products = list(map(int, sys.stdin.readline().split()))
# multiTap = []
# ans = 0
#
# while products:
#     prod = products.pop(0)
#     if prod not in multiTap and len(multiTap) < n:
#         multiTap.append(prod)
#     elif prod not in multiTap and len(multiTap) == n:
#         cur_mulit = [float('inf')] * n
#         for i in range(len(products)):
#             if products[i] in multiTap and cur_mulit[multiTap.index(products[i])] == float('inf'):
#                 cur_mulit[multiTap.index(products[i])] = i
#         # print('cur', cur_mulit)
#         delete_item = multiTap[cur_mulit.index(max(cur_mulit))]
#         multiTap.remove(delete_item)
#         multiTap.append(prod)
#         ans+=1
#     # print(multiTap)
#
# print(ans)

import sys
from collections import deque

mulTap, n = map(int, sys.stdin.readline().split())
items = deque(map(int, sys.stdin.readline().split()))
plug = []
ans = 0

while items:
    item = items.popleft()

    if item not in plug and len(plug) < mulTap:
        plug.append(item)
    if item not in plug and len(plug) >= mulTap:
        idx = [float('inf')] * mulTap
        for i in range(len(plug)):
            for j in range(len(items)):
                if items[j] == plug[i] :
                    idx[i] = j
                    break
        removePlug = plug[idx.index(max(idx))]
        plug.remove(removePlug)
        plug.append(item)
        ans +=1

print(ans)