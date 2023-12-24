# https://adventofcode.com/2023
import pathlib
import sys
from copy import deepcopy

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

def to_char(label):
    return chr(label + ord('A'))


# 5,0,87~8,0,87
cube_at = {}
cubes = []
max_x, max_y, max_z = 0, 0, 0
with open(data_file) as f:
    for label, line in enumerate(f.read().splitlines()):
        start, end = line.split('~')

        x1, y1, z1 = list(map(int, start.split(',')))
        x2, y2, z2 = list(map(int, end.split(',')))

        cubes.append((label, (x1, y1, z1), (x2, y2, z2)))
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    cube_at[(x, y, z)] = label
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                    max_z = max(max_z, z)


def print_board():
    for z in range(max_z, -1, -1):
        row = []
        for x in range(0, max_x+1):
            if z == 0:
                row.append('-')
            else:
                row.append('.')
            for y in range(0, max_y+1):
                if (x, y, z) in cube_at:
                    row[-1] = to_char(cube_at[(x, y, z)])
        print(''.join(row))


def settle(lookup, cube):
    label, (x1, y1, z1), (x2, y2, z2) = cube
    def get_fallen():
        for fallen, z in enumerate(range(z1 - 1, -1, -1)):
            if z == 0:
                return fallen
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if (x, y, z) in lookup:
                        return fallen
    fallen = get_fallen()
    return (label, (x1, y1, z1 - fallen), (x2, y2, z2 - fallen))

settled_cubes = []
for cube in sorted(cubes, key=lambda x: x[1][2]):
    new_cube = settle(cube_at, cube)
    label, (x1, y1, z1), (x2, y2, z2) = new_cube

    to_del = []
    for k, old_label in cube_at.items():
        if old_label == label:
            to_del.append(k)
    for d in to_del:
        del cube_at[d]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                cube_at[(x, y, z)] = label

    settled_cubes.append(new_cube)


moved = 0
for index, disintegrate_cube in enumerate(settled_cubes):
    print(f'{index=}')
    new_cube_at = deepcopy(cube_at)
    for k, old_label in cube_at.items():
        if old_label == disintegrate_cube[0]:
            del new_cube_at[k]

    for cube in sorted(settled_cubes, key=lambda x: x[1][2]):
        if cube == disintegrate_cube:
            continue

        new_cube = settle(new_cube_at, cube)
        if new_cube == cube:
            continue
        moved += 1

        label, (x1, y1, z1), (x2, y2, z2) = new_cube

        to_del = []
        for k, old_label in new_cube_at.items():
            if old_label == label:
                to_del.append(k)
        for d in to_del:
            del new_cube_at[d]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    new_cube_at[(x, y, z)] = label

print_green(f'{moved}')


# part 1
# # https://adventofcode.com/2023
# import pathlib

# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# def to_char(label):
#     return chr(label + ord('A'))


# # 5,0,87~8,0,87
# cube_at = {}
# cubes = []
# max_x, max_y, max_z = 0, 0, 0
# with open(data_file) as f:
#     for label, line in enumerate(f.read().splitlines()):
#         start, end = line.split('~')

#         x1, y1, z1 = list(map(int, start.split(',')))
#         x2, y2, z2 = list(map(int, end.split(',')))

#         cubes.append((label, (x1, y1, z1), (x2, y2, z2)))
#         for x in range(x1, x2+1):
#             for y in range(y1, y2+1):
#                 for z in range(z1, z2+1):
#                     cube_at[(x, y, z)] = label
#                     max_x = max(max_x, x)
#                     max_y = max(max_y, y)
#                     max_z = max(max_z, z)


# def print_board():
#     for z in range(max_z, -1, -1):
#         row = []
#         for x in range(0, max_x+1):
#             if z == 0:
#                 row.append('-')
#             else:
#                 row.append('.')
#             for y in range(0, max_y+1):
#                 if (x, y, z) in cube_at:
#                     row[-1] = to_char(cube_at[(x, y, z)])
#         print(''.join(row))


# def settle(cube):
#     label, (x1, y1, z1), (x2, y2, z2) = cube
#     def get_fallen():
#         for fallen, z in enumerate(range(z1 - 1, -1, -1)):
#             if z == 0:
#                 return fallen
#             for x in range(x1, x2+1):
#                 for y in range(y1, y2+1):
#                     if (x, y, z) in cube_at:
#                         return fallen
#     fallen = get_fallen()
#     return (label, (x1, y1, z1 - fallen), (x2, y2, z2 - fallen))

# max_x, max_y, max_z = 0, 0, 0
# settled_cubes = []
# for cube in sorted(cubes, key=lambda x: x[1][2]):
#     new_cube = settle(cube)
#     label, (x1, y1, z1), (x2, y2, z2) = new_cube

#     to_del = []
#     for k, old_label in cube_at.items():
#         if old_label == label:
#             to_del.append(k)
#     for d in to_del:
#         del cube_at[d]
#     for x in range(x1, x2+1):
#         for y in range(y1, y2+1):
#             for z in range(z1, z2+1):
#                 if (x, y, z) in cube_at:
#                     print('lol')
#                     exit()
#                 cube_at[(x, y, z)] = label

#     settled_cubes.append(new_cube)
#     max_x = max(max_x, x2)
#     max_y = max(max_y, y2)
#     max_z = max(max_z, z2)

# def search_up(cube):
#     label, (x1, y1, z1), (x2, y2, z2) = cube
#     supports = set()
#     for y in range(y1, y2+1):
#         for x in range(x1, x2+1):
#             if (x, y, z2+1) in cube_at:
#                 supports.add(cube_at[(x, y, z2+1)])
#     return supports


# supported_by = {}
# for cube in settled_cubes:
#     label = cube[0]
#     for what_i_support in search_up(cube):
#         if what_i_support not in supported_by:
#             supported_by[what_i_support] = []
#         supported_by[what_i_support].append(label)

# found = set()
# for needs_support, supported_by_arr in supported_by.items():
#     if len(supported_by_arr) == 1:
#         found.add(supported_by_arr[0])

# for label in sorted(found):
#     print(f'{to_char(label)} is integral')

# print_green(f'{len(cubes) - len(found)}, {len(cubes)=}, {len(found)=}')

