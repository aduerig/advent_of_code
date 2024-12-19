# https://adventofcode.com/2023
import sys
import pathlib

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
    a_x, a_y = guy.split(':')[1].split(',')
    return int(a_x.split('=')[1]) + add_extra, int(a_y.split('=')[1]) + add_extra


last_a_presses_inv = None
last_b_presses_inv = None
last_a_presses_def = None
last_a_presses_def = None
total = 0
for a, b, prize in things[1:]:
    a_x, a_y = extract(a)
    b_x, b_y = extract(b)
    # ans_x, ans_y = extract2(prize, add_extra=0)
    ans_x, ans_y = extract2(prize, add_extra=10000000000000)


    def works(a_presses, b_presses, a, b, ans):
        return a_presses * a + b_presses * b == ans

    num = 0
    while True:
        for i in range(2):
            first, second, invert = [[a_x, b_x, False], [b_x, a_x, True]][i]
            
            have = num * first
            needed = ans_x - have
            if needed % second == 0:
                a_presses = num
                b_presses = needed // second
                # print(f'X DETECTOR {ans_x, ans_y} at {a_presses, b_presses=} {a_x, a_y=}, {b_x, b_y=}, {have=}, {needed=}')

                if invert:
                    a_presses, b_presses = b_presses, a_presses

                # if invert:
                #     # if last_a_presses_inv is not None:
                #     #     print(f'Diff: {a_presses - last_a_presses_inv}, new: {a_presses}')

                #     last_a_presses_inv = a_presses
                #     last_b_presses_inv = b_presses
                # else:
                #     # if last_a_presses_def is not None:
                #     #     print(f'Diff: {a_presses - last_a_presses_def}, new: {a_presses}')

                #     last_a_presses_def = a_presses
                #     last_b_presses_def = b_presses

                if works(a_presses, b_presses, a_y, b_y, ans_y):
                    print(f'WOW: {a_presses, b_presses=}')
                # if not works(a_presses, b_presses, a_x, b_x, ans_x):
                #     print(f'FAILED')
                #     exit()
        num += 1


    # for cost, a_i, b_i in pairs:
    #     x = a_i * a_x + b_i * b_x
    #     y = a_i * a_y + b_i * b_y

    #     if (ans_x, ans_y) == (x, y):
    #         print(f'Win of prize {ans_x, ans_y} at {a_i, b_i}, {a_x, a_y=}, {b_x, b_y=}')
    #         total += cost
    #         break





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