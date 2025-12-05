# https://adventofcode.com/2023
from heapq import merge
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

ranges = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            break
        ranges.append(line.split('-'))

def merge(last_range, new_range):
    _start_1, end_1 = last_range
    start_2, end_2 = new_range

    if start_2 > end_1 + 1:
        return [start_2, end_2]
    last_range[1] = max(end_1, end_2)

        
merged_ranges = []
for a, b in sorted([sorted([int(a), int(b)]) for a, b in ranges]):
    if not merged_ranges:
        merged_ranges.append([a, b])
        continue
    optional = merge(merged_ranges[-1], [a, b])
    if optional:
        merged_ranges.append(optional)


total = 0
for a, b in merged_ranges:
    total += (b - a) + 1
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

# mode = False
# ranges = []
# nums = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if not line:
#             mode = True
#             continue


#         if mode:
#             nums.append(int(line))
#         else:
#             ranges.append(line.split('-'))

        
# total = 0
# for n in nums:
#     for a, b in ranges:
#         a, b = sorted([a, b])
#         if int(a) <= n <= int(b):
#             total += 1
#             break

# print(total)