# https://adventofcode.com/2023
import sys
import pathlib
import re

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

ingredients = []
with open(data_file) as f:
    for line in f.splitlines():
        ingredients.append(list(map(int, re.findall(r'-?\d+', line))))


def get_amts(curr, slots_left, total):
    if slots_left == 0:
        yield curr + [total]
        return
    for i in range(0, total + 1):
        yield from get_amts(curr + [i], slots_left - 1, total - i)

best = 0
for arr_of_amts in get_amts([], len(ingredients) - 1, 100):
    qualities = [0 for _ in range(5)]
    for qual_index in range(5):
        for ing_index in range(len(ingredients)):
            qualities[qual_index] += ingredients[ing_index][qual_index] * arr_of_amts[ing_index]
    if any([x < 1 for x in qualities]) or qualities[4] != 500:
        continue
    best = max(best, qualities[0] * qualities[1] * qualities[2] * qualities[3])
print(f'{best}')



# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib
# import re

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# ingredients = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             ingredients.append(list(map(int, re.findall(r'-?\d+', line))))



# def get_amts(curr, slots_left, total):
#     if slots_left == 0:
#         curr.append(total)
#         yield curr
#         curr.pop()
#         return

#     for i in range(0, total + 1):
#         curr.append(i)
#         yield from get_amts(curr, slots_left - 1, total - i)
#         curr.pop()



# best = 0
# for arr_of_amts in get_amts([], len(ingredients) - 1, 100):
#     qualities = [0 for _ in range(4)]
#     for qual_index in range(4):
#         for ing_index in range(len(ingredients)):
#             qualities[qual_index] += ingredients[ing_index][qual_index] * arr_of_amts[ing_index]
#     if any([x < 1 for x in qualities]):
#         continue

#     best = max(best, qualities[0] * qualities[1] * qualities[2] * qualities[3])

# print(f'{best:,}')