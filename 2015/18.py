# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


state = []
with open(data_file) as f:
    for line in f.read().splitlines():
        state.append(list(line))


def get_neigh(state, x, y):
    total = 0
    for new_x, new_y in [
            (x + 1, y + 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y - 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y),
            (x - 1, y),
        ]:
        if new_x < 0 or new_y < 0 or new_x == len(state[0]) or new_y == len(state) or state[new_y][new_x] == '.':
            continue
        total += 1
    return total


for i in range(100):
    new_state = [[state[y][x] for x in range(len(state[y]))] for y in range(len(state))]
    for y, arr in enumerate(state):
        for x, val in enumerate(arr):
            if (x, y) in [(0, 0), (0, len(state) - 1), (len(state[0]) - 1, 0), (len(state[0]) - 1, len(state) - 1)]:
                continue
            neigh = get_neigh(state, x, y)
            if val == '#':
                if neigh not in [2, 3]:
                    new_state[y][x] = '.'
            else:
                if neigh == 3:
                    new_state[y][x] = '#'    
    state = new_state

print(sum([x.count('#') for x in state]))


# part 1
# https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# state = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         state.append(list(line))


# def get_neigh(state, x, y):
#     total = 0
#     for new_x, new_y in [
#             (x + 1, y + 1),
#             (x - 1, y + 1),
#             (x + 1, y - 1),
#             (x - 1, y - 1),
#             (x, y - 1),
#             (x, y + 1),
#             (x + 1, y),
#             (x - 1, y),
#         ]:
#         if new_x < 0 or new_y < 0 or new_x == len(state[0]) or new_y == len(state) or state[new_y][new_x] == '.':
#             continue
#         total += 1
#     return total


# for i in range(4):
#     new_state = [[state[y][x] for x in range(len(state[y]))] for y in range(len(state))]

#     print(f'State: {i}:')
#     for y, arr in enumerate(state):
#         print(''.join(arr))

#     for y, arr in enumerate(state):
#         for x, val in enumerate(arr):
#             neigh = get_neigh(state, x, y)
#             if val == '#':
#                 if neigh not in [2, 3]:
#                     new_state[y][x] = '.'
#             else:
#                 if neigh == 3:
#                     new_state[y][x] = '#'    
#     state = new_state

# print(sum([x.count('#') for x in state]))