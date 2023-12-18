# https://adventofcode.com/2023
import pathlib
import sys
import random

sys.setrecursionlimit(500000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


dirs_letter = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1),
}

dirs_index = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

instructions = []
pos = (0, 0)
with open(data_file) as f:
    for line in f.read().splitlines():
        letter, amt_flat, color = line.split()

        amt_from_hex, direction_index = int(color[2:-2], 16), int(color[-2])
        instructions.append((amt_from_hex, dirs_index[direction_index]))

        # instructions.append((amt_flat, dirs_letter[letter]))


all_visited = set([pos])
up_down_visited = set([pos])
left_right_visited = set([pos])
last_dpos = None
for index, (amt, dpos) in enumerate(instructions):
    dx, dy = dpos
    print(f'{index+1}/{len(instructions)} - {amt} - {dpos}')

    if last_dpos == dpos:
        exit()

    if last_dpos == (-1, 0) and dpos == (0, 1):
        left_right_visited.add(pos)

    if last_dpos == (0, -1) and dpos == (1, 0):
        left_right_visited.add(pos)

    if last_dpos == (0, 1) and dpos == (1, 0):
        left_right_visited.add(pos)

    if last_dpos == (-1, 0) and dpos == (0, -1):
        left_right_visited.add(pos)


    up_down_visited.add(pos)

    for i in range(int(amt)):
        new_pos = pos[0] + dx, pos[1] + dy
        all_visited.add(new_pos)

        if int(amt) - 1 != i and dpos in [(1, 0), (-1, 0)]:
            left_right_visited.add(new_pos)
        elif dpos in [(0, 1), (0, -1)]:
            up_down_visited.add(new_pos)
        pos = new_pos
    
    last_dpos = dpos

print('making y_to_x')

y_to_x_arr = {}
x_to_y_arr = {}
for index, (x, y) in enumerate(up_down_visited):
    if random.random() < .000001:
        print(f'{index+1}/{len(up_down_visited)}')
    if y not in y_to_x_arr:
        y_to_x_arr[y] = []
    y_to_x_arr[y].append(x)


print('making x_to_y')
for index, (x, y) in enumerate(left_right_visited):
    if random.random() < .000001:
        print(f'{index+1}/{len(left_right_visited)}')
    if x not in x_to_y_arr:
        x_to_y_arr[x] = []
    x_to_y_arr[x].append(y)


def sort_all(the_dict):
    for arr in the_dict.values():
        arr.sort()

sort_all(x_to_y_arr)
sort_all(y_to_x_arr)

print('Done sortin')


def is_inside(x, y, ys_at_this_x):
    if not ys_at_this_x or y < ys_at_this_x[0]:
        return False
    index = 0
    while index < len(ys_at_this_x) - 1:
        val = ys_at_this_x[index]
        next_val = ys_at_this_x[index + 1]
        index += 1
        if val < y and y < next_val:
            if index % 2 == 1:
                return True
            return False
    if index == len(ys_at_this_x) - 1:
        return False
    if index % 2 == 1:
        return True
    return False


total = 0
for y, x_arr in y_to_x_arr.items():
    for index in range(len(x_arr)):
        total += 1
        if index == len(x_arr) - 1:
            continue

        v1, v2 = x_arr[index], x_arr[index+1]
        checker = v1 + 1
        if checker not in x_to_y_arr:
            continue
        ys_at_this_x = x_to_y_arr[checker]

        if y in ys_at_this_x:
            total += (v2 - v1) - 1
        elif is_inside(checker, y, ys_at_this_x):
            total += (v2 - v1) - 1
        

# for row in grid:
#     print(''.join(row))
print(total)


# working part 2 smart maybe
# # https://adventofcode.com/2023
# import pathlib
# import sys
# import random

# sys.setrecursionlimit(500000)

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# dirs_letter = {
#     'R': (1, 0),
#     'L': (-1, 0),
#     'D': (0, 1),
#     'U': (0, -1),
# }

# dirs_index = [
#     (1, 0),
#     (0, 1),
#     (-1, 0),
#     (0, -1),
# ]

# instructions = []
# pos = (0, 0)
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         letter, amt_flat, color = line.split()

#         # amt_from_hex, direction_index = int(color[2:-2], 16), int(color[-2])
#         # instructions.append((amt, dirs_index[direction_index]))

#         instructions.append((amt_flat, dirs_letter[letter]))


# all_visited = set([pos])
# up_down_visited = set([pos])
# left_right_visited = set([pos])
# last_dpos = None
# for index, (amt, dpos) in enumerate(instructions):
#     dx, dy = dpos
#     print(f'{index+1}/{len(instructions)} - {amt} - {dpos}')

#     if last_dpos == dpos:
#         exit()

#     if last_dpos == (-1, 0) and dpos == (0, 1):
#         left_right_visited.add(pos)

#     if last_dpos == (0, -1) and dpos == (1, 0):
#         left_right_visited.add(pos)

#     if last_dpos == (0, 1) and dpos == (1, 0):
#         left_right_visited.add(pos)

#     if last_dpos == (-1, 0) and dpos == (0, -1):
#         left_right_visited.add(pos)


#     up_down_visited.add(pos)

#     for i in range(int(amt)):
#         new_pos = pos[0] + dx, pos[1] + dy
#         all_visited.add(new_pos)

#         if int(amt) - 1 != i and dpos in [(1, 0), (-1, 0)]:
#             left_right_visited.add(new_pos)
#         elif dpos in [(0, 1), (0, -1)]:
#             up_down_visited.add(new_pos)
#         pos = new_pos
    
#     last_dpos = dpos


# tiniest = float('inf')
# biggest = float('-inf')
# for x, y in all_visited:
#     tiniest = min(x, y, tiniest)
#     biggest = max(x, y, biggest)

# shifted_all = set()
# for x, y in all_visited:
#     shifted_all.add((x + abs(tiniest), y + abs(tiniest)))

# shifted_up_down = set()
# for x, y in up_down_visited:
#     shifted_up_down.add((x + abs(tiniest), y + abs(tiniest)))

# shifted_left_right = set()
# for x, y in left_right_visited:
#     shifted_left_right.add((x + abs(tiniest), y + abs(tiniest)))


# dist = (biggest - tiniest) + 1
# grid = [['#' if (x, y) in shifted_all else '.' for x in range(dist)] for y in range(dist // 2)]


# y_to_x_arr = {}
# x_to_y_arr = {}
# for index, (x, y) in enumerate(shifted_up_down):
#     if y not in y_to_x_arr:
#         y_to_x_arr[y] = []
#     y_to_x_arr[y].append(x)

# for index, (x, y) in enumerate(shifted_left_right):
#     if x not in x_to_y_arr:
#         x_to_y_arr[x] = []
#     # grid[y][x] = grid[y][x]
#     x_to_y_arr[x].append(y)

# def sort_all(the_dict):
#     for arr in the_dict.values():
#         arr.sort()

# sort_all(x_to_y_arr)
# sort_all(y_to_x_arr)

# print('Done sortin')


# def is_inside(x, y, ys_at_this_x):
#     if not ys_at_this_x or y < ys_at_this_x[0]:
#         return False
#     index = 0
#     while index < len(ys_at_this_x) - 1:
#         val = ys_at_this_x[index]
#         next_val = ys_at_this_x[index + 1]
#         # grid[val][x] = red(grid[val][x])
#         index += 1
#         if val < y and y < next_val:
#             if index % 2 == 1:
#                 return True
#             return False
#     if index == len(ys_at_this_x) - 1:
#         return False
#     if index % 2 == 1:
#         return True
#     return False



# counted = {}

# total = 0
# for y, x_arr in y_to_x_arr.items():
#     for index in range(len(x_arr)):
#         grid[y][x_arr[index]] = red(grid[y][x_arr[index]])
#         total += 1
#         if (x_arr[index], y) not in counted:
#             counted[(x_arr[index], y)] = 0
#         counted[(x_arr[index], y)] += 1
        
#         if index == len(x_arr) - 1:
#             continue

#         v1, v2 = x_arr[index], x_arr[index+1]
#         checker = v1 + 1
#         if checker not in x_to_y_arr:
#             continue
#         ys_at_this_x = x_to_y_arr[checker]

#         # grid[ys_at_this_x[0]][x] = red(grid[ys_at_this_x[0]][x])

#         if y in ys_at_this_x:
#         # if (checker, y) in all_visited:
#             for color_index in range(v1 + 1, v2):
#                 # total += 1
#                 if (color_index, y) not in counted:
#                     counted[(color_index, y)] = 0
#                 counted[(color_index, y)] += 1

#                 grid[y][color_index] = red(grid[y][color_index])
#             total += (v2 - v1) - 1

#         elif is_inside(checker, y, ys_at_this_x):
#             for color_index in range(v1 + 1, v2):
#                 # total += 1
#                 if (color_index, y) not in counted:
#                     counted[(color_index, y)] = 0
#                 counted[(color_index, y)] += 1

#                 grid[y][color_index] = red(grid[y][color_index])
#             total += (v2 - v1) - 1
        


# doubles = 0
# for key, value in counted.items():
#     if value > 1:
#         print(key)
#     doubles += value - 1
# for row in grid:
#     print(''.join(row))
# print(total)
# print(f'{doubles=}')


# false is:   389393967981
# correct is: 952408144115



# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# sys.setrecursionlimit(500000)

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# dirs = {
#     'R': (1, 0),
#     'L': (-1, 0),
#     'D': (0, 1),
#     'U': (0, -1),
# }


# pos = (0, 0)

# first_visit = set([(0, 0)])
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         dir, amt, color = line.split()

#         dx, dy = dirs[dir]
#         for i in range(int(amt)):    
#             new_pos = tuple([pos[0] + dx, pos[1] + dy])
#             first_visit.add(new_pos)
#             pos = new_pos



# minny = float('inf')
# maxxy = float('-inf')
# for x, y in first_visit:
#     minny = min(minny, x)
#     minny = min(minny, y)

#     maxxy = max(maxxy, x)
#     maxxy = max(maxxy, y)


# original_walls = set()
# for x, y in first_visit:
#     original_walls.add((x + abs(minny), y + abs(minny)))

# dist = (maxxy - minny) + 10

# grid = [['#' if (x, y) in original_walls else '.' for x in range(dist)] for y in range(dist)]



# possible = [
#     (1, 0),
#     (-1, 0),
#     (0, 1),
#     (0, -1),
# ]



# def in_bounds(pos):
#     x, y = pos
#     if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
#         return False
#     return True


# visitors = []
# def in_visitors(pos):
#     for lol in visitors:
#         if pos in lol:
#             return True
#     return False

# def dfs(pos, visit, color):
#     x, y = pos
#     if pos in visit or not in_bounds(pos) or pos in original_walls:
#         return
#     grid[pos[1]][pos[0]] = color(grid[pos[1]][pos[0]])
#     visit.add(pos)
#     for dx, dy in possible:
#         new_pos = (dx + x, dy + y)
#         if in_bounds(new_pos) and grid[new_pos[1]][new_pos[0]] != '#':
#             dfs(new_pos, visit, color=color)


# wallers = set()
# to_do = []

# for x in range(len(grid[0])):
#     to_do.append((x, 0))
#     to_do.append((x, len(grid[0]) - 1))

# for y in range(len(grid)):
#     to_do.append((0, y))
#     to_do.append((len(grid) - 1, y))


# wall_visit = set()
# for x, y in to_do:
#     if grid[y][x] == '.':
#         dfs((x, y), wall_visit, color=red)

# print('huh')

# for x, y in original_walls:
#     for dx, dy in possible:
#         new_pos = x + dx, y + dy
#         if in_bounds(new_pos) and not in_visitors(new_pos) and new_pos not in original_walls and not new_pos in wall_visit:
#             visitors.append(set())
#             dfs(new_pos, visitors[-1], color=cyan)
#             # print(new_pos, len(visitors[-1]))
#             # grid[new_pos[1]][new_pos[0]] = red(grid[new_pos[1]][new_pos[0]])

# for y in range(len(grid)):
#     print(''.join(grid[y]))


# # possible: 307106 - total: 311426
# # possible: 51357 - total: 55677
# # possible: 2301 - total: 6621
# # possible: 13121 - total: 17441
# # possible: 803 - total: 5123
# # possible: 242 - total: 4562
# # possible: 100 - total: 4420
# # original 4320
    
# # wasnt 55677
    
# for v in visitors:
#     print(f'possible: {len(v)} - total: {len(v) + len(original_walls)}')
# print('original', len(original_walls))

