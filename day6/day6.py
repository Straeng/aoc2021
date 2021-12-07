#!/usr/bin/env python


def fish_after_days(days, starting_population):
    d = [fish.count(i) for i in range(9)]
    for _ in range(days):
        d1 = [d[1], d[2], d[3], d[4], d[5], d[6], d[0] + d[7], d[8], d[0]]
        d = d1
    return sum(d)


def part1(fish):
    for _ in range(80):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)


with open('input', 'r') as f:
    fish = list(map(int, f.read().split(',')))

    print(f'Part1: {part1(fish[:])}')
    print(f'Part2: {fish_after_days(256, fish[:])}')
