# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

with open(data_file) as f:
    a = 0
    for index, c in enumerate(f.readline()):
        if c == '(':
            a += 1
        else:
            a -= 1
        if a == -1:
            print(index + 1)
            exit()