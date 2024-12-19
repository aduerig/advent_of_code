# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

old_grid = []
dirs = []
new_mode = False
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            if new_mode:
                dirs += list(line)
            else:
                old_grid.append(list(line))
        else:
            new_mode = True

def print_grid(grid):
    for y in range(len(grid)):
        to_print = []
        for x in range(len(grid[0])):
            if (x, y) == pos:
                to_print.append('@')
            else:
                to_print.append(grid[y][x])
        print(''.join(to_print))
            

new_grid = []
for y, row in enumerate(old_grid):
    new_row = []
    for x, ele in enumerate(row):
        if ele == 'O':
            new_row += ['[', ']']
        elif ele == '@':
            new_row += ['@', '.']
        else:
            new_row += [ele] * 2
    new_grid.append(new_row)

for y in range(len(new_grid)):
    for x in range(len(new_grid[0])):
        if new_grid[y][x] == '@':
            pos = (x, y)


print('==== OLD')
print_grid(old_grid)

print('==== NEW')
print_grid(new_grid)


unpack = {
    'v': (0, 1),
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}
inverse_unpack = {y: x for x, y in unpack.items()}



new_grid[pos[1]][pos[0]] = '.'

def does_end(grid, pos, d, needs_pushed):
    x, y = pos
    # print(f'does_end: Trying at {pos=}, with direction {inverse_unpack[d]}')
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    
    ele = grid[y][x]
    if ele == '#':
        return False
    if ele == '.':
        return True

    # horizontal
    if d[0] != 0:
        return does_end(grid, (pos[0] + d[0] * 2, pos[1]), d, needs_pushed)
    # vertical
    else:
        if ele == '[':
            needs_pushed.add(pos)
            needs_pushed.add((pos[0]+1, pos[1]))
            return does_end(grid, (pos[0], pos[1] + d[1]), d, needs_pushed) and does_end(grid, (pos[0] + 1, pos[1] + d[1]), d, needs_pushed)
        else:
            needs_pushed.add(pos)
            needs_pushed.add((pos[0]-1, pos[1]))
            return does_end(grid, (pos[0], pos[1] + d[1]), d, needs_pushed) and does_end(grid, (pos[0] - 1, pos[1] + d[1]), d, needs_pushed)

def push_hori(grid, pos, d, prev):
    x, y = pos

    ele = grid[y][x]
    # print(f'push: Trying at {pos=} as {ele=}, with direction {inverse_unpack[d]}')

    if ele == '.' and prev == '.':
        return

    if ele != '.':
        push_hori(grid, (pos[0] + d[0], pos[1]), d, ele)
    grid[y][x] = prev

# if prev == '.':
#     grid[y][x] = '.'
#     grid[y][x+1] = '.'
# elif prev == '[':
#     pass

def get_new_vert(old_grid, d, needs_pushed):
    grid = []

    for y in range(len(old_grid)):
        row = []
        for x in range(len(old_grid[0])):
            ele = old_grid[y][x]
            if (x, y) not in needs_pushed:
                row.append(ele)
            else:
                row.append('.')
        grid.append(row)


    # for y in range(len(old_grid)):
    #     for x in range(len(old_grid[0])):
    #         ele = old_grid[y][x]

    for x, y in needs_pushed:
        grid[y + d[1]][x] = old_grid[y][x]
    return grid
        

for step, movement in enumerate(dirs):
    d = unpack[movement]
    ending_for_player = (pos[0] + d[0], pos[1] + d[1])

    # print(f'======== Grid at step {step}')
    # print_grid(new_grid)
    needs_pushed = set()
    if does_end(new_grid, ending_for_player, d, needs_pushed):
        
        if d[0] != 0:
            push_hori(new_grid, ending_for_player, d, '.')
    
        else:
            new_grid = get_new_vert(new_grid, d, needs_pushed)
        pos = ending_for_player

        # if end != n:
        #     new_grid[pos[1]][pos[0]] = '.'
        #     new_grid[end[1]][end[0]] = 'O'
        # input()



# gets coords of final
total = 0
for y in range(len(new_grid)):
    for x in range(len(new_grid[0])):
        if new_grid[y][x] == '[':
            total += 100 * y + x
print(total)


# 1575877 too low

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
# dirs = []
# new_mode = False
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             if new_mode:
#                 dirs += list(line)
#             else:
#                 grid.append(list(line))
#         else:
#             new_mode = True

# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == '@':
#             pos = (x, y)

# # def dist(d1, d2):
# #     return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])

# unpack = {
#     'v': (0, 1),
#     '^': (0, -1),
#     '>': (1, 0),
#     '<': (-1, 0),
# }
# grid[pos[1]][pos[0]] = '.'

# def ends(grid, pos, d):
#     x, y = pos
#     print(f'Trying at {pos=}, with direction {d}')
#     if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
#         return False
#     if grid[y][x] == '#':
#         return False
    
#     if grid[y][x] == '.':
#         return (x, y)
    
#     return ends(grid, (pos[0] + d[0], pos[1] + d[1]), d)


# for movement in dirs:
#     d = unpack[movement]
#     n = (pos[0] + d[0], pos[1] + d[1])
#     end = ends(grid, n, d)
#     if end:
#         # print(f'{movement}, huh, n was {n}, pos was: {pos}')
#         pos = n
#         if end != n:
#             grid[pos[1]][pos[0]] = '.'
#             grid[end[1]][end[0]] = 'O'


# for y in range(len(grid)):
#     to_print = []
#     for x in range(len(grid[0])):
#         if (x, y) == pos:
#             to_print.append('@')
#         else:
#             to_print.append(grid[y][x])
#     print(''.join(to_print))
        
# # 4848 too low

# total = 0
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == 'O':
#             total += 100 * y + x
# print(total)