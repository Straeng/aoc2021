#!/usr/bin/env python
from collections import Counter


with open('input', 'r') as f:
    data = f.read()

template, rule_input = data.strip().split('\n\n')
rules = {k: v for k, v in [x.strip().split(' -> ') for x in rule_input.split('\n')]}


def count_most_and_least(iterations):
    rule_counts = Counter({r: template.count(r) for r in rules})
    char_count = Counter(template)

    for _ in range(iterations):
        updates = Counter({k: 0 for k in rules})
        for k, v in rules.items():

            n = rule_counts[k]
            a = k[0]+v
            b = v+k[1]

            updates[k] -= n
            updates[a] += n
            updates[b] += n

            char_count[v] += n

        rule_counts = rule_counts + updates

    most_common_count = char_count.most_common(1)[0][1]
    least_common_count = char_count.most_common()[-1][1]

    return most_common_count - least_common_count


print(f'Part 1: {count_most_and_least(10)}')
print(f'Part 2: {count_most_and_least(40)}')