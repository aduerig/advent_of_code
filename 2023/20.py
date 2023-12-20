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
queue = deque([])

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


memory = {}
for name in flips:
    memory[name] = 0

for name, needed_names in conjunction_inputs.items():
    memory[name] = [1, {}]
    for needed_name in needed_names:
        memory[name][1][needed_name] = 0

@profile
def solve():    
    low_pulses_recieved = {}

    start_time = time.time()
    pressed = 1
    while True:
        iter_queue = deque(list(queue))
        if random.random() < .0001:
            rate = pressed / (time.time() - start_time)
            print(f'Pressed {pressed:,} times so far. {rate:,.0f} per second')
        
        while iter_queue:
            from_name, name, signal = iter_queue.popleft()

            if signal == 0:
                if name not in low_pulses_recieved:
                    low_pulses_recieved[name] = 0
                low_pulses_recieved[name] += 1
            
            if name in flips:
                if signal == 1:
                    continue
                memory[name] = 1 - memory[name]
                for sub_name in flips[name]:
                    queue.append((name, sub_name, memory[name]))

            elif name in conjunction_inputs:
                curr_signal, input_memory = memory[name]
                input_memory[from_name] = signal

                new_signal = int(not all([val == 1 for val in input_memory.values()]))
                
                for sub_name in conjunction_outputs[name]:
                    new_state = (name, sub_name, new_signal)
                    queue.append(new_state)
                memory[name][0] = new_signal

        if low_pulses_recieved.get('rx', 0) == 1:
            print_green(f'Took {pressed} presses')
            exit()
        pressed += 1
solve()

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