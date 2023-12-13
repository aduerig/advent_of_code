# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

problems = []
with open(data_file) as f:
    new = []
    for line in f.readlines():
        line = line.strip()
        if not line:
            problems.append(new)
            new = []
        else:
            new.append(list(line))
if new:
    problems.append(new)


def rows_above(island):
    answers = []
    for y1 in range(len(island) - 1):
        y2 = y1 + 1
        
        bad = False
        y1_iter = y1
        y2_iter = y2
        while y1_iter > -1 and y2_iter < len(island):
            if island[y1_iter] != island[y2_iter]:
                bad = True
                break
            y1_iter -= 1
            y2_iter += 1
        if not bad:
            answers.append(y2)
    return answers


def get_stuff(island):
    a = rows_above(island)
    rotated_island = []
    for x in range(len(island[0])):
        new = []
        for y in range(len(island)):
            new.append(island[y][x])
        rotated_island.append(list(reversed(new)))
    b = rows_above(rotated_island)
    return a, b

def switch(island, x, y):
    if island[y][x] == '#':
        island[y][x] = '.'
    else:
        island[y][x] = '#'


def different(orig, new_stuff):
    a, b = orig
    y, z = new_stuff
    switched = False
    if b:
        switched = True
        a, b = b, a
        y, z = z, y

    if any(new_stuff) and (a != y or b != z):
        if z:
            multiplier = 1
            if switched:
                multiplier = 100
            return z[0] * multiplier
        
        multiplier = 100
        if switched:
            multiplier = 1        
        for GOD_NO in y:
            if GOD_NO not in a:
                return GOD_NO * multiplier

total = 0
for index, island in enumerate(problems):
    orig = get_stuff(island)
    changed_island = [[ele for ele in y] for y in island]
    for y in range(len(island)):
        should_break = False
        for x in range(len(island[0])):
            switch(changed_island, x, y)
            stuff = get_stuff(changed_island)
            switch(changed_island, x, y)

            ans = different(orig, stuff)
            if ans is not None:
                print(f'{index=} - {ans=}, {orig=}, {stuff=}, changed: {x=} {y=}')
                total += ans
                should_break = True
                break
        if should_break:
            break

print(total)

# correct part 2: 40995

# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# problems = []
# with open(data_file) as f:
#     new = []
#     for line in f.readlines():
#         line = line.strip()
#         if not line:
#             problems.append(new)
#             new = []
#         else:
#             new.append(list(line))
# if new:
#     problems.append(new)


# def rows_above(island):
#     for y1 in range(len(island) - 1):
#         y2 = y1 + 1
        
#         bad = False
#         y1_iter = y1
#         y2_iter = y2
#         while y1_iter > -1 and y2_iter < len(island):
#             if island[y1_iter] != island[y2_iter]:
#                 bad = True
#                 break
#             y1_iter -= 1
#             y2_iter += 1
#         if not bad:
#             return y2
#     return -1


# total = 0
# for index, island in enumerate(problems):
#     a = rows_above(island)

#     rotated_island = []
#     for x in range(len(island[0])):
#         new = []
#         for y in range(len(island)):
#             new.append(island[y][x])
#         rotated_island.append(list(reversed(new)))
    
#     b = rows_above(rotated_island)

#     print(f'{index=}, {a=}, {b=}')
#     if a != -1:
#         total += a * 100
#     if b != -1:
#         total += b




# print(total)