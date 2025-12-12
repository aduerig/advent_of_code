# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line
        if line.strip() == '':
            continue
        grid.append(list(line))



def get_nums(nums, x):
    build = []
    for y in range(len(nums)):
        val = nums[y][x]
        if val == ' ':
            continue
        build.append(val)
    
    if not build:
        return None
    return int(''.join(build))


nums = grid[:-1]
ops = grid[-1]

total = 0
so_far = []
saved_op = None
for x, op in enumerate(ops):
    nums_at_x = get_nums(nums, x)
    if op != ' ':
        if so_far:
            print(so_far)
            yeah = f'{saved_op}'.join([str(s) for s in so_far])
            total += eval(yeah)
            so_far = []
        saved_op = op
    if nums_at_x is not None:
        so_far.append(nums_at_x)
if so_far:
    yeah = f'{saved_op}'.join([str(s) for s in so_far])
    total += eval(yeah)
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


# all_stuff = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         line = line.split()
#         all_stuff.append(line)



# nums = all_stuff[:-1]
# ops = all_stuff[-1]


# for index, ns in enumerate(nums):
#     nums[index] = [int(n) for n in ns]


# total = 0
# for x in range (len(nums[0])):
#     agg = []
#     for y in range(len(nums)):
#         val = nums[y][x]
#         agg.append(val)
#     yeah = f'{ops[x]}'.join([str(a) for a in agg])
#     total += eval(yeah)
    
# print(total)