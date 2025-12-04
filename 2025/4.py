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
        grid.append([x for x in line])

total = 0


dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]
def get_ele(grid, x, y):
    if y < 0 or y >= len(grid):
        return '.'
    if x < 0 or x >= len(grid[0]):
        return '.'
    return grid[y][x]


has_removed = True
while has_removed:
    has_removed = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '@':
                continue
            touching = 0
            for dx, dy in dirs:
                touching += int(get_ele(grid, x+dx, y+dy) == '@')
            if touching < 4:
                has_removed = True
                grid[y][x] = '.'
                total += 1

print(total)


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         grid.append([x for x in line])

# total = 0


# dirs = [
#     (1, 0),
#     (0, 1),
#     (-1, 0),
#     (0, -1),
#     (1, 1),
#     (1, -1),
#     (-1, 1),
#     (-1, -1),
# ]
# def get_ele(grid, x, y):
#     if y < 0 or y >= len(grid):
#         return '.'
#     if x < 0 or x >= len(grid[0]):
#         return '.'
#     return grid[y][x]


# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] != '@':
#             continue
#         touching = 0
#         for dx, dy in dirs:
#             touching += int(get_ele(grid, x+dx, y+dy) == '@')
#         if touching < 4:
#             total += 1


# print(total)