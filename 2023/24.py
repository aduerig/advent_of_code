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
        stones.append(((p[0], p[1], p[2]), (v[0], v[1], v[2])))


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


def solve_for_t(a, start, label='a'):
    print_eq(a, start, label, 't')
    a_term = 1 / a
    constant = start / (-1 * a)
    print_eq(a_term, constant, 't', label, green)
    return a_term, constant



# z into t for the x equation
# x = ((-z + 10) / -2) + 24

# x into t for the y equation
# y =  (24 - x) / 3 + 13

def get_ans(s1, s2, solve_for_label='y'):
    (x1, y1, z1), (xv1, yv1, zv1) = s1
    (x2, y2, z2), (xv2, yv2, zv2) = s2

    z1_for_t = solve_for_t(zv1, z1, label='z')
    inserted_1 = insert_into_a((xv1, x1), z1_for_t, 'x', 'z')

    x1_for_t = solve_for_t(xv1, x1, label='x')
    inserted_2 = insert_into_a((yv1, y1), x1_for_t, 'y', 'x')

    inserted_3 = insert_into_a(inserted_2, inserted_1, 'y', 'x')


    print('SECOND =====')
    z2_for_t = solve_for_t(zv2, z2, label='z')
    inserted_4 = insert_into_a((xv2, x2), z2_for_t, 'x', 'z')

    x2_for_t = solve_for_t(xv2, x2, label='x')
    inserted_5 = insert_into_a((yv2, y2), x2_for_t, 'y', 'x')

    inserted_6 = insert_into_a(inserted_5, inserted_4, 'y', 'x')

    ok = solve(inserted_3, inserted_6)
    print(f'{solve_for_label} = {ok}')
    return ok


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
    for index2 in range(index1 + 1, len(stones)):
        s2 = stones[index2]

        first_ans = get_ans(s1, s2)

        # s1_again = ((s1[0][1], s1[0][0], s1[0][2]), (s1[1][1], s1[1][0], s1[1][2]))
        # s2_again = ((s1[0][1], s1[0][0], s1[0][2]), (s1[1][1], s1[1][0], s1[1][2]))

        # second_ans = get_ans(s1_again, s2_again)

        # s1_again_again = ((s1[0][0], s1[0][2], s1[0][1]), (s1[1][0], s1[1][2], s1[1][1]))
        # s2_again_again = ((s1[0][0], s1[0][2], s1[0][1]), (s1[1][0], s1[1][2], s1[1][1]))

        # third_ans = get_ans(s1_again_again, s2_again_again)

print(f'{first_ans=}')
# print(f'{second_ans=}')
# print(f'{third_ans=}')







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


# z into t for the x equation
# x = ((-z + 10) / -2) + 24

# x into t for the y equation
# y =  (24 - x) / 3 + 13

# combine
# 



# x = -2t + 19
    # t = (19 - x) / 2
# y = t + 13
    # t = y - 13
# z = -2t + 30
    # t = (30 - z) / 2











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







# part 1
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# stones = []
# with open(data_file) as f:
#     for line in f.read().splitlines():
#         p, v = list(map(lambda x: x.strip().split(','), line.split('@')))
#         p = list(map(lambda x: int(x.strip()), p))
#         v = list(map(lambda x: int(x.strip()), v))
#         stones.append(((p[0], p[1]), (v[0], v[1])))


# def solve(left, right):
#     a1, constant_1 = left
#     a2, constant_2 = right

#     a1 -= a2
#     if round(a1, 6) == 0:
#         return None
#     constant_2 -= constant_1

#     return constant_2 / a1
    

# def insert_t_into_a(a_eq, t_eq):
#     t_term, constant_1 = a_eq
#     b_term, constant_2 = t_eq

#     leading = b_term * t_term

#     resultant_constant = constant_1 + (constant_2 * t_term)
#     return leading, resultant_constant


# def solve_for_t(v, start):
#     a_term = 1 / v
#     constant = start / (-1 * v)
#     return a_term, constant


# def get_ans(s1, s2):
#     (x1, y1), (xv1, yv1) = s1
#     (x2, y2), (xv2, yv2) = s2

#     y1_for_t = solve_for_t(yv1, y1)
#     inserted_1 = insert_t_into_a((xv1, x1), y1_for_t)

#     y2_for_t = solve_for_t(yv2, y2)
#     inserted_2 = insert_t_into_a((xv2, x2), y2_for_t)

#     return solve(inserted_1, inserted_2)


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


# # bounds = (5, 27)
# bounds = (200000000000000, 400000000000000)
# def is_in(pos):
#     for dim in pos:
#         if dim is None:
#             return False
#         if dim < bounds[0]:
#             return False
#         if dim > bounds[1]:
#             return False
#     return True


# total = 0
# for index1, s1 in enumerate(stones):
#     s1_reversed = (tuple(reversed(s1[0])), tuple(reversed(s1[1])))
#     for index2 in range(index1 + 1, len(stones)):
#         s2 = stones[index2]
#         s2_reversed = (tuple(reversed(s2[0])), tuple(reversed(s2[1])))

#         y = get_ans(s1, s2)
#         x = get_ans(s1_reversed, s2_reversed)
#         point = (x, y)
#         print_blue(f'{s1}, {s2}\n    {point}')
#         if is_in(point):
#             if stone_is_impossible(point, s1) or stone_is_impossible(point, s2):
#                 continue
#             total += 1
#             print(f'    INSIDE: {point}')
# print(total)
        

# # 14672 correct



# # 1. represent y as t for both
# # 2. sub t (1) into x for both
# # 3. set aboves equal to each other


# # Hailstone A: (19, 13) (-2,  1)
# # Hailstone B: (18, 19) (-1, -1)



# # x = (-2t + 19)
# # y = (t + 13)
#     # t = y - 13
# # x = -2y + 45


# # x = (-t + 18)
# # y = (-t + 19)
#     # t = 19 - y

# # x = y - 1

# # y - 1 = -2y + 45
# # 3y = 46
# # y = 46/3






