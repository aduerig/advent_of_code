# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

times_won = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            card, rest = line.split(':')
            rest = rest.strip().split('|')
            winning, mine = rest[0].strip().split(), rest[1].strip().split()
            times_won.append(len(list(filter(lambda x: x in winning, mine))))


to_process = [1 for _ in range(len(times_won))]
for id in range(len(times_won)):
    proc = to_process[id]
    next_id = id + 1
    for id_won in range(next_id, next_id + times_won[id]):
        to_process[id_won] += proc
print(sum(to_process))

# to_process = [1 for _ in range(len(times_won))]
# for id in range(len(times_won)):
#     proc = to_process[id]
#     for id2 in range(id + 1, id + 1 + times_won[id]):
#         to_process[id2] += proc
# print(sum(to_process))


# part 2 v1
# # https://adventofcode.com/2023
# import pathlib

# import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# cards = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             card, rest = line.split(':')
#             rest = rest.strip().split('|')
#             winning, mine = rest[0].strip().split(), rest[1].strip().split()
#             winning = set([int(x) for x in winning])
#             mine = [int(x) for x in mine]
#             times_won = 0
#             for i in mine:
#                 if i in winning:
#                     times_won += 1
#             cards.append(times_won)

# to_process = [1 for _ in range(len(cards))]
# for id in range(len(cards)):
#     proc = to_process[id]
#     times_won = cards[id]
#     for id2 in range(id + 1, id + 1 + times_won):
#         to_process[id2] += proc
# print(sum(to_process))


# part 1
# # https://adventofcode.com/2023
# import pathlib

# import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# total = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             card, rest = line.split(':')
#             rest = rest.strip().split('|')
#             winning, mine = rest[0].strip().split(), rest[1].strip().split()
#             winning = set([int(x) for x in winning])
#             mine = [int(x) for x in mine]
#             winners = 0
#             for i in mine:
#                 if i in winning:
#                     winners += 1
#             if winners:
#                 total += pow(2, winners - 1)

# print(total)