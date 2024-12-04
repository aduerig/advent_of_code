# part 2
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
        new_row = []
        line = line.strip()
        if line:
            for c in line:
                new_row.append(c)
        grid.append(new_row)

needed = [
    ('M', (0, 0)),
    ('M', (0, 2)),
    ('A', (1, 1)),
    ('S', (2, 0)),
    ('S', (2, 2)),    
]
def verify(grid, x_base, y_base):
    for letter, (x_offset, y_offset) in needed:
        x, y = x_base + x_offset, y_base + y_offset
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            return 0
        if grid[y][x] != letter:
            return 0
    return 1


def rotate(grid):
    new_grid = []
    for x in range(len(grid)):
        new_row = []
        for y in reversed(range(len(grid[0]))):
            new_row.append(grid[y][x])
        new_grid.append(new_row)
    return new_grid

rotated_grid = grid
total = 0
for rotation in range(4):
    rotated_grid = rotate(rotated_grid)
    for y in range(len(rotated_grid)):
        for x in range(len(rotated_grid[0])):
            total += verify(rotated_grid, x, y)
print(f'Total: {total}')

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
#         new_row = []
#         line = line.strip()
#         if line:
#             for c in line:
#                 new_row.append(c)
#         grid.append(new_row)


# letters = {
#     'X': 'M',
#     'M': 'A',
#     'A': 'S',
#     'S': 'DONE',    
# }

# def search(grid, x, y, dir, needed):
#     if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
#         return False
#     if grid[y][x] == needed:
#         if letters[needed] == 'DONE':
#             return True
#         return search(grid, x + dir[0], y + dir[1], dir, letters[needed])

# total = 0
# for y in range(len(grid)):
#     for x in range(len(grid[y])):
#         for dir in [
#             (0, 1), 
#             (1, 0),
#             (1, 1),
#             (1, -1),
#             (0, -1),
#             (-1, 0),
#             (-1, -1),
#             (-1, 1),
#         ]:
#             if search(grid, x, y, dir, 'X'):
#                 total += 1

# print(f'Total: {total}')