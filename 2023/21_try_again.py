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

# blockers = set()
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == '#':
#             blockers.add((x, y))

def bfs(grid, queue):
    visited = set()
    reached = set()
    steps_needed = 0
    og_steps = queue[0][1]
    while queue:
        pos, left = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if left % 2 == 0:
            steps_needed = max(steps_needed, og_steps - left)
            reached.add(pos)

        if left == 0:
            continue

        x, y = pos
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid) or grid[new_y][new_x] == '#':
                continue
            queue.append(((new_x, new_y), left - 1))
    return len(reached)


long_grid = [row * 4 for row in grid]

cache = {}
for step in range(1, 131):
    for y in range(len(grid)):
        cache[(y, step)] = bfs(long_grid, deque([((0, y), step)]))

steps_left = 5000
while True:
    
    y -= 1
    steps_left -= len(grid)
    arrived_at = (0, len())
