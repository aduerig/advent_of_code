# https://adventofcode.com/2023
import pathlib
import sys

sys.setrecursionlimit(10000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# i deleted part 1 but its basically the same, just top left ot the right
grid = []
with open(data_file) as f:
    for line in f.read().splitlines():
        grid.append(line)

dir_and_tile_to_new_dir = {
    ((1, 0), '/'): [[0, -1]],
    ((1, 0), '\\'): [[0, 1]],
    ((-1, 0), '/'): [[0, 1]],
    ((-1, 0), '\\'): [[0, -1]],
    ((0, 1), '/'): [[-1, 0]],
    ((0, 1), '\\'): [[1, 0]],
    ((0, -1), '/'): [[1, 0]],
    ((0, -1), '\\'): [(-1, 0)],
    ((1, 0), '|'): [(0, 1), (0, -1)],
    ((-1, 0), '|'): [(0, 1), (0, -1)],
    ((0, 1), '-'): [(1, 0), (-1, 0)],
    ((0, -1), '-'): [(1, 0), (-1, 0)],
}

global_seen = set()
def recurse(grid, x, y, dir, seen):
    if (x, y, dir) in seen:
        return
    seen.add((x, y, dir))
    global_seen.add((x, y, dir))

    if (dir, grid[y][x]) not in dir_and_tile_to_new_dir:
        new_x = x + dir[0]
        new_y = y + dir[1]
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
            recurse(grid, new_x, new_y, dir, seen)
        return seen
    for (dx, dy) in dir_and_tile_to_new_dir.get((dir, grid[y][x]), []):
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
            recurse(grid, new_x, new_y, tuple([dx, dy]), seen)
    return seen



to_do = []
for x in range(len(grid[0])):
    to_do.append((x, 0, (0, 1)))
    to_do.append((x, len(grid) - 1, (0, -1)))

for y in range(len(grid)):
    to_do.append((0, y, (1, 0)))
    to_do.append((len(grid[0]) - 1, y, (-1, 0)))    



m = 0
for x, y, dir in to_do:
    squares = set()
    for x, y, dir in recurse(grid, x, y, dir, set()):
        squares.add((x, y))
    m = max(m, len(squares))
print(m)



# part 2 og submission
# # https://adventofcode.com/2023
# import pathlib
# import sys

# sys.setrecursionlimit(10000)

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# # i deleted part 1 but its basically the same, just top left ot the right
# grid = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         grid.append(line)


# dir_and_tile_to_new_dir = {
#     ((1, 0), '/'): [[0, -1]],
#     ((1, 0), '\\'): [[0, 1]],
#     ((-1, 0), '/'): [[0, 1]],
#     ((-1, 0), '\\'): [[0, -1]],
#     ((0, 1), '/'): [[-1, 0]],
#     ((0, 1), '\\'): [[1, 0]],
#     ((0, -1), '/'): [[1, 0]],
#     ((0, -1), '\\'): [(-1, 0)],
#     ((1, 0), '|'): [(0, 1), (0, -1)],
#     ((-1, 0), '|'): [(0, 1), (0, -1)],
#     ((0, 1), '-'): [(1, 0), (-1, 0)],
#     ((0, -1), '-'): [(1, 0), (-1, 0)],
# }



# seen = set()
# def recurse(grid, x, y, dir):
#     if (x, y, dir) in seen:
#         return
#     seen.add((x, y, dir))


#     if (dir, grid[y][x]) not in dir_and_tile_to_new_dir:
#         new_x = x + dir[0]
#         new_y = y + dir[1]
#         if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#             recurse(grid, new_x, new_y, dir)
#     else:
#         for new_dir in dir_and_tile_to_new_dir.get((dir, grid[y][x]), []):
#             print(new_dir, x, y, grid[y][x], (dir, grid[y][x]))
#             new_x = x + new_dir[0]
#             new_y = y + new_dir[1]
#             if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#                 recurse(grid, new_x, new_y, tuple(new_dir))



# m = 0
# for x in range(len(grid[0])):
#     seen = set()
#     recurse(grid, x, 0, (0, 1))
#     squares = set()
#     for x, y, dir in seen:
#         squares.add((x, y))
#     m = max(m, len(squares))

# for x in range(len(grid[0])):
#     seen = set()
#     recurse(grid, x, len(grid) - 1, (0, -1))
#     squares = set()
#     for x, y, dir in seen:
#         squares.add((x, y))
#     m = max(m, len(squares))

# for y in range(len(grid)):
#     seen = set()
#     recurse(grid, 0, y, (1, 0))
#     squares = set()
#     for x, y, dir in seen:
#         squares.add((x, y))
#     m = max(m, len(squares))


# for y in range(len(grid)):
#     seen = set()
#     recurse(grid, len(grid[0]) - 1, y, (-1, 0))
#     squares = set()
#     for x, y, dir in seen:
#         squares.add((x, y))
#     m = max(m, len(squares))

# print(m)



# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# sys.setrecursionlimit(10000)

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# # i deleted part 1 but its basically the same, just top left ot the right
# grid = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         grid.append(line)


# dir_and_tile_to_new_dir = {
#     ((1, 0), '/'): [[0, -1]],
#     ((1, 0), '\\'): [[0, 1]],
#     ((-1, 0), '/'): [[0, 1]],
#     ((-1, 0), '\\'): [[0, -1]],
#     ((0, 1), '/'): [[-1, 0]],
#     ((0, 1), '\\'): [[1, 0]],
#     ((0, -1), '/'): [[1, 0]],
#     ((0, -1), '\\'): [(-1, 0)],
#     ((1, 0), '|'): [(0, 1), (0, -1)],
#     ((-1, 0), '|'): [(0, 1), (0, -1)],
#     ((0, 1), '-'): [(1, 0), (-1, 0)],
#     ((0, -1), '-'): [(1, 0), (-1, 0)],
# }



# seen = set()
# def recurse(grid, x, y, dir):
#     if (x, y, dir) in seen:
#         return
#     seen.add((x, y, dir))


#     if (dir, grid[y][x]) not in dir_and_tile_to_new_dir:
#         new_x = x + dir[0]
#         new_y = y + dir[1]
#         if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#             recurse(grid, new_x, new_y, dir)
#     else:
#         for new_dir in dir_and_tile_to_new_dir.get((dir, grid[y][x]), []):
#             print(new_dir, x, y, grid[y][x], (dir, grid[y][x]))
#             new_x = x + new_dir[0]
#             new_y = y + new_dir[1]
#             if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
#                 recurse(grid, new_x, new_y, tuple(new_dir))



# seen = set()
# recurse(grid, 0, 0, (-1, 0))
# squares = set()
# for x, y, dir in seen:
#     squares.add((x, y))
# print(len(squares))


