# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

stones = []
with open(data_file) as f:
    for line in f.read().splitlines():
        p, v = list(map(lambda x: x.strip().split(','), line.split('@')))
        p = list(map(lambda x: int(x.strip()), p))
        v = list(map(lambda x: int(x.strip()), v))
        stones.append((p, v))


bounds = (5, 27)
# bounds = (200000000000000, 400000000000000)
def is_in(pos):
    for dim in pos:
        if dim < bounds[0]:
            return False
        if dim > bounds[1]:
            return False
    return True


for stone in stones:
    (x, y, z), (xv, yv, zv) = stone




# Hailstone A: (19, 13) (-2,  1)
# Hailstone B: (18, 19) (-1, -1)














# Hailstone A: (19, 13) (-2,  1)
# Hailstone B: (18, 19) (-1, -1)


# x = (-2t + 19)
    # t = (x + 19) / 2
# y = (t + 13)
    # t = y - 13


# x = (-t + 18)
    # t = 18 - x
# y = (-t + 19)
    # t = 19 - y



# -2t + 19 = -t + 18
# -2t + 1 = -t
# 1 = t



# 200,000,000,000,000


# 200000000000000
# 400000000000000