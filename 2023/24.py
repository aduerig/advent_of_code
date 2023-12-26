# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

stones = []
with open(data_file) as f:
    for line in f.read().splitlines():
        p, v = list(map(lambda x: x.strip().split(','), line.split('@')))
        p = list(map(lambda x: int(x.strip()), p))
        v = list(map(lambda x: int(x.strip()), v))
        stones.append(((p[0], p[1]), (v[0], v[1])))


def solve(left, right):
    a1, constant_1 = left
    a2, constant_2 = right

    a1 -= a2
    if round(a1, 6) == 0:
        return None
    constant_2 -= constant_1

    return constant_2 / a1
    

def insert_t_into_a(a_eq, t_eq):
    t_term, constant_1 = a_eq
    b_term, constant_2 = t_eq

    leading = b_term * t_term

    resultant_constant = constant_1 + (constant_2 * t_term)
    return leading, resultant_constant


def solve_for_t(v, start):
    a_term = 1 / v
    constant = start / (-1 * v)
    return a_term, constant


def get_ans(s1, s2):
    (x1, y1), (xv1, yv1) = s1
    (x2, y2), (xv2, yv2) = s2

    y1_for_t = solve_for_t(yv1, y1)
    inserted_1 = insert_t_into_a((xv1, x1), y1_for_t)

    y2_for_t = solve_for_t(yv2, y2)
    inserted_2 = insert_t_into_a((xv2, x2), y2_for_t)

    return solve(inserted_1, inserted_2)


def dim_is_impossible(actual, direction, constant):
    if actual == constant:
        return False
    if actual > constant:
        if direction <= 0:
            return True
    else:
        if direction >= 0:
            return True
    return False


def stone_is_impossible(real_point, stone):
    (x, y), (xv, yv) = stone
    if dim_is_impossible(real_point[0], xv, x):
        return True
    if dim_is_impossible(real_point[1], yv, y):
        return True
    return False


# bounds = (5, 27)
bounds = (200000000000000, 400000000000000)
def is_in(pos):
    for dim in pos:
        if dim is None:
            return False
        if dim < bounds[0]:
            return False
        if dim > bounds[1]:
            return False
    return True


total = 0
for index1, s1 in enumerate(stones):
    s1_reversed = (tuple(reversed(s1[0])), tuple(reversed(s1[1])))
    for index2 in range(index1 + 1, len(stones)):
        s2 = stones[index2]
        s2_reversed = (tuple(reversed(s2[0])), tuple(reversed(s2[1])))

        y = get_ans(s1, s2)
        x = get_ans(s1_reversed, s2_reversed)
        point = (x, y)
        print_blue(f'{s1}, {s2}\n    {point}')
        if is_in(point):
            if stone_is_impossible(point, s1) or stone_is_impossible(point, s2):
                continue
            total += 1
            print(f'    INSIDE: {point}')
print(total)
        

# 14672 correct



# 1. represent y as t for both
# 2. sub t (1) into x for both
# 3. set aboves equal to each other


# Hailstone A: (19, 13) (-2,  1)
# Hailstone B: (18, 19) (-1, -1)



# x = (-2t + 19)
# y = (t + 13)
    # t = y - 13
# x = -2y + 45


# x = (-t + 18)
# y = (-t + 19)
    # t = 19 - y

# x = y - 1

# y - 1 = -2y + 45
# 3y = 46
# y = 46/3






