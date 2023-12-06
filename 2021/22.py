import time
import signal
import sys


from helpers import * 

data = []

with open('22.data') as f:
    for line in f.readlines():
        line = line.strip()

        on_off, rest = line.split(' ')

        x, y, z = rest.strip().split(',')
        x = x.replace('x=', '').strip()
        y = y.replace('y=', '').strip()
        z = z.replace('z=', '').strip()

        x1, x2 = map(int, x.split('..'))
        y1, y2 = map(int, y.split('..'))
        z1, z2 = map(int, z.split('..'))

        # x1 = max(x1, -50)
        # y1 = max(y1, -50)
        # z1 = max(z1, -50)
        # x2 = min(x2, 50)
        # y2 = min(y2, 50)
        # z2 = min(z2, 50)

        if x2 < x1:
            print_red(f'something wrong with x, {x1=}, {x2=}')
        if y2 < y1:
            print_red(f'something wrong with y, {y1=}, {y2=}')
        if z2 < z1:
            print_red(f'something wrong with z, {z1=}, {z2=}')

        data.append((on_off, [x1, x2], [y1, y2], [z1, z2]))


def end():
    end_time = time.time()
    print(f'{total_x_y=:,}, {end_time - start_time=:,.2f} seconds, {nodes / (end_time - start_time):,.2f} nodes per second')

def signal_handler(sig, frame):
    end()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


cubes = {}

start_time = time.time()
total_x_y = 0
nodes = 0

ons = []
offs = []
for index, (on_off, x_set, y_set, z_set) in enumerate(data):
    if on_off == 'on':
        ons.append((x_set, y_set, z_set))
    else:
        offs.append((x_set, y_set, z_set))


def num_things(x_set, y_set, z_set):
    # print(f'Going to do {index}/{len(data)}, {x_set=}, {y_set=}, {z_set}')
    computed_counting = y_set[1] - y_set[0]
    computed_counting *= z_set[1] - z_set[0]
    # print(f'Going to do {index}/{len(data)}, {x_set=}, {y_set=}, {z_set}, {computed_counting=:,}')

    return computed_counting * (x_set[1] - x_set[0])
    # nodes = 04
    # for x in range(x_set[0], x_set[1] + 1):
    #     for y in range(y_set[0], y_set[1] + 1):
    #         nodes += 1
    # print(f'finished, took, {nodes=:,}')


on_amount = 0
for i in ons:
    on_amount += num_things(*i)
print(f'{on_amount=:,}, {len(ons)=:,}')

off_amount = 0
for i in offs:
    off_amount += num_things(*i)
print(f'{off_amount=:,}, {len(offs)=:,}')


min_z = float('inf')
max_z = -float('inf')
min_y = float('inf')
max_y = -float('inf')
all_z_set = set()
all_y_set = set()
for i in ons:
    for z_num in range(i[2][0], i[2][1] + 1):
        all_z_set.add(z_num)
    for y_num in range(i[1][0], i[1][1] + 1):
        all_y_set.add(y_num)

    min_z = min(min_z, i[2][0])
    max_z = max(max_z, i[2][1])
    min_y = min(min_y, i[1][0])
    max_y = max(max_y, i[1][1])
for i in offs:
    for z_num in range(i[2][0], i[2][1] + 1):
        all_z_set.add(z_num)
    for y_num in range(i[1][0], i[1][1] + 1):
        all_y_set.add(y_num)

    min_z = min(min_z, i[2][0])
    max_z = max(max_z, i[2][1])
    min_y = min(min_y, i[1][0])
    max_y = max(max_y, i[1][1])

import datetime
time_start = time.time()
def print_time_to_finish(iteration, max_iterations):
    time_so_far = time.time() - time_start

    time_per_iteration = time_so_far / iteration
    time_left = time_per_iteration * (max_iterations - iteration)
    date_done = datetime.datetime.now() + datetime.timedelta(seconds=time_left)
    print(f'{date_done.strftime("%Y-%m-%d %H:%M:%S")}, {time_left=:,.2f} seconds left, {time_so_far=:,.2f} seconds so far, {iteration=:,}, {max_iterations=:,}, {100 * iteration / max_iterations:,.2f}% done')


print(f'{min_z=}, {max_z=}, {len(all_z_set)=:,}, {len(all_y_set)=:,} things')
for lol_index, curr_x_pos in enumerate(all_z_set):
    for curr_y_pos in all_y_set:
        for index, (on_off, x_set, y_set, z_set) in enumerate(data):
            if z_set[0] <= curr_x_pos <= z_set[1] and y_set[0] <= curr_y_pos <= y_set[1]:
                if on_off == 'on':
                    pass
                else:
                    pass
    print(f'{curr_x_pos}, {100 * lol_index / len(all_z_set):,.2f}%')
    print_time_to_finish(lol_index + 1, len(all_z_set) + 1)


# end()


# total_x_y=64,539,952,562, end_time - start_time=3,837.63 seconds, 28954.11 nodes per second




# real
# total_x_y=162,878,611,127
# total_x_z=161,928,752,695
# total_y_z=156,957,179,661

# test
# total_x_y=261,575,530,894
# total_x_z=257,298,717,922
# total_y_z=251,468,725,569




# data = []

# with open('22.data') as f:
#     for line in f.readlines():
#         line = line.strip()

#         on_off, rest = line.split(' ')

#         x, y, z = rest.strip().split(',')
#         x = x.replace('x=', '').strip()
#         y = y.replace('y=', '').strip()
#         z = z.replace('z=', '').strip()

#         x1, x2 = map(int, x.split('..'))
#         y1, y2 = map(int, y.split('..'))
#         z1, z2 = map(int, z.split('..'))
 
#         # x1 = max(x1, -50)
#         y1 = max(y1, -50)
#         z1 = max(z1, -50)
#         # x2 = min(x2, 50)
#         y2 = min(y2, 50)
#         z2 = min(z2, 50)

#         data.append((on_off, [x1, x2], [y1, y2], [z1, z2]))


# # for i in data:
# #     print(i)

# # set_map = {'on': 1, 'off': 0}
# cubes = {}

# counter = 0
# for on_off, x_set, y_set, z_set in data:
#     print('finished {}/{}'.format(counter, len(data)))
#     for x in range(x_set[0], x_set[1] + 1):
#         for y in range(y_set[0], y_set[1] + 1):
#             for z in range(z_set[0], z_set[1] + 1):
#                 if on_off == 'on':
#                     if (x, y, z) not in cubes:
#                         cubes[(x, y, z)] = 1
#                 else:
#                     if (x, y, z) in cubes:
#                         del cubes[(x, y, z)]
#     counter += 1
# print(len(cubes))