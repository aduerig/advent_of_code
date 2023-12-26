# https://adventofcode.com/2023
import pathlib
import sys

sys.setrecursionlimit(1000000)
filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

all_nodes = set()
connections = set()
graph = {}
with open(data_file) as f:
    for line in f.read().splitlines():
        from_thing, to_arr = line.split(':')
        from_thing = from_thing.strip()
        if from_thing not in graph:
            graph[from_thing] = []

        for i in to_arr.strip().split():
            if i not in graph:
                graph[i] = []
            graph[i].append(from_thing)
            graph[from_thing].append(i)
            connections.add(tuple(sorted([i, from_thing])))
            all_nodes.add(i)
            all_nodes.add(from_thing)



def visit_things(curr, graph, bad_connections, visited):
    if curr in visited:
        return
    visited.add(curr)
    
    for node in graph[curr]:
        if (node, curr) in bad_connections or (curr, node) in bad_connections:
            continue
        visit_things(node, graph, bad_connections, visited)


cached = 0
connections = list(connections)
bad_connections = set()
for a in range(len(connections)):
    print_blue(f'{a=}')
    a_ele = connections[a]
    bad_connections.add(a_ele)
    for b in range(a+1, len(connections)):
        print(f'{b=}')
        b_ele = connections[b]
        bad_connections.add(b_ele)
        for c in range(b+1, len(connections)):
            c_ele = connections[c]
            bad_connections.add(c_ele)
            visited = set()
            for index, node in enumerate(all_nodes):
                seen = visit_things(node, graph, bad_connections, visited)
                if len(visited) == len(all_nodes):
                    if index == 0:
                        break
                    else:
                        print(cached * (len(visited) - cached))
                        exit()
                cached = len(visited)
            bad_connections.remove(c_ele)
        bad_connections.remove(b_ele)
    bad_connections.remove(a_ele)
