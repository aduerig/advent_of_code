# https://adventofcode.com/2023
import pathlib
import sys
import math
import functools

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath('24.dat')

stones = []
with open(data_file) as f:
    for line in f.read().splitlines():
        p, v = list(map(lambda x: x.strip().split(','), line.split('@')))
        p = list(map(lambda x: int(x.strip()), p))
        v = list(map(lambda x: int(x.strip()), v))
        stones.append(((p[0], p[1], p[2]), (v[0], v[1], v[2])))

for dim in [0, 1, 2]:
    exist = set()
    for stone in exist:
        if stone[0][dim] in exist:
            print(f'Duplicate on dim: {dim}: {stone[0][dim]}')
            exit()
        exist.add(stone[0][dim])


stones_by_y = sorted(stones, key=lambda x: x[0][1])


def dim_label(dim):
    return ['x', 'y', 'z'][dim]


def scale(min_n, max_n, n):
    diff = max_n - min_n
    amt = n - min_n

    return 100 * (amt / diff)



# search for the lowest t between 2 stones in a loop
def inner_bst(collider, stone, left, right):
    print(f'starting inner_bst: {id(stone)}')
    while left <= right:
        mid = (left + right) // 2
        to_compute = [mid - 1, mid, mid + 1]
        costs = []
        for t in to_compute:
            costs.append(get_cost(t, collider, stone))

        if costs[0] < costs[1]:
            right = mid - 1
        elif costs[2] < costs[1]:
            left = mid + 1
        else:
            print_green(f'inner_bst: somehow this is the best... {(left, right)}, {mid=}, {costs}, voiding this')
            left = mid
            right = mid - 1
    return (get_cost(left, collider, stone), t)


def get_cost(t, collider, stone):
    (x1, y1, z1), (xvel1, yvel1, zvel1) = collider
    (x2, y2, z2), (xvel2, yvel2, zvel2) = stone

    cost = 0
    cost += abs((t * xvel1 + x1) - (t * xvel2 + x2))
    cost += abs((t * yvel1 + y1) - (t * yvel2 + y2))
    cost += abs((t * zvel1 + z1) - (t * zvel2 + z2))
    return cost


def print_grid(t=0, axis='x', my_collider=None, highlight_stone=None):
    if axis == 'x':
        dim = 0
    elif axis == 'z':
        dim = 2

    abs_mins = [float('inf'), float('inf'), float('inf')]
    abs_maxs = [-float('inf'), -float('inf'), -float('inf')]

    for sub_dim in [0, 1, 2]:
        for s in stones:
            abs_mins[sub_dim] = min(abs_mins[sub_dim], s[0][sub_dim])
            abs_maxs[sub_dim] = max(abs_maxs[sub_dim], s[0][sub_dim])

    (cx_start, cy_start, cz_start), (cxvel, cyvel, czvel) = my_collider
    cx = cxvel * t + cx_start
    cy = cyvel * t + cy_start
    cz = czvel * t + cz_start


    cscales = [scale(abs_mins[0], abs_maxs[0], cx), (scale(abs_mins[1], abs_maxs[1], cy)), scale(abs_mins[2], abs_maxs[2], cz)]

    grid = [[[] for y in range(101)] for x in range(101)]
    for stone in stones:
        (x_start, y_start, z_start), (xv, yv, zv) = stone

        x = xv * t + x_start
        y = yv * t + y_start
        z = zv * t + z_start

        scaled_x = scale(abs_mins[0], abs_maxs[0], x)
        scaled_y = scale(abs_mins[1], abs_maxs[1], y)
        scaled_z = scale(abs_mins[2], abs_maxs[2], z)
        scales = [int(scaled_x), int(scaled_y), int(scaled_z)]

        if scales[1] > -1 and scales[1] < len(grid) and scales[dim] > -1 and scales[dim] < len(grid[0]):
            grid[scales[1]][scales[dim]].append(stone)

    if cscales[1] > -1 and cscales[1] < len(grid) and cscales[dim] > -1 and cscales[dim] < len(grid[0]):
        grid[int(cscales[1])][int(cscales[dim])].insert(0, my_collider)


    for row in grid:
        to_print = []
        maxes = [-float('inf'), -float('inf'), -float('inf')]
        mins = [float('inf'), float('inf'), float('inf')]
        for col in row:
            if not col:
                to_print.append('·')
            else:
                relevant_vels = []
                for (_, _, _), (xvel, yvel, zvel) in col:
                    maxes[0] = max(maxes[0], xvel)
                    maxes[1] = max(maxes[1], yvel)
                    maxes[2] = max(maxes[2], zvel)
                    mins[0] = min(mins[0], xvel)
                    mins[1] = min(mins[1], yvel)
                    mins[2] = min(mins[2], zvel)

                    vel_dims = [xvel, yvel, zvel]
                    relevant_vels.append(vel_dims[dim])

                char = ''
                if my_collider in col and highlight_stone in col:
                    color = green
                    char = '█'
                elif highlight_stone in col:
                    color = yellow
                    char = '█'
                elif my_collider in col:
                    color = yellow
                    char = '>' if relevant_vels[col.index(my_collider)] > 0 else '<'
                else:
                    positive = True if relevant_vels[0] > 0 else False
                    for vel in relevant_vels:
                        if positive:
                            if vel < 0:
                                char = '*'
                                color = cyan
                                break
                            char = '>'
                            color = blue
                        else:
                            if vel > 0:
                                char = '*'
                                color = cyan
                                break
                            char = '<'
                            color = red
                to_print.append(color(char))

        # if maxes[dim] != -float('inf'):
        #     to_print.append(f'{maxes[dim]:>8}, {mins[dim]:>8}')
        print(''.join(to_print))
    print(f'Showing y and {axis}, t = {t}. {stone_y_index=}. Total cost of collider: {total_cost:,}')
    print(f'x: {abs_mins[0]:,} - {abs_maxs[0]:,}, y: {abs_mins[1]:,} - {abs_maxs[1]:,}, z: {abs_mins[2]:,} - {abs_maxs[2]:,}')
    print(f'{cxvel=}, {cyvel=}, {czvel=}')


# things move meaningfully at ~1000000000 (1,000,000,000)
# most have been hit by       ~759460080040 (759,460,080,040)

t = 0
dim = 'x'

my_collider = (
    (
        300000000000000, 
        100000000000000,
        255000000000000,
    ), 
    (
        -12,
        330,
        70,
    ),
)
# y def positive, z probably positive, x not sure, maybe negative

# def total_cost_collider(collider):
#     cost = 0
#     for stone in stones:
#         sub_cost, best_t = inner_bst(collider, stone, 0, 2000000080040)
#         cost += sub_cost
#     return cost
# total_cost = total_cost_collider(my_collider)
total_cost = 0

last_change = 3000000000


stone_y_index = 0

print_grid(t=t, axis=dim, my_collider=my_collider)
while True:
    ok = input('')
    if ok in ['x', 'z']:
        dim = ok
        print_grid(t=t, axis=dim, my_collider=my_collider)
    elif ok.startswith ('c '):
        x, y, z, xvel, yvel, zvel = ok[2:].strip().split()
        my_collider = ((x, y, z), (xvel, yvel, zvel))
    elif ok.isnumeric():
        t = int(ok)
        print_grid(t=t, axis=dim, my_collider=my_collider)
    elif ok.startswith('+') or ok.startswith('-'):
        last_change = int(ok[1:])
        t += last_change
        print_grid(t=t, axis=dim, my_collider=my_collider)
    elif not ok.strip() and last_change is not None:
        if stone_y_index < len(stones_by_y):
            stone_y_index += 1
            t = inner_bst(my_collider, stones_by_y[stone_y_index], 0, 2000000080040)[1]
            print_grid(t=t, axis=dim, my_collider=my_collider, highlight_stone=stones_by_y[stone_y_index])
    elif ok.strip() == 'u':
        if stone_y_index > 0:
            stone_y_index -= 1
            t = inner_bst(my_collider, stones_by_y[stone_y_index], 0, 2000000080040)[1]
            print_grid(t=t, axis=dim, my_collider=my_collider, highlight_stone=stones_by_y[stone_y_index])
    elif ok.strip() == 'a':
        t += last_change
        print_grid(t=t, axis=dim, my_collider=my_collider)
    else:
        print_red(f'didnt understand {ok}')
