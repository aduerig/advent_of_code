# Each instruction also reads the 3-bit number after it as an input; this is called its operand.

# the program (instruction: operand)
# bst: 4
# bxl: 1
# cdv: 5
# bxc: 7
# bxl: 4
# adv: 3
# out: 5
# jnz: 0


# part 2
# https://adventofcode.com/2023
import copy
import time

# real
initial_regs = {
    'a': 30553366,
    'b': 0,
    'c': 0,
}
prog = [2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0]

# test
# initial_regs = {
#     'a': 2024,
#     'b': 0,
#     'c': 0,
# }
# prog = [0,3,5,4,3,0]

# test 2
# initial_regs = {
#     'a': 729,
#     'b': 0,
#     'c': 0,
# }
# prog = [0,1,5,4,3,0]



def encode(the_list):
    encoded = 0
    for index, num in enumerate(the_list):
        encoded |= num << (index * 3)
    return encoded, index + 1

def decode(encoded, the_len):
    decoded = []
    for i in range(the_len):
        mask = (1 << ((i+1) * 3)) - 1
        extract = mask & encoded
        rel = extract >> (i * 3)
        decoded.append(rel)
    return decoded

prog_encoded, prog_len = encode(prog)
prog_decoded = decode(prog_encoded, prog_len)

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

POW2_TABLE = [2**i for i in range(32)]
regs = copy.deepcopy(initial_regs)
def try_it(a_val):
    regs[4] = a_val
    regs[5] = 0
    regs[6] = 0
    final_encoded = 0
    final_len = 0
    instruction_pointer = 0
    while instruction_pointer < prog_len - 1:
        # print(regs)
        literal = prog[instruction_pointer + 1]
        combo = regs[literal]
        opcode = prog[instruction_pointer]

        if opcode == 0:
            regs[4] = regs[4] // POW2_TABLE[combo]
            instruction_pointer += 2
        if opcode == 1:
            regs[5] = regs[5] ^ literal
            instruction_pointer += 2
        if opcode == 2:
            regs[5] = combo & 7
            instruction_pointer += 2
        if opcode == 3:
            if regs[4] != 0:
                instruction_pointer = literal
            else:
                instruction_pointer += 2
        if opcode == 4:
            regs[5] = regs[5] ^ regs[6]
            instruction_pointer += 2
        if opcode == 5:
            final_encoded |= (combo % 8) << final_len
            final_len += 3
            instruction_pointer += 2
        if opcode == 7:
            regs[6] = regs[4] // POW2_TABLE[combo]
            instruction_pointer += 2
        if (prog_encoded & ((1 << final_len) - 1)) ^ final_encoded:
            return False
    return final_encoded == prog_encoded


starter = 0
num_workers = 1
time_start = time.time()
for i in range(starter, 10000000000000000000, num_workers):
    if i == starter or i % 10000000 == 0:
        print(f'{starter=}, {i:,} iter/s: {round(((i + 1) // num_workers // (time.time() - time_start))):,}')
    if try_it(i):
        print(f'{i=}')
        break



# # part 2 (bruteforce, too slow)
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


# initial_regs = [
#     0,
#     1,
#     2,
#     3,
#     initial_regs['a'],
#     initial_regs['b'],
#     initial_regs['c'],
#     7,
# ]
# def adv(literal, combo, instruction_pointer):
#     regs[4] = regs[4] // pow(2, combo)
#     return instruction_pointer + 2

# def bxl(literal, combo, instruction_pointer):
#     regs[5] = regs[5] ^ literal
#     return instruction_pointer + 2

# def bst(literal, combo, instruction_pointer):
#     regs[5] = combo % 8
#     return instruction_pointer + 2

# def jnz(literal, combo, instruction_pointer):
#     if regs[4] != 0:
#         return literal
#     return instruction_pointer + 2

# def bxc(literal, combo, instruction_pointer):
#     regs[5] = regs[5] ^ regs[6]
#     return instruction_pointer + 2

# def out(literal, combo, instruction_pointer):
#     final.append(combo % 8)
#     return instruction_pointer + 2

# def bdv(literal, combo, instruction_pointer):
#     regs[5] = regs[4] // pow(2, combo)
#     return instruction_pointer + 2

# def cdv(literal, combo, instruction_pointer):
#     regs[6] = regs[4] // pow(2, combo)
#     return instruction_pointer + 2


# cache = {}
# ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
# regs = copy.deepcopy(initial_regs)
# def try_it(a_val):
#     global regs, final, pointers
#     regs[4] = a_val
#     regs[5] = 0
#     regs[6] = 0
#     final = []
#     instruction_pointer = 0
#     pointers = []
#     while True:
#         # key = (instruction_pointer, regs[4], regs[5], regs[6])
#         # if key in cache:
#         #     return False
#         # cache[key] = False
#         pointers.append(instruction_pointer)
#         if instruction_pointer >= len(prog) - 1:
#             print(final)
#             break
#         operand = prog[instruction_pointer + 1]
#         instruction_pointer = ops[prog[instruction_pointer]](operand, regs[operand], instruction_pointer)
#         if (final and final[len(final) - 1] != prog[len(final) - 1]) or len(final) > len(prog):
#             # print(final)
#             return False
#     # print(final)
#     return len(final) == len(prog)

# # print(','.join(map(str, try_it(117440))))
# # exit()

# starter = 0
# num_workers = 1
# time_start = time.time()
# for i in range(starter, 10000000000000000000000000000, num_workers):
#     if i == starter or i % 10000000 == 0:
#         print(f'{starter=}, {i:,} iter/s: {round(((i + 1) // num_workers // (time.time() - time_start))):,}')
#     if try_it(i):
#         print(f'{i=}')
#         break
#     global pointers
#     print(pointers)


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