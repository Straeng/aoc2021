#!/usr/bin/env python


with open('input', 'r') as f:
    # Part 1
    input_data = list(f.readlines())
    fwd = sum(list(map(lambda x: int(x.split()[1]), filter(lambda x: x.startswith('forward'), input_data))))
    up = sum(list(map(lambda x: int(x.split()[1]), filter(lambda x: x.startswith('up'), input_data))))
    dn = sum(list(map(lambda x: int(x.split()[1]), filter(lambda x: x.startswith('down'), input_data))))

    print(f'Part1: {fwd * (dn-up)}')

    # Part 2
    aim = 0
    depth = 0
    pos = 0
    for line in input_data:
        (cmd, val) = line.split()
        if cmd == 'up':
            aim -= int(val)
        elif cmd == 'down':
            aim += int(val)
        if cmd == 'forward':
            depth += aim*int(val)
            pos += int(val)

    print(f'Part2: {pos*depth}')
