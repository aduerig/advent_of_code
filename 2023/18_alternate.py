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
pos = (0, 0)
with open(data_file) as f:
    for line in f.read().splitlines():
        _letter, _amt_flat, color = line.split()
        amt_from_hex, direction_index = int(color[2:-2], 16), int(color[-2])
        instructions.append((amt_from_hex, dirs_index[direction_index]))


corners = []

all_visited = set([pos])
for index, (amt, dpos) in enumerate(instructions):
    dx, dy = dpos
    
    print(f'{index+1}/{len(instructions)} - {amt} - {dpos}')
    for i in range(int(amt)):
        new_pos = pos[0] + dx, pos[1] + dy

        all_visited.add(new_pos)
print(new_pos)
# test is: 952408144115