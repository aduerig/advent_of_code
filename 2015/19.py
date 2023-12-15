# https://adventofcode.com/2023
import sys
import pathlib
from queue import PriorityQueue 
import random
sys.setrecursionlimit(10000)
  

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

def split_into_chemicals(string):
    arr = []
    i = 0
    while i < len(string):
        a = string[i]
        if i != len(string) - 1 and string[i+1].islower():
            a += string[i+1]
            i += 1
        arr.append(a)
        i += 1
    return tuple(arr)

mapping = {}
with open(data_file) as f:
    lines = f.read().splitlines()
    for index, line in enumerate(lines):
        if not line:
            goal = lines[index + 1]
            break

        fr, to = line.split(' => ')
        if fr not in mapping:
            mapping[fr] = []
        mapping[fr].append(split_into_chemicals(to))

goal_chemicals = split_into_chemicals(goal)

def can_reduce(chemical):
    if chemical not in mapping:
        return False
    
    for sub in mapping[chemical]:
        if chemical not in sub:
            return False
    return True


import functools
seen = set()
@functools.cache
def dfs_left(chemical, goal_chemical):
    if chemical in seen:
        return False
    seen.add(chemical)
    for resultant_chemicals in mapping.get(chemical, tuple()):
        if resultant_chemicals[0] == goal_chemical:
            return True
        if dfs_left(resultant_chemicals[0], goal_chemical):
            return True
    return False


def is_possible_left(chemicals, goal_chemicals):
    global seen
    for chemical, goal_chem in zip(chemicals, goal_chemicals):
        if chemical != goal_chem:
            seen = set()
            return dfs_left(chemical, goal_chem)
    return True


avaliable = {}
for chemical in goal_chemicals:
    if not can_reduce(chemical):
        avaliable[chemical] = goal_chemicals.count(chemical)
print(avaliable)
print(f'Win when have: {len(goal_chemicals)} chemicals')

seen_depths = set()

queue = PriorityQueue()
queue.put([0, -1, tuple(['e']), 0, avaliable.copy()])
# queue = collections.deque([['e', 0]])

cache = set()
linear_increaser = 1
max_len = 0

cut_from_no_more = 0
cut_from_too_long = 0
cut_from_visited = 0
cut_from_left_possible = 0
looked_at = 0
while not queue.empty():
    # curr, the_len, depth = queue.popleft()
    depth, the_len, curr, _, avaliable = queue.get_nowait()
    if curr == goal_chemicals:
        print_green('SUCCESS')
        break

    if -the_len > len(goal_chemicals):
        cut_from_too_long += 1
        continue

    if curr in cache:
        cut_from_visited += 1
        continue
    cache.add(curr)

    if not is_possible_left(curr, goal_chemicals):
        cut_from_left_possible += 1
        continue

    looked_at += 1

    if random.random() < .0001:
        print_blue(f'    random chemical: {"".join(curr)}')
        print_cyan(f'    {looked_at=:,}, {cut_from_left_possible=:,}, {cut_from_no_more=:,}, {cut_from_too_long=:,}, {cut_from_visited=:,}')

    if depth not in seen_depths:
        seen_depths.add(depth)
        print(f'{depth=}, {max_len=}')

    max_len = max(max_len, len(curr))
    for index, chemical in enumerate(curr):
        prev = curr[:index]
        for resultant_chemicals in mapping.get(chemical, tuple()):
            new_avaliable = avaliable.copy()
            
            no_good = False
            for sub_chemical in resultant_chemicals:
                if sub_chemical in new_avaliable:
                    new_avaliable[sub_chemical] -= 1
                    if new_avaliable[sub_chemical] < 0:
                        no_good = True
                        break
            if no_good:
                cut_from_no_more += 1
                continue

            new = prev + resultant_chemicals + curr[index + 1:]
            queue.put([depth + 1, -len(new), new, linear_increaser, new_avaliable])
            linear_increaser += 1

print(f'{depth} - produced: {curr}')

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# mapping = {}
# with open(data_file) as f:
#     lines = f.read().splitlines()
#     for index, line in enumerate(lines):
#         if not line:
#             seq = lines[index + 1]
#             break

#         fr, to = line.split(' => ')
#         if fr not in mapping:
#             mapping[fr] = []
#         mapping[fr].append(to)

# possible = set()
# for index in range(len(seq)):
#     prev = seq[:index]
#     curr_till_end = seq[index:]
#     for input, outputs in mapping.items():
#         if curr_till_end.startswith(input):
#             rest = seq[index + len(input):]
#             for out in outputs:
#                 possible.add(prev + out + rest)
# print(len(possible))



# this is nonsense
# # https://adventofcode.com/2023
# import sys
# import pathlib
# from tqdm import tqdm

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# mapping = {}
# with open(data_file) as f:
#     lines = f.read().splitlines()
#     for index, line in enumerate(lines):
#         if not line:
#             seq = lines[index + 1]
#             break

#         fr, to = line.split(' => ')
#         if fr not in mapping:
#             mapping[fr] = []
#         mapping[fr].append(to)

# chemicals = []
# index = 0
# while index < len(seq):
#     chemical = seq[index]
#     if index != len(seq) - 1 and seq[index+1].islower():
#         chemical += seq[index+1]
#     if chemical in mapping:
#         chemicals.append(chemical)
#     index += len(chemical)

# building = set([''])
# for index, chemical in tqdm(enumerate(chemicals), total=len(chemicals)):
#     new_building = set()
#     for out in mapping.get(chemical, [chemical]):
#         for build in building:
#             new_building.add(build + out)
#     building = new_building
# print(len(building))



# # 627 too high