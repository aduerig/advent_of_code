# part 2
# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()

#         new_line = []
#         if line:
#             for char in line:
#                 grid.append(char)
#         new_line.append(grid)

new_section = False
updates = []
before = {}
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()

        if line:
            if not new_section:
                a, b = line.split('|')
                if a not in before:
                    before[a] = set()
                before[a].add(b)
            else:
                updates.append(line.split(','))
        else:
            new_section = True


# no good
# 1578
# 8273

def try_it(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            a, b = update[i], update[j]
            if b in before and a in before[b]:
                update[i], update[j] = update[j], update[i]
                return False
    return True

total = 0
for update in updates:
    good = True
    idk = list(update)


    first = try_it(update)
    while not try_it(update):
        pass
    update_set = set(update)

    # for a, b_list in before.items():
    #     b_index = 0
    #     while b_index < len(b_list):
    #         b = b_list[b_index]
    #         if a in update_set and b in update_set:
    #             if update.index(a) > update.index(b):
    #                 update[update.index(a)], update[update.index(b)] = update[update.index(b)], update[update.index(a)]
    #             else:
    #                 b_index += 1
    #         else:
    #             b_index += 1
                        


    if not first:
        print(f'{idk}\n    {update}')

        middle_idx = len(update) // 2
        middle_num = update[middle_idx]
        total += int(middle_num)

print(f'{total}')



# # part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# # grid = []
# # with open(data_file) as f:
# #     for line in f.readlines():
# #         line = line.strip()

# #         new_line = []
# #         if line:
# #             for char in line:
# #                 grid.append(char)
# #         new_line.append(grid)

# new_section = False
# updates = []
# before = {}
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()

#         if line:
#             if not new_section:
#                 a, b = line.split('|')
#                 if a not in before:
#                     before[a] = []
#                 before[a].append(b)
#             else:
#                 updates.append(line.split(','))
#         else:
#             new_section = True


# # no good
# # 1578
# # 8273

# total = 0
# for update in updates:
#     good = True
#     # for i in range(len(update)):
#     #     for j in range(i+1, len(update)):
#     #         a, b = update[i], update[j]
#     #         if b in before and before[b] == a:
#     #             good = False

#     update_set = set(update)

#     for a, b_list in before.items():
#         for b in b_list:
#             if a in update_set and b in update_set:
#                 print(f'{a} {b}, {update.index(a)} {update.index(b)}')
#                 if update.index(a) > update.index(b):
#                     good = False


#     if good:
#         middle_idx = len(update) // 2
#         middle_num = update[middle_idx]
#         total += int(middle_num)

# print(f'{total}')
