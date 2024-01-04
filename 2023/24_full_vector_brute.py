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
        


min_x = float('inf')
max_x = -float('inf')

abs_mins = [float('inf'), float('inf'), float('inf')]
abs_maxs = [-float('inf'), -float('inf'), -float('inf')]


for dim in [0, 1, 2]:
    for s in stones:
        abs_mins[dim] = min(abs_mins[dim], s[0][dim])
        abs_maxs[dim] = max(abs_maxs[dim], s[0][dim])


# print(f'{max_x=}, {min_x=}')
# print(f'{max_x - min_x:,}')



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
    sign = '+' if constant < 0 else '-'
    print(color(f'{label1} = {leading:.2f} * {label2} * {sign} {abs(constant):.2f}'))

# collider
# t = -3x + 24


# misc
# 19, 13, 30 @ -2, 1, -2
# 18, 19, 22 @ -1, -1, -2
    
# t = -2x + 19
# t = -x + 18



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



def get_collision_times(pos, vel, stones, dim):
    collider = [[0, 0, 0], [0, 0, 0]]
    collider[0][dim] = pos
    collider[1][dim] = vel
    collider = (tuple(collider[0]), tuple(collider[1]))

    collisions = []
    for stone in stones:
        collisions.append(collide_at(collider, stone, dim))
    return collisions


def bs_to_starting_pos(stones, vel, left, right):
    while left <= right:
        pos = (left + right) // 2
        collisions = get_collision_times(pos, vel, stones, dim)
        if all([c == 0 for c in collisions]):
            print_green(f'found')
            exit()
        
        # if any([c < 0 for c in collisions]):
        #     left = pos + 1
        # else:
        #     right = pos - 1
        
        last_collisions = get_collision_times(pos - 1, vel, stones, dim)
        for a, b in zip(collisions, last_collisions):
            if a < 0:
                if b < a:
                    left = pos + 1
                else:
                    right = pos - 1
                break
    return left
    

def get_diffs(old_pos, new_pos, vel, stones, dim):
    old_collisions = get_collision_times(old_pos, vel, stones, dim)
    new_collisions = get_collision_times(new_pos, vel, stones, dim)
    return [round(abs(a - b), 7) if type(a) != bool else 0 for a, b in zip(old_collisions, new_collisions)]



def get_cycle_lengths(old_pos, new_pos, vel, stones, dim):
    lens = [round(1 / x, 4) if x != 0 else 0 for x in get_diffs(old_pos, new_pos, vel, stones, dim)]
    return list(map(int, lens))


def get_cycle_positions(cycles, collisions):
    cycle_positions = []
    for cycle_length, collisions in zip(cycles, collisions):
        remain = collisions - int(collisions)
        cycle_positions.append(round(remain * cycle_length, 4))
    return cycle_positions


# ans = curr / cycle_length


def inv(a, m):
    m0 = m  
    x0 = 0
    x1 = 1
  
    if (m == 1):  
        return 0
    while (a > 1):  
        q = a // m    
        t = m  
  
        m = a % m  
        a = t  
  
        t = x0    
        x0 = x1 - q * x0  
  
        x1 = t  
    if (x1 < 0) :  
        x1 = x1 + m0  
  
    return x1  

def findMinX(num, rem, k):  
    prod = 1
    for i in range(0, k) :  
        prod = prod * num[i]  
    result = 0
    for i in range(0, k):  
        pp = prod // num[i]
        print(i, pp, num[i])
        thing = inv(pp, num[i])
        result = result + rem[i] * thing * pp  
    return result % prod  


def cycle_math(pos, cycle_positions, cycles):
    # filtered_cycles = []
    # filtered_positions = []

    # for a, b in zip(cycles, cycle_positions):
    #     if a != 0:
    #         filtered_cycles.append(a)
    #         filtered_positions.append(b)

    # ans = findMinX(filtered_cycles, filtered_positions, len(filtered_cycles))
    # print(ans)

    paired = [[b, a] for a, b in zip(cycle_positions, cycles)]
    paired.sort(reverse=True)
    print('trying')
    for offset in range(paired[0][0] * 100):
        turned = 0
        for index, (cycle_len, curr) in enumerate(paired):
            if cycle_len == 0:
                turned += 1
            else:
                paired[index][1] -= 1
                if paired[index][1] < 0:
                    paired[index][1] = paired[index][0] - 1
                    turned += 1
        if turned == len(paired):
            return True, pos - offset, paired[0][0]

    return False, None, None


def inc_vel(dim):
    i = 1
    while True:
        yield i, -1, abs_mins[dim] // 2
        yield -i, 1, abs_maxs[dim] * 2
        i += 1

@profile
def okokok():
    for dim in [0, 1, 2]:
        print(f'Starting dim: {dim_label(dim)}')
        for vel, dir, extreme in inc_vel(dim):
            if vel % 100 == 0 and vel > 0:
                print(f'{vel=}')

            # print(f'{dim_label(dim)}: {vel, dir, extreme}')
            collisions = get_collision_times(extreme, vel, stones, dim)
            if any([c < 0 for c in collisions]):
                continue

            if any([x is bool for x in collisions]):
                print(f'{vel} skipping due to bool')
                continue

            # if any([c < 1 for c in collisions]):
            #     break

            cycles = get_cycle_lengths(extreme, extreme + dir, vel, stones, dim)

            pos = extreme
            collisions = get_collision_times(pos, vel, stones, dim)
            cycle_positions = get_cycle_positions(cycles, collisions)

            possible, starting_pos, offset = cycle_math(pos, cycle_positions, cycles)

            if not possible:
                # print('SKIPPING')
                continue

            print_blue(f'{dim_label(dim)}: {vel=}')


            print(f'    ', end='')
            for i in cycles:
                print_yellow(f'{i:>8} ', end='')
            print()

            print(f'    ', end='')
            for i, j in zip(collisions, cycle_positions):
                if type(i) == bool:
                    print(f'{str(i):>9} ', end='')
                else:
                    if round(j, 8) != j:
                        print_red('bad round')
                        exit()
                    print(f'{i:>9.3f}, {blue(str(int(j)))}', end='')
            print()



            # for i in range(100):
            #     pos -= 1

            #     collisions = get_collision_times(pos, vel, stones, dim)
            #     if any([c < 1 for c in collisions]):
            #         break

            #     print_red(f'   {pos=}')
            #     print(f'    ', end='')
            #     for i in collisions:
            #         if type(i) == bool:
            #             print(f'{str(i):>9} ', end='')
            #         else:
            #             print(f'{i:>9.3f} ', end='')
            #     print()

okokok()



# for v in range(-10000, 10000):
#     if v == 0:
#         continue

#     collider = [[0, 0, 0], [0, 0, 0]]
#     collider[1][0] = v
#     for index, stone in enumerate(stones):
#         t = collide_at(collider, stone, 0)
#         if t is not True and t != int(t):
#             break
#     else:
#         print_green(f'{dim_label(0)} WORKED: {collider}')




# def insert_into_a(a_eq, t_eq, label1, label2):
#     og_term, constant_1 = a_eq
#     into_term, constant_2 = t_eq
#     print_eq(og_term, constant_1, label1, 't')
#     print_eq(into_term, constant_2, 't', label2)

#     leading = into_term * og_term

#     resultant_constant = constant_1 + (constant_2 * og_term)
#     print_eq(leading, resultant_constant, label1, label2, color=red)
#     return leading, resultant_constant




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

