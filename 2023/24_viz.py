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




def print_grid(t=0, axis='x'):
    if axis == 'x':
        dim = 0
    else:
        dim = 2

    abs_mins = [float('inf'), float('inf'), float('inf')]
    abs_maxs = [-float('inf'), -float('inf'), -float('inf')]

    for dim in [0, 1, 2]:
        for s in stones:
            abs_mins[dim] = min(abs_mins[dim], s[0][dim])
            abs_maxs[dim] = max(abs_maxs[dim], s[0][dim])

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

    for row in grid:
        to_print = []
        maxes = [-float('inf'), -float('inf'), -float('inf')]
        mins = [float('inf'), float('inf'), float('inf')]
        for col in row:
            if not col:
                to_print.append('·')
            else:
                first_stone = col[0]
                xvel, yvel, zvel = first_stone[1]

                maxes[0] = max(maxes[0], xvel)
                maxes[1] = max(maxes[1], yvel)
                maxes[2] = max(maxes[2], zvel)
                mins[0] = min(mins[0], xvel)
                mins[1] = min(mins[1], yvel)
                mins[2] = min(mins[2], zvel)

                # char = red('^') if yvel < 0 else blue('v')

                char = red('<') if xvel < 0 else blue('>')
                # char = red('<') if zvel < 0 else blue('>')

                to_print.append(char)
        if maxes[dim] != -float('inf'):
            to_print.append(f'{maxes[dim]:>8}, {mins[dim]:>8}')
        print(''.join(to_print))
    print(f'Showing y and {axis}, t = {t}')

t = 0
dim = 'x'

print_grid(t=t, axis=dim)
while True:
    ok = input('')
    if ok in ['x', 'z']:
        dim = ok
        print_grid(t=t, axis=dim)
    elif ok.isnumeric():
        t = int(ok)
        print_grid(t=t, axis=dim)
    else:
        print_red(f'didnt understand {ok}')