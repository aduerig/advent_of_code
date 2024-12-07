# part 1 and 2, the only difference is commented out line

# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


probs = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            ans, rest = line.strip().split(':')
            ans = int(ans)
            rest = list(map(int, rest.strip().split()))
            probs.append((ans, rest))

def recurse(so_far, rest, ans):
    if so_far > ans:
        return False
    if not rest:
        return so_far == ans
    first, *others = rest
    # part 1
    # return recurse(so_far + first, others, ans) or recurse(so_far * first, others, ans)

    # part 2
    return recurse(so_far + first, others, ans) or recurse(so_far * first, others, ans) or recurse(int(str(so_far) + str(first)), others, ans)



total = 0
for ans, rest in probs:
    if recurse(rest[0], rest[1:], ans):
        total += ans
print(total)