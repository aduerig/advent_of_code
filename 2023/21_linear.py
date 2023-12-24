# https://adventofcode.com/2023
import pathlib
import sys
from collections import deque
from tqdm import tqdm

sys.setrecursionlimit(1000000)

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

queue = deque([(start_pos, 0)])


def is_bad(grid, pos):
    x, y = pos
    # if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
    #     return True
    if x < 0:
        x = len(grid[0]) - (abs(x) % len(grid[0]))
    if y < 0:
        y = len(grid) - (abs(y) % len(grid))
    return grid[y % len(grid)][x % len(grid[0])] == '#'
    # return grid[abs(y) % len(grid)][abs(x) % len(grid[0])] == '#'


def bfs(grid, queue):
    reached = 0
    visited = set()
    while queue:
        pos, left = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if left % 2 == 0:
            reached += 1
        
        if left == 0:
            continue

        x, y = pos
        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if is_bad(grid, (new_x, new_y)):
                continue
            queue.append(((new_x, new_y), left - 1))
    return reached

def rotate(grid):
    return [[grid[y][x] for y in reversed(range(len(grid)))] for x in range(len(grid[0]))]


grid_orientations = [
    grid,
    rotate(grid),
    rotate(rotate(grid)),
    rotate(rotate(rotate(grid))),
]



def bfs_up_right(grid, queue):
    reached = 0
    visited = set()
    while queue:
        pos, left = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if left % 2 == 0:
            reached += 1
        
        if left == 0:
            continue

        x, y = pos
        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if x < 0 or y < 0 or grid[new_y % len(grid)][new_x % len(grid[0])]:
                continue
            queue.append(((new_x, new_y), left - 1))
    return reached


65



ok = {}
results = {}
last = 0
for i in tqdm(range(65, 100, 2)):
    queue = deque([(start_pos, i)])
    results[i] = bfs(grid, queue)

diffs = []
last = 0
for k, v in sorted(results.items()):
    diffs.append(v - last)
    last = v

curr = 1
while curr + 131 < len(diffs):
    start = diffs[curr]
    new = []
    for i in diffs[curr:curr+131]:
        new.append(i - start)
    print(f'    {start}')
    curr += 131
