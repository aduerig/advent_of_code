# https://adventofcode.com/2023
import pathlib
import sys
from collections import deque
sys.setrecursionlimit(1000000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

grid = []
with open(data_file) as f:
    for y, line in enumerate(f.read().splitlines()):
        if y == 0:
            start = (line.index('.'), y)
        end = (line.index('.'), y)
        grid.append(list(line))


max_steps = 0
def recurse(pos, steps, visited):
    x, y = pos

    visited.add(pos)

    global max_steps
    max_steps = max(max_steps, steps)

    if pos == end:
        return
    
    for d_pos in dirs:
        dx, dy = d_pos
        new_pos = x + dx, y + dy
        new_x, new_y = new_pos

        if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
            continue

        if grid[new_y][new_x] == '#':
            continue

        if new_pos in visited:
            continue
        
        recurse((x + dx, y + dy), steps + 1, set(visited))

recurse(start, 0, set())
print(max_steps)





# queue = deque([start, set()])

# while queue:
#     longest =



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


# dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# allowed = {
#     '^': (0, -1),
#     '>': (1, 0),
#     '<': (-1, 0),
#     'v': (0, 1),
# }


# grid = []
# with open(data_file) as f:
#     for y, line in enumerate(f.read().splitlines()):
#         if y == 0:
#             start = (line.index('.'), y)
#         end = (line.index('.'), y)
#         grid.append(list(line))


# max_steps = 0
# def recurse(pos, steps, visited):
#     x, y = pos

#     visited.add(pos)

#     global max_steps
#     max_steps = max(max_steps, steps)
    
#     for d_pos in dirs:
#         dx, dy = d_pos
#         new_pos = x + dx, y + dy
#         new_x, new_y = new_pos

#         if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
#             continue

#         if grid[new_y][new_x] == '#':
#             continue

#         if new_pos in visited:
#             continue


#         if grid[new_y][new_x] in '<>^v':
#             if d_pos != allowed[grid[new_y][new_x]]:
#                 continue
        
#         recurse((x + dx, y + dy), steps + 1, set(visited))



# recurse(start, 0, set())
# print(max_steps)





# # queue = deque([start, set()])

# # while queue:
# #     longest =