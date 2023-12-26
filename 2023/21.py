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

# 301: 78416
# 302: 78828
# 431: 160410
# 432: 161316
# 433: 161912


def is_bad(grid, pos):
    x, y = pos
    # if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
    #     return True
    if x < 0:
        x = len(grid[0]) - (abs(x) % len(grid[0]))
    if y < 0:
        y = len(grid) - (abs(y) % len(grid))
    return grid[y % len(grid)][x % len(grid[0])] == '#'


def bfs(queue):
    reached = {}
    visited = set()
    while queue:
        pos, left = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if left % 2 == 0:
            reached[pos] = left

        if left == 0:
            continue

        x, y = pos
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_bad(grid, (new_x, new_y)):
                continue
            queue.append(((new_x, new_y), left - 1))
    return len(reached)

print(bfs(deque([(start_pos, 65)])))
print(bfs(deque([(start_pos, 65 + (131 * 2))])))
print(bfs(deque([(start_pos, 65 + (131 * 4))])))
print(bfs(deque([(start_pos, 65 + (131 * 6))])))


# 3755
# 92811
# 300179
# 625859

# 92811 - 3755 = 89056
# 300179 - 92811 = 207368
# 625859 - 300179 = 325680


total = 3755
change = 89056
change_to_change = 118312

start = 65
end = 26501365
while start != end:
    total += change
    change += change_to_change
    start += 131 * 2

print(total)




# 2420982504013755 too high


# 207368 - 89056 = 118312
# 325680 - 207368 = 118312






# recurse(start_pos, 26501365)


# old part 2
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


# recurse(start_pos, 26501365)
# # recurse(start_pos, 6)
# print(len(reached))

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
