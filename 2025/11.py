# forgot to save part 1 this is part 2

# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

graph = {}
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        word, words = line.split(':')
        words = words.strip().split()
        word = word.strip()

        if word not in graph:
            graph[word] = []
        for dest in words:
            graph[word].append(dest)

def recurse(graph, node, seen, seen_dac, seen_fft):
    if node == 'out':
        return int(seen_dac and seen_fft)
    
    the_hash = (node, seen_dac, seen_fft)
    if the_hash in seen:
        return seen[the_hash]

    total = 0
    for sub_node in graph[node]:
        total += recurse(graph, sub_node, seen, seen_dac or sub_node == 'dac', seen_fft or sub_node == 'fft')
    seen[the_hash] = total
    return total

seen = {}
recurse(graph, 'svr', seen, False, False)
print(seen[('svr', False, False)])


# 333852915427200