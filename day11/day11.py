#!/usr/bin/env python


class Grid:

    def __init__(self, lines):
        self._grid = [[int(c) for c in line.strip()] for line in lines]

    def size(self):
        return (len(self._grid[0]), len(self._grid))

    def coords(self):
        xsz, ysz = self.size()
        for y in range(ysz):
            for x in range(xsz):
                yield (x, y)

    def is_outside(self, x, y):
        xsz, ysz = self.size()
        return x < 0 or y < 0 or x >= xsz or y >= ysz

    def inc_all(self):
        for x, y in self.coords():
            self._grid[y][x] += 1

    def inc_adj(self, x, y):
        for y1 in range(y-1, y+2):
            for x1 in range(x-1, x+2):
                if (y1 == y and x1 == x) or self.is_outside(x1, y1):
                    continue
                self._grid[y1][x1] += 1

    def will_flash(self, x, y):
        return self._grid[y][x] > 9

    def reset(self, coords):
        for x, y in coords:
            self._grid[y][x] = 0


def check_flashes(grid):
    has_flashed = []

    while True:
        new_flashes = 0
        for x, y in grid.coords():
            if (x, y) in has_flashed:
                continue

            if grid.will_flash(x, y):
                has_flashed.append((x, y))
                grid.inc_adj(x, y)
                new_flashes += 1
        if new_flashes == 0:
            break

    grid.reset(has_flashed)
    return len(has_flashed)


with open('input', 'r') as f:
    lines = f.readlines()
    grid = Grid(lines)

    # Part 1
    flashes = 0
    for step in range(100):
        grid.inc_all()
        flashes += check_flashes(grid)
    print(f'Part1: {flashes}')

    # Part 2
    grid = Grid(lines)
    step = 1
    while True:
        grid.inc_all()
        if check_flashes(grid) == 100:
            print(f'Part2: {step}')
            break
        step += 1
