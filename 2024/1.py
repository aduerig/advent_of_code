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
# first_list = []
# second_list = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:

#             first, second = line.split()
#             first_list.append(int(first))
#             second_list.append(int(second))


# first_list.sort()
# second_list.sort()
# for first, second in zip(first_list, second_list):
#     total += abs(int(first) - int(second))

# print(total)


# part 2
# https://adventofcode.com/2023
