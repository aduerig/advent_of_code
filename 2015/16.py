# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


things = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

with open(data_file) as f:
    for sue_num, line in enumerate(f.read().splitlines(), start=1):
        for pair in ':'.join(line.split(':')[1:]).split(','):
            thing, quan = pair.split(':')
            thing = thing.strip()
            quan = int(quan)
            if thing in ['cats', 'trees']:
                if quan <= things[thing]:
                    break
            elif thing in ['goldfish', 'pomeranians']:
                if quan >= things[thing]:
                    break
            elif things[thing] != int(quan):
                break
        else:
            print_green(sue_num)
            break




# part 1
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# things = {
#     'children': 3,
#     'cats': 7,
#     'samoyeds': 2,
#     'pomeranians': 3,
#     'akitas': 0,
#     'vizslas': 0,
#     'goldfish': 5,
#     'trees': 3,
#     'cars': 2,
#     'perfumes': 1,
# }

# with open(data_file) as f:
#     for sue_num, line in enumerate(f.read().splitlines(), start=1):
#         for pair in ':'.join(line.split(':')[1:]).split(','):
#             thing, quan = pair.split(':')
#             if things[thing.strip()] != int(quan):
#                 break
#         else:
#             print_green(sue_num)
#             break
