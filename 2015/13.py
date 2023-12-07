# https://adventofcode.com/2023
import sys
import pathlib
import re
import random

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


m = {}
people = set()
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            units = int(re.search(r'\d+', line)[0])
            if 'lose' in line:
                units *= -1

            a = re.search(r'\w+', line)[0]
            b = re.search(r'\w+', line[::-1])[0][::-1]
            people.add(a)
            people.add(b)
            m[(a, b)] = units


for p in people:
    m[('me', p)] = 0
    m[(p, 'me')] = 0

people.add('me')

def perms(index, collection, builder):
    if index == len(collection):
        yield builder
        return
    for ele in collection:
        if ele not in builder:
            builder.append(ele)
            yield from perms(index + 1, collection, builder)
            builder.pop()

for k, v in m.items():
    print(f'{k}: {v}')

best = 0
for perm in perms(0, list(people), []):
    total = 0
    for i in range(len(perm)):
        if i == 0:
            last = perm[-1]
        else:
            last = perm[i-1]
        total += m[(perm[i], last)]
        total += m[(last, perm[i])]
    best = max(best, total) 
        
print(best)



# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib
# import re
# import random

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# m = {}
# people = set()
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             units = int(re.search(r'\d+', line)[0])
#             if 'lose' in line:
#                 units *= -1

#             a = re.search(r'\w+', line)[0]
#             b = re.search(r'\w+', line[::-1])[0][::-1]
#             people.add(a)
#             people.add(b)
#             m[(a, b)] = units

# def perms(index, collection, builder):
#     if index == len(collection):
#         yield builder
#         return
#     for ele in collection:
#         if ele not in builder:
#             builder.append(ele)
#             yield from perms(index + 1, collection, builder)
#             builder.pop()

# for k, v in m.items():
#     print(f'{k}: {v}')

# best = 0
# for perm in perms(0, list(people), []):
#     total = 0
#     for i in range(len(perm)):
#         if i == 0:
#             last = perm[-1]
#         else:
#             last = perm[i-1]
#         total += m[(perm[i], last)]
#         total += m[(last, perm[i])]
#     best = max(best, total) 
        
# print(best)