# https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# safe = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
        
#         if line:
#             levels = line.split()
#             inc = None
#             good = True
#             for a, b in zip(levels, levels[1:]):
#                 a = int(a)
#                 b = int(b)
#                 if inc is None:
#                     if a < b:
#                         inc = True
#                     elif a > b:
#                         inc = False
#                     else:
#                         good = False
#                         break
#                 if inc and a > b:
#                     good = False
#                     break
#                 if not inc and a < b:
#                     good = False
#                     break
#                 if abs(a - b) > 0 and abs(a - b) < 4:
#                    pass
#                 else:
#                     good = False
#                     break 
#             if good:
#                 safe += 1

# print(safe) 


# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


def is_safe(level):
    inc = None
    good = True
    for a, b in zip(level, level[1:]):
        a = int(a)
        b = int(b)
        if inc is None:
            if a < b:
                inc = True
            elif a > b:
                inc = False
            else:
                good = False
                break
        if inc and a > b:
            good = False
            break
        if not inc and a < b:
            good = False
            break
        if abs(a - b) > 0 and abs(a - b) < 4:
            pass
        else:
            good = False
            break 
    return good

safe = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        
        if line:
            levels = line.split()

            if is_safe(levels):
                safe += 1
            else:
                for i in range(len(levels)):
                    partial = levels[:i] + levels[i+1:]
                    if is_safe(partial):
                        safe += 1
                        break

print(safe) 