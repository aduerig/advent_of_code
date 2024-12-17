# # part 2
# # https://adventofcode.com/2023
# import sys
# import pathlib
# import copy

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# initial_regs = {}
# with open(data_file) as f:
#     a, b, c = f.readline(), f.readline(), f.readline()
#     f.readline()
#     prog = f.readline()
#     for line, label in [(a, 'a'), (b, 'b'), (c, 'c')]:
#         line = line.strip()
#         initial_regs[label] = int(line.split(':')[1].strip())
#     prog = list(map(int, prog.split(':')[1].split(',')))


# # initial_regs = [
# #     0,
# #     1,
# #     2,
# #     3,
# #     initial_regs['a'],
# #     initial_regs['b'],
# #     initial_regs['c'],
# #     7,
# # ]

# initial_regs = {
#     4: initial_regs['a'],
#     5: initial_regs['b'],
#     6: initial_regs['c'],
# }

# def adv(literal, combo):
#     regs[4] = regs[4] // pow(2, combo)

# def bxl(literal, combo):
#     regs[5] = regs[5] ^ literal

# def bst(literal, combo):
#     regs[5] = combo % 8

# def jnz(literal, combo):
#     global instruction_pointer
#     if regs[4] != 0:
#         instruction_pointer = literal
#         return True

# def bxc(literal, combo):
#     regs[5] = regs[5] ^ regs[6]

# def out(literal, combo):
#     final.append(combo % 8)

# def bdv(literal, combo):
#     regs[5] = regs[4] // pow(2, combo)

# def cdv(literal, combo):
#     regs[6] = regs[4] // pow(2, combo)

# ops = {
#     0: adv,
#     1: bxl,
#     2: bst,
#     3: jnz,
#     4: bxc,
#     5: out,
#     6: bdv,
#     7: cdv,
# }

# combos = [
#     lambda: 0,
#     lambda: 1,
#     lambda: 2,
#     lambda: 3,
#     lambda: regs[4],
#     lambda: regs[5],
#     lambda: regs[6],
#     lambda: 7,
# ]

# def match_so_far(a, b):
#     for x, z in zip(a, b):
#         if x != z:
#             return False
#     return True

# regs = None
# final = None
# instruction_pointer = 0
# def try_it(a_val):
#     global regs, final, instruction_pointer
#     regs = copy.deepcopy(initial_regs)
#     regs[4] = a_val
#     final = []
#     instruction_pointer = 0
#     while True:
#         print(f'{regs}')
#         if len(final) > len(prog) or not match_so_far(prog, final) or instruction_pointer >= len(prog) - 1:
#             break
#         operand = prog[instruction_pointer + 1]
#         combo = combos[operand]()
#         operand_func = ops[prog[instruction_pointer]]
#         if not operand_func(operand, combo):
#             instruction_pointer += 2
#     return final


# print(','.join(map(str, try_it(117440))))
# exit()

# for i in range(1000000000):
#     if i % 1000000 == 0:
#         print(f'{i:,}')
#     if prog == try_it(i):
#         print(i)
#         exit()




# part 2
# https://adventofcode.com/2023
import sys
import pathlib
import copy

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

initial_regs = {}
with open(data_file) as f:
    a, b, c = f.readline(), f.readline(), f.readline()
    f.readline()
    prog = f.readline()
    for line, label in [(a, 'a'), (b, 'b'), (c, 'c')]:
        line = line.strip()
        initial_regs[label] = int(line.split(':')[1].strip())
    prog = list(map(int, prog.split(':')[1].split(',')))

initial_regs = [
    0,
    1,
    2,
    3,
    initial_regs['a'],
    initial_regs['b'],
    initial_regs['c'],
    7,
]

def adv(literal, combo):
    regs[4] = regs[4] // pow(2, combo)

def bxl(literal, combo):
    regs[5] = regs[5] ^ literal

def bst(literal, combo):
    regs[5] = combo % 8

def jnz(literal, combo):
    global instruction_pointer
    if regs[4] != 0:
        instruction_pointer = literal
        return True

def bxc(literal, combo):
    regs[5] = regs[5] ^ regs[6]

def out(literal, combo):
    final.append(combo % 8)

def bdv(literal, combo):
    regs[5] = regs[4] // pow(2, combo)

def cdv(literal, combo):
    regs[6] = regs[4] // pow(2, combo)

ops = [
    adv,
    bxl,
    bst,
    jnz,
    bxc,
    out,
    bdv,
    cdv,
]

combos = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: regs[4],
    5: lambda: regs[5],
    6: lambda: regs[6],
    7: lambda: 7,
}

def match_so_far(a, b):
    for x, z in zip(a, b):
        if x != z:
            return False
    return True

regs = None
final = None
instruction_pointer = 0
def try_it(a_val, print_out=False):
    global regs, final, instruction_pointer
    regs = copy.deepcopy(initial_regs)
    regs[4] = a_val
    final = []
    instruction_pointer = 0
    while True:
        if len(final) > len(prog) or not match_so_far(prog, final) or instruction_pointer >= len(prog) - 1:
            break
        opcode, operand = prog[instruction_pointer], prog[instruction_pointer + 1]
        combo = combos[operand]()
        operand_func = ops[opcode]
        ret = operand_func(operand, combo)
        if not ret:
            instruction_pointer += 2
    return final


# print(','.join(map(str, try_it(117440))))
# exit()

time_start = time.time()
for i in range(10000000000000000000):
    print_out = False
    if i % 1000000 == 0:
        print(f'{i:,} iter/s: {int((i + 1) / (time.time() - time_start)):,}')
        print_out = True
    if prog == try_it(i, print_out=print_out):
        print(i)
        exit()


# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# instruction_pointer = 0
# regs = {}
# with open(data_file) as f:
#     a, b, c = f.readline(), f.readline(), f.readline()
#     f.readline()
#     prog = f.readline()
#     for line, label in [(a, 'a'), (b, 'b'), (c, 'c')]:
#         line = line.strip()
#         regs[label] = int(line.split(':')[1].strip())
#     print(prog)
#     prog = list(map(int, prog.split(':')[1].split(',')))


# def adv(literal, combo):
#     regs['a'] = regs['a'] // pow(2, combo)

# def bxl(literal, combo):
#     regs['b'] = regs['b'] ^ literal

# def bst(literal, combo):
#     regs['b'] = combo % 8

# def jnz(literal, combo):
#     global instruction_pointer
#     if regs['a'] != 0:
#         instruction_pointer = literal
#         return True

# def bxc(literal, combo):
#     regs['b'] = regs['b'] ^ regs['c']

# final = []
# def out(literal, combo):
#     final.append(str(combo % 8))

# def bdv(literal, combo):
#     regs['b'] = regs['a'] // pow(2, combo)

# def cdv(literal, combo):
#     regs['c'] = regs['a'] // pow(2, combo)

# ops = {
#     0: adv,
#     1: bxl,
#     2: bst,
#     3: jnz,
#     4: bxc,
#     5: out,
#     6: bdv,
#     7: cdv,
# }

# combos = {
#     4: lambda: regs['a'],
#     5: lambda: regs['b'],
#     6: lambda: regs['c'],
# }

# def track(the_id):
#     for func in ops.values():
#         if id(func) == the_id:
#             return func 

# ins_used = {id(x): False for x in ops.values()}
# while True:
#     if instruction_pointer >= len(prog) - 1:
#         break
#     opcode, operand = prog[instruction_pointer], prog[instruction_pointer + 1]
#     combo = combos.get(operand, lambda: operand)()
#     operand_func = ops[opcode]
#     ins_used[id(operand_func)] = True
#     ret = operand_func(operand, combo)
#     if not ret:
#         instruction_pointer += 2


# print('Not used instructions')
# for ins_id, v in ins_used.items():
#     if not v:
#         print(track(ins_id))



# print(','.join(final))

# # 7,7,7,7,7,5,7,7,5 wrong