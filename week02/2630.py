# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：2630.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-12 오전 12:20 
'''

# input
import sys

n = int(sys.stdin.readline().split()[0])
matrix = list(list(map(int, sys.stdin.readline().split())) for i in range(n))

# _00 = []
# _01 = []
# _10 = []
# _11 = []
# for i in range(len(matrix)):
#     if i < n//2:
#         _00.append(matrix[i][:n//2])
#         _01.append(matrix[i][n // 2:])
#     else:
#         _10.append(matrix[i][:n // 2])
#         _11.append(matrix[i][n // 2:])
# for i in _00:
#     print(i)
# print()
# for i in _01:
#     print(i)
# print()
# for i in _10:
#     print(i)
# print()
# for i in _11:
#     print(i)
# print()



# print(sum(map(sum,matrix)))

white = 0
blue = 0
def divideConquer(m, n):
    # print(m)
    # print(sum(map(sum,m)))
    # print(n)
    # print( sum(map(sum,m)) == n*n)
    global white,blue
    if sum(map(sum,m)) == (n*n):
        # print('blue')
        blue+=1
        return
    if sum(map(sum,m)) == 0:
        # print('white')
        white+=1
        return

    _00 = []
    _01 = []
    _10 = []
    _11 = []
    for i in range(len(m)):
        if i < n // 2:
            _00.append(m[i][:n // 2])
            _01.append(m[i][n // 2:])
        else:
            _10.append(m[i][:n // 2])
            _11.append(m[i][n // 2:])

    divideConquer(_00, n//2)
    divideConquer(_01, n//2)
    divideConquer(_10, n // 2)
    divideConquer(_11, n // 2)

divideConquer(matrix,n)

print(white)
print(blue)