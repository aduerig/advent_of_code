with open('17.data') as f:
    x, y = f.readline().strip().replace('target area: ', '').split(',')
    x1, x2 = x.strip().replace('x=', '').split('..')
    y1, y2 = y.strip().replace('y=', '').split('..')
    
    
    x_area = (int(x1.strip()), int(x2.strip()))
    x_range = range(x_area[0], x_area[1] + 1)
    y_area = (int(y1.strip()), int(y2.strip()))
    y_range = range(y_area[0], y_area[1] + 1)


def is_in(xvel, yvel):
    x = 0
    y = 0

    # max_y = y

    step = 0
    # print('simulation on', xvel, yvel, 'go to', x_area, y_area)
    while True:
        # print(f'step: {step}, ({x}, {y}), [xvel, yvel] [{xvel}, {yvel}]')
        if x in x_range and y in y_range:
            return True
        if xvel == 0:
            if x not in x_range:
                return None
        elif xvel > 0:
            if x > x_area[1]:
                return None
        elif x < x_area[0]:
            return None
        if yvel < 0 and y < y_area[0]:
            return None

        y += yvel
        x += xvel
        # max_y = max(max_y, y)

        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1
        # step += 1


if (x_area[0] < 0 and x_area[1] > 1) or 0 in x_area:
    print('this wont work...')
    exit()

direction = -1
if x_area[0] > 0:
    direction = 1

total = 0
for xvel in range(1 * direction, 162 * direction, direction):
    for yvel in range(-2000, 4000):
        num = is_in(xvel, yvel)
        if num is not None:
            total += 1
print(total)

# not 2850

# 1777 too low