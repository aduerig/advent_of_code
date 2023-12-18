# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            grid.append(list(line))

from queue import PriorityQueue



following = {
    (1, 0): [(0, 1), (0, -1), (1, 0)],
    (-1, 0): [(0, 1), (0, -1), (-1, 0)],
    (0, 1): [(0, 1), (1, 0), (-1, 0)],
    (0, -1): [(0, -1), (1, 0), (-1, 0)],
}

queue = PriorityQueue()
queue.put((0, (0, 0), (1, 0), 0))
queue.put((0, (0, 0), (0, 1), 0))

seen = set()
while not queue.empty():
    heat, (x, y), (last_x, last_y), amt = queue.get_nowait()
    if x == len(grid[0]) - 1 and y == len(grid) - 1:
        print(heat)
        break

    if (x, y, last_x, last_y, amt) in seen:
        continue
    seen.add((x, y, last_x, last_y, amt))

    for dx, dy in following[(last_x, last_y)]:
        if (dx, dy) != (last_x, last_y) and amt < 4:
            continue
        if (dx, dy) == (last_x, last_y) and amt > 9:
            continue
        if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
            new_amt = amt + 1
            if dx != last_x or dy != last_y:
                new_amt = 1
            new_heat = int(grid[x + dx][y + dy])
            queue.put((heat + new_heat, (x + dx, y + dy), (dx, dy), new_amt))

# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             grid.append(list(line))

# from queue import PriorityQueue


# queue = PriorityQueue()
# queue.put((0, (0, 0), (1, 0), 0))
# queue.put((0, (0, 0), (0, 1), 0))


# following = {
#     (1, 0): [(0, 1), (0, -1), (1, 0)],
#     (-1, 0): [(0, 1), (0, -1), (-1, 0)],
#     (0, 1): [(0, 1), (1, 0), (-1, 0)],
#     (0, -1): [(0, -1), (1, 0), (-1, 0)],
# }


# seen = set()
# while not queue.empty():
#     heat, (x, y), (last_x, last_y), amt = queue.get_nowait()
#     if x == len(grid[0]) - 1 and y == len(grid) - 1:
#         print(heat)
#         break

#     if (x, y, last_x, last_y, amt) in seen:
#         continue
#     seen.add((x, y, last_x, last_y, amt))

#     for dx, dy in following[(last_x, last_y)]:
#         if (dx, dy) == (last_x, last_y) and amt >= 3:
#             continue
#         if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
#             new_amt = amt + 1
#             if dx != last_x or dy != last_y:
#                 new_amt = 1
#             new_heat = int(grid[x + dx][y + dy])
#             queue.put((heat + new_heat, (x + dx, y + dy), (dx, dy), new_amt))