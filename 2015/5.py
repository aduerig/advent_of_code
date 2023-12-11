import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')
    
def has_twice(s):
    for index in range(len(s) - 1):
        looking_for = s[index:index + 2]        
        if looking_for in s[:index] or looking_for in s[index + 2:]:
            return True
    return False


def in_between(line):
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            return True
    return False


nice = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            trying = 0
            if has_twice(line):
                print_green(f'has_twice! {line}')
                trying += 1
            if in_between(line):
                print_green(f'in_between! {line}')
                trying += 1
            if trying == 2:
                nice += 1

print(nice)
# part 1
# https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')
    



# nice = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             if line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u') < 3:
#                 continue
#             if line.count('ab') + line.count('cd') + line.count('pq') + line.count('xy') > 0:
#                 continue
#             if not any([a == b for a, b in zip(line, line[1:])]):
#                 continue
#             nice += 1

# print(nice)