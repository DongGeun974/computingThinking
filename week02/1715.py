# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：1715.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오후 8:10 
'''

# wrong answer
# import heapq
# import sys
#
# n = int(sys.stdin.readline())
# # data = list(int(sys.stdin.readline()) for _ in range(n))
# # print(data)
# card1 = []
# card2 = []
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     if len(card1) == len(card2):
#         heapq.heappush(card2, x)
#     else:
#         heapq.heappush(card1,x)
#
# answer = 0
#
# while len(card1) and len(card2):
#     print('1-1', card1)
#     print('2-1', card2)
#     temp1 = heapq.heappop(card1)
#     temp2 = heapq.heappop(card2)
#     print(temp1)
#     print(temp2)
#     temp = temp1+temp2
#     answer+= temp
#
#     if len(card1) > len(card2):
#         heapq.heappush(card2, temp)
#     else:
#         heapq.heappush(card1,temp)
#     print('1',card1)
#     print('2',card2)
#     print()
#
# print(answer)
#
# # if len(card1):
# #     answer+=heapq.heappop(card1)
# # if len(card2):
# #     answer+=heapq.heappop(card2)
# #
# # print(answer)

import heapq
import sys

n = int(sys.stdin.readline())
card_deck = []

for _ in range(n):
    heapq.heappush(card_deck, int(sys.stdin.readline()))

if len(card_deck) == 1:
    print(0)
else:
    answer = 0
    while len(card_deck) >1:
        temp1 = heapq.heappop(card_deck)
        temp2 = heapq.heappop(card_deck)
        answer+=temp1+temp2
        heapq.heappush(card_deck, temp1+temp2)

    print(answer)