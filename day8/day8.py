#!/usr/bin/env python
from collections import Counter


def part1():
    with open('input', 'r') as f:
        lines = f.readlines()

        n = 0
        for line in lines:
            for x in line.split('|')[1].split():
                if len(x) in [2, 3, 4, 7]:
                    n += 1
        return n


def remove_chars(pattern, remove):
    for c in remove:
        pattern = pattern.replace(c, '')
    return pattern


def filter_char_count(patterns, count):
    all_chars = ''.join(patterns)
    counts = Counter([c for c in all_chars])
    return ''.join([k for k, v in counts.items() if v == count])


def figure_out_segments(clues):
    clues_by_length = {}
    for clue in clues.split():
        clues_by_length.setdefault(len(clue), []).append(clue)

    # Should only be one of these
    cf = clues_by_length[2][0]
    acf = clues_by_length[3][0]
    bcdf = clues_by_length[4][0]
    abcdefg = clues_by_length[7][0]

    a = remove_chars(acf, cf)

    # len5
    # 2:   a cde g
    # 3:   a cd fg
    # 5:   ab d fg
    # ------------
    #       b  e
    be = filter_char_count(clues_by_length[5], count=1)
    bd = remove_chars(bcdf, cf)

    e = remove_chars(be, bd)
    d = remove_chars(bd, be)
    b = remove_chars(be, e)
    g = remove_chars(abcdefg, b+d+e+acf)

    # len6
    # 0:    abc efg
    # 6:    ab defg
    # 9:    abcd fg
    # -------------
    #         cde
    cde = filter_char_count(clues_by_length[6], count=2)

    c = remove_chars(cde, e+d)
    f = remove_chars(cf, c)
    return {a: 'a', b: 'b', c: 'c', d: 'd', e: 'e', f: 'f', g: 'g'}


digit_map = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']


def decode_digits(patterns, table):
    digits = []
    for pattern in patterns:
        segments = [table[c] for c in pattern]
        segments.sort()
        digits.append(digit_map.index(''.join(segments)))
    return digits


def part2():
    with open('input', 'r') as f:
        records = f.readlines()

        tot = 0
        for r in records:
            clues, patterns = r.split('|')
            table = figure_out_segments(clues)
            digits = decode_digits(patterns.split(), table)
            tot += int(''.join([str(d) for d in digits]))
        return tot


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
