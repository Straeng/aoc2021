#!/usr/bin/env python

from functools import reduce

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
points_p1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points_p2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def closing_char(ch):
    return closing[opening.index(ch)]


with open('input', 'r') as f:
    lines = f.readlines()

    stack = []
    bad = []
    incomplete = []

    for line in lines:
        for ch in line.strip():
            if ch in opening:
                stack.append(ch)
            else:
                o = stack.pop()
                if opening.index(o) != closing.index(ch):
                    bad.append(ch)
                    stack.clear()
                    break

        if len(stack) != 0:
            stack.reverse()
            incomplete.append(stack[:])
            stack.clear()

    completions = [[closing_char(ch) for ch in remaining] for remaining in incomplete]
    scores = [reduce(lambda score, x: score*5 + points_p2[x], seq, 0) for seq in completions]
    scores.sort()

    bad_score = sum([points_p1[ch] for ch in bad])
    mid_score = scores[len(scores)//2]

    print(f'Part1: {bad_score}')
    print(f'Part2: {mid_score}')
