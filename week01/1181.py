# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：1181.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 10:21 
'''
import sys

max= 0

# input n
n = int(sys.stdin.readline().split()[0])
ls= []

# input data and find max of length
for i in range(n):
    temp = sys.stdin.readline().split()[0]
    ls.append(temp)
    max = max if max > len(temp) else len(temp)

ls.sort()

# print ls order by length
for i in range(max+1):
    for j in range(len(ls)):
        if len(ls[j]) == i:
            if i == 1 :
                print(ls[j])
            # for deduplication
            elif ls[j-1] != ls[j]:
                print(ls[j])


# ls=list(set(ls))
#
# ls.sort()
# ls.sort(key=len)
#
# print(ls)
