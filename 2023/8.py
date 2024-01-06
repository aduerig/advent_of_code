# https://adventofcode.com/2023
import pathlib
import sys
import time

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
# from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


rl_to_index = {
    'R': 1,
    'L': 0,
}

graph = {}
all_nodes = set()
with open(data_file) as f:
    path_rl = f.readline().strip()
    for line in f.readlines():
        if line.strip():
            fr, to = line.strip().split('=')

            a, b = to.replace('(', '').replace(')', '').strip().split(',')

            
            graph[fr.strip()] = [a.strip(), b.strip()]
            all_nodes.add(fr.strip())
            all_nodes.add(a.strip())
            all_nodes.add(b.strip())

path_indexes = [rl_to_index[action] for action in path_rl]


starters = {x for x in all_nodes if x[-1] == 'A'}
enders = {x for x in all_nodes if x[-1] == 'Z'}

current = [s for s in starters]
periodic = [None for _ in starters]

for index in range(len(current)):
    step = 0
    pos = current[index]
    ends = {}
    for i in range(1000000):
        action = path_indexes[step % len(path_indexes)]
        pos = graph[pos][action]
        step += 1
        if pos in enders and pos not in ends:
            ends[pos] = step
    print(f'Finished: {pos}')
    periodic[index] = ends

print(periodic)

nums = [list(x.values())[0] for x in periodic]
print(nums)


prev = nums[0]
for i in nums[1:]:
    import math
    prev = math.lcm(prev, i)
print(prev)




# correct was 13,289,612,809,129


# bad brute force
# maxer = 0
# start_time = time.time()
# while True:
#     dir_index = path_indexes[step % len(path_indexes)]
#     done = True
#     for node_index in range(len(current)):
#         node = current[node_index]
#         if done and node[-1] != 'Z':
#             maxer = max(maxer, node_index)
#             done = False
#         current[node_index] = graph[node][dir_index]
#     if done:
#         break
#     if step % 5000000 == 0:
#         rate = step / (time.time() - start_time)
#         print(f'{rate:,.0f} per second. On step {step:,}, got to {maxer}/{len(current)} once')        
#     step += 1
# print(step)


# part 1
# # https://adventofcode.com/2023
# import pathlib

# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# graph = {}
# with open(data_file) as f:
#     path = f.readline().strip()
#     for line in f.readlines():
#         if line.strip():
#             fr, to = line.strip().split('=')

#             a, b = to.replace('(', '').replace(')', '').strip().split(',')

#             graph[fr.strip()] = [a.strip(), b.strip()]

# rl_to_index = {
#     'R': 1,
#     'L': 0,
# }

# step = 0
# pos = 'AAA'
# while pos != 'ZZZ':
#     action = path[step % len(path)]
#     pos = graph[pos][rl_to_index[action]]
#     step += 1
# print(step)