# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

all_islands = []
with open(data_file) as f:
    for section in f.read().split('\n\n'):
        new = []    
        for line in section.splitlines():
            if line.strip():
                new.append(list(line))
        all_islands.append(new)


def does_reflect(island, y1, y2):
    for x1, x2 in zip(range(y1, -1, -1), range(y2, len(island))):
        if island[x1] != island[x2]:
            return False
    return True


def rows_above(island):
    answers = []
    for y1, y2 in zip(range(len(island)), range(1, len(island))):
        if does_reflect(island, y1, y2):
            answers.append(y2)
    return answers


def horizontal_and_vertical(island):
    a = rows_above(island)
    rotated_island = [[island[y][x] for y in reversed(range(len(island)))] for x in range(len(island[0]))]
    b = rows_above(rotated_island)
    return a, b


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



def smudge_and_get_answer(island):
    original_reflections = horizontal_and_vertical(island)
    for y in range(len(island)):
        for x in range(len(island[0])):
            changed_island = [[ele for ele in y] for y in island]
            changed_island[y][x] = {'#': '.', '.': '#'}[changed_island[y][x]]
            
            new_reflections = horizontal_and_vertical(changed_island)
            ans = different(original_reflections, new_reflections)
            if ans is not None:
                return ans

print(sum((smudge_and_get_answer(island) for island in all_islands)))


# def different(orig, new):
#     if any(new) and orig != new:
#         for index, (a, b) in enumerate(reversed(list(zip(orig, new)))):
#             if a != b:
#                 return index * 99 + 1



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