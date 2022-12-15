#!/bin/env python3 
import re

sensors: list[tuple[int, int, int, int]] = []
search_space = 4000000

def distance(s):
    return abs(s[0] - s[2]) + abs(s[1] - s[3])

def checkpos(x, y):
    for s in sensors:
        if abs(x - s[0]) + abs(y - s[1]) <= distance(s):
            return False
    return True

with open('input.txt', 'r') as file:
    for line in file:
        e = re.split("[=,:]", line.rstrip())
        sensors.append((int(e[1]), int(e[3]), int(e[5]), int(e[7])))



for sensor in sensors:
    d = distance(sensor)
    x = sensor[0]
    y = sensor[1] + d + 1
    dx = 1
    dy = -1
    #print('Sensor', sensor, d)
    for _ in range(d * 8):
        if x >= 0 and x <= search_space and y >= 0 and y <= search_space and checkpos(x, y):
            print(x, y, x * 4000000 + y)
            exit()

        #print(x, y)
        x += dx
        y += dy

        if x > sensor[0] + d:
            dx = -1

        if x < sensor[0] - d:
            dx = 1

        if y > sensor[1] + d:
            dy = -1

        if y < sensor[1] - d:
            dy = 1







