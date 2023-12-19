# https://adventofcode.com/2023
import pathlib
import sys
import functools
import time

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


start_time = time.time()

def to_range(rule):
    condition, next_stage = rule.split(':')
    if '>' in rule:
        name, amt = condition.split('>')
        amt = int(amt)
        condition_range = (amt + 1, 4000)
    else:
        name, amt = condition.split('<')
        amt = int(amt)
        condition_range = (1, amt - 1)
    return name, condition_range, next_stage


all_workflows = {}
with open(data_file) as f:
    workflows, _parts = f.read().split('\n\n')
    for workflow in workflows.splitlines():
        start = workflow.index('{')
        name = workflow[:start]
        all_workflows[name] = []
        for rule in workflow[start + 1:-1].split(','):
            if '>' in rule or '<' in rule:
                rule = to_range(rule)
            all_workflows[name].append(rule)


def range_intersect(r1, r2):
    r3 = max(r1[0], r2[0]), min(r1[1], r2[1])
    if r3[0] > r3[1]:
        return None
    return r3


def get_range_split(source, condition):
    passes = range_intersect(source, condition)
    if passes is None:
        return [], []
    
    if passes == source:
        return [source], []
    elif passes[0] == source[0]:
        return [passes], [(passes[1] + 1, source[1])]
    elif passes[1] == source[1]:
        return [passes], [(source[0], passes[0] - 1)]
    return [passes], [(condition[0], passes[0] - 1), (passes[1] + 1, condition[1])]


def perms(parts):
    return functools.reduce(lambda a, b: a * b, [(end - start) + 1 for start, end in parts.values()])


def accepted(parts, stage='in', index=0):
    if stage == 'A':
        return perms(parts)
    if stage == 'R':
        return 0
        
    rule = all_workflows[stage][index]
    if not isinstance(rule, tuple):
        return accepted(parts, rule)
            
    rating_name, range_condition, if_true_stage = rule
    existing_range = parts[rating_name]

    in_ranges, out_ranges = get_range_split(existing_range, range_condition)

    save = parts[rating_name]
    total = 0
    if in_ranges:
        parts[rating_name] = in_ranges[0]
        total += accepted(parts, if_true_stage)
        parts[rating_name] = save

    for out_range in out_ranges:
        parts[rating_name] = out_range
        total += accepted(parts, stage, index + 1)
        parts[rating_name] = save
        
    return total

parts = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000),
}
# 125744206494820 right
# total_perms (4 1-4000) = 255616175976000

print_blue(f'Took: {time.time() - start_time:.8f} seconds')
print_green(accepted(parts))




# part 1 
# # https://adventofcode.com/2023
# import pathlib
# import sys

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# all_workflows = {}
# all_parts = []
# with open(data_file) as f:
#     workflows, parts = f.read().split('\n\n')

#     for workflow in workflows.splitlines():
#         start = workflow.index('{')
#         name = workflow[:start]
#         all_workflows[name] = []
#         for rule in workflow[start + 1:-1].split(','):
#             all_workflows[name].append(rule)


#     for part in parts.splitlines(): 
#         new_part = {}    
#         for quality in part[1:-1].split(','):    
#             name, amt = quality.split('=')
#             amt = int(amt)
#             new_part[name] = amt
#         all_parts.append(new_part)

# for workflow_name, workflow_rules in all_workflows.items():
#     for rule in workflow_rules:
#         print(f'{rule} - ', end='')
#     print()


# def condition_true(part, condition):
#     if '>' in condition:
#         left_value, num_needed = condition.split('>')
#         num_needed = int(num_needed)
#         evalu = lambda x, y: x > y
#     elif '<' in condition:
#         left_value, num_needed = condition.split('<')
#         num_needed = int(num_needed)
#         evalu = lambda x, y: x < y

#     if left_value in part and evalu(part[left_value], num_needed):
#         return True
#     return False


# def accepted(part, stage='in'):
#     if stage == 'A':
#         return True
#     elif stage == 'R':
#         return False
#     print(f'Looking at {part=} on stage: {stage}')
#     for rule in all_workflows[stage]:
#         print(f'Following rule {rule}')
#         if rule == 'A':
#             return True
#         if rule == 'R':
#             return False
#         if ':' not in rule:
#             return accepted(part, rule)
#         condition, if_true_stage = rule.split(':')
        
#         if condition_true(part, condition):
#             return accepted(part, if_true_stage)
#     return False


# # print_green('=== parts')
# total = 0
# for part in all_parts:
#     if accepted(part):
#         total += sum(part.values())

# print(total)