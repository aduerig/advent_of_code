# https://adventofcode.com/2023
import pathlib
import sys
import random
from copy import deepcopy

sys.setrecursionlimit(1000000)
filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 


data_file = filepath.parent.joinpath('25.dat')


def add_to_graph(f, t):
    if f not in graph:
        graph[f] = []
    graph[f].append(t)


graph = {}
with open(data_file) as f:
    for line in f.read().splitlines():
        from_node, to_arr = list(map(str.strip, line.split(':')))
        for to_node in to_arr.split():
            add_to_graph(from_node, to_node)
            add_to_graph(to_node, from_node)


def get_edges(graph):
    return [[i, j] for i in graph for j in graph[i]]


def mincut(graph):
    while len(graph) > 2:
        edges = get_edges(graph)
        mega, deleted = random.choice(edges)
        graph[mega] = [node for node in graph[mega] if node != deleted]
        for connected in graph[deleted]:
            if connected == mega:
                continue
            for index, sub_node in enumerate(graph[connected]):
                if sub_node == deleted:
                    graph[connected][index] = mega
                    graph[mega].append(connected)
        del graph[deleted]
    print(graph)
    return len(get_edges(graph))


minner = float('inf')
for _ in range(500):
    print(minner)
    minner = min(minner, mincut(deepcopy(graph)))
print_green(minner)