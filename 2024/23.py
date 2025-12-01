# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


data = {}
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            a, b = line.split('-')
            if a not in data:
                data[a] = set()
            if b not in data:
                data[b] = set()
            data[b].add(a)
            data[a].add(b)

def remove_non(node, skippers, potential):
    found = set([node])
    for other in data[node]:
        found.add(other)
    # print(f'   For {node} we {found}')
    return found.intersection(potential)


def get_connections_for(node):
    potential = set([node])
    for p in data[node]:
        potential.add(p)

    # print(f'==== Looking at {node} with starters: {potential}')
    skippers = set([node])
    for p in list(potential):
        if p == node:
            continue
        if p not in potential:
            continue
        # print(f'Going into remove of {p} with {potential=}')
        potential = remove_non(p, skippers, potential)
    return potential

final = None
m = 0
for p in data:
    # if p != 'wq':
    #     continue
    res = get_connections_for(p)
    if len(res) >= m:
        m = len(res)
        final = res

ok = sorted(list(final))
print(','.join(ok))


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# data = {}
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             a, b = line.split('-')
#             if a not in data:
#                 data[a] = set()
#             if b not in data:
#                 data[b] = set()
#             data[b].add(a)
#             data[a].add(b)


# total = set()

# data_l = list(data)

# for x_index in range(len(data_l)):
#     for y_index in range(x_index+1, len(data_l)):
#         for z_index in range(y_index+1, len(data_l)):
#             x = data_l[x_index]
#             y = data_l[y_index]
#             z = data_l[z_index]
#             if x not in data[y] or x not in data[z]:
#                 continue

#             if y not in data[z]:
#                 continue
            
#             g, h, j = sorted([x, y, z])
#             if any([o.startswith('t') for o in [x, y, z]]):
#                 total.add((g, h, j))

# print(len(total))