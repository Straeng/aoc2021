#!/usr/bin/env python


def most_common(pos, data, eqval):
    n1 = 0
    n0 = 0
    for line in data:
        if line[pos] == '1':
            n1 += 1
        else:
            n0 += 1
    if n1 > n0:
        return '1'
    elif n0 > n1:
        return '0'
    else:
        return eqval


def part1(input_data):
    n = len(input_data[0])
    nr = len(input_data)
    gamma = ''
    for i in range(n):
        n1 = 0
        for line in input_data:
            if line[i] == '1':
                n1 += 1
            else:
                pass
        if n1 > nr/2:
            gamma += '1'
        else:
            gamma += '0'
    
    epsilon = ''.join(['0' if c == '1' else '1' for c in gamma])
    gammav = int(gamma, 2)
    epsilonv = int(epsilon, 2)
    return gammav*epsilonv


def part2(input_data):
    n = len(input_data[0])

    oxygen_data = input_data[:]
    co2_data = input_data[:]
    for i in range(n):

        vo = most_common(i, oxygen_data, '1')
        vc = most_common(i, co2_data, '1')

        if len(oxygen_data) > 1:
            oxygen_data = list(filter(lambda strval: strval[i] == vo, oxygen_data))
        if len(co2_data) > 1:    
            co2_data = list(filter(lambda strval: strval[i] != vc, co2_data))

    oxygen = int(oxygen_data[0], 2)
    co2 = int(co2_data[0], 2)
    return oxygen*co2

with open('input', 'r') as f:
    input_data = [s.strip() for s in f.readlines()]
    
    print(f'Part1: {part1(input_data)}')
    print(f'Part2: {part2(input_data)}')
