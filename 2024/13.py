# part 2, assuming only 1 answer
# https://adventofcode.com/2023
import sys
import pathlib
import math


filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


lines = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
things = []
index = 0
while index < len(lines):
    line = lines[index].strip()
    if line:
        button_a = lines[index]
        button_b = lines[index+1]
        prize = lines[index+2]
        things.append((button_a, button_b, prize))
        index += 3
    else:
        index += 1


def extract(guy):
    a_x, a_y = guy.split(':')[1].split(',')
    return int(a_x.split('+')[1]), int(a_y.split('+')[1])


def extract2(guy, add_extra=0):
    ans_x, ans_y = guy.split(':')[1].split(',')
    return int(ans_x.split('=')[1]) + add_extra, int(ans_y.split('=')[1]) + add_extra


tokens = 0
for index, (a, b, prize) in enumerate(things):
    a_x, a_y = extract(a)
    b_x, b_y = extract(b)
    # ans_x, ans_y = extract2(prize, add_extra=0)
    ans_x, ans_y = extract2(prize, add_extra=10000000000000)

    if a_x % b_x == 0 or b_x % a_x == 0:
        print(f'{index}: Have: a - {a_x, a_y}, b - {b_x, b_y}, Need answer: {ans_x, ans_y}')
    continue
    print(f'{index}: Have: a - {a_x, a_y}, b - {b_x, b_y}, Need answer: {ans_x, ans_y}')

    def works(a_presses, b_presses, a, b, ans):
        return a_presses * a + b_presses * b == ans
    # if index== 1:
    #     exit()
    def calc(first, second, ans, n=10):
        num = 0
        valids = []
        while len(valids) < n and num < 10000000:
            have = num * first
            needed = ans - have
            if needed % second == 0:
                a_presses = num
                b_presses = needed // second
                valids.append((a_presses, b_presses, first, second, ans))
            num += 1
        return valids
    
    valid_x_1 = calc(a_x, b_x, ans_x)
    valid_y_1 = calc(a_y, b_y, ans_y)

    if len(valid_x_1) < 3 or len(valid_y_1) < 3:
        continue

    def find_diffy(valids):
        a_diff = valids[1][0] - valids[0][0]
        b_diff = valids[1][1] - valids[0][1]

        a_start = valids[0][0]
        b_start = valids[0][1]

        a_iter = a_start
        b_iter = b_start
        index = 0
        # print(f'{a_start=}, {b_start=}, {a_diff=}, {b_diff=}')
        while index < len(valids):
            a_presses, b_presses, first, second, ans = valids[index]
            if a_iter != a_presses:
                print(f'{index}: No matchy for a: {a_iter} != {a_presses}')
                exit()
            if b_iter != b_presses:
                print(f'{index}: No matchy for b: {b_iter} != {b_presses}')
                exit()
            a_iter += a_diff
            b_iter += b_diff
            index += 1
        return a_start, a_diff, b_start, b_diff

    diffy_x_1 = find_diffy(valid_x_1)
    diffy_y_1 = find_diffy(valid_y_1)
    
    print(diffy_x_1)
    print(diffy_y_1)

    def find_first(diffy_x_1, diffy_y_1):
        for i in range(max(diffy_x_1[0], diffy_y_1[0]), 100000000):
            if i % diffy_x_1[1] == diffy_x_1[0] and i % diffy_y_1[1] == diffy_y_1[0]:
                return i
    

    a_curr_presses = find_first(diffy_x_1[:2], diffy_y_1[:2])
    if a_curr_presses is None:
        continue

    a_to_add = math.lcm(diffy_x_1[1], diffy_y_1[1])

    def solve(a_curr_presses):
        print(f'{a_curr_presses=}, {a_to_add=}')
        for i in range(1000000000000000):
            curr_x = a_curr_presses * a_x
            curr_y = a_curr_presses * a_y

            needed_x = ans_x - curr_x
            needed_y = ans_y - curr_y

            needed_b_presses_x = needed_x / b_x
            # needed_b_presses_y = needed_y / b_y


            if needed_x // b_x == needed_y // b_y:
                # print(f'Answer: {a_curr_presses=}, {needed_b_presses_x=}, {needed_b_presses_y=}')
                return a_curr_presses, int(needed_b_presses_x)
            
            if needed_b_presses_x < 0:
                return None, None

            # loss = abs(needed_x) + abs(needed_y)
            # if i % 100000000 == 0:
            #     print(f'{a_curr_presses:,}: {loss}, {needed_b_presses_x:.2f}, {needed_b_presses_y:.2f}')

            a_curr_presses += a_to_add
    
    a_press, b_press = solve(a_curr_presses)
    print(f'     Answer: {a_press=}, {b_press=}')
    if a_press is not None:
        tokens += a_press * 3 + b_press
print('TOTAL TOKENS:', tokens)


# TOTAL TOKENS: 74914228471331

# part 2 old strat
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# lines = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         lines.append(line)
# things = []
# index = 0
# while index < len(lines):
#     line = lines[index].strip()
#     if line:
#         button_a = lines[index]
#         button_b = lines[index+1]
#         prize = lines[index+2]
#         things.append((button_a, button_b, prize))
#         index += 3
#     else:
#         index += 1


# def extract(guy):
#     a_x, a_y = guy.split(':')[1].split(',')
#     return int(a_x.split('+')[1]), int(a_y.split('+')[1])


# def extract2(guy, add_extra=0):
#     a_x, a_y = guy.split(':')[1].split(',')
#     return int(a_x.split('=')[1]) + add_extra, int(a_y.split('=')[1]) + add_extra


# to_solve = []
# for a, b, prize in things:
#     a_x, a_y = extract(a)
#     b_x, b_y = extract(b)
#     # ans_x, ans_y = extract2(prize, add_extra=0)
#     ans_x, ans_y = extract2(prize, add_extra=10000000000000)
#     to_solve.append(((a_x, a_y), (b_x, b_y), (ans_x, ans_y)))
# costs = {i:1 for i in range(len(to_solve))}


# start_time = 0
# print_every = .5
# last_print_time = time.time() - .3
# total = 0
# index = 0
# while True:
#     cost = costs[index]
#     if last_print_time < time.time() - print_every:
#         stuff = []
#         total = 0
#         for p, cost in costs.items():
#             if isinstance(cost, tuple):
#                 stuff.append(f'S! {cost}')
#             else:
#                 stuff.append(cost)
#         print(f'On cost: {cost}, solved: {stuff}')
#         last_print_time = time.time()

#     if not isinstance(cost, tuple):
#         (a_x, a_y), (b_x, b_y), (ans_x, ans_y) = to_solve[index]
        
#         a_i = 0
#         b_i = cost
#         while True:
#             if a_i * 3 > cost or b_i < 0:
#                 break
            
#             x = a_i * a_x + b_i * b_x
#             y = a_i * a_y + b_i * b_y
#             # print(f'Trying of prize {ans_x, ans_y} at {a_i, b_i}, {a_x, a_y=}, {b_x, b_y=}')

#             if ans_x % x == 0 and ans_y % y == 0:
#                 print(f'Win of prize {ans_x, ans_y} at {a_i, b_i}, {a_x, a_y=}, {b_x, b_y=}')
#                 total += cost
#                 costs[index] = (a_i, b_i)
#                 break
#             b_i -= 3
#             a_i += 1

#     if not isinstance(costs[index], tuple):
#         costs[index] += 1
#     index = (index + 1) % len(costs)
        

# 1280 wrong


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# # def gcd(x, y):
# #     if y == 0:
# #         return x
# #     return gcd(y, x % y)


# # grid = []
# # with open(data_file) as f:
# #     for line in f.readlines():
# #         line = line.strip()
# #         if line:
# #             grid.append(list(line))



# lines = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         lines.append(line)
# things = []
# index = 0
# while index < len(lines):
#     line = lines[index].strip()
#     if line:
#         button_a = lines[index]
#         button_b = lines[index+1]
#         prize = lines[index+2]
#         things.append((button_a, button_b, prize))
#         index += 3
#     else:
#         index += 1


# def extract(guy):
#     a_x, a_y = guy.split(':')[1].split(',')
#     return int(a_x.split('+')[1]), int(a_y.split('+')[1])


# def extract2(guy):
#     a_x, a_y = guy.split(':')[1].split(',')
#     return int(a_x.split('=')[1]), int(a_y.split('=')[1])

# pairs = []
# for a_i in range(100):
#     for b_i in range(100):
#         pairs.append((3 * a_i + b_i * 1, a_i, b_i,))
# pairs.sort()

# total = 0
# for a, b, prize in things:
#     a_x, a_y = extract(a)
#     b_x, b_y = extract(b)
#     ans_x, ans_y = extract2(prize)

#     for cost, a_i, b_i in pairs:
#         x = a_i * a_x + b_i * b_x
#         y = a_i * a_y + b_i * b_y

#         if (ans_x, ans_y) == (x, y):
#             print(f'Win of prize {ans_x, ans_y} at {a_i, b_i}, {a_x, a_y=}, {b_x, b_y=}')
#             total += cost
#             break

# print(total)

# # 1280 wrong