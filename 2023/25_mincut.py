# https://adventofcode.com/2023
import pathlib
import sys

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
            add_to_graph(from_node, to_node)


def mincut(node1, node2, iterations):
    pass


for node1 in graph:
    for node2 in graph:
        if node1 == node2:
            continue
        mincut(node1, node2, 1000)