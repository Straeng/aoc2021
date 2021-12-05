#!/usr/bin/env python

from functools import reduce
import itertools
import re


def omnidirectional_range(a, b):
    return range(a, b+1) if a <= b else range(a, b-1, -1)


def get_populated_grid(grid_size, data, allow_diagonal=False):
    grid = [[0]*grid_size for i in range(grid_size)]
    point_gen = (values[i:i+4] for i in range(0, len(values), 4))

    for x1, y1, x2, y2 in point_gen:
        xstart, xend = sorted([x1, x2])
        ystart, yend = sorted([y1, y2])

        if xstart == xend:  # Vertical
            for y in range(ystart, yend+1):
                grid[xstart][y] += 1
        elif ystart == yend:  # Horizontal
            for x in range(xstart, xend+1):
                grid[x][ystart] += 1
        elif allow_diagonal:
            for x, y in zip(omnidirectional_range(x1, x2), omnidirectional_range(y1, y2)):
                grid[x][y] += 1

    return grid


def count_greater_than_one(grid):
    def accumulator(count, x):
        return count+1 if x > 1 else count
    return reduce(accumulator, itertools.chain(*grid), 0)


with open('input', 'r') as f:
    str_values = list(filter(lambda s: s.isnumeric(), re.split(',| |\n', f.read())))
    values = list(map(int, str_values))
    grid_size = reduce(max, values, 0) + 1

    p1_grid = get_populated_grid(grid_size, values)
    p2_grid = get_populated_grid(grid_size, values, allow_diagonal=True)

    print(f'Part1: {count_greater_than_one(p1_grid)}')
    print(f'Part2: {count_greater_than_one(p2_grid)}')
