#!/bin/env python3

# assuming the positions don't go into negatives 
max_x = 0
max_y = 0
min_x = 100000000

lines: list[list[tuple[int, int]]] = []

with open('input.txt') as file:
    for line in file:
        vertices = line.rstrip().split(' -> ')
        tmp = []
        for vertex in vertices:
            pos = vertex.split(',')
            pos = (int(pos[0]), int(pos[1]))
            tmp.append(pos)
            max_x = max(max_x, pos[0])
            max_y = max(max_y, pos[1])
            min_x = min(min_x, pos[0])
        lines.append(tmp)

min_x = 0 #500 - max_y // 2
max_x = 500 + max_y + 1

board = [[' ' for _ in range(max_x - min_x + 2)] for _ in range(max_y + 3)]
board[0][500 - min_x] = '+'
floor = max_y + 1 

for line in lines:
    for i in range(len(line) - 1):
        for x in range(line[i][0], line[i+1][0] + 1):
            for y in range(line[i][1], line[i+1][1] + 1):
                board[y][x - min_x] = '#'
        for x in range(line[i+1][0], line[i][0] + 1):
            for y in range(line[i+1][1], line[i][1] + 1):
                board[y][x - min_x] = '#'

resting_grains_of_sand = 0
while not board[0][500 - min_x] == 'o':
    x = 500
    y = 0
    while True:
        if y == floor:
            resting_grains_of_sand += 1
            board[y][x - min_x] = 'o'
            break
        elif board[y + 1][x - min_x] == ' ':
            y += 1
        elif board[y + 1][x - min_x - 1] == ' ':
            y += 1
            x -= 1
        elif board[y + 1][x - min_x + 1] == ' ':
            y += 1
            x += 1
        else:
            resting_grains_of_sand += 1
            board[y][x - min_x] = 'o'
            break


print(resting_grains_of_sand)

