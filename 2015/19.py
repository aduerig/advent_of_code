# https://adventofcode.com/2023
import sys
import pathlib
import collections

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

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
        mapping[fr].append(to)

seen_depths = set()
queue = collections.deque([['e', 0]])
print_blue(f'Looking for goal len of {len(goal)}')

cache = set()
max_len = 0
while queue:
    curr, depth = queue.popleft()
    if curr == goal:
        break

    if curr in cache:
        continue

    cache.add(curr)

    if depth not in seen_depths:
        seen_depths.add(depth)
        print(f'{depth=}, {max_len=}')

    max_len = max(max_len, len(curr))
    for index in range(len(curr)):
        prev = curr[:index]
        curr_till_end = curr[index:]
        for input, outputs in mapping.items():
            if curr_till_end.startswith(input):
                rest = curr[index + len(input):]
                for out in outputs:
                    queue.append([prev + out + rest, depth + 1])
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