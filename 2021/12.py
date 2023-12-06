data = {}

with open('12.data') as f:
    for x in f.readlines():
        a, b = x.strip().split('-')
        if a not in data:
            data[a] = []
        data[a].append(b)

        if b not in data:
            data[b] = []
        data[b].append(a)



def dfs(data, pos, rem2, used_small):
    other = 0
    if pos == 'end':
        return 1
    if pos.upper() != pos:
        if pos not in rem2:
            rem2[pos] = 0

        if rem2[pos] == 1 and not used_small and pos != 'start':
            for child in data[pos]:
                other += dfs(data, child, rem2, True)

        if rem2[pos] > 0:
            return other

        rem2[pos] += 1

    for child in data[pos]:
        if child != 'start':
            other += dfs(data, child, rem2, used_small)

    if pos.upper() != pos:
        rem2[pos] -= 1
    return other


print(dfs(data, 'start', {}, False))