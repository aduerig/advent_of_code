# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

def md5(s):
    import hashlib
    return hashlib.md5(s.encode()).hexdigest()

with open(data_file) as f:
    key = f.readline().strip()

    for i in range(1, 10000000000):
        if md5(key + str(i)).startswith('000000'):
        # if md5(key + str(i)).startswith('00000'): # part 1
            print(i)
            exit()