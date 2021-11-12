# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：9663.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-06 오후 7:14 
'''
import sys

n = int(sys.stdin.readline().split()[0])

pos = [0]*n         # column
flag_a = [False]*n  # row
flag_b = [False]*(n*2 -1) # diagonal1
flag_c = [False]*(n*2 -1) # diagonal2

# number of all case can set queen
cnt = 0

# set i column queen
def set (i, n) :
    global cnt
    for j in range(n):                          # run all row
        if (    not flag_a[j]                   # check row
                and not flag_b[i+j]             # check diagonal1
                and not flag_c[i-j +(n-1)]):    # check diagonal1
            """
                      i                   i
                      0 1 2 3           0 1 2 3
                       
                j 0   0 1 2 3     j 0   3 4 5 6
                  1   1 2 3 4       1   2 3 4 5
                  2   2 3 4 5       2   1 2 3 4
                  3   3 4 5 6       3   0 1 2 3
            """
            pos[i]=j                            # set column

            # i is column, so i == n-1 is last column
            # this case is n queens is set
            if i == n-1:
                # put(n)
                cnt = cnt +1
                print(pos)

            # i != n-1 is not last column
            else:
                # set row, diagonals
                flag_a[j] = flag_b[j+i] = flag_c[i-j + (n-1)] = True
                # call next column
                set(i+1, n)
                # put row, diagonals
                flag_a[j] = flag_b[j+i] = flag_c[i-j + (n-1)] = False
        # else:
        #     print(pos)

set(0,n)
print(cnt)

