# -*- coding: UTF-8 -*-
'''
@Project ：week02 
@File ：3190.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-15 오후 2:15 
'''

import sys

board = int(sys.stdin.readline().split()[0])
apple_n = int(sys.stdin.readline().split()[0])
apple_list = list(list(map(int, sys.stdin.readline().split())) for i in range(apple_n))
snake_n = int(sys.stdin.readline().split()[0])
snake_list = list( sys.stdin.readline().split() for i in range(snake_n))

# print(board)
# print(apple_n)
# print(apple_list)
# print(snake_n)
# print(snake_list)

def move(direction , x, y):
    # 오른쪽으로 돌면 +1, 왼쪽으로 돌면 -1
    nx = [x,x+1,x,x-1]
    ny = [y+1, y, y-1, y]
    return [nx[direction%4], ny[direction%4]]

direction = 0
snake = [[0,0]]

# print(move(direction, snake[0][0], snake[0][1]))
# direction-=1
# print(move(direction, snake[0][0], snake[0][1]))
# direction-=1
# print(move(direction, snake[0][0], snake[0][1]))
# direction-=1
# print(move(direction, snake[0][0], snake[0][1]))

def check_boundary(x,y):
    if x >= board or y >= board or x < 0 or y <0:
        return False
    else:
        return True

time = 0



while True:
    # """
    #     for test
    # """
    # matrix = [['□'] * board for i in range(board)]
    # for s in snake:
    #     matrix[s[0]][s[1]] = '■'
    # for a in apple_list:
    #     matrix[a[0]-1][a[1]-1] = '＠'
    # for i in range(len(matrix)):
    #     print(matrix[i])

    # print('time : ', time)
    # print('snake : ', snake)
    # print('direction : ', direction)
    # print('snake_list : ', snake_list)
    # print('apple_list : ', apple_list)

    # check direction
    if snake_list and time == int(snake_list[0][0]):
        if snake_list[0][1] == 'D':
            direction+=1
        elif snake_list[0][1] =='L':
            direction-=1
        # remove direction
        snake_list.remove(snake_list[0])

    # move
    head = snake[-1]
    move_x, move_y = move(direction, head[0], head[1])

    # check boundary
    check = check_boundary(move_x,move_y)
    if check == False:
        break

    # check snake
    if [move_x, move_y] in snake:
        break

    # check apple and remake snake
    if [move_x+1,move_y+1] in apple_list:
        snake.append([move_x, move_y])
        # remove apple
        apple_list.remove([move_x+1,move_y+1])
    else:
        snake.append([move_x, move_y])
        # remove tail
        snake.remove(snake[0])

    time+=1

    # print()

print(time+1)