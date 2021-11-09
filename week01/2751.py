# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：2751.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-07 오후 3:40 
'''
import sys

def shell(ls):
    n = len(ls)
    h = 1

    # find proper h
    while h < n // 9:
        print(h)
        h = h * 3 + 1
    #print(h)

    # h is step
    while h > 0:
        # sort arr, step h
        for i in range(h, n):
            # j is pre position index
            j = i - h
            # temp is current position element
            temp = ls[i]
            # j is no minus(check all pre index),
            # and pre element is bigger than current element
            while j >= 0 and ls[j] > temp:
                ls[j + h] = ls[j]
                j -= h
            ls[j + h] = temp
        h //= 2

# find middle index, and sort three element
def sort3(a, idx1, idx2, idx3):
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]:
        a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def quick(ls, left, right):
    n = len(ls)
    pl = left       # start index
    pr = right      # last index

    # find middle index, and sort start element, middle element and last element
    m = sort3(ls, pl, (pl + pr) // 2, pr)

    x = ls[m]       # middle element, pivot

    # swap middle element and pre-last element
    ls[m], ls[pr - 1] = ls[pr - 1], ls[m]

    # start, last element is already sorted
    pl += 1
    pr -= 2

    # sort by pivot, smaller than pivot in pl, bigger than pivot in pr
    while pl <= pr:
        # find big in pl
        while ls[pl] < x:
            pl += 1
        # find small in pr
        while ls[pr] > x:
            pr -= 1
        # if exist outliers, swap them
        if pl <= pr:
            ls[pl], ls[pr] = ls[pr], ls[pl]
            pl += 1
            pr -= 1

    # if start index is smaller than pr
    if left < pr:
        quick(ls, left, pr)
    if pl < right:
        quick(ls, pl, right)


def merge(ls):

    def _merge(ls, left, right):
        if left < right:
            center = (left + right) // 2
            _merge(ls, left, center)
            _merge(ls, center+1, right)

            # p is start pointer of buff
            # i is start pointer of ls
            # j is start pointer of buff
            # k is start pointer of ls
            p = j = 0
            i = k = left

            # copy ls to buff
            while i <= center:
                buff[p] = ls[i]
                p+=1
                i+=1

            # p is end pointer of buff
            # i is middle pointer of ls
            # j is start pointer of buff
            # k is start pointer of ls
            # put element to buff, compare ls element and buff element
            while i <= right and j < p:
                if buff[j] <= ls[i]:
                    ls[k] = buff[j]
                    j+=1
                else:
                    ls[k] = ls[i]
                    i+=1
                k+=1

            # j is middle pointer of buff
            # p is end pointer of buff
            # k is middle pointer of ls
            while j < p:
                ls[k] = buff[j]
                k+=1
                j+=1

    n = len(ls)
    buff = [None] * n
    _merge(ls, 0,n-1)

    del buff


def heap(ls):

    def down_heap(ls, left, right):
        temp = ls[left]         # parent element
        parent = left           # parent index

        # repeat if parent have child
        while parent < (right+1) //2 :
            cl = parent*2+1
            cr = cl + 1

            # select big one, from children
            child = cr if (cr <= right and ls[cr] > ls[cl]) else cl

            # if parent is bigger than child
            if temp >= ls[child]:
                break

            # swap parent and child
            ls[parent] = ls[child]
            # this code make heap all element, if exist exchange
            parent = child

        ls[parent] =temp

    n = len(ls)
    # from half length of ls(parent index) make heap
    for i in range((n-1)//2, -1, -1):
        down_heap(ls, i, n-1)

    # ls is heap, so ls[0] is biggest in ls
    # so ls[0] and ls[-1, -2, ,,,, -(n-1)] exchange
    for i in range(n-1, 0, -1):
        ls[0], ls[i] = ls[i], ls[0]
        # make heap
        down_heap(ls, 0, i-1)


n = int(sys.stdin.readline().split()[0])
ls = []
for i in range(n):
    ls.append(int(sys.stdin.readline().split()[0]))

heap(ls)

for i in ls:
    print(i)
