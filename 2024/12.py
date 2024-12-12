# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            grid.append(list(line))


visited = set()
def dfs(grid, letter, pos, visited_this_session, sides):
    x, y = pos
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    if grid[y][x] != letter:
        return False
    if (x, y) in visited:
        return True
    
    visited.add(pos)
    visited_this_session[pos] = True
    
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        new_x, new_y = dx + x, dy + y
        res = dfs(grid, letter, (new_x, new_y), visited_this_session, sides)
        if not res:
            sides[0] += 1

    return True

def w_dir(s):
    return {
        'left': (-1, 0),
        'right': (1, 0),
        'up': (0, -1),
        'down': (0, 1),

        # 'downright': (1, 1),
        # 'downleft': (-1, 1),
        # 'upright': (1, -1),
        # 'upleft': (-1, -1),

        'downright': (0, 0),
        'downleft': (-1, 0),
        'upright': (0, -1),
        'upleft': (-1, -1),
    }[s]

mapper = [
    [['upright', 'downleft', 'downright'], ['left', 'up']], 
    [['upleft', 'downright', 'downleft'], ['up', 'right']], 

    [['upright', 'upleft', 'downright'], ['left', 'down']], 
    [['upleft', 'upright', 'downleft'], ['down', 'right']], 

    [['upleft', 'downleft'], ['up', 'down']], 
    [['upright', 'downright'], ['up', 'down']], 

    [['upleft', 'upright'], ['left', 'right']], 
    [['downleft', 'downright'], ['left', 'right']], 

    [['upleft'], ['up', 'left']], 
    [['upright'], ['up', 'right']], 
    [['downleft'], ['down', 'left']], 
    [['downright'], ['down', 'right']], 
]

def inverse(s):
    return {
        'left': 'right',
        'right': 'left',
        'up': 'down',
        'down': 'up',
    }.get(s, False)


def is_there(grid, pos, letter, do_region, region):
    x, y = pos
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    if grid[y][x] != letter:
        return False
    if do_region and (x, y) not in region:
        return False
    return True


def get_match(grid, letter, half_pos, region, from_dir):
    print(f'{half_pos}')
    half_x, half_y = half_pos
    for conditions, options in mapper:
        all_true = True

        if from_dir == 'up' and conditions == ['upright']:
            continue
        if from_dir == 'up' and conditions == ['upleft']:
            continue

        if from_dir == 'down' and conditions == ['downleft']:
            continue
        if from_dir == 'down' and conditions == ['downright']:
            continue

        if from_dir == 'left' and conditions == ['upleft']:
            continue
        if from_dir == 'left' and conditions == ['downleft']:
            continue

        if from_dir == 'right' and conditions == ['upright']:
            continue
        if from_dir == 'right' and conditions == ['downright']:
            continue

        for condition in conditions:
            dx, dy = w_dir(condition)
            x, y = half_x + dx, half_y + dy

            if not is_there(grid, (x, y), letter, True, region):
                all_true = False
            # if conditions == ['upleft']:
            #     print(f'get_match: {half_pos=}, {condition}, {x, y=}, {letter=}, {all_true=}, {from_dir=}')


        if all_true:
            # print(f'Condition true! {conditions}, returning {options}')
            return options
    print(f'IMPOSSIBLE {letter=}, {half_pos=}, {from_dir}')

def dfs_half_count_turns(half_pos, from_dir, letter, turns, this_visited, region, original_entry_half_pos):
    if half_pos in this_visited and from_dir in this_visited[half_pos]:
        return False
    if half_pos not in this_visited:
        this_visited[half_pos] = []

    # print(f'{half_pos=}')
    directions = get_match(grid, letter, half_pos, region, from_dir)
    
    for index, direction in enumerate(directions):
        if inverse(direction) == from_dir:
            # print('failed, dont go back')
            continue
        if direction != from_dir:
            turns[0] += 1
        if original_entry_half_pos == (3, 1) and letter == 'A':
            print(f'{direction=}')

        other_direction = directions[1-index]
        this_visited[half_pos].append(inverse(other_direction))

        dx, dy = w_dir(direction)
        new_x, new_y = half_pos[0] + dx, half_pos[1] + dy
        dfs_half_count_turns((new_x, new_y), direction, letter, turns, this_visited, region, original_entry_half_pos)
        break

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        letter = grid[y][x]
        region = {}
        sides = [0]

        dfs(grid, grid[y][x], (x, y), region, sides)
        if region:
            this_visited = {}
            for letter_pos in region:
                for dx, dy in [[0, 0], [1, 0], [0, 1], [1, 1]]:
                    half_pos = (dx + letter_pos[0], dy + letter_pos[1])
                    # if half_pos[0] >= len(grid[0]) or half_pos[1] >= len(grid):
                    #     continue

                    all_true = True
                    for condition in ['upleft', 'upright', 'downright', 'downleft']:
                        dx2, dy2 = w_dir(condition)
                        if not is_there(grid, (half_pos[0] + dx2, half_pos[1] + dy2), letter, False, {}):
                            all_true = False
                    if all_true:
                        continue
                    if half_pos in this_visited:
                        continue

                    turns = [0]
                    dfs_half_count_turns(half_pos, None, letter, turns, this_visited, region, half_pos)
                    if turns[0] > 1:
                        amt = len(region) * turns[0]
                        print(f'NEW ABOVE {letter}, {letter_pos}, {dx, dy=}, {turns[0]=}, {amt=}')
                        total += amt
                        # print(f'{letter=}, {amt=}, {total=}, {len(region)=}, {turns[0]=}, {x, y}')



# 746045 not the right answer

print(total)


# part 2
# # https://adventofcode.com/2023
# import sys
# import pathlib

# filepath = pathlib.Path(__file__)
# sys.path.append(str(filepath.parent.parent))
# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             grid.append(list(line))


# visited = set()
# def dfs(grid, letter, pos, visited_this_session, sides):
#     x, y = pos
#     if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
#         return False
#     if grid[y][x] != letter:
#         return False
#     if (x, y) in visited:
#         return True
    
#     # print(pos)
#     visited.add(pos)
#     visited_this_session.add(pos)

    
#     for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#         new_x, new_y = dx + x, dy + y
#         res = dfs(grid, letter, (new_x, new_y), visited_this_session, sides)
#         if not res:
#             sides[0] += 1

#     return True

# total = 0
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         letter = grid[y][x]
#         this_session = set()
#         sides = [0]


#         dfs(grid, grid[y][x], (x, y), this_session, sides)
#         if this_session:
#             amt = len(this_session) * sides[0]
#             total += amt
#             print(f'{letter=}, {amt=}, {total=}, {len(this_session)=}, {sides[0]}, {x, y}')


# print(total)