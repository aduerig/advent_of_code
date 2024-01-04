# https://adventofcode.com/2023
import pathlib
import sys
import math

import numba

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

# @numba.njit
def iter_divisors(n):
    mult = 1
    if n < 0:
        mult = -1
        n = abs(n)
    if n == 0:
        return

    sqrt = math.sqrt(n)
    for i in range(1, math.ceil(sqrt)):
        if n % i == 0:
            yield mult * i
            yield mult * n // i
    
    if sqrt.is_integer():
        yield mult * int(sqrt)


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
    sign = '+'
    if constant < 0:
        sign = '-'
    print(color(f'{label1} = {leading:.2f} * {label2} * {sign} {abs(constant):.2f}'))



def insert_into_a(a_eq, t_eq, label1, label2):
    og_term, constant_1 = a_eq
    into_term, constant_2 = t_eq
    print_eq(og_term, constant_1, label1, 't')
    print_eq(into_term, constant_2, 't', label2)

    leading = into_term * og_term

    resultant_constant = constant_1 + (constant_2 * og_term)
    print_eq(leading, resultant_constant, label1, label2, color=red)
    return leading, resultant_constant


def solve_for_t(a, start, label='a', quiet=True):
    if not quiet: print_eq(a, start, label, 't')
    a_term = 1 / a
    constant = start / (-1 * a)
    if not quiet: print_eq(a_term, constant, 't', label, green)
    return a_term, constant


def solve_a(s1, s2, dim, quiet=True):
    a1_for_t = solve_for_t(s1[1][dim], s1[0][dim], label=dim_label(dim))
    a2_for_t = solve_for_t(s2[1][dim], s2[0][dim], label=dim_label(dim))
    ans = solve(a1_for_t, a2_for_t)
    if ans is None:
        return None
    ans = round(ans, 9)
    if not quiet: print(f'{dim_label(dim)} = {ans}')
    return ans


def collide_at(s1, s2, dim, quiet=True):
    a = solve_a(s1, s2, dim)
    if a is None:
        return True
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

# for v in range(-10000, 10000):
#     if v == 0:
#         continue
#     for a in range(-10000, 10000):
#         collider = ((a, 0, 0), (v, 0, 0))
#         for index, stone in enumerate(stones):
#             t = collide_at(collider, stone, 0)
#             if t != int(t):
#                 break
#         else:
#             print(f'WORKED: {collider}')

# for index1, s1 in enumerate(stones):
#     for index2, s2 in enumerate(stones[index1+1:], start=index1+1):
#         if collides(s1, s2):
#             print_green(f'{index1}, {index2}')


# collider = (24, 13, 10), (-3, 1, 2)


def get_divisors(x, y, z):
    xs = list(iter_divisors(xdiff))
    ys = list(iter_divisors(ydiff))
    zs = list(iter_divisors(ydiff))

    for x in xs:
        for y in ys:
            for z in zs:
                yield x, y, z


(first_x, first_y, first_z), (first_vx, first_vy, first_vz) = stones[0]
(second_x, second_y, second_z), (second_vx, second_vy, second_vz) = stones[1]
other_stones = stones[2:]
t = 0
while True:
    x = first_vx * t + first_x
    y = first_vy * t + first_y
    z = first_vz * t + first_z

    print(t)
    
    for other_t in range(0, 10):
        other_x = second_vx * other_t + second_x
        other_y = second_vy * other_t + second_y
        other_z = second_vz * other_t + second_z

        # diff 
        # xdiff = max(other_x, x) - min(other_x, x)
        # ydiff = max(other_y, y) - min(other_y, y)
        # zdiff = max(other_z, z) - min(other_z, z)
        xdiff = other_x - x
        ydiff = other_y - y
        zdiff = other_z - z

        for xv, yv, zv in get_divisors(xdiff, ydiff, zdiff):
            quiet = True
            if xv == -3 and yv == 1 and zv == 2:
                print(f'Trying {x, y, z}, {xv, yv, zv}, {t=}, {other_t=}')
                quiet = False
            collider = ((x - (t * xv), y - (t * yv), z - (t * zv)), (xv, yv, zv))

            for stone in other_stones:
                # print(f'    {stone=}')
                if not collides(collider, stone, quiet=quiet):
                    break
                elif not quiet:
                    print_green('COLLIDES')
            else:
                print_green(f'{t=}, {other_t=}, {x, y, z}, {collider=}')
                exit()

    t += 1
    if t > 10:
        exit()


# print_green(f'{collider=} works!')

# 272,206,447,651,388





# 24, 13, 10 @ -3, 1, 2
# 19, 13, 30 @ -2, 1, -2

# collides at t = 5: x=9, y=18, z=20

# x = -3t + 24
# y =   t + 13
# z =  2t + 10


# x = -2t + 19
# y =   t + 13
# z = -2t + 30



# x = -3t + 24
    # t = (24 - x) / 3
# y =   t + 13
    # t = y - 13
# z =  2t + 10
    # t = (z - 10) / 2


# x = -2t + 19
    # t = (19 - x) / 2
# y = t + 13
    # t = y - 13
# z = -2t + 30
    # t = (30 - z) / 2




# def dim_is_impossible(actual, direction, constant):
#     if actual == constant:
#         return False
#     if actual > constant:
#         if direction <= 0:
#             return True
#     else:
#         if direction >= 0:
#             return True
#     return False


# def stone_is_impossible(real_point, stone):
#     (x, y), (xv, yv) = stone
#     if dim_is_impossible(real_point[0], xv, x):
#         return True
#     if dim_is_impossible(real_point[1], yv, y):
#         return True
#     return False
        




    
# def get_ans(s1, s2, solve_for_label='y'):
#     (x1, y1, z1), (xv1, yv1, zv1) = s1
#     (x2, y2, z2), (xv2, yv2, zv2) = s2

#     z1_for_t = solve_for_t(zv1, z1, label='z')
#     inserted_1 = insert_into_a((xv1, x1), z1_for_t, 'x', 'z')

#     x1_for_t = solve_for_t(xv1, x1, label='x')
#     inserted_2 = insert_into_a((yv1, y1), x1_for_t, 'y', 'x')

#     inserted_3 = insert_into_a(inserted_2, inserted_1, 'y', 'x')

#     return ok

