#!/usr/bin/env python
import re


def parse_boards(lines):
    for i in range(0, len(lines), 6):
        yield [[int(n) for n in row.strip().split()] for row in lines[i:i+5]]



class Board:

    def __init__(self, numbers):
        self._numbers = numbers
        self._marks = [[False]*5 for i in range(5)]

    def mark(self, n):
        for i, row in enumerate(self._numbers):
            try:
                j = row.index(n)
                self._marks[i][j] = True
            except:
                pass

    def check(self):
        for i in range(5):
            row = self._marks[i]
            col = [row[i] for row in self._marks]
            if all(row) or all(col):
                return True
        return False

    def score(self):
        s = 0
        for i in range(5):
            for j in range(5):
                if not self._marks[i][j]:
                    s += self._numbers[i][j]
        return s


if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()
        draw_order = [int(n) for n in lines[0].split(',')]
        boards = [Board(b) for b in parse_boards(lines[2:])]


        winners = []
        for nbr in draw_order:
            for n, board in enumerate(boards):
                if board.check():
                    continue

                board.mark(nbr)

                if board.check():
                    winners.append(board.score()*nbr)
    
    print(f'Part1: First win score = {winners[0]}')
    print(f'Part2: Last win score = {winners[-1]}')
