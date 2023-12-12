
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

instructions = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            line = line.replace('turn ', '')

            before, last = line.split('through')
            x2, y2 = list(map(int, last.strip().split(','))) 
            on_off, first = before.strip().split()
            x1, y1 = list(map(int, first.strip().split(',')))
            on_off_toggle = on_off.strip()
            instructions.append((on_off, [x1, y1], [x2, y2]))

val = {
    'toggle': 2,
    'on': 1,
    'off': -1,
}

grid = [[0 for _ in range(1000)] for _ in range(1000)]
for on_off_toggle, (x1, y1), (x2, y2) in instructions:
    if x2 < x1:
        print_red('ok') or exit()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[y][x] = max(0, grid[y][x] + val[on_off_toggle])

print(sum([sum(x) for x in grid]))

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# instructions = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             line = line.replace('turn ', '')

#             before, last = line.split('through')
#             x2, y2 = list(map(int, last.strip().split(','))) 
#             on_off, first = before.strip().split()
#             x1, y1 = list(map(int, first.strip().split(',')))
#             on_off_toggle = on_off.strip()
#             instructions.append((on_off, [x1, y1], [x2, y2]))

# val = {
#     'on': 1,
#     'off': 0,
# }


# grid = [[0 for _ in range(1000)] for _ in range(1000)]
# for on_off_toggle, (x1, y1), (x2, y2) in instructions:
#     if x2 < x1:
#         print_red('ok') or exit()
#     for x in range(x1, x2 + 1):
#         for y in range(y1, y2 + 1):
#             if on_off_toggle == 'toggle':
#                 grid[y][x] = 1 - grid[y][x]
#             else:
#                 grid[y][x] += val[on_off_toggle]

# print(sum([x.count(1) for x in grid]))