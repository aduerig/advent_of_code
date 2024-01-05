# https://adventofcode.com/2023
import pathlib
import sys

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


def dim_label(dim):
    return ['x', 'y', 'z'][dim]




# x_limits = [290669830322265, 29219830322265]
# y_limits = [102468749999999, 104468749999999]
# z_limits = [250542352437971, 252542352437971]



# x_limits = [291669830322265, 291669830322266]
# y_limits = [102468749999999, 104468749999999]
# z_limits = [250542352437971, 252542352437971]



# x_limits = [291669830322265, 291669830322266]
# y_limits = [103_597_793_579_100, 103_597_793_579_101]
# z_limits = [251_542_352_437_971, 251_543_352_437_971]

# find_best_positions: time elapsed: 24.371342420578003. Starting index=24 high level loop of x dims, [[291669802334309, 291669802338479], [103597793579100, 103597793579101], [251542418325420, 251542418325421]], best collider last loop: ((291669802338480, 103597793579100, 251542418325420), (-11, 330, 91)), cost: 6,155,584,940


# x_limits = [291_669_802_364_363, 291_669_852_464_364]
# y_limits = [103_597_823_579_025, 103_597_826_579_025]
# z_limits = [251_542_422_239_297, 251_542_422_239_297]


# x_limits = [291_669_802_645_684, 291_669_802_645_684]
# y_limits = [103_597_826_479_025, 103_597_827_079_026]
# z_limits = [251_542_427_219_459, 251_542_428_019_460]



dim_order = [1, 2, 0]

x_limits = [291_669_802_654_110, 291_669_802_654_111]
y_limits = [103_597_826_800_230, 103_597_826_800_231]
z_limits = [251_542_427_650_413, 251_542_427_650_414]


x_vel_limits = [-12, -9]
y_vel_limits = [329, 332]
z_vel_limits = [89, 93]



pos_limits = [x_limits, y_limits, z_limits]
vel_limits = [x_vel_limits, y_vel_limits, z_vel_limits]

def get_midpoint(pair):
    return (pair[1] + pair[0]) // 2


def find_best_positions_bs(pos_limits):
    index = 0
    start_time = time.time()
    costs_and_collider = [[-1, -1], [-1, ((0, 0, 0), (0, 0, 0))], [-1, -1]]

    while any([pos_limits[dim][0] <= pos_limits[dim][1] for dim in set(dim_order)]):
        for dim in dim_order:
            l, r = pos_limits[dim]
            print(f'find_best_positions_bs: time elapsed: {time.time() - start_time}. Starting {index=} high level loop of {dim_label(dim)} dims, {pos_limits}, best collider last loop: {costs_and_collider[1][1]}, underscore_pos: {[f"{x:_}" for x in costs_and_collider[1][1][0]]}, cost: {costs_and_collider[1][0]:,}')

            if l > r:
                continue

            curr_position = [get_midpoint(pos_limits[0]), get_midpoint(pos_limits[1]), get_midpoint(pos_limits[2])]

            print(f'{curr_position=}')

            mid_for_dim = (l + r) // 2
            to_compute = [mid_for_dim - 1, mid_for_dim, mid_for_dim + 1]
            costs_and_collider = []
            for relevant_pos_for_dim in to_compute:
                curr_position[dim] = relevant_pos_for_dim
                costs_and_collider.append(lowest_dist_pos(*curr_position))
            
            dists = [cost for cost, collider in costs_and_collider]
            if dists[0] < dists[1]:
                pos_limits[dim][1] = mid_for_dim - 1
            elif dists[2] < dists[1]:
                pos_limits[dim][0] = mid_for_dim + 1
            else:
                print_green(f'find_best_positions_bs: {dim_label(dim)} somehow this is the best: {mid_for_dim}, existing range: {pos_limits[dim]}, voiding this dim.')
                pos_limits[dim] = [mid_for_dim, mid_for_dim - 1]
        index += 1
    (_, x), (_, y), (_, z) = pos_limits
    cost, collider = lowest_dist_pos(x, y, z)
    print_green(f'Finished: {pos_limits=}')
    print_blue(f'best collider is: {collider}, cost is: {cost:,}')



# !TODO somehow optimize below to hill climbing?
def lowest_dist_pos(x, y, z):
    lowest_collider = (float('inf'), ((0, 0, 0), (0, 0, 0)))
    for xvel in range(x_vel_limits[0], x_vel_limits[1]):
        for yvel in range(y_vel_limits[0], y_vel_limits[1]):
            for zvel in range(z_vel_limits[0], z_vel_limits[1]):
                collider = ((x, y, z), (xvel, yvel, zvel))
                cost = total_cost_collider(collider)
                if cost == 0:
                    print(collider)
                    exit()
                lowest_collider = min(lowest_collider, (cost, collider))
    return lowest_collider


def total_cost_collider(collider):
    return sum([inner_bst(collider, stone, 0, 2000000080040) for stone in stones])


# search for the lowest t between 2 stones in a loop
def inner_bst(collider, stone, left, right):
    while left <= right:
        mid = (left + right) // 2
        costs = [get_cost(t, collider, stone) for t in [mid - 1, mid, mid + 1]]

        if costs[0] < costs[1]:
            right = mid - 1
        elif costs[2] < costs[1]:
            left = mid + 1
        else:
            left = mid
            right = mid - 1
    return get_cost(left, collider, stone)


def get_cost(t, collider, stone):
    (x1, y1, z1), (xvel1, yvel1, zvel1) = collider
    (x2, y2, z2), (xvel2, yvel2, zvel2) = stone
    return abs((t * xvel1 + x1) - (t * xvel2 + x2)) + abs((t * yvel1 + y1) - (t * yvel2 + y2)) + abs((t * zvel1 + z1) - (t * zvel2 + z2))

find_best_positions_bs(pos_limits)