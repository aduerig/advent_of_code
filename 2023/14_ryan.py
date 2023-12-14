# https://adventofcode.com/2023
import pathlib
import sys
import time

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath('14.dat')



with open(data_file) as f:
    grid = [line for line in f.read().splitlines()]

def west_roll(grid):
    return ['#'.join([('O' * segment.count('O')) + ('.' * (len(segment) - segment.count('O'))) for segment in row.split('#')]) for row in grid]

def rotate_right(grid):
    return [''.join([grid[y][x] for y in reversed(range(len(grid)))]) for x in range(len(grid[0]))]

def roll_all(grid):
    for _ in range(4):
        grid = west_roll(grid)
        grid = rotate_right(grid)
    return grid


start_time = time.time()
for _ in range(3): # we have to roll west, and currently things are facing north, so we rotate 3 times
    grid = rotate_right(grid)
iterations = 1000000000
for i in range(iterations):
    if i % 100 == 0 and i:
        rate = (time.time() - start_time) / i
        iterations - i
        print(f'{(rate * (iterations - i)) / (60 * 60 * 24):,.2f} days remaining to finish')
    grid = roll_all(grid)
grid = rotate_right(grid) # turn back to original direction

print(sum([(len(grid) - index) * line.count('O') for index, line in enumerate(grid)]))