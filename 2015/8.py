# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

total = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            encoded = line.replace('\\', '\\\\').replace('"', '\\"')
            total += (2 + len(encoded)) - len(line)

print(total)

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# total = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             memory = len(eval(line))
#             total += len(line) - memory

# print(total)