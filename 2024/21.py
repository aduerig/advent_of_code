# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# real
# pad_numeric = [
#     '789A',
#     '540A',
#     '285A',
#     '140A',
#     '189A',
# ]

# test
pad_numeric = [
    '789',
    '456',
    '123',
    'X0A',
]


pad_directional = [
    'X^A',
    '<v>',
]
directional_start = [2, 0]
numeric_start = [len(pad_numeric[0]) - 1, len(pad_numeric) - 1]


def get_pos():
    pass

def do_it(code):
    needed_index = 0

    numeric = [list(pad_numeric), list(numeric_start)]
    d1 = [list(pad_directional), list(directional_start)]
    d2 = [list(pad_directional), list(directional_start)]

    while needed_index < len(code):
        needed_button = code[needed_index]

        get_pos(needed_button, numeric)


total = 0
needed_codes = ['029A', '980A', '179A', '456A', '379A']
for code in needed_codes:
    shortest = do_it(code)
    leading = int(code[:-1])
    total += shortest * leading
    exit()

