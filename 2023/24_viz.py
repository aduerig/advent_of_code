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


def dim_label(dim):
    return ['x', 'y', 'z'][dim]


def scale(min_n, max_n, n):
    diff = max_n - min_n
    amt = n - min_n

    return 100 * (amt / diff)



# search for the lowest t between 2 stones in a loop
def inner_bst(collider, stone, left, right):
    # print(f'starting inner_bst: {id(stone)}')
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
            # print_green(f'inner_bst: somehow this is the best... {(left, right)}, {mid=}, {costs}, voiding this')
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


def get_cost_by_dim(t, collider, stone):
    (x1, y1, z1), (xvel1, yvel1, zvel1) = collider
    (x2, y2, z2), (xvel2, yvel2, zvel2) = stone
    return [abs((t * xvel1 + x1) - (t * xvel2 + x2)), abs((t * yvel1 + y1) - (t * yvel2 + y2)), abs((t * zvel1 + z1) - (t * zvel2 + z2))]


def total_cost_collider(collider):
    return sum([inner_bst(collider, stone, 0, 2000000080040)[0] for stone in stones])


x_vel_limits = [-20, 20]
y_vel_limits = [310, 350]
z_vel_limits = [65, 80]
def lowest_dist_pos(x, y, z):
    lowest_collider = (float('inf'), ((0, 0, 0), (0, 0, 0)))
    for xvel in range(x_vel_limits[0], x_vel_limits[1]):
        for yvel in range(y_vel_limits[0], y_vel_limits[1]):
            for zvel in range(z_vel_limits[0], z_vel_limits[1]):
                if 0 in [xvel, yvel, zvel]:
                    continue
                collider = ((x, y, z), (xvel, yvel, zvel))
                cost = total_cost_collider(collider)
                lowest_collider = min(lowest_collider, (cost, collider))
    return lowest_collider


def print_grid(t=0, axis='x', my_collider=None, highlight_stone=None, cost_for_collided=None):
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
                    color = lambda x: x
                    char = '😮'
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
    print(f'Showing y and {axis}, t = {t}. Total cost of collider: {total_cost:,}')
    print(f'x: {abs_mins[0]:,} - {abs_maxs[0]:,}, y: {abs_mins[1]:,} - {abs_maxs[1]:,}, z: {abs_mins[2]:,} - {abs_maxs[2]:,}')
    print(f'{cxvel=}, {cyvel=}, {czvel=}')

    if cost_for_collided is not None:
        print_red(f'{wanted_t_index=}. {cost_for_collided=:,}')



# original, by eye
    # conclusions about with eye: y def positive, z probably positive, x not sure, maybe negative
    # things move meaningfully at ~1000000000 (1,000,000,000)
    # most have been hit by       ~759460080040 (759,460,080,040)
    # cost: 4,610,000,502,923,827
# my_collider = (
#     (
#         300000000000000, 
#         100000000000000,
#         255000000000000,
#     ), 
#     (
#         -12,
#         330,
#         70,
#     ),
# )


# cost: 12,044,122,529
# my_collider = (
#     (
#         291669830322265,
#         103597793579100,
#         251542418325420,
#     ), 
#     (
#         -11,
#         330,
#         91,
#     ),
# )


# cost: 1,544,780,587
# my_collider = (
#     (
#         291669802645684,
#         103597825079025,
#         251542422239297,
#     ), 
#     (
#         -11,
#         330,
#         91,
#     ),
# )


# cost: 318,336,578
# my_collider = (
#     (
#         291669802645684,
#         103597825079025,
#         251542427219459,
#     ), 
#     (
#         -11,
#         330,
#         91,
#     ),
# )

# cost: 195,689
my_collider = (
    (
        291669802653686,
        103597826799890,
        251542427650302,
    ), 
    (
        -11,
        330,
        91,
    ),
)

# c = lowest_dist_pos(*my_collider[0])[1]
# print(c)

def total_cost_collider(collider):
    cost = 0
    for stone in stones:
        sub_cost, best_t = inner_bst(collider, stone, 0, 2000000080040)
        cost += sub_cost
    return cost
total_cost = total_cost_collider(my_collider)

last_change = 3000000000


all_best_ts = []
for stone in stones:
    cost, best_t = inner_bst(my_collider, stone, 0, 2000000080040)
    all_best_ts.append((best_t, cost, stone))
all_best_ts.sort()


best_xs = []
best_ys = []
best_zs = []
for t, _, stone in all_best_ts:
    x, y, z = get_cost_by_dim(t, my_collider, stone)
    best_xs.append(x)
    best_ys.append(y)
    best_zs.append(z)
best_xs.sort()
best_ys.sort()
best_zs.sort()

def stringify_digits(arr):
    stringified_t_digits = []
    for lol in arr:
        stringified_t_digits.append(len(str(lol)))
    return sorted(stringified_t_digits)

just_ts = []
for tuple_thing in all_best_ts:
    just_ts.append(tuple_thing[0])

stringified_t_digits = stringify_digits(just_ts)
print(f'{stringified_t_digits}')

print_blue(f'{stringify_digits(best_xs)=}')
print_blue(f'{stringify_digits(best_ys)=}')
print_blue(f'{stringify_digits(best_zs)=}')

wanted_t_index = 0

t = 0
dim = 'x'
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
        if wanted_t_index < len(stones) - 1:
            wanted_t_index += 1
            t = all_best_ts[wanted_t_index][0]
            print_grid(t=t, axis=dim, my_collider=my_collider, highlight_stone=all_best_ts[wanted_t_index][2], cost_for_collided=all_best_ts[wanted_t_index][1])
    elif ok.strip() == 'u':
        if wanted_t_index > 0:
            wanted_t_index -= 1
            t = all_best_ts[wanted_t_index][0]
            print_grid(t=t, axis=dim, my_collider=my_collider, highlight_stone=all_best_ts[wanted_t_index][2], cost_for_collided=all_best_ts[wanted_t_index][1])
    elif ok.strip() == 'a':
        t += last_change
        print_grid(t=t, axis=dim, my_collider=my_collider)
    else:
        print_red(f'didnt understand {ok}')

# potentially a better vel? (-20, 332, 79)), found by running above
        

# my_collider = (
#     (
#         (303124999999998 + 287500000000000) // 2, 
#         (125000000000001 + 129687499999999) // 2, 
#         (259687500000000 + 276874999999998) // 2, 
#     ), 
#     (
#         -12,
#         330,
#         70,
#     ),
# )
        






# cost: 2,137,913,926,411,860
# my_collider = (
#     (
#         291680906093095,
#         125000000000001,
#         261284666061400,
#     ), 
#     (
#         -11,
#         310,
#         79,
#     ),
# )


# cost: 1,649,869,568,620,495
# my_collider = (
#     (
#         292402839660642,
#         125000000000000,
#         257318763732907,
#     ), 
#     (
#         -12,
#         304,
#         84,
#     ),
# )

# cost: 1,607,903,794,208,109
# my_collider = (
#     (
#         291638374328611,
#         102499999999999,
#         251389770507811,
#     ), 
#     (
#         -11,
#         319,
#         84,
#     ),
# )


# cost: 924,596,141,549,029
# my_collider = (
#     (
#         291638374328611,
#         104499999999999,
#         251389770507811,
#     ), 
#     (
#         -8,
#         325,
#         88,
#     ),
# )


# cost: 675,252,312,003,545
# my_collider = (
#     (
#         290457153320311,
#         104499999999999,
#         251389770507811,
#     ), 
#     (
#         -9,
#         325,
#         88,
#     ),
# )

# cost: 675,252,312,003,545
# my_collider = (
#     (
#         290457153320311,
#         104499999999999,
#         251389770507811,
#     ), 
#     (
#         -9,
#         325,
#         88,
#     ),
# )



# cost: 169,802,055,732,096
# my_collider = (
#     (
#         291056213378905,
#         105156249999999,
#         252282714843749,
#     ), 
#     (
#         -10,
#         328,
#         90,
#     ),
# )


# cost: 167,424,259,206,369
# my_collider = (
#     (
#         291110839843749,
#         104218749999999,
#         250982761383055,
#     ), 
#     (
#         -10,
#         329,
#         92,
#     ),
# )

# cost: 167,424,259,206,369
# my_collider = (
#     (
#         291093750000000,
#         104062500000000,
#         251562500000000,
#     ), 
#     (
#         -10,
#         329,
#         91,
#     ),
# )
        
# cost: 53,466,768,727,427
# my_collider = (
#     (
#         291669830322265,
#         102968749999999,
#         251542352437971,
#     ), 
#     (
#         -11,
#         331,
#         91,
#     ),
# )

# cost: 25,835,072,929,008
# my_collider = (
#     (
#         291669830322265,
#         103468749999999,
#         251542352437971,
#     ), 
#     (
#         -11,
#         330,
#         91,
#     ),
# )

# cost: 26,980,495,287
# my_collider = (
#     (
#         291669830322265,
#         103597793579100,
#         251542352437971,
#     ), 
#     (
#         -11,
#         330,
#         91,
#     ),
# )