data = []
all_folds = []


global height; height = 895
global width; width = 1311

for i in range(height):
    data.append([0] * width)

with open('13.data') as f:
    folds = False
    for i in f.readlines():
        if not i.split():
            folds = True
        elif not folds:
            x, y = map(lambda x: int(x), i.strip().split(','))
            data[y][x] = 1
        else:
            _, _, rel = i.strip().split(' ')
            axis, num = rel.strip().split('=')
            all_folds.append((axis, int(num)))




def fold_x(fold_line):
    global height; global width;
    for y in range(height):
        for x in range(width):
            if x > fold_line:
                if data[y][x]:
                    data[y][width - (x + 1)] = data[y][x] 
    width = width // 2


def fold_y(fold_line):
    global height; global width;
    for y in range(height):
        for x in range(width):
            if y > fold_line:
                if data[y][x]:
                    data[height - (y + 1)][x] = data[y][x]
    height = height // 2


runners = {
    'x': fold_x,
    'y': fold_y,
}
lol = {
    0: '.',
    1: '#',
}


for axis, num in all_folds:
    runners[axis](num)

for y in range(height):
    print(''.join(map(lambda x: lol[x], data[y][:width])))

