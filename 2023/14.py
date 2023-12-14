# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


graph = []
with open(data_file) as f:
    for line in f.read().splitlines():
        if line:
            graph.append(list(line))


def north_roll(graph):
    for x in range(len(graph[0])):
        empty = 0
        for y in range(len(graph)):
            if graph[y][x] == 'O':
                graph[y][x] = '.'
                graph[empty][x] = 'O'
                empty += 1
            elif graph[y][x] == '#':
                empty = y + 1

def rotate_right(graph):
    return [[graph[y][x] for y in reversed(range(len(graph)))] for x in range(len(graph[0]))]


def roll_all(graph):
    north_roll(graph)
    graph = rotate_right(graph)
    north_roll(graph)
    graph = rotate_right(graph)
    north_roll(graph)
    graph = rotate_right(graph)
    north_roll(graph)
    graph = rotate_right(graph)
    return graph


cache = {}
i = 0
while i < 1000000000:
    graph = roll_all(graph)
    key = tuple([tuple(line) for line in graph])
    if key in cache:
        diff = i - cache[key]
        i += diff * ((1000000000 - i) // diff)
    cache[key] = i
    i += 1

total = 0
for index, line in enumerate(graph):
    total += (len(graph) - index) * line.count('O')
print(total)


# original part 2
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# graph = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         if line:
#             graph.append(list(line))



# def roll():
#     for y in range(len(graph)):
#         for x in range(len(graph[0])):
#             if graph[y][x] == '.':
#                 new = y + 1
#                 while new < len(graph):
#                     if graph[new][x] == '#':
#                         break
#                     if graph[new][x] == 'O':
#                         graph[new][x]= '.'
#                         graph[y][x]= 'O'
#                         break
#                     new += 1
#     # west
#     for x in range(len(graph[0])):
#         for y in range(len(graph)):
#             if graph[y][x] == '.':
#                 new = x + 1
#                 while new < len(graph):
#                     if graph[y][new] == '#':
#                         break
#                     if graph[y][new] == 'O':
#                         graph[y][new]= '.'
#                         graph[y][x]= 'O'
#                         break
#                     new += 1
#     # south
#     for y in reversed(range(len(graph))):
#         for x in range(len(graph[0])):
#             if graph[y][x] == '.':
#                 new = y - 1
#                 while new > -1:
#                     if graph[new][x] == '#':
#                         break
#                     if graph[new][x] == 'O':
#                         graph[new][x]= '.'
#                         graph[y][x]= 'O'
#                         break
#                     new -= 1
#     # east
#     for x in reversed(range(len(graph[0]))):
#         for y in range(len(graph)):
#             if graph[y][x] == '.':
#                 new = x - 1
#                 while new > -1:
#                     if graph[y][new] == '#':
#                         break
#                     if graph[y][new] == 'O':
#                         graph[y][new]= '.'
#                         graph[y][x]= 'O'
#                         break
#                     new -= 1


# cache = {}

# i = 0
# while i < 1000000000:
#     if i == 102:
#         while i + 42 < 1000000000:
#             i += 42
        
#     roll()
#     key = tuple([tuple(line) for line in graph])
#     if key in cache:
#         print(f'CYCLE AT {cache[key]}')

#     if key not in cache:
#         cache[key] = []
#     cache[key].append(i)
#     i += 1

# total = 0
# for index, line in enumerate(graph):
#     total += (len(graph) - index) * line.count('O')

# print(total)


# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# graph = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         graph.append(list(line))



# for y in range(len(graph)):
#     for x in range(len(graph[0])):
#         if graph[y][x] == '.':
#             new = y + 1
#             while new < len(graph):
#                 if graph[new][x] == '#':
#                     break
#                 if graph[new][x] == 'O':
#                     graph[new][x]= '.'
#                     graph[y][x]= 'O'
#                     break
#                 new += 1


# total = 0
# last = len(graph) - 1
# while last > -1:
#     total += graph[last].count('O') * (last + 1)
#     last -= 1

# print(total)