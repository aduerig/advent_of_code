# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


funcs = {
    'AND': lambda x, y: x & y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
    'OR': lambda x, y: x | y,
}


def get_val(s):
    if s in thing:
        return thing[s]
    return int(s)

thing = {}
instructions = {}
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        ops, assignee = line.split('->')
        
        ops = ops.strip()
        assignee = assignee.strip()

        dependancies = [x for x in ops.split() if x.islower()]
        instructions[assignee] = [ops, dependancies]


visited = set()
order = []
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for d in instructions[node][1]:
        dfs(d)
    order.append(node)
dfs('a')

for assignee in order:
    ops = instructions[assignee][0]
    if 'NOT' in ops:
        thing[assignee] = ~thing[ops.replace('NOT ', '')]
    else:
        for key, func in funcs.items():
            if key in ops:
                l, r = ops.split(f' {key} ')
                val = func(get_val(l), get_val(r))
                break
        else:
            val = get_val(ops)
        thing[assignee] = val


print(thing['a'])