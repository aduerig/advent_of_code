# https://adventofcode.com/2023
import sys
import pathlib
import copy

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            grid.append(list(line))


# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
        
dones = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        ele = grid[y][x]
        if ele == '9':
            dones.append((x, y))

memo = {}
def recurse(pos):
    if pos in memo:
        return memo[pos]

    ele = int(grid[pos[1]][pos[0]])
    if ele == 0:
        memo[pos] = 1
        return 1

    paths = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = pos[0] + dx
        new_y = pos[1] + dy
        if new_x >= 0 and new_x < len(grid[0]) and new_y >= 0 and new_y < len(grid):
            new_ele = int(grid[new_y][new_x])
            if new_ele == ele - 1:
                paths += recurse((new_x, new_y))
    memo[pos] = paths
    return paths

total = 0
for tail in dones:
    to_add = recurse(tail)
    total += to_add

print(total)




# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib
# import copy

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             grid.append(list(line))


# # with open(data_file) as f:
# #     for line in f.readlines():
# #         line = line.strip()
        
# heads = []
# for y in range(len(grid)):
#     for x in range(len(grid[y])):
#         ele = grid[y][x]
#         if ele == '0':
#             heads.append((x, y))

# def bfs(pos):
#     total = 0
#     queue = [(pos[0], pos[1], set())]
#     finished = set()
#     while queue:
#         x, y, visited = queue.pop(0)
#         if (x, y) in visited:
#             continue
#         visited.add((x, y))
#         if grid[y][x] == '9' and (x, y) not in finished:
#             total += 1
#             finished.add((x, y))
#         for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             new_x = x + dx
#             new_y = y + dy
#             if new_x >= 0 and new_x < len(grid[0]) and new_y >= 0 and new_y < len(grid):
#                 new_ele = int(grid[new_y][new_x])
#                 if new_ele - int(grid[y][x]) == 1:
#                     queue.append((new_x, new_y, copy.deepcopy(visited)))
#     return total

# total = 0
# for head in heads:
#     to_add = bfs(head)
#     total += to_add

# print(total)

