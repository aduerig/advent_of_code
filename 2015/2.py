# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

with open(data_file) as f:
    ok = 0
    for line in f.readlines():
        a, b, c = list(map(int, line.strip().split('x')))
        ok += min(2 * (a + b), 2 * (a + c), 2 * (c + b))
        ok += a * b * c

    print(ok)

# part 1 
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# with open(data_file) as f:
#     ok = 0
#     for line in f.readlines():
#         a, b, c = list(map(int, line.strip().split('x')))
        
#         ok += (2 * a * b) + (2 * b * c) + (2 * c * a)
#         ok += min(a * b, b * c, c * a)


#     print(ok)