# https://adventofcode.com/2023
import sys
import pathlib
import time

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


start_time = time.time()

final_mode = False
regions = []
shapes = {}
new_shape = None
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()

        if not final_mode:
            if line:
                if new_shape is None:
                    if ' ' in line:
                        final_mode = True
                    else:
                        new_shape = [int(line.strip(':')), []]
                else:
                    new_shape[-1].append(line)
            else:
                shapes[new_shape[0]] = new_shape[1]
                new_shape = None

        if final_mode:
            first, second = line.split(':')
            width, height = first.split('x')
            presents = list(map(int, second.split()))
            obj = ((int(width), int(height)), presents)
            regions.append(obj)


def num_spots(shape):
    total = 0
    for row in shape:
        for char in row:
            if char == '#':
                total += 1
    return total
                

def rotate(shape) -> str:
    new = []
    for col_index in reversed(list(range(len(shape[0])))):
        ok = []
        for row_index in range(len(shape)):
            ok.append(shape[row_index][col_index])
        new.append(''.join(ok))
    return tuple(new)


def to_bitboard(bitboard_width: int, shape: str) -> int:
    final = 0
    row_inc = 0
    for row in list(reversed(range(len(shape)))):
        building = 0
        col_inc = 0
        for col in list(reversed(range(len(shape[0])))):
            if shape[row][col] == '#':
                building |= 1 << col_inc
            col_inc += 1
        final |= building << (row_inc * bitboard_width)
        row_inc += 1
    return final

def bitboard_to_string(width, height, bitboard):
    rows = []
    for row in range(height):
        all_ones = ((1 << width) - 1)
        row_bits = (bitboard >> (row * width)) & all_ones
        row_stringing = []
        for i in reversed(range(width)):
            if row_bits & (1 << i):
                row_stringing.append('#')
            else:
                row_stringing.append('.')
        rows.append(''.join(row_stringing))
    return '\n'.join(reversed(rows))


def print_all_shape_bitboards(width, height, all_shapes_bitboards):
    for index, (rotations, bitboards) in all_shapes_bitboards.items():
        print(f"Shape {index}:")
        for _rot, bitboard in zip(rotations, bitboards):
            print(bitboard_to_string(width, height, bitboard))
            print()

all_shapes_rotated = {}
for index, shape in shapes.items():
    rotations = set()
    for i in range(4):
        rotations.add(rotate(shape))
        shape = rotate(shape)
    all_shapes_rotated[index] = list(rotations)


backtracks = 0
def recurse(curr_board, width, height, req, just_bitboards, visited, non_occupied):
    visited.add(curr_board)
    all_good = True
    for shape_index, needed in enumerate(req):
        if not needed:
            continue
        all_good = False
        for bitboard in just_bitboards[shape_index]:
            for row, col in non_occupied:
                moved_bitboard = (bitboard << col) << (row * width)
                if moved_bitboard & curr_board == 0:
                    next_board = curr_board | moved_bitboard
                    if next_board not in visited:
                        req[shape_index] -= 1
                        non_occupied.remove((row, col))
                        if recurse(next_board, width, height, req, just_bitboards, visited, non_occupied):
                            return True
                        backtracks += 1
                        req[shape_index] += 1
                        non_occupied.add((row, col))
    if all_good:
        print_green(bitboard_to_string(width, height, curr_board))
        return True

def solve(width, height, required_shapes, just_bitboards):
    print(f'\nGoing to solve: {width}x{height}')
    visited = set()

    non_occupied = set()
    for col in range(width - 2):
        for row in range(height - 2):
            non_occupied.add((row, col))

    return recurse(0, width, height, list(required_shapes), just_bitboards, visited, non_occupied)


final = 0
for region in regions:
    (width, height), required_shapes = region
    all_shapes_bitboards = {}
    for index, rotations in all_shapes_rotated.items():
        bitboards = []
        for i in rotations:
            bitboards.append(to_bitboard(width, i))
        all_shapes_bitboards[index] = [rotations, bitboards]

    needed = 0
    for index, req in enumerate(required_shapes):
        the_shape = all_shapes_rotated[index][0]
        in_shape = num_spots(the_shape)
        needed += in_shape * req
    
    if needed > width * height:
        print_red('Impossible (due to size)')
        continue

    just_bitboards = {key: value[1] for key, value in all_shapes_bitboards.items()}
    if solve(width, height, required_shapes, just_bitboards):
        final += 1
    else:
        print_red('Impossible placement')

end_time = time.time()
print_blue(f'\nAnswer is {final}, solved in {end_time - start_time:.2f} seconds')



