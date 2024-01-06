# 41777096
# 249136211271011

# 249136211271011 = t * (41777096 - t)
# 249136211271011 = 41777096t - t^2
# 249136211271011 = -t^2 + 41777096t
# 0 = -t^2 + 41777096t - 249136211271011

# t = (-b +- math.sqrt(b^2 - 4ac)) / 2a

# t = (-41777096 +- sqrt(pow(41777096, 2) - (4 * -1 * -249136211271011))) / -2

# t = (-41777096 +- math.sqrt(pow(41777096, 2) - (4 * -1 * -249136211271011))) / -2
# t = (-41777096 +- 27363861.297506463) / -2

# t = (-69140957.29750647 / -2), (-14413234.702493537 / -2)
# t = 34570478.64875323, 7206617.351246769

# all ts between 7206617.351246769 and 34570478.64875323 will win. meaning 34570479 - 7206618 = 27363861

# https://adventofcode.com/2023
import pathlib
import time
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

def process(f):
    return int(''.join(f.readline().split(':')[-1].strip().split()))

with open(data_file) as f:
    total_time, dist = process(f), process(f)

start_time = time.time()

def win(hold_time):
    return hold_time * (total_time - hold_time) > dist


def binary_search(want_to_win):
    left, right = 0, total_time - 1
    while left <= right:
        mid = (left + right) // 2
        if not (win(mid) ^ want_to_win):
            right = mid - 1
        else:
            left = mid + 1
    return left

print(binary_search(False) - binary_search(True))


# initial part 2 solve, takes 5.9 seconds
# ways = 0
# for hold_time in range(1, total_time):
#     remaining_time = total_time - hold_time
#     distance = hold_time * remaining_time
#     if distance > record:
#         ways += 1
        
# print_green(f'{ways}, took {time.time() - start_time} seconds')


# part 1
# # https://adventofcode.com/2023
# import pathlib

# import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# def process(f):
#     return list(map(int, f.readline().split(':')[-1].strip().split()))

# with open(data_file) as f:
#     times, records = process(f), process(f)

# ways = [0 for _ in times]
# for index, (total_time, record) in enumerate(zip(times, records)):
#     for hold_time in range(1, total_time):
#         remaining_time = total_time - hold_time
#         distance = hold_time * remaining_time
#         if distance > record:
#             ways[index] += 1

# product = ways[0]
# for way in ways[1:]:
#     product *= way
# print(product)