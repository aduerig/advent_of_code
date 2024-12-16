# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
dirs = []
new_mode = False
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            if new_mode:
                dirs += list(line)
            else:
                grid.append(list(line))
        else:
            new_mode = True

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '@':
            pos = (x, y)

# def dist(d1, d2):
#     return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])

unpack = {
    'v': (0, 1),
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}
grid[pos[1]][pos[0]] = '.'

def ends(grid, pos, d):
    x, y = pos
    print(f'Trying at {pos=}, with direction {d}')
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    if grid[y][x] == '#':
        return False
    
    if grid[y][x] == '.':
        return (x, y)
    
    return ends(grid, (pos[0] + d[0], pos[1] + d[1]), d)


for movement in dirs:
    d = unpack[movement]
    n = (pos[0] + d[0], pos[1] + d[1])
    end = ends(grid, n, d)
    if end:
        # print(f'{movement}, huh, n was {n}, pos was: {pos}')
        pos = n
        if end != n:
            grid[pos[1]][pos[0]] = '.'
            grid[end[1]][end[0]] = 'O'


for y in range(len(grid)):
    to_print = []
    for x in range(len(grid[0])):
        if (x, y) == pos:
            to_print.append('@')
        else:
            to_print.append(grid[y][x])
    print(''.join(to_print))
        
# 4848 too low

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            total += 100 * y + x
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
# dirs = []
# new_mode = False
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             if new_mode:
#                 dirs += list(line)
#             else:
#                 grid.append(list(line))
#         else:
#             new_mode = True

# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == '@':
#             pos = (x, y)

# # def dist(d1, d2):
# #     return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])

# unpack = {
#     'v': (0, 1),
#     '^': (0, -1),
#     '>': (1, 0),
#     '<': (-1, 0),
# }
# grid[pos[1]][pos[0]] = '.'

# def ends(grid, pos, d):
#     x, y = pos
#     print(f'Trying at {pos=}, with direction {d}')
#     if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
#         return False
#     if grid[y][x] == '#':
#         return False
    
#     if grid[y][x] == '.':
#         return (x, y)
    
#     return ends(grid, (pos[0] + d[0], pos[1] + d[1]), d)


# for movement in dirs:
#     d = unpack[movement]
#     n = (pos[0] + d[0], pos[1] + d[1])
#     end = ends(grid, n, d)
#     if end:
#         # print(f'{movement}, huh, n was {n}, pos was: {pos}')
#         pos = n
#         if end != n:
#             grid[pos[1]][pos[0]] = '.'
#             grid[end[1]][end[0]] = 'O'


# for y in range(len(grid)):
#     to_print = []
#     for x in range(len(grid[0])):
#         if (x, y) == pos:
#             to_print.append('@')
#         else:
#             to_print.append(grid[y][x])
#     print(''.join(to_print))
        
# # 4848 too low

# total = 0
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == 'O':
#             total += 100 * y + x
# print(total)