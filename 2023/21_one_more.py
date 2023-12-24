# https://adventofcode.com/2023
import pathlib
import sys
from collections import deque

sys.setrecursionlimit(10000000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath('21.dat')

grid = []
with open(data_file) as f:
    for y, line in enumerate(f.read().splitlines()):
        grid.append(list(line))

        if 'S' in grid[-1]:
            start_pos = (grid[-1].index('S'), y)
            grid[-1][start_pos[0]] = '.'

def make_blockers(grid):
    blockers = set()
    for y in range(-1, len(grid)+1):
        for x in range(-1, len(grid[0]) + 1):
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '#':
                blockers.add((x, y))
    return blockers


def rotate(grid):
    return [[grid[y][x] for y in reversed(range(len(grid)))] for x in range(len(grid[0]))]


grid_orientations = [
    grid,
    rotate(grid),
    rotate(rotate(grid)),
    rotate(rotate(rotate(grid))),
]

def best_starter(grid, blockers, queue):
    visited = set()
    reached = set()
    steps_needed = 0
    while queue:
        pos, taken = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if taken % 2 == 0:
            steps_needed = max(steps_needed, taken)
            reached.add(pos)
        else:
            if pos[1] == len(grid) - 1:
                return taken + 1, (pos[0], 0)

        x, y = pos
        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (new_x, new_y) in blockers:
                continue
            queue.append(((new_x, new_y), taken + 1))
    return steps_needed, len(reached)

total_eles = len(grid) * len(grid[0])
def bfs_needed(blockers, queue):
    visited = set()
    reached = set()
    steps_needed = 0
    while queue:
        pos, taken = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if taken % 2 == 0:
            steps_needed = max(steps_needed, taken)
            reached.add(pos)

        x, y = pos
        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (new_x, new_y) in blockers:
                continue
            queue.append(((new_x, new_y), taken + 1))
    return steps_needed, len(reached)

total = 0
for index, grid in enumerate(grid_orientations):
    print_blue(f'==== ORIENTATION {index} ====')

    blockers = make_blockers(grid)

    cache = {}
    for x in range(1, len(grid[0]), 2):
        pos = (x, 0)
        needed, reached = bfs_needed(blockers, deque([(pos, 0)]))
        cache[pos] = (needed, reached)
        print(f'{pos}, {needed=}, {reached=}')

    steps_taken_already, start = best_starter(grid, blockers, deque([(start_pos, 0)]))
    meta_x = 0
    steps_to_this_x = 5000 - steps_taken_already

    print_yellow(f'Took {steps_taken_already} to get to {red("X")}, have {steps_to_this_x} left')
    for y, row in enumerate(grid):
        to_print = []
        for x, char in enumerate(row):
            if (x, y) == start:
                to_print.append(red('X'))
            else:
                to_print.append(char)
        print(''.join(to_print))

    total = cache[start][1]
    # exit()

    while steps_to_this_x > 0:
        steps_left = steps_to_this_x
        while True:
            needed, reached = cache[start]
            if steps_left < needed:
                # total += steps_left // 2
                break
            total += reached
            steps_left -= len(grid[0])

        steps_to_this_x -= len(grid[0])
        meta_x += 1
        start = (1, 0)

print(total)

# 25000000 - 16733044
# 8266956

# 0.668697
# 0.66932176


# 2375319
# 16733044

# steps_left = 5000
# while True:
    
#     y -= 1
#     steps_left -= len(grid)
#     arrived_at = (0, len())
