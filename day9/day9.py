#!/usr/bin/env python


def get_adjacent(grid, x, y):
    above = grid[y-1][x] if y > 0 else 10
    below = grid[y+1][x] if y < len(grid) - 1 else 10
    left = grid[y][x-1] if x > 0 else 10
    right = grid[y][x+1] if x < len(grid[0]) - 1 else 10
    return [above, left, right, below]


def explore_basin(grid, x, y, locations: set):
    if (x, y) in locations:
        return

    if grid[y][x] < 9:
        locations.add((x, y))

        if x > 0:
            explore_basin(grid, x-1, y, locations)
        if x < (len(grid[0]) - 1):
            explore_basin(grid, x + 1, y, locations)
        if y > 0:
            explore_basin(grid, x, y-1, locations)
        if y < len(grid) - 1:
            explore_basin(grid, x, y+1, locations)


def find_low_points(grid):
    low_points = []
    ysize = len(grid)
    xsize = len(grid[0])
    for y in range(ysize):
        for x in range(xsize):
            v = grid[y][x]
            if all(v < adj for adj in get_adjacent(grid, x, y)):
                low_points.append((x, y))
    return low_points


def part1(low_points):
    risk_level = 0
    for x, y in low_points:
        risk_level += 1 + grid[y][x]
    print(f'Part1: {risk_level}')


def part2(grid, low_points):
    basin_sizes = []
    for x, y in low_points:
        locations = set()
        explore_basin(grid, x, y, locations)
        basin_sizes.append(len(locations))
    basin_sizes.sort()
    answer = basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]
    print(f'Part2: {answer}')


with open('input', 'r') as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]
    low_points = find_low_points(grid)
    part1(low_points)
    part2(grid, low_points)
