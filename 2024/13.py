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


def extract2(guy):
    a_x, a_y = guy.split(':')[1].split(',')
    return int(a_x.split('=')[1]) + 10000000000000, int(a_y.split('=')[1]) + 10000000000000


to_solve = []
for a, b, prize in things:
    a_x, a_y = extract(a)
    b_x, b_y = extract(b)
    ans_x, ans_y = extract2(prize)
    to_solve.append(((a_x, a_y), (b_x, b_y), (ans_x, ans_y)))

costs = {i:1 for i in range(len(to_solve))}


start_time = 0
print_every = .5
last_print_time = time.time() - .3
total = 0
index = 0
while True:
    cost = costs[index]
    if last_print_time < time.time() - print_every:
        stuff = []
        total = 0
        for p, cost in costs.items():
            if isinstance(cost):
                stuff.append(f'S! {cost}')
            else:
                stuff.append(cost)
        print(f'On cost: {cost}, solved: {stuff}')
        last_print_time = time.time()

    if isinstance(cost, tuple):
        continue
    (a_x, a_y), (b_x, b_y), (ans_x, ans_y) = to_solve[index]
    
    a_i = 0
    b_i = cost
    while True:
        if a_i * 3 > cost or b_i < 0:
            break
        
        x = a_i * a_x + b_i * b_x
        y = a_i * a_y + b_i * b_y

        if ans_x % x == 0 and ans_y % y == 0:
            print(f'Win of prize {ans_x, ans_y} at {a_i, b_i}, {a_x, a_y=}, {b_x, b_y=}')
            total += cost
            costs[index] = (a_i, b_i)
            break

        b_i -= 3
        a_i += 3
    costs[index] += 1
    index = (index + 1) % len(costs)
        

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