# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1655.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오후 6:51 
'''

# import sys
#
# # max heap
# def push(heap, x):
#     heap.append(x)
#
#     child = len(heap)-1
#     parent = (child-1)//2
#
#     while heap[parent] < heap[child]:
#         temp = heap[parent]
#         heap[parent] = heap[child]
#         heap[child] = temp
#         temp = parent
#         child =parent
#         parent = (temp)//2
#
#     return heap
#
# # min heap
# def push(heap, x):
#     heap.append(x)
#
#     child = len(heap)-1
#     parent = (child-1)//2
#
#     while heap[parent] > heap[child]:
#         temp = heap[parent]
#         heap[parent] = heap[child]
#         heap[child] = temp
#         temp = parent
#         child =parent
#         parent = (temp)//2
#
#     return heap
#
# n = int(sys.stdin.readline().split()[0])
# data = list(int(sys.stdin.readline().split()[0]) for i in range(n))
# heap = []
# print(data)
# for i in data:
#     print(push(heap, i))

import heapq
import sys

n=int(sys.stdin.readline())
minhq = []
maxhq = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if len(minhq) == len(maxhq):
        heapq.heappush(maxhq, -x)
    else:
        heapq.heappush(minhq, x)
    print('maxhq : ' , maxhq)
    print('minhq : ', minhq)

    if minhq and minhq[0]<-maxhq[0]:
        mx = -heapq.heappop(maxhq)
        mn = heapq.heappop(minhq)
        heapq.heappush(maxhq, -mn)
        heapq.heappush(minhq, mx)
    print()
    print('maxhq : ', maxhq)
    print('minhq : ', minhq)

    print(-maxhq[0])