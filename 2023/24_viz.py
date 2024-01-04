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


def scale(min_n, max_n, n):
    diff = max_n - min_n
    amt = n - min_n

    return 100 * (amt / diff)



def print_grid(t=0, axis='x', my_collider=None):
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

    print(cscales)
    if cscales[1] > -1 and cscales[1] < len(grid) and cscales[dim] > -1 and cscales[dim] < len(grid[0]):
        grid[int(cscales[1])][int(cscales[dim])].insert(0, my_collider)
        print('inserted at')


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

                if my_collider in col:
                    color = yellow
                    char = '>' if relevant_vels[col.index(my_collider)] > 0 else '<'
                else:
                    char = ''
                    positive = True if relevant_vels[0] > 0 else False
                    for vel in relevant_vels:
                        if positive:
                            if vel < 0:
                                char = '*'
                                color = green
                                break
                            char = '>'
                            color = blue
                        else:
                            if vel > 0:
                                char = '*'
                                color = green
                                break
                            char = '<'
                            color = red
                to_print.append(color(char))

        if maxes[dim] != -float('inf'):
            to_print.append(f'{maxes[dim]:>8}, {mins[dim]:>8}')
        print(''.join(to_print))
    print(f'Showing y and {axis}, t = {t}.')
    print(f'x: {abs_mins[0]:,} - {abs_maxs[0]:,}, y: {abs_mins[1]:,} - {abs_maxs[1]:,}, z: {abs_mins[2]:,} - {abs_maxs[2]:,}')


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

last_change = 3000000000

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
        t += last_change
        print_grid(t=t, axis=dim, my_collider=my_collider)
    else:
        print_red(f'didnt understand {ok}')