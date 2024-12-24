# part 2
# https://adventofcode.com/2023
import sys
import pathlib
from collections import deque

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')



grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            grid.append(list(line))


for y in range(len(grid)):
    for x in range(len(grid[0])):
        ele = grid[y][x]
        if ele == 'S':
            start_pos = (x, y)
            grid[y][x] = '.'
        if ele == 'E':
            end_pos = (x, y)
            grid[y][x] = '.'

def bfs(pos):
    queue = deque([(pos, 0)])
    x, y = pos
    if grid[y][x] == '#':
        return None
    visited = set()
    while queue:
        (x, y), seconds = queue.popleft()
        if (x, y) == end_pos:
            return seconds
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        for dx, dy in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                ]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue

            if grid[ny][nx] == '.':
                queue.append(((nx, ny), seconds + 1))


def smaller_bfs(grid, pos, to_go):
    visited = {}
    queue = deque([(pos, 0, to_go)])
    while queue:
        (x, y), seconds, to_go = queue.popleft()
        if (x, y) in visited:
            continue
        visited[(x, y)] = seconds
        # if (x, y) == end_pos:
        #     continue
        if to_go < 0:
            continue
        for dx, dy in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                ]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            
            queue.append(((nx, ny), seconds + 1, to_go - 1))

    only_visited_valid = {}
    for pos, seconds in visited.items():
        if grid[pos[1]][pos[0]] == '.':
            only_visited_valid[pos] = seconds
    return only_visited_valid



has_cheated_tuples = {}
def bfs_cheat(grid, start, best_time, best_times):
    queue = deque([(start, 0)])
    counter = {}

    visited = set()
    while queue:
        (x, y), seconds_taken = queue.popleft()
        saved = best_time - seconds_taken
        if saved <= 0:
            continue
        if (x, y) == end_pos:
            saved = best_time - seconds_taken
            if saved not in counter:
                counter[saved] = 0
            counter[saved] += 1
            continue

        if (x, y) in visited:
            continue
        
        already = {}
        for cheat_pos, time_used_to_cheat in smaller_bfs(grid, (x, y), 19).items():
            snap_to_end_time = time_used_to_cheat + seconds_taken + best_times[cheat_pos]
            if cheat_pos in already:
                continue
            already[cheat_pos] = True
            # if best_time - snap_to_end_time == 54:
            #     print(f'{x, y} to {cheat_pos}, in {snap_to_end_time=}, {time_used_to_cheat=}, {seconds_taken=}, {best_times[cheat_pos]=}')

            #     for py in range(len(grid)):
            #         to_print = []
            #         for px in range(len(grid[0])):
            #             ele = grid[py][px]
                        
            #             if (x, y) == (px, py):
            #                 to_print.append(yellow('C'))
            #             elif cheat_pos == (px, py):
            #                 to_print.append(blue('W'))
            #             elif (px, py) == start_pos:
            #                 to_print.append(green('S'))
            #             elif (px, py) == end_pos:
            #                 to_print.append(red('E'))
            #             elif ele == '.':
            #                 to_print.append('.')
            #             else:
            #                 to_print.append('#')
            #         print(''.join(to_print))
            #     input()

            queue.append((end_pos, snap_to_end_time))


        visited.add((x, y))
        for dx, dy in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                ]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue

            if grid[ny][nx] == '.':
                queue.append(((nx, ny), seconds_taken + 1))

    hundred_and_above = 0
    for k, v in sorted(counter.items(), key=lambda x: x[0]):
        if k >= 0:
            print(f'{v}: {k}')
        if k >= 100:
            hundred_and_above += v
    print(f'hundred_and_above: {hundred_and_above}')


the_timer = time.time()


best_times = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        best_time = bfs((x, y))
        if best_time is not None:
            best_times[(x, y)] = best_time


# for y in range(len(grid)):
#     to_print = []
#     for x in range(len(grid[0])):
#         if (x, y) in best_times:
#             best = str(best_times[(x, y)])
#             to_print.append(best[-1])
#         else:
#             to_print.append('#')
#     print(''.join(to_print))
# exit()


# 1136619 too high

# 1136643 too high

print(f'Finsihed best bfs from everywhere in {time.time() - the_timer:.2f} seconds')
print(f'{best_times=}')

bfs_cheat(grid, start_pos, best_times[start_pos], best_times)
print(f'{best_times[start_pos]=}')


print(f'Calculated in {time.time() - the_timer:.2f} seconds')


# part 1 but not good enough
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             grid.append(list(line))


# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         ele = grid[y][x]
#         if ele == 'S':
#             start = (x, y)
#         if ele == 'E':
#             end = (x, y)
#             grid[y][x] = '.'

# def bfs(cheats, best_score):
#     queue = [(start, 0, cheats, set())]
#     counter = {}

#     the_timer = time.time()
#     while queue:
#         (x, y), seconds, cheats, visited = queue.pop(0)

#         if best_score is not None and seconds >= best_score:
#             continue

#         # only for real
#         if best_score is not None and best_score - seconds < 100:
#             continue

#         if (x, y) == end:
#             if best_score is None:
#                 return seconds
#             if best_score - seconds not in counter:
#                 counter[best_score - seconds] = 0
#             counter[best_score - seconds] += 1
#         if (x, y, cheats) in visited:
#             continue
        
#         visited.add((x, y, cheats))
#         for dx, dy in [
#                     (1, 0),
#                     (-1, 0),
#                     (0, 1),
#                     (0, -1),
#                 ]:
#             nx, ny = x + dx, y + dy
#             if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
#                 continue

#             if grid[ny][nx] == '#' and cheats:
#                 queue.append(((nx, ny), seconds + 1, cheats-1, set(visited)))
#             if grid[ny][nx] == '.':
#                 queue.append(((nx, ny), seconds + 1, cheats, set(visited)))

#     the_s = 0
#     for k, v in counter.items():
#         print(f'{k}: {v}')
#         the_s += v
#     print(f'Cheats that save you 100s: {the_s}. Calculated in {time.time() - the_timer:.2f} seconds')



# best_time_no_cheats = bfs(0, None)
# print(f'{best_time_no_cheats=}')
# bfs(1, best_time_no_cheats)
