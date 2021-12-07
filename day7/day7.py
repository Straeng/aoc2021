#!/usr/bin/env python


with open('input', 'r') as f:
    pos = list(map(int, f.read().split(',')))
    # pos = [16,1,2,0,4,2,7,1,2,14]

    pos.sort()
    median = pos[len(pos)//2]
    dist_med = list(map(lambda p: abs(p - median), pos))
    print(f'Part1: {sum(dist_med)}')

    avg = sum(pos)//len(pos)
    dist_avg = list(map(lambda p: abs(p - avg), pos))
    cost = [sum(range(1, d+1)) for d in dist_avg]
    print(f'Part2: {sum(cost)}')
