#!/usr/bin/env python

testdata = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

inputdata = """
re-js
qx-CG
start-js
start-bj
qx-ak
js-bj
ak-re
CG-ak
js-CG
bj-re
ak-lg
lg-CG
qx-re
WP-ak
WP-end
re-lg
end-ak
WP-re
bj-CG
qx-start
bj-WP
JG-lg
end-lg
lg-iw
"""


data = inputdata


def cave_map():
    cave_map = {}
    for line in data.split():
        src, dst, *_ = line.split('-')
        cave_map.setdefault(src, set()).add(dst)
        cave_map.setdefault(dst, set()).add(src)
    return cave_map


def path_explorer(node, cave_map, path, results, allow_small_twice):

    if node.islower() and node in path:
        if node == allow_small_twice:
            allow_small_twice = ''
        else:
            return

    if node == 'start' and len(path) > 0:
        return

    path.append(node)

    if node == 'end':
        results.add(','.join(path))
        return

    for connected_node in cave_map[node]:
        path_explorer(connected_node, cave_map, path[:], results, allow_small_twice)
        if connected_node.islower() and allow_small_twice is True:
            path_explorer(connected_node, cave_map, path[:], results, connected_node)


# Part 1:
results = set()
path_explorer('start', cave_map(), [], results, allow_small_twice=False)
print(f'Part1: {len(results)}')

# Part 2:
results = set()
path_explorer('start', cave_map(), [], results, allow_small_twice=True)
print(f'Part2: {len(results)}')
