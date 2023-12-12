# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


space = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            space.append(line)

fully_blank = [{}, {}]
for y, line in enumerate(space):
    if all([x == '.' for x in line]):
        fully_blank[1][y] = True
for x in range(len(space[0])):
    if all([space[y][x] == '.' for y in range(len(space))]):
        fully_blank[0][x] = True


galaxies = []
for y in range(len(space)):
    for x in range(len(space[0])):
        if space[y][x] == '#':
            galaxies.append((x, y))


def traverse(p1, p2, axis):
    p1, p2 = min(p1, p2), max(p1, p2)
    agg = 0
    for new_p in range(p1+1, p2+1):
        if new_p in fully_blank[axis]:
            agg += 999999
        agg += 1
    return agg


total = 0
for i1, gal_1 in enumerate(galaxies):
    for i2, gal_2 in enumerate(galaxies[i1+1:], start=i1+1):
        total += traverse(gal_1[0], gal_2[0], 0)
        total += traverse(gal_1[1], gal_2[1], 1)
print_green(total)



# for y in range(len(space)):
#     for x in range(len(space[0])):
#         if (x, y) in multiplier:
#             print_blue('#', end='')
#         else:
#             print('#', end='')
#     print()

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# space = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             space.append(line)

# def expand(space):
#     new_space = []
#     for line in space:
#         if all([x == '.' for x in line]):
#             new_space.append(line)
#         new_space.append(line)
#     return new_space

# space = expand(space)

# rotated_space = []
# for x in range(len(space[0])):
#     rotator = [space[y][x] for y in range(len(space))]
#     rotated_space.append(list(reversed(rotator)))

# space = expand(rotated_space)






# galaxies = []
# for y in range(len(space)):
#     for x in range(len(space[0])):
#         ele = space[y][x]
#         if ele == '#':
#             galaxies.append((x, y))


# total = 0
# for i1, galaxy in enumerate(galaxies):
#     x, y = galaxy
#     for i2, other in enumerate(galaxies[i1+1:], start=i1+1):
#         if i1 == i2:
#             continue
#         ox, oy = other
#         dx, dy = ox - x, oy - y

#         distance = abs(dx) + abs(dy)
#         total += distance
#         print_blue(f'{i1+1} - {i2+1} = {distance}')

# print_green(total)