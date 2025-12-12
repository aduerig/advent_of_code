# forgot to save part 1

# https://adventofcode.com/2023
import sys
import pathlib
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


def solve_machine(needed_jolt, all_buttons):
    start_state = [0] * len(needed_jolt)
    queue = [[tuple(start_state), 0]]
    queue = deque(queue)
    seen = set()
    least_seen = float('inf')
    print(f'{needed_jolt=}')

    unchanged = 0
    while queue:
        curr_jolt, presses = queue.popleft()
        if curr_jolt in seen:
            continue
        seen.add(curr_jolt)
        if curr_jolt == needed_jolt:
            return presses

        unchanged += 1

        if unchanged > 100000 and least_seen < float('inf'):
            return least_seen
        
        mults = []
        for to_go, needed in zip(curr_jolt, needed_jolt):
            if to_go > needed:
                continue

            if to_go == 0:
                if needed == 0:
                    mults.append(True)
                else:
                    mults.append(-1)
            elif needed % to_go == 0:
                mults.append(needed // to_go)
                
        samer = None
        all_same = True
        for m in mults:
            if m is True:
                continue
            if samer is None:
                samer = m
            if m != samer:
                all_same = False
        
        if samer and all_same and samer != -1:
            new = samer * presses
            if new < least_seen:
                least_seen = new
                unchanged = 0

        for b in all_buttons:
            new_jolt = list(curr_jolt)
            for to_flip in b:
                new_jolt[to_flip] += 1
            new_state = [tuple(new_jolt), presses + 1]
            queue.append(new_state)

# too high: 25975

# too low: 6939
        

presses = 0
for indic, all_buttons, jolts in machines:
    print(f'indic: {indic}, all_buttons: {all_buttons}, jolts: {jolts}')
    presses += solve_machine(tuple(jolts), all_buttons)

print(f'Needs {presses} presses')