# https://adventofcode.com/2023
import pathlib
import sys
from collections import deque

sys.setrecursionlimit(1000000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
with open(data_file) as f:
    for y, line in enumerate(f.read().splitlines()):
        grid.append(list(line))

        if 'S' in grid[-1]:
            start_pos = (grid[-1].index('S'), y)
            grid[-1][start_pos[0]] = '.'


reached = set()
visited = set()
def recurse(pos, left):
    x, y = pos
    if left == 0:
        return reached.add(pos)

    key = hash((pos, left % 2, left % 3, left % 4, left % 5, left % 6, left % 7, left % 8, left % 9, left % 11, left % 13))
    if key in visited:
        return
    visited.add(key)

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy

        if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid) or grid[new_y][new_x] == '#':
            continue
        recurse((new_x, new_y), left - 1)
        if left == 64:
            print('finished 64')


recurse(start_pos, 26501365)
# recurse(start_pos, 6)
print(len(reached))

# 641 not right
# 5xx too low



# bfs
# queue = deque([pos, 0])

# while queue:
#     x, y = queue.popleft()


#     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         pass




# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys
# from collections import deque

# sys.setrecursionlimit(1000000)

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# grid = []
# with open(data_file) as f:
#     for y, line in enumerate(f.read().splitlines()):
#         grid.append(list(line))

#         if 'S' in grid[-1]:
#             start_pos = (grid[-1].index('S'), y)
#             grid[-1][start_pos[0]] = '.'


# reached = set()
# visited = set()
# def recurse(pos, left):
#     x, y = pos
#     if left == 0:
#         return reached.add(pos)

#     key = hash((pos, left % 2, left % 3, left % 4, left % 5, left % 6, left % 7, left % 8, left % 9, left % 11, left % 13))
#     if key in visited:
#         return
#     visited.add(key)

#     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         new_x, new_y = x + dx, y + dy

#         if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid) or grid[new_y][new_x] == '#':
#             continue
#         recurse((new_x, new_y), left - 1)
#         if left == 64:
#             print('finished 64')


# recurse(start_pos, 64)
# # recurse(start_pos, 6)
# print(len(reached))

# # 641 not right
# # 5xx too low



# # bfs
# # queue = deque([pos, 0])

# # while queue:
# #     x, y = queue.popleft()


# #     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
# #         pass
