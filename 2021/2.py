cmds = []
with open('2.data') as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            cmd, dist = x.split()
            cmds.append((cmd, int(dist)))


hori = 0
aim = 0
depth = 0

for cmd, dist in cmds:
    if cmd == 'forward':
        hori += dist
        depth += aim * dist
    if cmd == 'down':
        aim += dist
    if cmd == 'up':
        aim -= dist

print(hori, depth)

print(hori * depth)