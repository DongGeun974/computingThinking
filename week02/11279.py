# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：11279.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 11:38 
'''

# import collections
# import sys
#
#
# def heapify(parent, arr):
#     # check parent have child at least one
#     if parent >= len(arr)//2:
#         # this parent have no child
#         return
#     # print(parent)
#
#     # check how many have child
#     left = 2*parent+1
#     right = left+1
#     if right >= len(arr):
#         right=-1
#     # print('left : ', left, 'right : ', right)
#     # print('left : ', arr[left], 'right : ', arr[right])
#
#     child = left if (arr[left] >= arr[right]) else right
#     # print(child)
#
#     # compare parent and max(child)
#     temp = arr[parent]
#     # this case is child bigger than parent
#     if temp < arr[child]:
#         arr[parent] = arr[child]
#         arr[child] = temp
#         heapify(child, arr)
#
#
# n = int(sys.stdin.readline().split()[0])
# data = list(int( sys.stdin.readline().split()[0]) for i in range(n))
#
# # print(data)
#
# # # queue
# queue = collections.deque()
# # print(queue)
# #
# # for i in data:
# #     queue.append(i)
# #
# # print(queue)
# # print(len(data)//2-1)
# # print(len(data))
# # for i in range(len(data)//2-1, -1, -1):
# #     heapify(i, data)
# # print(data)
#
# # time over
# for i in data:
#     if i == 0:
#         if len(queue) == 0:
#             print(0)
#         else:
#             print(queue.popleft())
#
#     else:
#         queue.insert(0,i)
#         for i in range(len(queue) // 2 - 1, -1, -1):
#             heapify(i, queue)
#         # queue.insert(0, i)
#         # heapify(0, queue)

import sys

# n = int(sys.stdin.readline().split()[0])
# data = list(int( sys.stdin.readline().split()[0]) for i in range(n))

import sys

input = sys.stdin.readline

heap = [0]
capacity = 0


def push(heap, n):
    global capacity

    if len(heap) - 1 == capacity:
        heap = heap + [0] * len(heap)

    capacity += 1
    heap[capacity] = n

    # child
    tn = capacity
    while tn > 1:
        if heap[tn] > heap[tn // 2]:
            temp = heap[tn]
            heap[tn] = heap[tn // 2]
            heap[tn // 2] = temp
            tn //= 2
        else:
            break
    return heap


def pop(heap):
    global capacity

    if capacity == 0:
        return 0

    p = heap[1]

    # smallest to top
    heap[1] = heap[capacity]
    heap[capacity] = 0

    # parent
    tn = 1
    while (capacity > tn * 2):
        if heap[tn * 2] == 0 and heap[tn * 2 + 1] == 0:
            break
        if heap[tn] < max(heap[tn * 2], heap[tn * 2 + 1]):
            temp = heap[tn]
            if heap[tn * 2] > heap[tn * 2 + 1]:
                heap[tn] = heap[tn * 2]
                heap[tn * 2] = temp
                tn *= 2
            else:
                heap[tn] = heap[tn * 2 + 1]
                heap[tn * 2 + 1] = temp
                tn =tn* 2 + 1
        else:
            break

    capacity -= 1

    return p


# for i in data:
#     x = int(i)
#     if x:
#         heap=push(heap, x)
#     else:
#         print(pop(heap))
for i in range(int(input())):
    x = int(input())
    if x:
        heap = push(heap, x)
    else:
        print(pop(heap))
