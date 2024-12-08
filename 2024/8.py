# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
grid_by_id = {}
with open(data_file) as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        if line:
            grid.append(list(line))
            for x, char in enumerate(line):
                if char != '.':
                    if char not in grid_by_id:
                        grid_by_id[char] = []
                    grid_by_id[char].append((x, y))

def in_bounds(x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

unique = set()

def try_it(start_x, x_diff, start_y, y_diff):
    x, y = start_x + x_diff, start_y + y_diff
    while in_bounds(x, y):
        unique.add((x, y))
        x += x_diff
        y += y_diff


for freq, the_list in grid_by_id.items():
    for index1 in range(len(the_list)):
        perma_x1, perma_y1 = the_list[index1]
        unique.add((perma_x1, perma_y1))
        for index2 in range(index1 + 1, len(the_list)):
            perma_x2, perma_y2 = the_list[index2]
            x1, y1 = perma_x1, perma_y1
            x2, y2 = perma_x2, perma_y2

            if (x1 > x2):
                x1, x2, y1, y2 = x2, x1, y2, y1

            x_diff, y_diff = abs(x2 - x1), abs(y2 - y1)
            if y1 < y2:
                pass
                try_it(x1,  -x_diff, y1,  -y_diff)
                try_it(x2, x_diff, y2, y_diff)
            else:
                try_it(x1, -x_diff, y1, y_diff)
                try_it(x2, x_diff, y2, -y_diff)


for y in range(len(grid)):
    to_print = []
    for x in range(len(grid[0])):
        if (x, y) in unique:
            to_print.append(red('#'))
        elif grid[y][x] == '.':
            to_print.append('.')
        else:
            to_print.append(blue(grid[y][x]))
    print(''.join(to_print))

print(len(unique))



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
# grid_by_id = {}
# with open(data_file) as f:
#     for y, line in enumerate(f.readlines()):
#         line = line.strip()
#         if line:
#             grid.append(list(line))
#             for x, char in enumerate(line):
#                 if char != '.':
#                     if char not in grid_by_id:
#                         grid_by_id[char] = []
#                     grid_by_id[char].append((x, y))

# def in_bounds(x, y):
#     return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

# unique = set()

# def try_it(new_x, new_y):
#     if in_bounds(new_x, new_y):
#         unique.add((new_x, new_y))

# for freq, the_list in grid_by_id.items():
#     for index1 in range(len(the_list)):
#         perma_x1, perma_y1 = the_list[index1]
#         for index2 in range(index1 + 1, len(the_list)):
#             perma_x2, perma_y2 = the_list[index2]
#             x1, y1 = perma_x1, perma_y1
#             x2, y2 = perma_x2, perma_y2

#             if (x1 > x2):
#                 x1, x2, y1, y2 = x2, x1, y2, y1

#             x_diff, y_diff = abs(x2 - x1), abs(y2 - y1)
#             if y1 < y2:
#                 pass
#                 try_it(x1 - x_diff, y1 - y_diff)
#                 try_it(x2 + x_diff, y2 + y_diff)
#             else:
#                 try_it(x1 - x_diff, y1 + y_diff)
#                 try_it(x2 + x_diff, y2 - y_diff)


# for y in range(len(grid)):
#     to_print = []
#     for x in range(len(grid[0])):
#         if (x, y) in unique:
#             to_print.append(red('#'))
#         elif grid[y][x] == '.':
#             to_print.append('.')
#         else:
#             to_print.append(blue(grid[y][x]))
#     print(''.join(to_print))

# print(len(unique))