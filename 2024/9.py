# part 2
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
        if line:
            nums = list(map(int, line))



thing = []
for index, num in enumerate(nums):
    if index % 2 == 0:
        thing.append((num, (index + 1) // 2))
    else:
        thing.append((num, '.'))


left = 0
right = len(thing) - 1


def convert(thing):
    total_list = []
    for n, digit in thing:
        for i in range(n):
            total_list.append(digit)
    return total_list

right = len(thing) - 1
while right > 0:
    if thing[right][1] == '.':
        right -= 1
        continue

    left = 0
    while left < right:
        if thing[left][1] == '.' and thing[left][0] >= thing[right][0]:
            diff = thing[left][0] - thing[right][0]
            if diff == 0:
                thing[left] = (thing[right][0], thing[right][1])
            else:
                thing.insert(left, (thing[right][0], thing[right][1]))
                thing[left+1] = (diff, '.')
                right += 1
                left += 1
            thing[right] = (thing[right][0], '.')
            break
        left += 1
    
    right -= 1



# print(convert(thing))

c = convert(thing)
total = 0
index = 0
while index < len(c):
    num = c[index]
    if num != '.':
        total += index * int(num)
    index += 1
print(total)


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
#         if line:
#             nums = list(map(int, line))



# thing = []
# for index, num in enumerate(nums):
#     for i in range(num):
#         if index % 2 == 0:
#             thing.append((index + 1) // 2)
#         else:
#             thing.append('.')


# left = 0
# right = len(thing) - 1

# while left < right:
#     if thing[left] == '.' and thing[right] != '.':
#         thing[left], thing[right] = thing[right], thing[left]
#         right -= 1
#     elif thing[left] != '.':
#         left += 1
#     elif thing[right] == '.':
#         right -= 1

# total = 0
# index = 0
# while index < len(thing):
#     num = thing[index]
#     if num != '.':
#         total += index * int(num)
#     index += 1
# print(total)