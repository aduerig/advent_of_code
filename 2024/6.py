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

        new_line = []
        if line:
            for char in line:
                new_line.append(char)
        grid.append(new_line)

dirs = {
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
}

n_dir = {
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
}


def in_bounds(x, y):
    return not (x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid))

start_pos = None
start_dir = None
for y in range(len(grid)):
    for x in range(len(grid[0])):
        for thing, d in dirs.items():
            if thing == grid[y][x]:
                start_pos = (x, y)
                start_dir = d


def does_loop(grid):
    loop_cache = {}
    pos = start_pos
    dir = start_dir
    while True:
        if (dir, pos) in loop_cache:
            return True
        loop_cache[(dir, pos)] = True
        n_x, n_y = pos[0] + dir[0], pos[1] + dir[1]
        if not in_bounds(n_x, n_y):
            return False
        ele = grid[n_y][n_x]
        if ele == '#':
            dir = n_dir[dir]
        else:
            pos = n_x, n_y


total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x, y) != start_pos and grid[y][x] == '.':
            grid[y][x] = '#'
            if does_loop(grid):
                total += 1
            grid[y][x] = '.'
print(total)
