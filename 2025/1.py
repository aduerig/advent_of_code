# im sorry for what I had to do

# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


curr = 50
total = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()

        d, amt = line[0], int(line[1:])
        if d == 'L':
            for i in range(amt):
                curr -= 1
                if curr == 0:
                    total += 1
                if curr < 0:
                    curr = 99
        elif d == 'R':
            for i in range(amt):
                curr += 1
                if curr == 100:
                    total += 1
                if curr > 99:
                    curr = 0
print(total) 