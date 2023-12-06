image = []


with open('20.data') as f:
    algo = list(f.readline().strip())
    f.readline()
    for line in f.readlines():
        if line.strip():
            image.append(list(line.strip()))


def str_to_dec(s: str) -> int:
    lol = 0
    for index, i in enumerate(reversed(s)):
        if i == '#':
            lol += pow(2, index)
    return lol





def make_str(image, x, y, outer_reaches):
    new_str = []
    for s_y in range(y - 1, y + 2):
        for s_x in range(x - 1, x + 2):
            new_str.append(outer_reaches)
            if s_x > -1 and s_y > -1 and s_x < len(image[0]) and s_y < len(image):
                new_str[-1] = image[s_y][s_x]
    return ''.join(new_str)

outer_reaches = '.'

for i in range(50): 
    # print(f"LAYER {i} ====")
    # for ok in image:
    #     print(''.join(ok))
    # print(f"LAYER {i} ====")



    new_image = []
    for y in range(-1, len(image) + 1):
        new_row = []
        for x in range(-1, len(image[0]) + 1):
            new_str = make_str(image, x, y, outer_reaches)
            dec_num = str_to_dec(new_str)
            # print(new_str, dec_num)
            new_row.append(algo[dec_num])
        new_image.append(new_row)
    image = new_image

    if algo[0] == '#':
        if outer_reaches == '.':
            outer_reaches = '#'
        else:
            outer_reaches = '.'


lit = 0
for i in image:
    for j in i:
        if j == '#':
            lit += 1


print("DONE === ")

# for i in image:
#     print(''.join(i))

print(lit)



# 5607 too high
