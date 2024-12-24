# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


rules = {}
inits = {}
first = True
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            if first:
                sig, val = line.split(':')
                val = int(val.strip())
                sig = sig.strip()
                inits[sig] = val
            else:
                combos, result = line.split('->')
                result = result.strip()
                c1, op, c2 = combos.strip().split()
                if result in rules:
                    print(f'huh')
                    exit()
                rules[result] = [c1, c2, op]
        else:
            first = False

print(f'Inits: {len(inits)}')
print(f'Rules: {len(rules)}')

mapper = {
    'XOR': lambda x, y: x ^ y,
    'OR': lambda x, y: x | y,
    'AND': lambda x, y: x & y,
}

curr = dict(inits)
changed_last_iter = True
while changed_last_iter:
    changed_last_iter = False
    for to_calc, (c1, c2, op) in rules.items():
        if to_calc not in curr and c1 in curr and c2 in curr:
            curr[to_calc] = mapper[op](curr[c1], curr[c2])
            changed_last_iter = True

just_z = [(int(k[1:]), v) for k, v in curr.items() if k.startswith('z')]
just_z.sort(key=lambda x: x[0], reverse=True)

bin_str = ''
for k, v in just_z:
    bin_str += str(v)

print(f'Total: {int(bin_str, 2)}')

# to enter: 36902370467952

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# rules = {}
# inits = {}
# first = True
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             if first:
#                 sig, val = line.split(':')
#                 val = int(val.strip())
#                 sig = sig.strip()
#                 inits[sig] = val
#             else:
#                 combos, result = line.split('->')
#                 result = result.strip()
#                 c1, op, c2 = combos.strip().split()
#                 if result in rules:
#                     print(f'huh')
#                     exit()
#                 rules[result] = [c1, c2, op]
#         else:
#             first = False

# print(f'Inits: {len(inits)}')
# print(f'Rules: {len(rules)}')

# mapper = {
#     'XOR': lambda x, y: x ^ y,
#     'OR': lambda x, y: x | y,
#     'AND': lambda x, y: x & y,
# }

# curr = dict(inits)
# changed_last_iter = True
# while changed_last_iter:
#     changed_last_iter = False
#     for to_calc, (c1, c2, op) in rules.items():
#         if to_calc not in curr and c1 in curr and c2 in curr:
#             curr[to_calc] = mapper[op](curr[c1], curr[c2])
#             changed_last_iter = True

# just_z = [(int(k[1:]), v) for k, v in curr.items() if k.startswith('z')]
# just_z.sort(key=lambda x: x[0], reverse=True)

# bin_str = ''
# for k, v in just_z:
#     bin_str += str(v)

# print(f'Total: {int(bin_str, 2)}')