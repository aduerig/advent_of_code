# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


numerals = '0123456789'
def scan(the_string):
    if not the_string.startswith('mul('):
        return None
    first_num = ''
    second_num = ''
    comma = False
    index = 4
    GOOD = False
    while index < len(the_string):
        if the_string[index] == ')':
            if not first_num or not second_num:
                return None
            index += 1
            GOOD = True
            break
        letter = the_string[index]
        if letter == ',':
            if not first_num:
                return None
            comma = True
        elif letter not in numerals:
            return None
        elif not comma:
            first_num += letter
        else:
            second_num += letter
        index += 1
    if not GOOD:
        return None
    return int(first_num) * int(second_num)

total = 0
positives = 0
negatives = 0
muls = 0
to_print = []
with open(data_file) as f:
    blob = ''
    for char in f.read():
        blob += char

    should_count = True
    index = 0
    while index < len(blob):
        rest_of_string = blob[index:]
        if rest_of_string.startswith("do()"):
            should_count = True
            positives += 1
        elif rest_of_string.startswith("don't()"):
            should_count = False
            negatives += 1
        mult_result = scan(rest_of_string)
        if mult_result is not None:
            if should_count:
                total += mult_result
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



# numerals = '0123456789'
# def scan(index, the_string):
#     if not the_string[index:].startswith('mul('):
#         return None, None
#     index += 4
#     first_num = ''
#     second_num = ''
#     comma = False
#     while index < len(the_string):
#         if the_string[index] == ')':
#             if not first_num or not second_num:
#                 return None, None
#             index += 1
#             break
#         letter = the_string[index]
#         if letter == ',':
#             if not first_num:
#                 return None, None
#             comma = True
#         elif letter not in numerals:
#             return None, None
#         elif not comma:
#             first_num += letter
#         else:
#             second_num += letter
#         index += 1
#     if not first_num or not second_num:
#         return None, None
#     return int(first_num) * int(second_num), index

# total = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             index = 0
#             while index < len(line):
#                 result, new_index = scan(index, line)
#                 if result is None:
#                     index += 1
#                 else:
#                     total += result
#                     index = new_index

# print(total)

