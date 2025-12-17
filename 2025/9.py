# https://adventofcode.com/2023
import sys
import pathlib
import time

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


start_time = time.time()
points = []
min_y = 99999999999
min_x = 99999999999
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()

        points.append(list(map(int, line.split(','))))
        min_x = min(min_x, points[-1][0])
        min_y = min(min_y, points[-1][1])

for index in range(len(points)):
    points[index][0] -= min_x
    points[index][1] -= min_y

max_x = 0
max_y = 0
for p in points:
    max_x = max(max_x, p[0])
    max_y = max(max_y, p[1])


print('Making grid with size:', (max_x + 1), 'x', (max_y + 1))
grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
print(f'Grid made: {time.time() - start_time:.6f} seconds')
for p in points:
    x = p[0]
    y = p[1]
    grid[y][x] = 1


print('Started visiting all nodes')
ok = 0
for y in range(len(grid)):
    print('ok')
    for x in range(len(grid[0])):
        ok += 1

end_time = time.time()
print(f"visiting all nodes and making grid: {end_time - start_time:.6f} seconds, num nodes: {ok}")







# aller = []
# for a in range(len(points)):
#     for b in range(a + 1, len(points)):
#         pa = points[a]
#         pb = points[b]

#         x_dist = abs(pa[0] - pb[0]) + 1
#         y_dist = abs(pa[1] - pb[1]) + 1
#         aller.append(x_dist * y_dist)

# print(max(aller))



# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# points = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         points.append(list(map(int, line.split(','))))

# aller = []
# for a in range(len(points)):
#     for b in range(a + 1, len(points)):
#         pa = points[a]
#         pb = points[b]

#         x_dist = abs(pa[0] - pb[0]) + 1
#         y_dist = abs(pa[1] - pb[1]) + 1
#         aller.append(x_dist * y_dist)

# print(max(aller))
