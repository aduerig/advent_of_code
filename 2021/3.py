# https://adventofcode.com/2021/day/3#part2


cmds = []
with open('3.data') as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            cmds.append(x)



def binary_to_decimal(bin_arr):
    tot = 0
    for i, x in enumerate(list(reversed(bin_arr))):
        tot += int(x) * pow(2, i)
    return tot

nums = cmds


def get_count(x, index):
    counting = [[0, '0'], [0, '1']]
    for num in x:
        counting[int(num[index])][0] += 1
    return counting


def trace(things, reversed_thing, index):
    if len(things) < 2:
        return binary_to_decimal(things[0])
    new_things = []
    
    count = sorted(get_count(things, index), reverse = not reversed_thing)
    picked = count[0][1]

    for i in things:
        if i[index] == picked:
            new_things.append(i)
    return trace(new_things, reversed_thing, index + 1)


print(trace(nums[:], True, 0) * trace(nums[:], False, 0))