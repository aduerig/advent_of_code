# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


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


def get_range_split(curr_range, range_condition):
    intersection = range_intersect(curr_range, range_condition)
    if intersection is None:
        return None, None
    

    if intersection == curr_range:
        return [curr_range], []
    elif intersection[0] == curr_range[0]:
        return [intersection], [(intersection[1] + 1, curr_range[1])]
    elif intersection[1] == curr_range[1]:
        return [intersection], [(curr_range[0], intersection[0] - 1)]
    return [intersection], [(range_condition[0], intersection[0] - 1), (intersection[1] + 1, range_condition[1])]


def perms(parts):
    vals = list(parts.values())
    start, end = vals[0]
    total = (end - start) + 1
    for start, end in vals[1:]:
        total *= (end - start) + 1
    return total


def accepted(parts, stage='in', index=0):
    if stage == 'A':
        return perms(parts)
    if stage == 'R':
        return 0
    
    for start, end in parts.values():
        if end < start:
            print(f'{start, end}')
            exit()
    

    rule = all_workflows[stage][index]
    if type(rule) != tuple:
        return accepted(parts, rule)
            
    rating_name, range_condition, if_true_stage = rule
    existing_range = parts[rating_name]

    in_ranges, out_ranges = get_range_split(existing_range, range_condition)
    print(f'{existing_range} - {range_condition} - {in_ranges} - {out_ranges}')

    total = 0
    if in_ranges:
        correct_version = parts.copy()
        correct_version[rating_name] = in_ranges[0]
        total += accepted(correct_version, if_true_stage)

    if out_ranges:
        for out_range in out_ranges:
            false_version = parts.copy()
            false_version[rating_name] = out_range
            total += accepted(false_version, stage, index + 1)
        
    return total

parts = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000),
}

print(accepted(parts))







total_perms = 255616175976000
# accepted:   167409079868000
# rejected:   88207096108000



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