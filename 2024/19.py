# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


to_try = []
with open(data_file) as f:
    possible = list(map(lambda x: x.strip(), f.readline().strip().split(',')))
    f.readline()
    for line in f.readlines():
        line = line.strip()
        if line:
            to_try.append(line)

cache = {}
def combos(corpus, goal):
    if not goal:
        return 1
    
    result = False
    if goal not in cache:
        for i in corpus:
            if goal.startswith(i):
                result += combos(corpus, goal[len(i):])
        cache[goal] = result
    return cache[goal]

total = 0
for to_make in to_try:
    total += combos(possible, to_make)
print(total)


# # part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# to_try = []
# with open(data_file) as f:
#     possible = list(map(lambda x: x.strip(), f.readline().strip().split(',')))
#     f.readline()
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             to_try.append(line)

# cache = {}
# def is_possible(corpus, goal):
#     if not goal:
#         return True
    
#     result = False
#     if goal not in cache:
#         for i in corpus:
#             if goal.startswith(i):
#                 if is_possible(corpus, goal[len(i):]):
#                     result = True
#                     break
        
#         cache[goal] = result
#     return cache[goal]

# total = 0
# for to_make in to_try:
#     if is_possible(possible, to_make):
#         total += 1
# print(total)