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

board = [[' ' for _ in range(max_x - min_x + 2)] for _ in range(max_y + 2)]
board[0][500 - min_x] = '+'

for line in lines:
    for i in range(len(line) - 1):
        for x in range(line[i][0], line[i+1][0] + 1):
            for y in range(line[i][1], line[i+1][1] + 1):
                board[y][x - min_x] = '#'
        for x in range(line[i+1][0], line[i][0] + 1):
            for y in range(line[i+1][1], line[i][1] + 1):
                board[y][x - min_x] = '#'


sand_has_fallen_into_the_abyss = False
resting_grains_of_sand = 0
while not sand_has_fallen_into_the_abyss:
    x = 500
    y = 0
    while True:
        if y == max_y:
            sand_has_fallen_into_the_abyss = True
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

for line in board:
    print(' '.join(line))

print(resting_grains_of_sand)

