# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()


# 1227775554
def invalid(n):
    s = str(n)
    half = len(s) // 2

    for chunk_length in range(1, half+1):
        if len(s) % chunk_length != 0:
            continue

        chunks = []
        for i in range(len(s) // chunk_length):
            chunks.append(s[i*chunk_length:(i+1)*chunk_length])
        
        if all([c == chunks[0] for c in chunks]):
            return True
    return False



for i in range(200):
    print(f'{i}: {invalid(i)}')

total = 0
ranges = line.split(',')
for r in ranges:
    first_id, last_id = map(lambda x: int(x.strip()), r.split('-'))
    print(f'Processing range {first_id}-{last_id}')
    for i in range(first_id, last_id + 1):
        if invalid(i):
            total += i

print(total)

# 1227775554
# 651329497582753


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()


# # 1227775554
# def invalid(n):
#     s = str(n)
#     if len(s) % 2 == 0:
#         half = len(s) // 2
#         a, b = s[:half], s[half:]
#         return a == b
#     return False

# for i in range(200):
#     print(f'{i}: {invalid(i)}')

# total = 0
# ranges = line.split(',')
# for r in ranges:
#     first_id, last_id = map(lambda x: int(x.strip()), r.split('-'))
#     print(f'Processing range {first_id}-{last_id}')
#     for i in range(first_id, last_id + 1):
#         if invalid(i):
#             total += i

# print(total)

# # 1227775554
# # 651329497582753