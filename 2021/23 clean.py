def get_hashable_state(the_dict):
    return tuple(sorted(the_dict.items()))
    # thing = sorted(the_dict.items())
    # thing2 = ((x, y[0]) if y is not None else (x, None) for x, y in thing)
    # return tuple(thing2)

# finished state

finished_dict = {(x, 0):None for x in range(11)}

finished_dict[(2, 1)] = 'A'
finished_dict[(2, 2)] = 'A'
finished_dict[(2, 3)] = 'A'
finished_dict[(2, 4)] = 'A'

finished_dict[(4, 1)] = 'B'
finished_dict[(4, 2)] = 'B'
finished_dict[(4, 3)] = 'B'
finished_dict[(4, 4)] = 'B'

finished_dict[(6, 1)] = 'C'
finished_dict[(6, 2)] = 'C'
finished_dict[(6, 3)] = 'C'
finished_dict[(6, 4)] = 'C'


finished_dict[(8, 1)] = 'D'
finished_dict[(8, 2)] = 'D'
finished_dict[(8, 3)] = 'D'
finished_dict[(8, 4)] = 'D'
finished_pos = get_hashable_state(finished_dict)


# inputs
positions = {(x, 0):None for x in range(11)}

# test input
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
positions[(2, 1)] = 'B'
positions[(2, 2)] = 'D'
positions[(2, 3)] = 'D'
positions[(2, 4)] = 'A'

positions[(4, 1)] = 'C'
positions[(4, 2)] = 'C'
positions[(4, 3)] = 'B'
positions[(4, 4)] = 'D'

positions[(6, 1)] = 'B'
positions[(6, 2)] = 'B'
positions[(6, 3)] = 'A'
positions[(6, 4)] = 'C'

positions[(8, 1)] = 'D'
positions[(8, 2)] = 'A'
positions[(8, 3)] = 'C'
positions[(8, 4)] = 'A'

# real input
#############
#...........#
###C#A#B#D###
  #B#A#D#C#
  #########
positions[(2, 1)] = 'C'
positions[(2, 2)] = 'D'
positions[(2, 3)] = 'D'
positions[(2, 4)] = 'B'

positions[(4, 1)] = 'A'
positions[(4, 2)] = 'C'
positions[(4, 3)] = 'B'
positions[(4, 4)] = 'A'

positions[(6, 1)] = 'B'
positions[(6, 2)] = 'B'
positions[(6, 3)] = 'A'
positions[(6, 4)] = 'D'

positions[(8, 1)] = 'D'
positions[(8, 2)] = 'A'
positions[(8, 3)] = 'C'
positions[(8, 4)] = 'C'


costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

belong = {
    'A': set([(2, 1), (2, 2), (2, 3), (2, 4)]),
    'B': set([(4, 1), (4, 2), (4, 3), (4, 4)]),
    'C': set([(6, 1), (6, 2), (6, 3), (6, 4)]),
    'D': set([(8, 1), (8, 2), (8, 3), (8, 4)]),
}

inverse_belong = {
    (2, 1): 'A', (2, 2): 'A', (2, 3): 'A', (2, 4): 'A',
    (4, 1): 'B', (4, 2): 'B', (4, 3): 'B', (4, 4): 'B',
    (6, 1): 'C', (6, 2): 'C', (6, 3): 'C', (6, 4): 'C',
    (8, 1): 'D', (8, 2): 'D', (8, 3): 'D', (8, 4): 'D',
}

rooms = set([
    (2, 1), (2, 2), (2, 3), (2, 4), 
    (4, 1), (4, 2), (4, 3), (4, 4),
    (6, 1), (6, 2), (6, 3), (6, 4), 
    (8, 1), (8, 2), (8, 3), (8, 4),
    ])

space_to_intention = {
    (2, 1): 'A',
    (2, 2): 'A',
    (2, 3): 'A',
    (2, 4): 'A',
    (4, 1): 'B',
    (4, 2): 'B',
    (4, 3): 'B',
    (4, 4): 'B',
    (6, 1): 'C',
    (6, 2): 'C',
    (6, 3): 'C',
    (6, 4): 'C',
    (8, 1): 'D',
    (8, 2): 'D',
    (8, 3): 'D',
    (8, 4): 'D',
}

connections = {}
for x in range(11):
    if x in [2, 4, 6, 8]:
        continue
    for room_pos in space_to_intention.keys():
        rx, ry = room_pos
        space_cost = abs(x - rx) + ry
        hallway_pos = (x, 0)
        if room_pos not in connections:
            connections[room_pos] = []
        # connections[room_pos].append((space_cost, hallway_pos))
        connections[room_pos].append(hallway_pos)

        if hallway_pos not in connections:
            connections[hallway_pos] = []
        # connections[hallway_pos].append((space_cost, room_pos))
        connections[hallway_pos].append(room_pos)


connections_with_paths = {}
for from_pos, to_pos_list in connections.items():
    connections_with_paths[from_pos] = []
    for to_pos in to_pos_list:
        if from_pos not in rooms:
            if to_pos[1] > 1:
                continue
        target_x, target_y = to_pos
        path = []
        looking = from_pos
        while looking != to_pos:
            x, y = looking
            curr_cost = abs(x - target_x) + abs(y - target_y)
            for dx, dy in [
                            [1, 0],
                            [-1, 0],
                            [0, 1],
                            [0, -1],
                          ]:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in positions:
                    if abs(new_x - target_x) + abs(new_y - target_y) < curr_cost:
                        path.append((new_x, new_y))
                        looking = (new_x, new_y)
                        break
            # print(looking, from_pos, to_pos,)
        connections_with_paths[from_pos].append((to_pos, path))


# for i, j in connections_with_paths.items():
#     print('LOL', i)
#     for z in j:
#         print(z)
# exit()

from copy import deepcopy


def children(pos_dict, print_logs=False):
    all_children = []
    for pos_from, resident in pos_dict.items():
        if resident is None:
            continue
        is_room_from = pos_from in rooms

        if is_room_from and inverse_belong[pos_from] == resident:
            dont_check = False
            for search_y in range(4, 0, -1):
                try_this = (pos_from[0], search_y)
                if try_this == pos_from:
                    dont_check = True
                    break

                if pos_dict[try_this] != inverse_belong[try_this]:
                    break
            if dont_check:
                continue


        for pos_to, path in connections_with_paths[pos_from]:
            generate_pos = None
            is_room_to = pos_to in rooms

            extra = 0
            if is_room_to:
                if pos_to in belong[resident]:
                    if print_logs:
                        print('trying', pos_from, pos_to, resident)
                    for search_y in range(4, 0, -1):
                        try_this = (pos_to[0], search_y)
                        if print_logs:
                            print('searching for', resident, try_this)
                        if pos_dict[try_this] is None:
                            if print_logs:
                                print('found a spot for', resident, try_this)
                            generate_pos = (pos_to[0], search_y)
                            extra = search_y - 1
                            break
                        if pos_dict[try_this] != resident:
                            break
            else:
                generate_pos = pos_to

            if generate_pos is not None:
                nah = False
                for inter_pos in path:
                    if pos_dict[inter_pos] is not None:
                        nah = True
                if nah:
                    continue
                new_dict = deepcopy(pos_dict)
                new_dict[generate_pos] = new_dict[pos_from]
                new_dict[pos_from] = None
                all_children.append(((len(path) + extra) * costs[resident], new_dict))
    if print_logs:
        exit()
    return all_children

f = open('23.dat_file', 'w')


def print_board(the_dict):
    print('-----')
    for y in range(-1, 6):
        builder = []
        for x in range(-1, 12):
            if (x, y) not in the_dict:
                if y < 2 or (x > 0 and x < 10):
                    builder.append('#')
                else:
                    builder.append(' ')
            elif the_dict[(x, y)] == None:
                builder.append('.')
            else:
                builder.append(the_dict[(x, y)][0])
        whole_str = ''.join(builder).rstrip()
        print(whole_str)
        f.writelines([whole_str, '\n'])
    f.flush()

import heapq

visited = set()
queue = [(0, -1, positions)]
increase = 0
track_set = set()
track_once = False
while queue:
    cost, increase_num, pos_dict = heapq.heappop(queue)
    pos = get_hashable_state(pos_dict)
    if pos == finished_pos:
        print('DONE!')
        print_board(pos_dict)
        print(pos)
        print(cost)
        break



    track_it = False
    # if not track_once and (
    #     pos_dict[(10, 0)] == 'D' and pos_dict[(9, 0)] == 'B' and pos_dict[(0, 0)] == 'A' and pos_dict[(1, 0)] == 'A' and pos_dict[(5, 0)] == 'C'
    #     ):
    #     track_once = True
    #     track_it = True
    # if increase_num == 133384:
    #     track_it = True

    if len(visited) % 600 == 0:
    # if track_it or increase_num in track_set:     
        print('increase_num', increase_num, 'visited:', len(visited), len(queue), cost)
        print_board(pos_dict)
        print(pos_dict)
    
    if pos in visited:
        continue
    visited.add(pos)


    for movement_cost, neighbor_dict in children(pos_dict, False):
        heapq.heappush(queue, (cost + movement_cost, increase, neighbor_dict))
        if track_it:
            track_set.add(increase)
        increase += 1
    if track_it:
        print('found', len(track_set), 'children')
