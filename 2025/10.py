# forgot to save part 1

# https://adventofcode.com/2023
import sys
import pathlib
import time
from collections import deque

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}



machines = []
with open(data_file) as f:
    for line in f.readlines():

        line = line.strip()
        other, jolts = line.split('{')
        jolts = list(map(int, jolts.strip().strip('}').split(',')))

        indic, other = other.split(']')
        indic = list(indic.strip().strip('['))

        all_buttons = []
        for b in other.strip().split():
            b = b.strip('()')
            whole_button = list(map(int, b.split(',')))
            all_buttons.append(whole_button)

        whole_machine = (indic, all_buttons, jolts)
        machines.append(whole_machine)


def recurse(curr, all_buttons, visited, presses):
    if all([x == 0 for x in curr]):
        return presses
    
    if curr in visited:
        return visited[curr]

    for button in all_buttons:
        legal = True
        for b in button:
            if not curr[b]:
                legal = False
        if legal:
            new_curr = list(curr)
            for b in button:
                new_curr[b] -= 1
            ans = recurse(tuple(new_curr), all_buttons, visited, presses + 1)
            if ans:
                return ans
    visited[curr] = None


def solve_machine(needed_jolt, all_buttons):
    all_buttons.sort(key=lambda x: -len(x))
    return recurse(tuple(needed_jolt), all_buttons, {}, 0)


        

presses = 0
for indic, all_buttons, jolts in machines:
    print(f'indic: {indic}, all_buttons: {all_buttons}, jolts: {jolts}')
    before = time.time()
    ans = solve_machine(tuple(jolts), all_buttons)
    after = time.time()
    presses += ans
    print(f'Solved with {ans} presses in {after - before:.2f} seconds')

print(f'Needs {presses} presses')


# too high: 25975

# too low: 6939
