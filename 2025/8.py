# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')



boxes = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        boxes.append(tuple(map(int, line.split(','))))

def get_dist(b1, b2):
    dist = 0
    x1, y1, z1 = b1
    x2, y2, z2 = b2
    ans = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    dist = pow(ans, .5)
    return dist


dists = []
for i1 in range(len(boxes)):
    for i2 in range(i1 + 1, len(boxes)):
        b1 = boxes[i1]
        b2 = boxes[i2]

        dists.append((get_dist(b1, b2), b1, b2))
dists.sort()

connections = {}
def dfs(box, visited):
    if box in visited:
        return 0
    visited.add(box)
    res = 1
    for n in connections.get(box, []):
        res += dfs(n, visited)
    return res

def is_full():
    visited = set()
    dfs(boxes[0], visited)
    return len(boxes) == len(visited)
    

for index, (dist, b1, b2) in enumerate(dists):
    if b1 not in connections:
        connections[b1] = set()
    if b2 not in connections:
        connections[b2] = set()
    connections[b1].add(b2)
    connections[b2].add(b1)

    if is_full():
        print(f'Connected after {index + 1} edges, between {b1} and {b2}')
        print(b1[0] * b2[0])
        exit()





# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# boxes = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         boxes.append(tuple(map(int, line.split(','))))

# def get_dist(b1, b2):
#     dist = 0
#     x1, y1, z1 = b1
#     x2, y2, z2 = b2
#     ans = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
#     dist = pow(ans, .5)
#     return dist


# dists = []
# for i1 in range(len(boxes)):
#     for i2 in range(i1 + 1, len(boxes)):
#         b1 = boxes[i1]
#         b2 = boxes[i2]

#         dists.append((get_dist(b1, b2), b1, b2))
# dists.sort()

# connections = {}
# for index, (dist, b1, b2) in enumerate(dists):
#     if index == 1000:
#         break
#     if b1 not in connections:
#         connections[b1] = set()
#     if b2 not in connections:
#         connections[b2] = set()
#     connections[b1].add(b2)
#     connections[b2].add(b1)

# visited = set()
# def dfs(box):
#     if box in visited:
#         return 0
#     visited.add(box)
#     res = 1
#     for n in connections.get(box, []):
#         res += dfs(n)
#     return res

# sizes = []
# for box in boxes:
#     sizes.append(dfs(box))
# sizes.sort(reverse=True)
# a, b, c = sizes[:3]
# print(f'{a} * {b} * {c} = {a * b * c}')