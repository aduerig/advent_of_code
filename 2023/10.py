# https://adventofcode.com/2023
import sys
import pathlib
import copy

sys.setrecursionlimit(100000)

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


graph = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            line = line.replace('F', '┌').replace('7', '┐').replace('L', '└').replace('J', '┘')
            graph.append(list(line))

for y, row in enumerate(graph):
    for x, col in enumerate(row):
        if col == 'S':
            start = (x, y)
start_x, start_y = start

def printy(stuff):
    if type(stuff) == dict:
        for y in range(len(stuff)):
            for x in range(len(stuff[0])):
                if (x, y) in stuff:
                    print_blue(stuff[(x, y)], end='')
                else:
                    print('.', end='')
            print()
    else:
        for y in range(len(stuff)):
            for x in range(len(stuff[0])):
                print(stuff[y][x], end='')
            print()

mapping = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    '└': [(0, -1), (1, 0)],
    '┘': [(0, -1), (-1, 0)],
    '┐': [(-1, 0), (0, 1)],
    '┌': [(1, 0), (0, 1)],
}

def in_bounds(pos, arr):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(arr[0]) and pos[1] < len(arr)

def allowed(p1, p2):
    if not in_bounds(p2, graph):
        return False
    ele = graph[p2[1]][p2[0]]
    for dx, dy in mapping.get(ele, []):
        newx, newy = p2[0] + dx, p2[1] + dy
        if (newx, newy) == p1:
            return True
    return False


def traverse(pos, fr, reached, depth):
    if pos in reached:
        return

    x, y = pos    
    ele = graph[y][x]
    if type(reached) == dict:
        reached[pos] = depth

    for index, (dx, dy) in enumerate(mapping.get(ele, [])):
        new_pos = (x + dx, y + dy)
        if allowed(pos, new_pos):
            if fr:
                if new_pos == fr:
                    continue
                traverse(new_pos, (x, y), reached, depth + 1)
            else:
                traverse(new_pos, (x, y), reached[index], depth + 1)
            
for trying_char in mapping:
    reached = [{start: 0}, {start: 0}]
    graph[start_y][start_x] = trying_char
    traverse(start, None, reached, 0)
    dir_1, dir_2 = reached
    if len(dir_1) == len(dir_2) and len(dir_1) > 1:
        break
print(f'WITH {trying_char=}, {len(dir_1)=}')

combined = {pos for pos in dir_1 if pos in dir_2}
graph = [[graph[y][x] if (x, y) in combined else '.' for x in range(len(graph[0]))] for y in range(len(graph))]

printy(graph)
mapping_2 = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    '└': [(1, -1)],
    '┘': [(-1, -1)],
    '┐': [(-1, 1)],
    '┌': [(1, 1)],
}

def in_visited_arr(visited, ele):
    for v in visited:
        if ele in v:
            return True
    return False

tracker = {i: next_color_f() for i in range(8)}
def visited_to_color(visited, ele, char):
    for index, v in enumerate(visited):
        if ele in v:
            return tracker[index](char)
    return ' '

def very_fancy_print():
    for y in range(0, len(graph)):
        for x in range(0, len(graph[0])):
            pipe_infer = ' '
            if x != len(graph[0]) - 1:
                next_pipe = graph[y][x+1]
                if next_pipe in '┐-┘':
                    pipe_infer = '─'
            print_red(f'{graph[y][x]}{pipe_infer}', end='')
        print()

        if y != len(graph) - 1:
            for x in range(0, len(graph[0])):
                char = visited_to_color(global_visited, (x+1, y+1), '█')
                pipe_infer = ' '
                next_pipe = graph[y+1][x]
                if next_pipe in '|┘└':
                    pipe_infer = '|'
                print_red(f'{pipe_infer}{char}', end='')
            print()


def dfs(pos, visited):
    if not in_bounds(pos, graph):
        return
    if in_visited_arr(global_visited, pos):
        return
    visited.add(pos)
    very_fancy_print()
    input()

    x, y = pos
    up_left = graph[y - 1][x - 1]
    up_right = graph[y - 1][x]
    down_left = graph[y][x - 1]
    down_right = graph[y][x]

    up = True
    down = True
    left = True
    right = True

    if up_left in '|┌┐' or down_left in '|└┘':
        left = False
    if up_left in '-└┌' or up_right in '-┘┐':
        up = False
    if up_right in '|┌┐' or down_right in '|└┘':
        right = False

    if down_left in '-└┌' or down_right in '-┐┘':
        down = False

    if left:
        dfs((x - 1, y), visited)
    if right:
        dfs((x + 1, y), visited)
    if up:
        dfs((x, y - 1), visited)
    if down:
        dfs((x, y + 1), visited)

global_visited = []
for pos in combined:
    for dx, dy in mapping_2[graph[pos[1]][pos[0]]]:
        new_pos = (pos[0] + dx, pos[1] + dy)
        if not in_visited_arr(global_visited, new_pos):
            if not in_bounds(new_pos, graph):
                continue
            global_visited.append(set())
            dfs(new_pos, global_visited[-1])


very_fancy_print()


def count_dots(visited):
    count = 0
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if (x, y) in visited and graph[y][x] == '.':
                count += 1
    return count


for index, visited in enumerate(global_visited):
    count = count_dots(visited)
    print(f'Set {index} - len: {len(visited):>4}, dots: {count}')



# very_fancy_print()


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