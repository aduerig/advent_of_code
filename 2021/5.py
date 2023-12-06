

pairs = []
with open('5.data') as f:
    for x in f.readlines():
        left, right = x.strip().split('->')
        start_point = tuple(map(lambda x: int(x), left.strip().split(',')))
        end_point = tuple(map(lambda x: int(x), right.strip().split(',')))
        # start_point = tuple(sorted(map(lambda x: int(x), left.strip().split(','))))
        # end_point = tuple(sorted(map(lambda x: int(x), right.strip().split(','))))
        if start_point[0] == end_point[0] or start_point[1] == end_point[1]:
            pairs.append((start_point, end_point))



used = set()


def overlap(a, b, x, z):
    if z < x:
        x, z = z, x

    if b < a:
        a, b = b, a
        
    
    start = max(a, x)
    end = min(b, z) + 1
    if start < end:
        # print(f'range1: ({a}, {b}), range2: ({x}, {z}), intersect: ({start}, {end-1})')
        return range(start, end)

    return range(2, 1)

# 5499 too high

def intersect(used, pair1, pair2):
    point1, point2 = pair1
    point3, point4 = pair2

    if point1[0] == point2[0]:
        if point3[0] == point4[0]:
            if point1[0] == point3[0]:
                the_range = overlap(point1[1], point2[1], point3[1], point4[1])
                for i in the_range:
                    a = point1[0]
                    b = i
                    used.add((a, b))
            return
        else:
            hori = (point3, point4)
            vert = (point1, point2)



    elif point1[1] == point2[1]:
        if point3[1] == point4[1]:
            if point1[1] == point3[1]:
                the_range = overlap(point1[0], point2[0], point3[0], point4[0])
                for i in the_range:
                    a = i
                    b = point1[1]
                    used.add((a, b))
            return
        else:
            hori = (point1, point2)
            vert = (point3, point4)


    temp = sorted((hori[0][0], hori[1][0]))
    if vert[0][0] in range(temp[0], temp[1] + 1):
        temp = sorted((vert[0][1], vert[1][1]))
        if hori[0][1] in range(temp[0], temp[1] + 1):
            a = hori[0][1]
            b = vert[0][0]
            print(f'hori: {hori}\nvert: {vert}, collide at ({a}, {b})')
            used.add((b, a))
    
# not 2989
        
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        intersect(used, pairs[i], pairs[j])

print(len(used))



