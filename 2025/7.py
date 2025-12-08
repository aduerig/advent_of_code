# forgot to save part 1

# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        grid.append(list(line))


visited = {}
def dfs(grid, pos):
    x, y = pos
    if x < 0 or x >= len(grid[0]):
        return 0
    if y == len(grid) - 1:
        return 1
    if (x, y) in visited:
        return visited[(x, y)]
    saver = 0
    if grid[y][x] == '^':
        saver = dfs(grid, (x + 1, y + 1)) + dfs(grid, (x - 1, y + 1))
    else:
        saver = dfs(grid, (x, y + 1))
    visited[(x, y)] = saver
    return saver

total = dfs(grid, (grid[0].index('S'), 0))
print(total)