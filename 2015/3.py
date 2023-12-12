# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

poses = [(0, 0), (0, 0)]
amt = {(0, 0)}
with open(data_file) as f:
    for index, c in enumerate(f.readline().strip()):
        x, y = poses[index % 2]
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1
        poses[index % 2] = (x, y)
        amt.add(poses[index % 2])
print(len(amt))