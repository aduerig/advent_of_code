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


def solve(left, right):
    a1, constant_1 = left
    a2, constant_2 = right

    a1 -= a2
    if round(a1, 6) == 0:
        return None
    constant_2 -= constant_1

    return constant_2 / a1


def print_eq(leading, constant, label1, label2, color=lambda x: x):
    sign = '+' if constant < 0 else '-'
    print(color(f'{label1} = {leading:.2f} * {label2} * {sign} {abs(constant):.2f}'))


def solve_for_t(a, start, label='a', quiet=True):
    if not quiet: print_eq(a, start, label, 't')
    a_term = 1 / a
    constant = start / (-1 * a)
    if not quiet: print_eq(a_term, constant, 't', label, green)
    return a_term, constant


def solve_a(s1, s2, dim, quiet=True):
    a1_for_t = solve_for_t(s1[1][dim], s1[0][dim], label=dim_label(dim), quiet=True)
    a2_for_t = solve_for_t(s2[1][dim], s2[0][dim], label=dim_label(dim), quiet=True)
    ans = solve(a1_for_t, a2_for_t)
    if ans is None:
        return None
    ans = round(ans, 9)
    if not quiet: print(f'{dim_label(dim)} = {ans}')
    return ans


def collide_at(s1, s2, dim, quiet=True):
    if s1[1][dim] == s2[1][dim]:
        if s1[0][dim] == s2[0][dim]:
            return 0
        return False

    a = solve_a(s1, s2, dim)
    if a is None:
        assert(False)
        # return s1[0][dim] == s2[0][dim]
    t_ans = round((s1[0][dim] - a) / -s1[1][dim], 9) # why is this negative -s1
    if not quiet: print(f'{dim_label(dim)}: t = {t_ans}')
    return t_ans


def collides(s1, s2, quiet=True):
    t1 = collide_at(s1, s2, 0)
    t2 = collide_at(s1, s2, 1)
    t3 = collide_at(s1, s2, 2)
    if not quiet: print(f'{t1, t2, t3=}')
    last = None

    for i in [t1, t2, t3]:
        if i is not True:
            if last is not None and last != i:
                return False
            last = i
    return True



x_limits = [288000000000000, 292000000000000]
y_limits = [10000000000000, 110000000000000]

z_limits = [251542205810546, 251542205810546]
# z_limits = [245000000000000, 265000000000000]
z_limits = [235000000000000, 255000000000000]
pos_limits = [x_limits, y_limits, z_limits]


# best collider is: ((291638374328611, 102499999999999, 251389770507810), (-11, 319, 88)), cost is: 1378740501490319
x_vel_limits = [-12, -8]
y_vel_limits = [329, 338]
z_vel_limits = [85, 100]
vel_limits = [x_vel_limits, y_vel_limits, z_vel_limits]


def get_midpoint(pair):
    return (pair[1] + pair[0]) // 2


def find_best_positions(pos_limits):
    index = 0
    start_time = time.time()
    costs_and_collider = [[-1, -1], [-1, -1], [-1, -1]]
    while any([l <= r for l, r in pos_limits]):
        print(f'find_best_positions: time elapsed: {time.time() - start_time}. Starting {index=} high level loop of all 3 dims, {pos_limits}, best collider last loop: {costs_and_collider[1][1]}, cost: {costs_and_collider[1][0]:,}')
        for dim, (l, r) in enumerate(pos_limits):
            if l > r:
                continue

            curr_position = [get_midpoint(pos_limits[0]), get_midpoint(pos_limits[1]), get_midpoint(pos_limits[2])]

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
                print_green(f'find_best_positions: {dim_label(dim)} somehow this is the best: {mid_for_dim}, existing range: {pos_limits[dim]}, voiding this dim.')
                pos_limits[dim] = [mid_for_dim, mid_for_dim - 1]
        index += 1
    (_, x), (_, y), (_, z) = pos_limits
    cost, collider = lowest_dist_pos(x, y, z)
    print_green(f'Finished: {pos_limits=}')
    print_blue(f'best collider is: {collider}, cost is: {cost}')


# !TODO somehow optimize below to hill climbing?
def lowest_dist_pos(x, y, z):
    lowest_collider = (float('inf'), ((0, 0, 0), (0, 0, 0)))
    for xvel in range(x_vel_limits[0], x_vel_limits[1]):
        for yvel in range(y_vel_limits[0], y_vel_limits[1]):
            for zvel in range(z_vel_limits[0], z_vel_limits[1]):
                collider = ((x, y, z), (xvel, yvel, zvel))
                cost = total_cost_collider(collider)
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

find_best_positions(pos_limits)