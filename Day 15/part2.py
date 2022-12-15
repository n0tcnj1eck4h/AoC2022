#!/bin/env python3 
import re

class DONTCAREEXCEPTION(Exception):
    pass

sensors: list[tuple[int, int, int, int]] = []
search_space = 4000000

def distance(s):
    return abs(s[0] - s[2]) + abs(s[1] - s[3])

with open('input.txt', 'r') as file:
    for line in file:
        e = re.split("[=,:]", line.rstrip())
        sensors.append((int(e[1]), int(e[3]), int(e[5]), int(e[7])))

for level in range(0, search_space + 1):
    positions = 0
    try:
        for sensor in sensors:
            if sensor[1] == level and sensor[0] >= 0 and sensor[0] <= search_space:
                positions |= 1 << sensor[0]
            if sensor[3] == level and sensor[2] >= 0 and sensor[2] <= search_space:
                positions |= 1 << sensor[2]
            m = sensor[0]
            d = distance(sensor)
            h = abs(level - sensor[1])
            w = d - h
            if w >= 0:
                x1 = max(m - w + 1, 0)
                x2 = min(m + w + 1, search_space)
                if x1 <= 0 and x2 >= search_space:
                    raise DONTCAREEXCEPTION
                positions |= ((1 << (x2 + 1)) - 1) & ~((1 << x1) - 1)

    except DONTCAREEXCEPTION:
        pass

    if level % 100 == 0:
        print(level, '/', search_space)
    #print(bin(positions).rjust(40))

    if not (positions + 1) & (1 << (search_space + 1)):
        print('Found a layer')
        for x in range(0, search_space + 1):
            if positions & (1 << x) == 0:
                print(f'Empty space found on {x - 1}, {level} frequency is {(x - 1) * 4000000 + level}')





                






