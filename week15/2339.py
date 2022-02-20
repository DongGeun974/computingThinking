# -*- coding: UTF-8 -*-
'''
@Project ：week14 
@File ：2339.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-12 오후 10:44 
'''

import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

def cut(sx, sy, ex, ey, dir):
    temp = 0
    v =[]
    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            if(arr[i][j] == 1):
                v.append([i,j])
            else:
                temp+=arr[i][j]
    if temp == 0:
        return 0
    elif temp==2 and len(v)==0:
        return 1
    elif len(v)==0:
        return 0

    result = 0
    if dir == 0:
        for trash in v:
            x, y = trash
            tmp = 0
            for i in range(sx,ex+1):
                tmp+=arr[i][y]
            if tmp==1:
                result+=cut(sx,sy,ex,y-1,1)*cut(sx,y+1,ex,ey,1)
    if dir == 1:
        for trash in v:
            x, y = trash
            tmp = 0
            for i in range(sy,ey+1):
                tmp+=arr[x][i]
            if tmp==1:
                result+=cut(sx,sy,x-1,ey,0)*cut(x+1,sy,ex,ey,0)
    return result

answer += cut(0,0,n-1,n-1,0)
answer += cut(0,0,n-1,n-1,1)

if answer==0:
    print(-1)
else:
    print(answer)