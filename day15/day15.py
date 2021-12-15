import math
from itertools import chain
from dataclasses import dataclass
from queue import PriorityQueue


@dataclass(order=True)
class Node:
    total: int
    pos: tuple
    risk: int
    prev: object
    visited: bool


def neighbors(node, nodes):
    n = []
    x, y = node.pos
    if x > 0:
        n.append(nodes[y][x-1])
    if y > 0:
        n.append(nodes[y-1][x])
    if x < len(nodes) - 1:
        n.append(nodes[y][x+1])
    if y < len(nodes[0]) - 1:
        n.append(nodes[y+1][x])
    return n


def dijkstra_eller_nåt(risk_grid):
    xmax = len(risk_grid)
    ymax = len(risk_grid[0])
    nodes = [[Node(math.inf, (x, y), risk_grid[y][x], None, False) for x in range(xmax)] for y in range(ymax)]

    Q = PriorityQueue(ymax*xmax)

    nodes[0][0].total = 0
    nodes[0][0].risk = 0

    Q.put(nodes[0][0])

    while not Q.empty():
        cur = Q.get()

        for n in neighbors(cur, nodes):
            if not n.visited and cur.total + n.risk < n.total:
                n.total = cur.total + n.risk
                n.prev = cur
                Q.put(n)

    n = nodes[ymax-1][xmax-1]
    return n.total


def wow_such_risk(risks):
    def incwrap(v, a):
        v += a
        return v if v <= 9 else v - 9

    more_risks = []
    for cols in risks:
        more_risks.append(list(chain(*[list(map(lambda v: incwrap(v, a), cols)) for a in range(5)])))

    even_more_risks = []
    for a in range(5):
        for row in more_risks:
            even_more_risks.append(list(map(lambda v: incwrap(v, a), row)))
    return even_more_risks


test = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

# data = test
with open('input', 'r') as f:
    data = f.read()

risks = [[int(c) for c in line] for line in data.strip().split()]

print(f'Part 1: {dijkstra_eller_nåt(risks)}')

many_risks = wow_such_risk(risks)
print(f'Part 2: {dijkstra_eller_nåt(many_risks)}')
