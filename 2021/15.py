small_grid = []

with open('15.data') as f:
    for i in f.readlines():
        if i.strip():
            small_grid.append(list(map(lambda x: int(x), list(i.strip()))))


def wrap(a: int, b: int) -> int:
    for _ in range(b):
        if a > 9:
            a = 1
        a += 1
        if a > 9:
            a = 1
    return a


ychunk = len(small_grid)
xchunk = len(small_grid[0])
print(xchunk, ychunk)

grid = []
for bigy in range(5 * len(small_grid)):
    one_layer = []
    for bigx in range(5 * len(small_grid[0])):
        dx = bigx // xchunk
        dy = bigy // ychunk
        one_layer.append(wrap(small_grid[bigy % ychunk][bigx % xchunk], dy + dx))
    grid.append(one_layer)        

print(len(small_grid), len(small_grid[0]))
print(len(grid), len(grid[0]))


import heapq

visited = set()
queue = [(0, 0, 0)]
need_to_explore = len(grid) * len(grid[0])

print(f'will need to explore {need_to_explore:,} nodes total')

while queue:
    cost, x, y = heapq.heappop(queue)
    if (x, y) in visited:
        continue
    visited.add((x, y))

    if (x, y) == (len(grid[0]) - 1, len(grid) - 1):
        print(cost) 
        break
    
    if len(visited) % (need_to_explore // 10) == 0:
        print(f'visited {len(visited)} nodes')

    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        newx = dx + x
        newy = dy + y
        if newx > -1 and newy > -1 and newy < len(grid) and newx < len(grid[0]):
            if (newx, newy) not in visited:
                heapq.heappush(queue, (cost + grid[newy][newx], newx, newy))

