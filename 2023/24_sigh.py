# https://adventofcode.com/2023
import pathlib
import sys
import math

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

abs_min_x = float('inf')
abs_max_x = -float('inf')


negatives = []
positives = []
for s in stones:
    abs_min_x = min(abs_min_x, s[0][0])
    abs_max_x = max(abs_max_x, s[0][0])
    if s[1][0] > 0:
        min_x = min(min_x, s[0][0])
        negatives.append((s[1][0], s[0][0]))
    else:
        max_x = max(max_x, s[0][0])
        positives.append((s[1][0], s[0][0]))

negatives.sort()
positives.sort()
print(f'{negatives=}')
print(f'{positives=}')


print(f'{max_x=}, {min_x=}')
print(f'{max_x - min_x:,}')



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
    a1_for_t = solve_for_t(s1[1][dim], s1[0][dim], label=dim_label(dim))
    a2_for_t = solve_for_t(s2[1][dim], s2[0][dim], label=dim_label(dim))
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
    

# def possible_velocities(dim):
#     vel = -1
#     while True:
#         # print_blue(f'{dim_label(dim)}: {vel=}')
#         collisions = get_collision_times(abs_max_x * 2, vel, stones, dim)
#         if any([c is False or c is True for c in collisions]):
#             vel -= 1
#             continue

#         if any([c < 1 for c in collisions]):
#             break

#         yield vel
#         vel -= 1

#     vel = 1
#     while True:
#         # print_blue(f'{dim_label(dim)}: {vel=}')
#         collisions = get_collision_times(abs_max_x * 2, vel, stones, dim)
#         if any([c < 1 for c in collisions]):
#             break

#         yield vel
#         vel += 1
    



for xvel in range(-100, 100):
    if xvel == 0: 
        continue

    for yvel in range(-100, 100):
        if yvel == 0: 
            continue
        for zvel in range(-100, 100):
            if zvel == 0: 
                continue
            
        pos = [0, 0, 0]
        while True:
            x_collisions = get_collision_times(abs_max_x * 2, pos[0], stones, 0)
            y_collisions = get_collision_times(abs_max_x * 2, pos[1], stones, 1)
            z_collisions = get_collision_times(abs_max_x * 2, pos[2], stones, 2)
            




