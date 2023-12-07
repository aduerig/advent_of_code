# https://adventofcode.com/2023
import pathlib

import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

def get_type(a, b, c, d, e):
    if a != b:
        return 1
    if a == b == c == d == e:
        return 7
    if a == b == c == d:
        return 6
    if a == b == c:
        if d == e:
            return 5
        return 4
    if c == d:
        return 3
    return 2

hands = []
with open(data_file) as f:
    for line in f.readlines():
        hand, bid = list(line.strip().split())

        mapping = {
            'T': 10,
            'J': 1,
            'Q': 11,
            'K': 12,
            'A': 13
        }
        hand = [int(mapping.get(x, x)) for x in hand]
                
        best_type = 0
        for new_j in range(2, 14):
            multiclone_hand = [new_j if x == 1 else x for x in hand]
            multiclone_hand = sorted(multiclone_hand, key=lambda x: (hand.count(x), x), reverse=True)
            best_type = max(best_type, get_type(*multiclone_hand))

        hands.append((best_type, hand, int(bid)))

total = 0
for i, (_, _, bid) in enumerate(sorted(hands), start=1):
    total += bid * i
print(total)


# part 1
# # https://adventofcode.com/2023
# import pathlib

# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# def get_type(hand):
#     a, b, c, d, e = hand
#     if a != b:
#         return 1
#     if a == b == c == d == e:
#         return 7
#     if a == b == c == d:
#         return 6
    

#     if a == b == c:
#         if d == e:
#             return 5
#         return 4
    
#     if c == d:
#         return 3
#     return 2
    


# hands = []
# with open(data_file) as f:
#     for line in f.readlines():
#         hand, bid = list(line.strip().split())

#         u = {
#             'T': 10,
#             'J': 11,
#             'Q': 12,
#             'K': 13,
#             'A': 14
#         }
#         hand = [int(x) if x.isdigit() else u[x] for x in hand]
#         og_hand = list(hand)

#         hand.sort(key=lambda x: (og_hand.count(x), x), reverse=True)
#         hands.append((get_type(hand), og_hand, int(bid)))

# hands.sort()
# total = 0
# for index, (_type, _hand, bid) in enumerate(hands):
#     total += bid * (index + 1)
#     print_green(_type, _hand)
# print(total)