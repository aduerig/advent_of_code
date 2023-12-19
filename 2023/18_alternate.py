# https://adventofcode.com/2023
import pathlib
import sys
import random

sys.setrecursionlimit(500000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath('18.dat')

dirs_index = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

instructions = []
with open(data_file) as f:
    for line in f.read().splitlines():
        _letter, _amt_flat, color = line.split()
        amt_from_hex, direction_index = int(color[2:-2], 16), int(color[-2])
        instructions.append((amt_from_hex, dirs_index[direction_index]))


actual_grid = {}
pos = (0, 0)
corners = set([pos])
for index, (amt, dpos) in enumerate(instructions):
    dx, dy = dpos
    
    print(f'{index+1}/{len(instructions)} - {amt} - {dpos}')
    pos = (pos[0] + (dx * amt)), (pos[1] + (dy * amt))
    corners.add(pos)

    actual_grid[pos] = True


print(pos)
print(corners)


def find_smallest(corners, given, given_index, bigger_than, bigger_index):
    found = None
    for point in corners:
        if point[given_index] != given:
            continue
        if point[bigger_index] <= bigger_than:
            continue
        
        if not found or point[bigger_index] < found[bigger_index]:
            found = point
    return found

unused = set(corners)
while unused:
    for point in unused:
        unused.remove(point)
        break

    x, y = point
    right_point = find_smallest(corners, y, 1, x, 0)
    down_point = find_smallest(corners, y, 1, x, 0)
    down_right_point = (right_point, down_point)

    if not right_point or not down_point or not down_right_point:
        continue





# test is: 952408144115