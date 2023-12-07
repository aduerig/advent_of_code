# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

instructions = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            line = line.replace('turn ', '')

            before, last = line.split('through')
            x2, y2 = list(map(int, last.strip().split(','))) 
            on_off, first = before.strip().split('')
            x1, y1 = list(map(int, first.strip().split(',')))
            on_off = on_off.strip()
            instructions.append(on_off, [x1, y1], [x2, y2])
        instructions.append(line)


grid = [[0 for _ in range(1000)] for _ in range(1000)]
for on_off, (x1, y1), (x2, y2) in instructions:
    if x2 < x1:
        print_red('ok')
        exit()
    for 
    pass