# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


rows = []
with open(data_file) as f:
    for line in f.read().splitlines()():
        map, constraints = line.split()

        constraints = list(map(int, constraints.split(',')))