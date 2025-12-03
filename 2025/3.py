# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


def find_from_back(line, start_index=0):
    print(f'find_from_back called with start_index={start_index}')
    pointer = start_index
    largest = [None, None]
    while pointer >= 0:
        n = int(line[pointer])

        if largest[0] is None:
            largest = [n, pointer + 1]
        else:
            if n >= largest[0]:
                largest = [n, pointer + 1]
        pointer -= 1
    print(f'find_from_back returning largest={largest}')
    return largest



def find_forward(line, left, start_index=0):
    print(f'find_forward called with left={left}, start_index={start_index}, seeing whats avaliable as {line[start_index:]}')
    largest = [int(line[start_index]), start_index + 1]
    pointer = start_index + 1
    while pointer + (left - 1) < len(line):
        n = int(line[pointer])
        if n > largest[0]:
            largest = [n, pointer + 1]
        pointer += 1
    print(f'find_forward returning largest={largest}')
    return largest

total = 0
with open(data_file) as f:
    for index, line in enumerate(f.readlines()):
        line = line.strip()

        largest, curr_index = find_from_back(line, start_index=len(line)-13)
        print(f'initial largest={largest}, curr_index={curr_index}')
        build = [largest]
        for left in range(11, 0, -1):
            largest, curr_index = find_forward(line, left, start_index=curr_index)
            print(f'left={left}, largest={largest}, curr_index={curr_index}')
            build.append(largest)
        
        best = int(''.join([str(x) for x in build]))
        total += best
        print(f'{best=}')



if total <= 170416932730169 and total != 3121910778619:
    print_red(total)
else:
    print_green(total)


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# total = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()

#         best_score = 0 
#         highest_yet = None
#         for num in line:
#             if highest_yet is None:
#                 highest_yet = int(num)
#                 continue
#             best_score = max(highest_yet * 10 + int(num), best_score)
#             highest_yet = max(highest_yet, int(num))
#         total += best_score

# print(total)