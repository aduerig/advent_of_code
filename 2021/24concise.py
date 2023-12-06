


def consise(w):
    w = list(reversed(w))

    z = w.pop() + 6
    z = (z * 26) + w.pop() + 11
    z = (z * 26) + w.pop() + 5
    z = (z * 26) + w.pop() + 6
    z = (z * 26) + w.pop() + 8


    tmp = w.pop()
    ztmp = (z % 26) - 1
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 14

    z = (z * 26) + w.pop() + 9

    tmp = w.pop()
    ztmp = (z % 26) - 16
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 4

    tmp = w.pop()
    ztmp = (z % 26) - 8
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 7

    z = (z * 26) + w.pop() + 13

    tmp = w.pop()
    ztmp = (z % 26) - 16
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 11

    tmp = w.pop()
    ztmp = (z % 26) - 13
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 11

    tmp = w.pop()
    ztmp = (z % 26) - 6
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 6

    tmp = w.pop()
    ztmp = (z % 26) - 6
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 1

    return z



import random

aval = list(map(str, range(1, 10)))


for index, i in enumerate(range(10000000000)):
    the_num = random.choices(aval, k=14)

    the_list = list(map(int, the_num))
    z = consise(the_list)

    print(z)