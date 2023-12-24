# https://adventofcode.com/2023
import pathlib
import sys
from collections import deque
import random
import time

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')




flips = {}
conjunction_inputs = {}
conjunction_outputs = {}
max_objects = 50
queue = deque([], max_objects)

with open(data_file) as f:
    for line in f.read().splitlines():
        first, second = list(map(lambda x: x.strip(), line.split('->')))

        second_arr = list(map(lambda x: x.strip(), second.split(',')))

        if first == 'broadcaster':
            for name in second_arr:
                queue.append(('broadcaster', name, 0))
            continue

        name = first[1:]
        if first.startswith('%'):
            if name in flips:
                print_red('Multiple flips?')
                exit()
            flips[name] = second_arr
        elif first.startswith('&'):
            if name in conjunction_outputs:
                print_red('Multiple conjunction_outputs?')
                exit()
            conjunction_outputs[name] = second_arr
            conjunction_inputs[name] = set()
        else:
            print_red(f'IDK - {line}')


for input_name, arr_of_outputs in list(flips.items()) + list(conjunction_outputs.items()):
    for output_name in arr_of_outputs:
        if output_name in conjunction_inputs:
            conjunction_inputs[output_name].add(input_name)


# 281,474,976,710,656
# 1,000,537,722

# 281474976710656
# 1000537722

@profile
def solve(initial_queue, num_iters):
    memory = {}
    for name in flips:
        memory[name] = 0

    for name, needed_names in conjunction_inputs.items():
        memory[name] = {}
        for needed_name in needed_names:
            memory[name][needed_name] = 0

    memory_hash_visited = set()
    lows = 0
    highs = 0
    pressed = 1
    start_time = time.time()
    to_track = {}
    while pressed < num_iters + 1:
        # low_pulses_recieved = {}
        low_rx_pulses = 0

        iter_queue = initial_queue.copy()
        if random.random() < .00001:
            rate = pressed / (time.time() - start_time)
            print(f'Pressed {pressed:,} times so far. {rate:,.0f} per second.')
        
        lows += 1

        the_hash = hash(tuple([(k, v) for k, v in memory.items() if not isinstance(v, dict)]))
        if the_hash in memory_hash_visited:
            print(f'Memory duplicate at {pressed}')
            exit()
        memory_hash_visited.add(the_hash)
        # print_blue(f'Memory =======')
        # for k, v in memory.items():
        #     print(f'{k} - {v}')

        while iter_queue:
            from_name, name, signal = iter_queue.popleft()

            if name == 'tg' and signal == 1:
                if from_name not in to_track:
                    to_track[from_name] = []
                to_track[from_name].append(pressed)

            if name == 'rx' and signal == 0:
                low_rx_pulses += 1
            # if signal == 0:
                # if name not in low_pulses_recieved:
                #     low_pulses_recieved[name] = 0
                # low_pulses_recieved[name] += 1
            # else:
            #     highs += 1

            if name in flips:
                if signal == 1:
                    continue
                memory[name] = 1 - memory[name]
                for sub_name in flips[name]:
                    iter_queue.append((name, sub_name, memory[name]))

            elif name in conjunction_inputs:
                memory[name][from_name] = signal
                new_signal = 0
                for i in memory[name].values():
                    if i == 0:
                        new_signal = 1
                        break


                for sub_name in conjunction_outputs[name]:
                    new_state = (name, sub_name, new_signal)
                    iter_queue.append(new_state)

        if low_rx_pulses == 1:
            print_green(f'Took {pressed} presses, broke due to rx')
            break
        # lows += sum(low_pulses_recieved.values())

        pressed += 1

        print()
        for k, v in to_track.items():
            diffs = []
            for a, b in zip(v, v[1:]):
                diffs.append(b - a)
            print(f'{k} - {v}')
            print(f'    {diffs}')
    return lows * highs


# above prints were
# tf - [3923, 7846, 11769, 15692, 19615, 23538, 27461, 31384]
#     [3923, 3923, 3923, 3923, 3923, 3923, 3923]
# db - [3929, 7858, 11787, 15716, 19645, 23574, 27503, 31432]
#     [3929, 3929, 3929, 3929, 3929, 3929, 3929]
# vq - [4007, 8014, 12021, 16028, 20035, 24042, 28049, 32056]
#     [4007, 4007, 4007, 4007, 4007, 4007, 4007]
# ln - [4091, 8182, 12273, 16364, 20455, 24546, 28637, 32728]
#     [4091, 4091, 4091, 4091, 4091, 4091, 4091]
# then math.lcm(3923, 3929, 4007, 4091)
# 252,667,369,442,479
# 281,474,976,710,656

print_yellow(solve(queue, float('inf')))
# print_yellow(solve(queue, 1000))


# answer was 819397964


# part 1 
# # https://adventofcode.com/2023
# import pathlib
# import sys
# from collections import deque

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# flips = {}
# conjunction_inputs = {}
# conjunction_outputs = {}
# queue = deque([])

# with open(data_file) as f:
#     for line in f.read().splitlines():
#         first, second = list(map(lambda x: x.strip(), line.split('->')))

#         second_arr = list(map(lambda x: x.strip(), second.split(',')))

#         if first == 'broadcaster':
#             for name in second_arr:
#                 queue.append(('broadcaster', name, 0))
#             continue

#         name = first[1:]
#         if first.startswith('%'):
#             if name in flips:
#                 print_red('Multiple flips?')
#                 exit()
#             flips[name] = second_arr
#         elif first.startswith('&'):
#             if name in conjunction_outputs:
#                 print_red('Multiple conjunction_outputs?')
#                 exit()
#             conjunction_outputs[name] = second_arr
#             conjunction_inputs[name] = set()
#         else:
#             print_red(f'IDK - {line}')


# for input_name, arr_of_outputs in list(flips.items()) + list(conjunction_outputs.items()):
#     for output_name in arr_of_outputs:
#         if output_name in conjunction_inputs:
#             conjunction_inputs[output_name].add(input_name)


# for key, val in conjunction_outputs.items():
#     print_cyan(f'conjunction_outputs: {key} - {val}')

# for key, val in conjunction_inputs.items():
#     print_blue(f'conjunction_inputs: {key} - {val}')

# for key, val in flips.items():
#     print_yellow(f'flips: {key} - {val}')



# lows = 0
# highs = 0
# memory = {}


# for name in flips:
#     memory[name] = 0

# for name, needed_names in conjunction_inputs.items():
#     memory[name] = [1, {}]
#     for needed_name in needed_names:
#         memory[name][1][needed_name] = 0
# print('\n')



# first_queue = deque(list(queue))

# for _ in range(1000):
#     queue = deque(list(first_queue))
#     lows += 1
#     while queue:
#         from_name, name, signal = queue.popleft()

#         if signal == 0:
#             lows += 1
#         else:
#             highs += 1
        
#         # input('')
#         if name in flips:
#             if signal == 1:
#                 # print(f'Skipping cause {from_name} sent flip flop high pulse')
#                 continue
#             memory[name] = 1 - memory[name]
#             # print_blue(f'{from_name} set {name} to {memory[name]}, queue len: {len(queue)} QUEUE: {red(list(queue))}')
#             for sub_name in flips[name]:
#                 # print(f'    Flipper: adding {sub_name}')
#                 queue.append((name, sub_name, memory[name]))

#         elif name in conjunction_inputs:
#             # print_blue(f'Conjunction {name}, got ({from_name}, {signal}), queue len: {len(queue)}')

#             curr_signal, input_memory = memory[name]
#             input_memory[from_name] = signal

#             new_signal = int(not all([val == 1 for val in input_memory.values()]))
            
#             for sub_name in conjunction_outputs[name]:
#                 new_state = (name, sub_name, new_signal)
#                 # print(f'    Adding {new_state}')
#                 queue.append(new_state)
#             memory[name][0] = new_signal

#     #     print(f'{key} - {value}')
# print_green(f'{lows * highs} - {lows=}, {highs=}')

# # 740238980 too low