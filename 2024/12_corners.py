# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath('12.dat')


grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            grid.append(list(line))

def in_bounds(grid, pos):
    x, y = pos
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    return True

def is_same(grid, pos, letter):
    x, y = pos
    if not in_bounds(grid, (x, y)):
        return False
    return grid[y][x] == letter


visited = set()
def dfs(grid, letter, pos, visited_this_session, sides):
    x, y = pos
    if not in_bounds(grid, (x, y)):
        return False
    if grid[y][x] != letter:
        return False
    if (x, y) in visited:
        return True
    


    visited.add(pos)
    visited_this_session[pos] = True
    
    total_diff = 0
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        new_x, new_y = dx + x, dy + y
        diff = not is_same(grid, (new_x, new_y), letter)
        total_diff += int(diff)
        print(f'Different {x, y=}, {dx, dy=}, {diff}')

    corners = {2: 1, 3: 2, 4: 4}.get(total_diff, 0)
    sides[0] += corners
    if corners:
        print(f'{corners} corners at: {x, y}, {total_diff=}')

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        new_x, new_y = dx + x, dy + y
        dfs(grid, letter, (new_x, new_y), visited_this_session, sides)

    return True


def is_there(grid, pos, letter, do_region, region):
    x, y = pos
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    if grid[y][x] != letter:
        return False
    if do_region and (x, y) not in region:
        return False
    return True


total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        letter = grid[y][x]
        region = {}
        sides = [0]
        dfs(grid, grid[y][x], (x, y), region, sides)
        if region:
            amt = len(region) * sides[0]
            print(f'NEW ABOVE {letter}, {sides}, {amt=}')
            total += amt
print(total)