

def solve(a, b=0):
    b = a & 7
    b = b ^ 1
    b = b ^ (a // (1 << b))
    b = b ^ 4
    return b


a = 5
last = -1
last_valid = None
while a < 1000:
    # for i in range(last+1, a):
    #     if (solve(i) & 7) == 2:
    #         print(f'HUH: {i}')
    #         exit()

    ans = solve(a)
    if (ans & 7) == 2:
        last_valid_string = ''
        if last_valid:
            last_valid_string = a - last_valid
        last_valid = a
        print(f'{a} - {ans} {ans & 7} {last_valid_string}')
        # print('HUH 2')
        # exit()
    last = a
    a += 1








