# https://adventofcode.com/2023
import sys
import pathlib
import re

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


def dfs(d):
    if type(d) == int:
        return d
    elif type(d) == list:
        return sum([dfs(s) for s in d])
    elif type(d) == dict:
        if 'red' in d or 'red' in d.values():
            return 0
        return sum([dfs(s) for s in d.values()])
    return 0

# 119433 too high


with open(data_file) as f:
    for line in f.readlines():
        print(dfs(eval(line.strip())))
        


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib
# import re

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# with open(data_file) as f:
#     for line in f.readlines():
#         print(sum(map(int, re.findall(r'-?\d+', line.strip()))))
