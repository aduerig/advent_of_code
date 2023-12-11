# https://adventofcode.com/2023
import sys
import pathlib
import re

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


def travel(speed, active, rest):
    dist = 0
    score = 0
    while timer < 2503:
        finish_time = min(2503, timer + active + rest)
        time_passed = finish_time - timer
        timer += time_passed
        dist += (min(active, time_passed) * speed)
    return dist

# 1092 low

best = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            num = travel(*map(int, re.findall(r'\d+', line)))
            print(num)
            best = max(best, num)
print(best)