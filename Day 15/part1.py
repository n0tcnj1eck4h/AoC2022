#!/bin/env python3 
import re

level=2000000

sensors: list[tuple[int, int, int, int]] = []
beacons_x_on_y = set()

def distance(s):
    return abs(s[0] - s[2]) + abs(s[1] - s[3])

with open('input.txt', 'r') as file:
    for line in file:
        e = re.split("[=,:]", line.rstrip())
        sensors.append((int(e[1]), int(e[3]), int(e[5]), int(e[7])))

ranges: list[tuple[int, int]] = []
positions = set()
for sensor in sensors:
    if sensor[3] == level:
        beacons_x_on_y.add(sensor[2])

    m = sensor[0]
    d = distance(sensor)
    h = abs(level - sensor[1])
    w = d - h
    if w > 0:
        x1 = m - w + 1
        x2 = m + w + 1
        ranges.append((x1, x2))
        for x in range(x1, x2 + 1):
            positions.add(x)

for x in beacons_x_on_y:
    positions.remove(x)

print(len(positions))




