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
        if line:
            stones = list(map(int, line.split()))



cache = {}
def needed(num, blink_left):
    if blink_left == 0:
        return 1
    if (num, blink_left) in cache:
        return cache[(num, blink_left)]
    
    if num == 0:
        ans = needed(1, blink_left - 1)

    elif len(str(num)) % 2 == 0:
        left, right = str(num)[:len(str(num))//2], str(num)[len(str(num))//2:]
        ans = needed(int(left), blink_left - 1) + needed(int(right), blink_left - 1)

    else:
        ans = needed(num * 2024, blink_left - 1)

    cache[(num, blink_left)] = ans
    return ans


total = 0
for s in stones:
    total += needed(s, 75)
print(total)