# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

data = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            data.append(int(line))

def mix(secret, other):
    return secret ^ other

def prune(secret):
    return secret % 16777216


total = 0
counter = {}
for starter in data:
    prev = int(str(starter)[-1])
    curr = starter
    diffies = []
    for s in range(2000):
        curr = mix(curr, curr * 64)
        curr = prune(curr)

        curr = mix(curr, curr // 32)
        curr = prune(curr)

        curr = mix(curr, curr * 2048)
        curr = prune(curr)
    
        last = int(str(curr)[-1])

        if prev is not None:
            diff = last - prev
            # print(diff)
            diffies.append(diff)
            if len(diffies) > 4:
                diffies.pop(0)
            the_seq = tuple(diffies)

            if len(diffies) == 4:
                if the_seq not in counter:
                    counter[the_seq] = {}
                if starter not in counter[the_seq]:
                    counter[the_seq][starter] = last

        prev = last
    
# for k, v in counter.items():
#     print(f'{k}: {v}')

stuff = list(counter.items())


the_max = 0
for k, v in stuff:
    total = sum(list(v.values()))
    the_max = max(the_max, total)
print(the_max)


# 326 too low


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# data = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             data.append(int(line))

# def mix(secret, other):
#     return secret ^ other

# def prune(secret):
#     return secret % 16777216

# total = 0
# for starter in data:
#     curr = starter
#     for s in range(2000):
#         curr = mix(curr, curr * 64)
#         curr = prune(curr)

#         curr = mix(curr, curr // 32)
#         curr = prune(curr)

#         curr = mix(curr, curr * 2048)
#         curr = prune(curr)
#     total += curr
#     print(f'{starter}: {curr}')
# print(total)