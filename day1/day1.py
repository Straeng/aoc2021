#!/usr/bin/env python
from functools import reduce


def count_increments(value, elem):
    if not value:
        return (0, elem)
    inc = 1 if elem > value[1] else 0
    return (value[0] + inc, elem)


with open('input', 'r') as f:
    input_data = list(map(int, f.readlines()))

    sliding_sums = [sum(input_data[i:i+3]) for i in range(len(input_data) - 2)]
    num_increments = reduce(count_increments, input_data, None)[0]
    num_inc_sliding = reduce(count_increments, sliding_sums, None)[0]
    print(f'Part1: {num_increments}')
    print(f'Part2: {num_inc_sliding}')
