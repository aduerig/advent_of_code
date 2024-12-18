# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

robots = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            p, v = line.split(' ')

            p = tuple(map(int, p.split('=')[1].split(',')))
            v = tuple(map(int, v.split('=')[1].split(',')))
            robots.append((p, v))


def dfs(visited, pos, robot_detector):
    x, y = pos
    if x < 0 or y < 0 or x >= width or y >= height:
        return
    
    if pos not in robot_detector:
        return

    if pos in visited:
        return
    
    visited[pos] = True
    for dx, dy in [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],

            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]:
        x, y = x + dx, y + dy
        dfs(visited, (x, y), robot_detector)


width = 101
height = 103

def cap(num, maxer):
    if num >= 0:
        return num % maxer
    return maxer + num

seen_before = {}
def print_robots(robots):
    print('\n' * 2)
    print(i)

    all_poses = set([x for x, _ in robots])
    the_hash = []
    for y in range(height):
        to_print = []
        for x in range(width):
            if (x, y) in all_poses:
                to_print.append('X')
            else:
                to_print.append('.')
        print(''.join(to_print))
        the_hash += to_print

    t = tuple(the_hash)
    if t in seen_before:
        print('ABOVE HAS BEEN SEEN')
        exit()
    seen_before[t] = True



print(f'Num robots: {len(robots)}')
least_sections = float('inf')
for i in range(100000000):
    new_robots = []
    for p, v in robots:
        x, y = p
        dx, dy = v

        x, y = x + dx, y + dy
        x = cap(x, width)
        y = cap(y, height)
        new_robots.append(((x, y), v))
    robots = new_robots

    detector = set([x for x, _ in new_robots])
    unique = 0
    for x, y in detector:
        visited = {}
        dfs(visited, (x, y), detector)
        unique += bool(visited)
    
    if (i - 67) % 101 == 0:
        print_robots(robots)
        print(i+1)
    # if unique < least_sections:
    #     print(f'NEW LOWEST: iter: {i}, connected sections: {unique}')
    #     least_sections = unique

    # if i > 568:
    #     time.sleep(.15)

# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# robots = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             p, v = line.split(' ')

#             p = tuple(map(int, p.split('=')[1].split(',')))
#             v = tuple(map(int, v.split('=')[1].split(',')))
#             robots.append((p, v))

# width = 101
# height = 103
# # width = 11
# # height = 7


# quad = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
# }
# def cap(num, maxer):
#     if num >= 0:
#         return num % maxer
#     else:
#         return maxer + num
#         # return -(-num % (maxer + 1))

# for p, v in robots:
#     for i in range(100):
#         x, y = p
#         dx, dy = v

#         x, y = x + dx, y + dy

#         x = cap(x, width)
#         y = cap(y, height)
#         p = (x, y)
#         print(p)

#     res = None
#     x, y = p
#     if x < width // 2 and y < height // 2:
#         res = 1
#     elif x > width // 2 and y < height // 2:
#         res = 2
#     elif x < width // 2 and y > height // 2:
#         res = 3
#     elif x > width // 2 and y > height // 2:
#         res = 4
#     if res:
#         quad[res] += 1

# # 49404168 too low

# total = 1
# for v in quad.values():
#     total *= v
# print(total)