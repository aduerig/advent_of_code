import functools
data = []

with open('9.data') as f:
    for x in f.readlines():
        data.append(list(map(lambda x: int(x), list(x.strip()))))


def dfs(data, x, y, visited):
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return 0
    if data[y][x] == 9:
        return 0
    if (x, y) in visited:
        return 0
    visited.add((x, y))

    others = 0
    for new_x, new_y in [
                            (x+1, y),
                            (x-1, y),
                            (x, y+1),
                            (x, y-1),
                        ]:
        others += dfs(data, new_x, new_y, visited)

    return 1 + others


scores = []
visited = set()
for x in range(len(data[0])):
    for y in range(len(data)):
        if basins := dfs(data, x, y, visited):
            scores.append(basins)

scores.sort(reverse=True)
print(functools.reduce(lambda x, y: x * y, scores[:3]))