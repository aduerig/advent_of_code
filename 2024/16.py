# part 2 (forgot to save part 1)
# https://adventofcode.com/2023
import sys
import pathlib

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


def print_best(best_total):
    best = {}
    for p, d in best_total:
        best[p] = True

    for y in range(len(grid)):
        to_print = []
        for x in range(len(grid[0])):
            spot = grid[y][x]
            if (x, y) in best:
                to_print.append('O')
            else:
                to_print.append(spot)
        print(''.join(to_print))


start_pos = None
start_dir = (1, 0)

best_tiles = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        spot = grid[y][x]
        if spot == 'S':
            start_pos = (x, y)
        # elif spot == 'E':
        #     best_tiles.add((x, y))


dir_mapper = {
    ((1, 0), 90): (0, 1),
    ((1, 0), -90): (0, -1),
    
    ((-1, 0), 90): (0, -1),
    ((-1, 0), -90): (0, 1),

    ((0, 1), 90): (-1, 0),
    ((0, 1), -90): (1, 0),

    ((0, -1), 90): (1, 0),
    ((0, -1), -90): (-1, 0),
}

start_time = time.time()
bottom_score = float('inf')
visited = {}
linkers = []
queue = [(start_pos, start_dir, 0, ())]
while queue:
    queue.sort(key=lambda x: x[2], reverse=True)
    pos, direction, score, path_so_far = queue.pop()
    x, y = pos
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '#':
        continue

    if grid[y][x] == 'E':
        bottom_score = score
        for p in path_so_far:
            best_tiles[p] = True
        continue
    
    if score > bottom_score:
        continue

    if (pos, direction) in visited:
        if score == visited[(pos, direction)]:
            linkers.append(((pos, direction), path_so_far))
        continue
    visited[(pos, direction)] = score

    for d_pos, d_direction in [
            [direction, None],
            [None, 90],
            [None, -90],
        ]:
        if d_direction:
            new_direction = dir_mapper[(direction, d_direction)]
            new_thing = (pos, new_direction, score + 1000, path_so_far)
        else:
            new_pos = (pos[0] + d_pos[0], pos[1] + d_pos[1])
            new_thing = (new_pos, direction, score + 1, path_so_far + ((pos, direction),))
        queue.append(new_thing)



def helper(linkers):
    for link, new_tiles in linkers:
        # if link == ((5, 7), (1, 0)):
        #     print(f'hi{8=}')
        #     exit()

        if link in best_tiles:
            needs_to_add = False
            for tile in new_tiles:
                if tile not in best_tiles:
                    needs_to_add = True

            if needs_to_add:
                for tile in new_tiles:
                    best_tiles[tile] = True
                return True

# print('before best_tiles length', len(best_tiles))
# print_best(best_tiles)


# for link, result in linkers:
#     p, d = link
#     if link == ((5, 7), (1, 0)):
#         print(f'{p}, {d} {link in best_tiles=} result: {result}')

# only_poses = []
# for p, d in best_tiles:
#     only_poses.append(p)
# print(f'{only_poses=}')



while helper(linkers):
    pass


# print('after best_tiles length', len(best_tiles))
# print_best(best_tiles)


# print(len(linkers))

final = set()
for pos, d in best_tiles:
    final.add(pos)
print(len(final) + 1)

print(f'Took {time.time() - start_time} seconds')