#import heapq
import math
from collections import namedtuple
from itertools import chain
from dataclasses import dataclass
from queue import PriorityQueue


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

#data = test
with open('input', 'r') as f:
    data = f.read()

risks = [[int(c) for c in line] for line in data.strip().split()]
xmax = len(risks)
ymax = len(risks[0])
print(f'Grid: {xmax}x{ymax}')
Pos = namedtuple('Pos', ['x', 'y'])


@dataclass(order=True)
class Node:
    total: int
    pos: tuple
    risk: int
    prev: object
    visited: bool


def x_iter(grid):
    for x in range(xmax):
        yield x

def y_iter(grid):
    for y in range(ymax):
        yield y

def xy_iter(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            yield x, y


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


nodes = [[Node(total=math.inf, risk=risks[y][x], pos=Pos(x, y), prev=None, visited=False) for x in x_iter(risks)] for y in y_iter(risks)]


n = nodes[ymax-1][xmax-1]
print(f'{n.pos}, {n.risk} {n.total}')

Q = PriorityQueue(ymax*xmax)
#unvisited = list(chain(*nodes))

nodes[0][0].total = 0
nodes[0][0].risk = 0

Q.put(nodes[0][0])

nr_visited = 0
while nr_visited < xmax*ymax:
    cur = Q.get()
    nr_visited += 1
    #print(f'{cur.pos}, R:{cur.risk} T:{cur.total}')
    
    for n in neighbors(cur, nodes):
        if not n.visited and cur.total + n.risk < n.total:
            n.total = cur.total + n.risk
            n.prev = cur
            Q.put(n)

#print(nodes)
n = nodes[ymax-1][xmax-1]
#print(f'{n.pos}, {n.risk} {n.total}')

s = 0
while True:
    print(f'{n.pos}, R:{n.risk} T:{n.total}')
    s += n.risk
    if not n.prev:
        break
    n = n.prev
print(s)
# n = nodes[ymax-1][xmax-1]
# n.prev = None
# print(n)


