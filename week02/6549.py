# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：6549.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-14 오후 1:16 
'''

# 히스토그램 좌, 우 넓이 구하기
# 가운데서부터 max_area, height, left, right pointer 사용해서 최대 넓이 구하기
# 좌, 우, 가운데서부터 시작한 넓이 중 큰 값 리턴


# wrong answer
import sys

def findArea(ls, start, end):
    # print(start, end)
    # start, end 같으면 막대 하나, 높이 리턴
    # print(start, end)
    if start == end:
        return ls[start]

    # 히스토그램 좌, 우 넓이 최대 값 구하기
    mid = (start+end)//2
    left = findArea(ls, start, mid)
    # print('left ', left)
    right = findArea(ls, mid+1, end)
    # print('right ', right)
    # 가운데부터 max_area 찾기
    # print('mid ', mid)
    pl = mid
    pr = mid + 1
    min_height = min(ls[pl], ls[pr])
    max_area = max(left, right, min_height*2)

    # print('start, end',start, end)

    while start < pl or pr < end:
        # print(pl, pr)
        # print('height ', min_height)
        if pr < end and (ls[pl-1] < ls[pr+1] or start == pl) :
            # print((pr-pl+1))
            #오른쪽을 이동
            #그곳에 있는 막대의 높이가 최소임을 확인
            #넓이를 구하고 그것이 최대임을 확인
            pr += 1

            min_height = min(min_height, ls[pr])
            max_area = max(max_area, (pr-pl+1)* min_height)


        else: #(ls[pl] >= ls[pr] and start != pl) or pr >= end
            # print((pr-pl+1))
            pl -= 1

            min_height = min(min_height, ls[pl])
            max_area = max(max_area, (pr-pl+1)* min_height)

#         # print('max area ',max_area)
#
#         # print()
#     # while pl > start and pr < end:
#     #     # print('1 pl : ', pl, 'pr : ', pr)
#     #     # if ls[pl-1] > ls[pr+1]:
#     #     #     pl -= 1
#     #     # else:
#     #     #     pr += 1
#     #     max_pointer = pl if (ls[pl-1] > ls[pr+1]) else pr
#     #     min_height = min(ls[max_pointer], min_height)
#     #     max_area = max(max_area, (pr-pl+1) * min_height)
#     #     if max_pointer == pl:
#     #         pl-=1
#     #     else:
#     #         pr+=1
#     #
#     # while pl > start and pr == end:
#     #     # print('2 pl : ', pl, 'pr : ', pr)
#     #     pl-=1
#     #     min_height = min(ls[pl], min_height)
#     #     max_area = max(max_area, (pr-pl+1) * min_height)
#     #
#     #
#     # while pr < end and pl == start:
#     #     # print('3 pl : ', pl, 'pr : ', pr)
#     #     pr+=1
#     #     min_height = min(ls[pr], min_height)
#     #     max_area = max(max_area, (pr-pl+1) * min_height)
#
#
#
    # print('max_area ' ,max_area)
    # print()
    return max_area




while True:
    data = sys.stdin.readline().split()
    n = int(data[0])
    if n == 0:
        break
    hist = list(map(int, data[1:]))
    max_area = findArea(hist,0,len(hist)-1)
    print(max_area)

# import sys
#
# def max_square(l, r):
#     if l == r:
#         return h[l]
#     else:
#         m = (l+r)//2
#         nl = m
#         nr = m+1
#         nh = min(h[nl], h[nr])
#         tmp = nh*2
#
#         cnt = 2 # nr - nl +1
#         while True:
#             if (h[nl] == 0 or nl ==l) and (h[nr] == 0 or nr== r):
#                 break
#             # left is done
#             elif h[nl] == 0 or nl==l:
#                 if h[nr+1] < nh:
#                     nh = h[nr+1]
#                 nr+=1
#             # right is done
#             elif h[nr] == 0 or nr==r:
#                 if h[nl-1] < nh:
#                     nh = h[nl-1]
#                 nl-=1
#             else:
#                 if h[nl-1] > h[nr+1]:
#                     if h[nl-1] < nh:
#                         nh = h[nl-1]
#                     nl-=1
#                 else:
#                     if h[nr+1] < nh:
#                         nh = h[nr+1]
#                     nr+=1
#             cnt+=1
#             tmp = max(tmp, nh*cnt)
#         return (max(max_square(l,m), max_square(m+1, r), tmp))
# while True:
#     h = list(map(int,sys.stdin.readline().split()))
#     if h[0] == 0 :
#         break
#     print(max_square(1, len(h) -1))