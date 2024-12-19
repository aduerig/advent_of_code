# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


width = 71
height = 71

# width = 7
# height = 7


data = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        
        if line:
            data.append(list(map(int, line.split(','))))



def reachable(data, to_go):
    safe_before = {}
    for index in range(to_go + 1):
        (x, y) = data[index]
        safe_before[(x, y)] = False

    queue = [(0, (0, 0))]
    visited = set()
    while queue:
        step, (x, y) = queue.pop(0)
        if (x, y) == (width - 1, height - 1):
            return True

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [
                [1, 0],
                [-1, 0],
                [0, -1],
                [0, 1],
            ]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or ny >= height or nx >= width:
                continue

            if not safe_before.get((x, y), True):
                continue

            queue.append((step + 1, (nx, ny)))


for index, (x, y) in enumerate(data):
    if not reachable(data, index):
        print((x, y))
        exit()

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# width = 71
# height = 71

# # width = 7
# # height = 7


# data = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
        
#         if line:
#             data.append(list(map(int, line.split(','))))


# safe_before = {}
# for step, (x, y) in enumerate(data):
#     if step > 1023:
#         break
#     safe_before[(x, y)] = False

# queue = [(0, (0, 0))]
# visited = set()
# while queue:
#     step, (x, y) = queue.pop(0)
#     if (x, y) == (width - 1, height - 1):
#         print(step)
#         exit()

#     if (x, y) in visited:
#         continue
#     visited.add((x, y))

#     for dx, dy in [
#             [1, 0],
#             [-1, 0],
#             [0, -1],
#             [0, 1],
#         ]:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or ny < 0 or ny >= height or nx >= width:
#             continue

#         when_safe = safe_before.get((x, y), True)
#         # when_safe = safe_before.get((x, y), float('inf'))
#         # if (nx, ny) == (3, 0):
#         #     print(f'{x, y=}, {step=}, {when_safe=}')
#         # if step > when_safe:
#         #     continue
#         if not when_safe:
#             continue

#         queue.append((step + 1, (nx, ny)))