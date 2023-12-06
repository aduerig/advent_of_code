data = []

with open('11.data') as f:
    for x in f.readlines():
        new_level = list(map(lambda x: int(x), list(x.strip())))
        data.append(new_level)



def add_to(data, x, y):
    if x > -1 and y > -1 and x < len(data[0]) and y < len(data):
        data[y][x] += 1

def add_around(data, x, y):
    add_to(data, x, y + 1)
    add_to(data, x, y - 1)
    add_to(data, x + 1, y + 1)
    add_to(data, x - 1, y - 1)
    add_to(data, x - 1, y + 1)
    add_to(data, x + 1, y - 1)
    add_to(data, x + 1, y)    
    add_to(data, x - 1, y)


flash = 0
i = 1
while True:
    added = set()
    while True:
        broken = False
        for x in range(len(data[0])):
            for y in range(len(data)):
                if (x, y) not in added:
                    data[y][x] += 1
                    added.add((x, y))
                if data[y][x] > 9 and data[y][x] != float('inf'):
                    add_around(data, x, y)
                    broken = True
                    flash += 1
                    data[y][x] = float('inf')
                    added.add((x, y))
                    break
            if broken:
                break
        if not broken:
            simul = True
            for x in range(len(data[0])):
                for y in range(len(data)):
                    if data[y][x] == float('inf'):
                        data[y][x] = 0
                    else:
                        simul = False
            if simul:
                print(i)
                exit()
            break
    i += 1