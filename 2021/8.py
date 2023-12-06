# https://adventofcode.com/2021/day/3#part2


data = []

with open('8.data') as f:
    for x in f.readlines():
        left, right = x.strip().split('|')
        right = right.strip().split()
        left = left.strip().split()

        data.append([left, right])



strict = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

possible = {
    5: [2, 3, 5],   # identify 3s, check for 4 in 5 that has 3 signals, last is 2
    6: [0, 6, 9],   # 9 is just with 4 signals, 0 is with 1 signals, 6 is remaining
}


def get_num(left, right):
    mapping = {}

    fives = []
    sixes = []
    for val in left:
        if len(val) in strict:
            mapping[strict[len(val)]] = val
            continue

        if len(val) == 5:
            fives.append((val, set(val)))
        else:
            sixes.append((val, set(val)))

    # three
    differ = [0, 0, 0]
    for i in range(len(fives)):
        for j in range(i + 1, len(fives)):
            s1 = fives[i][1]
            s2 = fives[j][1]
            if len(s1.difference(s2)) == 1:
                differ[i] += 1
                differ[j] += 1
    found_three = differ.index(2)
    mapping[3] = fives[found_three][0]
    del fives[found_three]

    # five
    for signal in set(mapping[4]):
        if signal not in set(mapping[3]):
            five_signal = signal

    for index, i in enumerate(fives):
        if five_signal in i[1]:
            found_five = index
    mapping[5] = fives[found_five][0]
    del fives[found_five]

    # two
    mapping[2] = fives[0][0]


    # 9
    for index, pot in enumerate(sixes):
        set_of_pot = pot[1]
        breaker = False
        for signal in set(mapping[4]):
            if signal not in set_of_pot:
                breaker = True
        if not breaker:
            found_nine = index
            break
    mapping[9] = sixes[found_nine][0]
    del sixes[found_nine]

    # 0
    for index, pot in enumerate(sixes):
        set_of_pot = pot[1]
        breaker = False
        for signal in set(mapping[1]):
            if signal not in set_of_pot:
                breaker = True
        if not breaker:
            found_zero = index
            break
    mapping[0] = sixes[found_zero][0]
    del sixes[found_zero]

    # 6
    mapping[6] = sixes[0][0]


    print(mapping)
    s = 0
    for index, i in enumerate(right):
        for real_num, hashes in mapping.items():
            breaker = False
            if len(hashes) != len(i):
                continue
            for h in hashes:
                if h not in i:
                    breaker = True
            if not breaker:
                break
        s += real_num * pow(10, (3 - index))
    return s



s = 0
for d in data:
    temp = get_num(d[0], d[1])
    print(temp)
    s += temp
print(s)