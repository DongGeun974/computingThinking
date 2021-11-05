# -*- coding: UTF-8 -*-
'''
@Project ：week01 
@File ：9020.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-05 오후 2:41 
'''


import sys

# only prime number in list
prime = list(range(2, 10001))
# print(prime)
for i in prime:
    for j in prime[prime.index(i)+1:]:
        if j%i == 0:
            # print(j, prime.index(j))
            prime.remove(j)
# print(prime)

testCase = int(sys.stdin.readline().split()[0])

for _ in range(testCase):
    data = int(sys.stdin.readline().split()[0])

    half = int(data / 2)

    # print(data , half)
    if half in prime:
        print(half , half)
    else:
        # idea from jihun Kim in jungle
        for i in range(1, half):
            if (half - i) in prime and (half + i) in prime:
                print((half - i), (half + i))
                break


