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
def adv(literal, combo, instruction_pointer):
    regs[4] = regs[4] // pow(2, combo)
    return instruction_pointer + 2

def bxl(literal, combo, instruction_pointer):
    regs[5] = regs[5] ^ literal
    return instruction_pointer + 2

def bst(literal, combo, instruction_pointer):
    regs[5] = combo % 8
    return instruction_pointer + 2

def jnz(literal, combo, instruction_pointer):
    if regs[4] != 0:
        return literal
    return instruction_pointer + 2

def bxc(literal, combo, instruction_pointer):
    regs[5] = regs[5] ^ regs[6]
    return instruction_pointer + 2

def out(literal, combo, instruction_pointer):
    final.append(combo % 8)
    return instruction_pointer + 2

def bdv(literal, combo, instruction_pointer):
    regs[5] = regs[4] // pow(2, combo)
    return instruction_pointer + 2

def cdv(literal, combo, instruction_pointer):
    regs[6] = regs[4] // pow(2, combo)
    return instruction_pointer + 2

ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
regs = copy.deepcopy(initial_regs)
def try_it(a_val):
    global regs, final
    regs[4] = a_val
    regs[5] = 0
    regs[6] = 0
    final = []
    instruction_pointer = 0
    while True:
        if instruction_pointer >= len(prog) - 1:
            break
        operand = prog[instruction_pointer + 1]
        if operand == 7:
            return False
        instruction_pointer = ops[prog[instruction_pointer]](operand, regs[operand], instruction_pointer)
        if (final and final[len(final) - 1] != prog[len(final) - 1]) or len(final) > len(prog):
            return False
    return len(final) == len(prog)

# print(','.join(map(str, try_it(117440))))
# exit()

# offset = 0
# if len(sys.argv) > 1:
#     sys.argv[1]


# starter = 0
# starter = 1
# starter = 2
# starter = 3
# starter = 4
# starter = 5
# starter = 6
starter = 7
time_start = time.time()
for i in range(starter, 10000000000000000000000000000, 8):
    if i == starter or i % 10000000 == 0:
        print(f'{starter=}, {i:,} iter/s: {round(((i + 1) // 8 // (time.time() - time_start))):,}')
    if try_it(i):
        print(f'{i=}')
        break


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