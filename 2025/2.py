# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()


def invalid(n):
    s = str(n)
    if n % 2 == 0:
        half = len(s) // 2
        a, b = s[:half], s[half:]
        return a == b
    return True

total = 0
ranges = line.split(',')
for r in ranges:
    first_id, last_id = map(int, r.split('-'))

    for i in range(first_id, last_id + 1):
        if invalid(i):
            total += i

print(total)

# 1227775554
# 651329497582753