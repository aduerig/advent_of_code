# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

with open(data_file) as f:
    for line in f.readlines():
        digits = list(reversed(list(map(int, line.strip()))))

# digits = [1, 1, 1, 2, 2, 1]

# digits = list(reversed(digits))

for i in range(50):
    new_guy = []
    while digits:
        thing = digits.pop()
        counter = 1
        while digits and digits[-1] == thing:
            digits.pop()
            counter += 1
        new_guy += [counter, thing]
    digits = list(reversed(new_guy))
# print(f'final digits {list(reversed(digits))}')
# 1317612 too high
# 731734 too high
# 12 is wrong
print(len(''.join(map(str, digits))))
