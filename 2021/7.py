# https://adventofcode.com/2021/day/3#part2


with open('7.data') as f:
    x = f.readline().strip()
    init = list(map(lambda x: int(x), x.split(',')))


thing = [0] * (max(init) + 1)
for i in init:
    thing[i] += 1


left = []
right = []

print(thing)

cost = 0
s = 0
drag_cost = 0
for i in thing:
    s += cost + drag_cost
    left.append(s)
    drag_cost += cost
    cost += i

cost = 0
drag_cost = 0
s = 0
for i in reversed(thing):
    s += cost + drag_cost
    right.append(s)
    drag_cost += cost
    cost += i

right = list(reversed(right))
print(left)
print(right)

new = []
for index in range(0, len(left)):
    new.append((left[index] + right[index], index))

print(new)

print(min(new))
