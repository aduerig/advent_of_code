# real 
a = 7
b = 4

# test input
# a = 3
# b = 7

global all_combinations
all_combinations = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            all_combinations.append(i + j + k)

global combo_dict
combo_dict = {}
for i in all_combinations:
    if i not in combo_dict:
        combo_dict[i] = 0
    combo_dict[i] += 1 

member = {}
def game(turn, pos, scores, member):
    global combo_dict
    if scores[1 - turn] >= 500:
        return [int(x == 1 - turn) for x in range(2)]

    
    pos_tupled = (turn, tuple(pos), tuple(scores))
    if pos_tupled in member:
        return member[pos_tupled]
    
    wins = [0, 0]
    
    for roll, times in combo_dict.items():
        new_pos = list(pos)
        new_pos[turn] = (new_pos[turn] + roll) % 10
        new_scores = list(scores)
        new_scores[turn] += new_pos[turn] + 1
        results = game(1 - turn, new_pos, new_scores, member)
        wins[0] += times * results[0]
        wins[1] += times * results[1]

    member[pos_tupled] = tuple(wins)
    return member[pos_tupled]

wins = game(0, [a, b], [0, 0], member)
print(wins)



# global dice
# dice = 1

# turn = 0
# players = [[a, 0], [b, 0]]
# rolls = 0

# def get_dice_roll():
#     global dice
#     tmp = dice
#     dice += 1
#     if dice > 100:
#         dice = 1
#     return tmp

# def get_n_dice_roll(n=3):
#     global dice
#     tmp = 0
#     for i in range(n):
#         tmp += get_dice_roll()
#     print('three rolls', tmp)
#     return tmp


# while True:
#     data = players[turn]

#     data[0] = (data[0] + get_n_dice_roll()) % 10
#     data[1] += data[0] + 1
#     print(data)

#     rolls += 3
#     if data[1] >= 1000:
#         print(players, rolls)
#         print(players[1 - turn][1] * rolls)
#         exit()

#     turn = 1 - turn

#     # print('players', players)
#     # exit()

