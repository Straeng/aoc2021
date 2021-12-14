#!/usr/bin/env python
from itertools import chain
from functools import reduce


testdata = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def pp(grid):
    import numpy as np
    print(np.matrix(grid))


def create_paper(coords):
    size_x = max(map(lambda c: c[0], coords)) + 1
    size_y = max(map(lambda c: c[1], coords)) + 1
    paper = [[0]*size_x for _ in range(size_y)]
    for x, y in coords:
        paper[y][x] = 1
    return paper


def count_dots(grid):
    return reduce(lambda n, x: n + 1 if x > 0 else n, chain(*grid), 0)


def merge(a, b):
    tuples = [zip(a_, b_) for a_, b_ in zip(a, b)]
    return [list(map(lambda x: x[0]|x[1], row)) for row in tuples]


def fold_y(grid, y):
    top = grid[:y]
    bottom = grid[y:]
    bottom.reverse()
    return merge(top, bottom)


def fold_x(grid, x):
    left = [row[:x] for row in grid]
    right = [reversed(row[x+1:]) for row in grid]
    return merge(left, right)


def follow_instructions(paper, instructions):
    for instr in instructions.split('\n'):
        axis, pos = instr[11:].split('=')
        if axis == 'x':
            paper = fold_x(paper, int(pos))
        else:
            paper = fold_y(paper, int(pos))
    return paper


def render(paper):
    print('\nPart 2\n---------------------------------------')
    for row in paper:
        print(''.join(map(lambda x: '#' if x else ' ', row)))
    print('---------------------------------------')


#data = testdata
with open('input', 'r') as f:
    data = f.read()

coord_input, instructions = data.split("\n\n")

coords = [tuple(map(int, line.split(','))) for line in coord_input.split()]
paper = create_paper(coords)


part1 = fold_x(paper, 655)
print(f'Part 1: {count_dots(part1)}')

part2 = follow_instructions(paper, instructions)
render(part2)
