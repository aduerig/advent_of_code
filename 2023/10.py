
# https://adventofcode.com/2023
import sys
import pathlib

sys.setrecursionlimit(100000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


graph = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            graph.append(list(line))

start = None
for y, row in enumerate(graph):
    for x, col in enumerate(row):
        if col == 'S':
            start = (x, y)
            break

print(f'Start is {start}')

mapping = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)],
    '.': [],
}

def allowed(p1, p2):
    if x < 0 or y < 0 or x >= len(graph[0]) or y >= len(graph):
        return False
    ele_2 = graph[p2[1]][p2[0]]
    for dx, dy in mapping[ele_2]:
        newx, newy = p2[0] + dx, p2[1] + dy
        if (newx, newy) == p1:
            return True
    return False


def traverse(pos, fr, reached, depth):
    x, y = pos
    if pos in reached:
        return

    ele = graph[y][x]
    if type(reached) == dict:
        reached[pos] = depth

    for index, (newx, newy) in enumerate(mapping[ele]):
        if allowed(pos, (x + newx, y + newy)):
            if fr == None:
                reached[index][pos] = 0
                traverse((x + newx, y + newy), (x, y), reached[index], depth + 1)
            else:
                if (x + newx, y + newy) == fr:
                    continue
                traverse((x + newx, y + newy), (x, y), reached, depth + 1)
    
def printy(stuff):
    print()
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if (x, y) in stuff:
                print_blue(stuff[(x, y)], end='')
            else:
                print('.', end='')
        print('\n')

start_x, start_y = start

for m in mapping:
    if m == '.':
        continue
    reached = [{}, {}]
    graph[start_y][start_x] = m
    traverse(start, None, reached, 0)
    a, b = reached

    if len(a) != len(b) or len(a) == 0 or len(b) == 0:
        continue

    combined = {start: 'S'}
    for k1, v1 in a.items():
        if k1 in b:
            combined[k1] = min(a[k1], b[k1])

    counted = {start: 'S'}

    total = 0
    for y in range(len(graph)):
        c = 0
        on = False
        for x in range(len(graph[0])):
            if (x, y) in combined:
                if on:
                    on = False
                else:
                    if graph[y][x] in '|7J':
                        on = True
            elif on:
                c += 1
                counted[(x, y)] = 'O'
        total += c

    printy(counted)
    
    print(f'WITH m: {m}, {len(a)}, {len(b)} {total}')


# 3024 is too high


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# sys.setrecursionlimit(100000)

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# graph = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             graph.append(list(line))

# start = None
# for y, row in enumerate(graph):
#     for x, col in enumerate(row):
#         if col == 'S':
#             start = (x, y)
#             break

# print(f'Start is {start}')

# mapping = {
#     '|': [(0, 1), (0, -1)],
#     '-': [(1, 0), (-1, 0)],
#     'L': [(0, -1), (1, 0)],
#     'J': [(0, -1), (-1, 0)],
#     '7': [(-1, 0), (0, 1)],
#     'F': [(1, 0), (0, 1)],
#     '.': [],
# }

# def allowed(p1, p2):
#     if x < 0 or y < 0 or x >= len(graph[0]) or y >= len(graph):
#         return False
    

#     ele_2 = graph[p2[1]][p2[0]]

#     for dx, dy in mapping[ele_2]:
#         newx, newy = p2[0] + dx, p2[1] + dy
#         if (newx, newy) == p1:
#             return True
#     return False



# def traverse(pos, fr, reached, depth):
#     x, y = pos
#     if pos in reached:
#         return

#     ele = graph[y][x]
#     if type(reached) == dict:
#         reached[pos] = depth

#     for index, (newx, newy) in enumerate(mapping[ele]):
#         if allowed(pos, (x + newx, y + newy)):
#             if fr == None:
#                 reached[index][pos] = 0
#                 traverse((x + newx, y + newy), (x, y), reached[index], depth + 1)
#             else:
#                 if (x + newx, y + newy) == fr:
#                     continue
#                 traverse((x + newx, y + newy), (x, y), reached, depth + 1)
    
# def printy(stuff):
#     print()
#     for y in range(len(graph)):
#         for x in range(len(graph[0])):
#             if (x, y) in stuff:
#                 print_blue(stuff[(x, y)], end='')
#             else:
#                 print('.', end='')
#         print('\n')

# start_x, start_y = start

# maxxy = 0
# for m in mapping:
#     if m == '.':
#         continue
#     reached = [{}, {}]
#     graph[start_y][start_x] = m
#     traverse(start, None, reached, 0)
#     a, b = reached

#     if len(a) != len(b):
#         continue

#     combined = {start: 'S'}
#     for k1, v1 in a.items():
#         if k1 in b:
#             combined[k1] = min(a[k1], b[k1])
#             maxxy = max(maxxy, combined[k1])

#     print(f'WITH m: {m}, {len(a)}, {len(b)}')
#     # printy(combined)
#     # printy(a)
#     # printy(b)

# # 13911 is too high
# print(maxxy)