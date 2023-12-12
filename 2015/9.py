# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


m = {}
all_places = set()
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            places, num = line.split('=')
            fr, to = places.split('to')
            fr = fr.strip()
            to = to.strip()
            if fr not in m:
                m[fr] = []
            if to not in m:
                m[to] = []
            m[fr].append((to.strip(), int(num.strip())))
            m[to].append((fr.strip(), int(num.strip())))

maxy = float('-inf')
def dfs(visited, place, dist):
    visited.add(place)
    if len(visited) == len(m):
        global maxy
        maxy = max(maxy, dist)
        print(f'Visited {len(visited)} places for {dist}, at {place}')
        return visited.remove(place)

    for next_place, cost in m.get(place, []):
        if next_place not in visited:
            dfs(visited, next_place, dist + cost)
    visited.remove(place)

for place in m:
    dfs(set(), place, 0)
print(maxy)




# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# m = {}
# all_places = set()
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             places, num = line.split('=')
#             fr, to = places.split('to')
#             fr = fr.strip()
#             to = to.strip()
#             if fr not in m:
#                 m[fr] = []
#             if to not in m:
#                 m[to] = []
#             m[fr].append((to.strip(), int(num.strip())))
#             m[to].append((fr.strip(), int(num.strip())))

# minny = float('inf')
# def dfs(visited, place, dist):
#     visited.add(place)
#     if len(visited) == len(m):
#         global minny
#         minny = min(minny, dist)
#         print(f'Visited {len(visited)} places for {dist}, at {place}')
#         return visited.remove(place)

#     for next_place, cost in m.get(place, []):
#         if next_place not in visited:
#             dfs(visited, next_place, dist + cost)
#     visited.remove(place)

# for place in m:
#     dfs(set(), place, 0)
# print(minny)
