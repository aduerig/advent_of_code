# https://adventofcode.com/2023
import pathlib
import sys
import time
from tqdm import tqdm

filepath = pathlib.Path(__file__).resolve()
sys.path.append(str(filepath.parent.parent))
from helpers import *

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# 1    2    3    4   5
# 3    18   108  648 3888 

# (b311) zetai 2023$ python 12.py
# 1 - combinations: 3, total so far: 0
# 2 - combinations: 4, total so far: 0
# 3 - combinations: 16, total so far: 0
# 4 - combinations: 11, total so far: 0
# 5 - combinations: 9, total so far: 0
# (b311) zetai 2023$ python 12.py
# 1 - combinations: 18, total so far: 0
# 2 - combinations: 33, total so far: 0
# 3 - combinations: 775, total so far: 0
# 4 - combinations: 135, total so far: 0
# 5 - combinations: 227, total so far: 0
# (b311) zetai 2023$ python 12.py
# 1 - combinations: 108, total so far: 0
# 2 - combinations: 311, total so far: 0
# 3 - combinations: 44583, total so far: 0
# 4 - combinations: 1779, total so far: 0
# 5 - combinations: 6379, total so far: 0
# (b311) zetai 2023$ 


problems = []
with open(data_file) as f:
    for line in f.read().splitlines():
        springs, constraints = line.split()
        duplications = 3
        springs = '?'.join([springs for _ in range(duplications)])
        constraints = ','.join([constraints for _ in range(duplications)])

        constraints = list(map(int, constraints.split(',')))
        problems.append([springs, constraints])

@profile
def recurse(spring, spring_index, constraints, constraint_index, to_place):
    if to_place == 0:
        while spring_index < len(spring):
            if spring[spring_index] == '#':
                return 0
            spring_index += 1
        return 1
    spaces_left = len(spring) - spring_index
    if to_place > spaces_left:
        return 0

    condition, num = spring[spring_index], constraints[constraint_index]
    total = 0
    if condition != '#':
        total += recurse(spring, spring_index + 1, constraints, constraint_index, to_place)

    if condition != '.':
        start = 0
        while start < num:
            if spring[start + spring_index] == '.':
                return total
            start += 1
        if num == spaces_left or spring[num + spring_index] != '#':
            total += recurse(spring, spring_index + num + 1, constraints, constraint_index + 1, to_place - num)
    return total

times_per_iter = []
start_time = time.time()
all_possible = 0
for index, (spring, constraints) in enumerate(problems, start=1):
# for index, (spring, constraints) in tqdm(enumerate(problems, start=1), total=len(problems)):
    start_iter_time = time.time()
    print(f'Working on {spring} - {constraints}')
    value = recurse(spring, 0, constraints, 0, sum(constraints))
    times_per_iter.append([time.time() - start_iter_time, index])
    print(f'{index} - combinations: {value}, total so far: {all_possible}')

times_per_iter.sort(reverse=True)

print_cyan(f'{duplications} - Top 10 slowest:')
for i in times_per_iter[:10]:
    print(f'    {i[1]} - {i[0]:.5f}')
print_green(f'Took {time.time() - start_time:.5f} seconds to complete all')
print(all_possible)


# print_blue(f'Looking to place - {spring[spring_index:]} - {constraints    l[constraint_index:]}')
# print_blue(f'placing! next is - {spring[spring_index + num + 1:]} - {constraints[constraint_index + 1:]}')




# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# problems = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         springs, constraints = line.split()
#         constraints = list(map(int, constraints.split(',')))
#         problems.append([springs, constraints])

# def recurse(spring, constraints):
#     if not constraints:
#         if all([x != '#' for x in spring]):
#             return 1
#         else:
#             return 0
#     if not spring:
#         return 0
#     condition, num = spring[0], constraints[0]

#     total = 0
#     try_place_springs = False
#     if condition == '#':
#         try_place_springs = True
#     elif condition == '.':
#         total += recurse(spring[1:], constraints)
#     else:
#         total += recurse(spring[1:], constraints)
#         try_place_springs = True

#     if try_place_springs and len(spring) >= num:
#         can_place = all([spring[i] != '.' for i in range(num)]) and (num == len(spring) or spring[num] != '#')
#         # print(f'Trying to place!\n{spring} - {constraints} - {can_place=}, next call is: {spring[num+1:]} and {constraints[1:]}')
#         if can_place:
#             total += recurse(spring[num+1:], constraints[1:])
#     return total

# all_possible = 0
# for index, (spring, constraints) in enumerate(problems, start=1):
#     print(f'INITIAL: {spring} - {blue(constraints)}')
#     value = recurse(spring, constraints)
#     all_possible += value
#     print(f'{index} - combinations: {value}, total so far: {all_possible}')

# print_green(all_possible)