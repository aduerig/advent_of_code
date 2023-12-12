# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



nums = []
with open(data_file) as f:
    for line in f.read().splitlines():
        nums.append(int(line))

totals = []
def recurse(amnts, index, left, used):
    if left == 0:
        totals.append(used)
        return
    if left < 0 or index == len(amnts):
        return
    recurse(amnts, index+1, left, used)
    recurse(amnts, index+1, left - amnts[index], used + 1)


recurse(nums, 0, 150, 0)
print(totals.count(min(totals)))

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# nums = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         nums.append(int(line))

# total = 0
# def recurse(amnts, index, left):
#     global total
#     if left == 0:
#         total += 1
#         return
#     if left < 0 or index == len(amnts):
#         return

#     recurse(amnts, index+1, left)
#     recurse(amnts, index+1, left - amnts[index])


# recurse(nums, 0, 150)
# print_green(total)
