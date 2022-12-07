#!/usr/bin/python3

stack_lines: list[str] = []
instructions: list[tuple[int, int, int]] = []

with open('input.txt', mode='r') as file:
    for line in file:
        if line.lstrip().startswith('['):
            stack_lines.append(line)
        elif line.startswith('move'):
            e = line.split()
            instructions.append((int(e[1]), int(e[3]) - 1, int(e[5]) - 1))


stacks: list[list[str]] = []
for i in range(1, len(stack_lines[0]), 4):
    stacks.append([])
    for line in reversed(stack_lines):
        if line[i] != ' ':
            stacks[len(stacks) - 1].append(line[i])

for count, src, dst in instructions:
    stacks[dst] += stacks[src][-count:]
    stacks[src] = stacks[src][:-count]

print(''.join(list(map(lambda x: x[-1], stacks))))
