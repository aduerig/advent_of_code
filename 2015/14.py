# https://adventofcode.com/2023
import sys
import pathlib
import re

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')




deer = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            speed, active, rest = list(map(int, re.findall(r'\d+', line)))
            deer.append([0, 0, speed, active, rest, active + rest])


def max_dim(arr, dim):
    best = float('-inf')
    for index in range(len(arr)):
        val = arr[index][dim]
        if val > best:
            best = val
    return best


def argmax(arr, dim):
    stuff = []
    best = max_dim(arr, dim)
    for index in range(len(arr)):
        if arr[index][dim] == best:
            stuff.append(index)
    return stuff


timer = 0
while timer < 2503:
    for index, (score, dist, speed, active, rest, combined) in enumerate(deer):
        offset = timer % combined
        if offset < active:
            deer[index][1] += speed
    for index in argmax(deer, 1):
        deer[index][0] += 1
    timer += 1

print(max_dim(deer, 0))

# too low 472 
# too low 647

# deleted part 1 by accident, its somewhere in git probably