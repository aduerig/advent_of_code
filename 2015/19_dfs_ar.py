# https://adventofcode.com/2023
import sys
import pathlib
import random
sys.setrecursionlimit(10000)
  

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 


def split_into_chemicals(string):
    arr = []
    i = 0
    while i < len(string):
        a = string[i]
        if i != len(string) - 1 and string[i+1].islower():
            a += string[i+1]
            i += 1
        arr.append(a)
        i += 1
    return tuple(arr)


def get_chemicals_to_indicies(chemicals):
    indicies = {}
    for index, chem in enumerate(chemicals):
        if chem not in indicies:
            indicies[chem] = []
        indicies[chem].append(index)
    return indicies


mapping = {}
reverse_mappings = []
with open(filepath.parent.joinpath('19.dat')) as f:
    lines = f.read().splitlines()
    for index, line in enumerate(lines):
        if not line:
            goal = lines[index + 1]
            break

        fr, to = line.split(' => ')
        if fr not in mapping:
            mapping[fr] = []
        mapping[fr].append(split_into_chemicals(to))

        reverse_mappings.append((split_into_chemicals(to), fr))


goal_chemical_ar_sections = [split_into_chemicals(x + 'Ar') for x in goal.split('Ar')[:-1]]
goal_chemicals = split_into_chemicals(goal)

def can_reduce(chemical):
    if chemical not in mapping:
        return False
    
    for sub in mapping[chemical]:
        if chemical not in sub:
            return False
    return True


avaliable = {}
cannot_remap = set()
for chemical in goal_chemicals:
    if chemical not in mapping:
        cannot_remap.add(chemical)
    
    if not can_reduce(chemical):
        avaliable[chemical] = goal_chemicals.count(chemical)
print(f'{avaliable=}')
print(f'{cannot_remap=}')
print(f'Win when have: {len(goal_chemicals)} chemicals')

cache = {}
def dfs(chemicals):
    if len(chemicals) == 1:
        return set([chemicals])

    if chemicals in cache:
        return cache[chemicals]
    
    chem_to_indicies = get_chemicals_to_indicies(chemicals)
    possibilities = set([chemicals])
    for from_sequence, to_chemical in reverse_mappings:
        for index in chem_to_indicies.get(from_sequence[0], []):
            if chemicals[index:index+len(from_sequence)] == from_sequence:
                new = chemicals[:index] + tuple([to_chemical]) + chemicals[index+len(from_sequence):]
                possibilities = possibilities.union(dfs(new))
    cache[chemicals] = possibilities
    return possibilities

for index, section in enumerate(goal_chemical_ar_sections):
    possible = dfs(section)
    print(f'{index} - {"".join(section)} - {len(possible)}')
    print(f'    {["".join(x) for x in possible]}')