import random
from multiprocessing import Pool


# def make_5(w):
#     return w[0] * 456976 + w[1] * 17576 + w[2] * 676 + w[3] * 26 + w[4] + 2938736


# def calc_all_init_5():
#     options = {}
#     aval = list(range(1, 10))
#     options = {}
#     for a in range(1, 10):
#         for b in range(1, 10):
#             for c in range(1, 10):
#                 for d in range(1, 10):
#                     for e in range(1, 10):
#                         options[make_5([a, b, c, d, e])] = a * 10000 + b * 1000 + c * 100 + d * 10 + e

#     for k, v in options.items():
#         print(k, v)
#     print(len(options))
# calc_all_init_5()


# def consise_written_out(w):
#     z = w[0] + 6
#     z = (z * 26) + w[1] + 11
#     z = (z * 26) + w[2] + 5
#     z = (z * 26) + w[3] + 6
#     z = (z * 26) + w[4] + 8

#     ztmp = (z % 26) - 1
#     z //= 26
#     if ztmp != w[5]:
#         z = (z * 26) + w[5] + 14

#     z = (z * 26) + w[6] + 9

#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != w[7]:
#         z = (z * 26) + w[7] + 4

#     ztmp = (z % 26) - 8
#     z //= 26
#     if ztmp != w[8]:
#         z = (z * 26) + w[8] + 7

#     z = (z * 26) + w[9] + 13

#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != w[10]:
#         z = (z * 26) + w[10] + 11

#     ztmp = (z % 26) - 13
#     z //= 26
#     if ztmp != w[11]:
#         z = (z * 26) + w[11] + 11

#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != w[12]:
#         z = (z * 26) + w[12] + 6

#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != w[13]:
#         z = (z * 26) + w[13] + 1

#     return z


# def consise_save_mathy(w):
#     z = w[0] * 456976 + w[1] * 17576 + w[2] * 676 + w[3] * 26 + w[4] + 2938736

#     ztmp = (z % 26) - 1
#     z //= 26
#     if ztmp != w[5]:
#         z = (z * 26) + w[5] + 14

#     z = (z * 26) + w[6] + 9

#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != w[7]:
#         z = (z * 26) + w[7] + 4

#     ztmp = (z % 26) - 8
#     z //= 26
#     if ztmp != w[8]:
#         z = (z * 26) + w[8] + 7

#     z = (z * 26) + w[9] + 13

#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != w[10]:
#         z = (z * 26) + w[10] + 11

#     ztmp = (z % 26) - 13
#     z //= 26
#     if ztmp != w[11]:
#         z = (z * 26) + w[11] + 11

#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != w[12]:
#         z = (z * 26) + w[12] + 6

#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != w[13]:
#         z = (z * 26) + w[13] + 1

#     return z



def consise_choose_em(w):
    full_num = w[:5]
    z = w[0] * 456976 + w[1] * 17576 + w[2] * 676 + w[3] * 26 + w[4] + 2938736

    ztmp = (z % 26) - 1
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    z = (z * 26) + w[5] + 9
    full_num.append(w[5])

    ztmp = (z % 26) - 16
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    ztmp = (z % 26) - 8
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    z = (z * 26) + w[6] + 13
    full_num.append(w[6])

    ztmp = (z % 26) - 16
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    ztmp = (z % 26) - 13
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    ztmp = (z % 26) - 6
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    ztmp = (z % 26) - 6
    z //= 26
    for i in range(1, 10):
        if ztmp == i:
            full_num.append(i)

    if len(full_num) != 14:
        return 999999

    if z == 0:
        print('FOUND IT WITH CHOOSE EM: {}'.format(''.join(map(str, full_num))))

    return z


for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            the_guys = [a, b, c, d, e, f, g]
                            if consise_choose_em(the_guys) == 0:
                                exit()


# aval = list(range(1, 10))
# for index, i in enumerate(range(10000000000)):
#     the_num = random.choices(aval, k=7)
#     my_z = consise_choose_em(the_num)
    
# print('finished searching choose ems....')
# exit()


def concise_int(w):
    return consise_save_mathy(list(map(int, str(w))))


# print(12, 64462981483139, concise_int(64462981483139))
# print(9, 34591292852249, concise_int(34591292852249))
# print(7, 12999181763287, concise_int(12999181763287))
# print(8, 24682937374159, concise_int(24682937374159))
# print(8, 23932981129788, concise_int(23932981129788))
# print(9, 31981292874186, concise_int(31981292874186))

# exit()



import time

# TIMING

# aval = list(range(1, 10))
# iters = 0
# sec_passed = 1
# start_time = time.time()

# while True:
#     the_num = random.choices(aval, k=14)
#     my_z = consise_save_mathy(the_num)
#     # print(start_time + sec_passed, time.time())
#     if start_time + sec_passed < time.time():
#         print('{:,} / per second'.format(int(iters / sec_passed)))
#         sec_passed += 1

#     if my_z < 10:
#         print('pid', pid, 'score', my_z, ''.join(map(str, the_num)))
#         if my_z == 0:
#             print('====== VALID!!!! =======')

#     iters += 1



# multiproccess


num_workers = 12
def do_work(pid):
    aval = list(range(1, 10))

    while True:
        the_num = random.choices(aval, k=14)
        my_z = consise_save_mathy(the_num)

        if my_z < 10:
            print('pid', pid, 'score', my_z, ''.join(map(str, the_num)))
            if my_z == 0:
                print('====== VALID!!!! =======')

if __name__ == '__main__':
    with Pool(num_workers) as p:
        print(p.map(do_work, range(num_workers)))



# random search
# aval = list(range(1, 10))
# for index, i in enumerate(range(10000000000)):
#     the_num = random.choices(aval, k=14)
#     my_z = consise(the_num)
    
#     if my_z == 0:
#         print(i, '========= VALID ==========')

#     if my_z < 100:
#         print(my_z, ''.join(map(str, the_num)))
#     if index % 10000000 == 0 and index != 0:
#         print('checked:', index)



# 12 64462981483139
# 9 34591292852249
# 10 41582981613146
# 15 93491892739738
# 10 41582981613146
# 15 93491892739738
# pid 1 score 7 12999181763287
# pid 4 score 8 24682937374159
# pid 4 score 8 23932981129788
# pid 7 score 9 31981292874186
# pid 8 score 7 13431881186438
# pid 6 score 9 33891816274278
# pid 8 score 7 13481899585138
# pid 6 score 9 32282992677517
# pid 3 score 7 13981839552188
# pid 8 score 3 31942992285162
# pid 6 score 7 13331881169728
# pid 1 score 9 33692981795358
# pid 4 score 8 24291856252219
# pid 5 score 8 23784292863168
# pid 7 score 5 53952981341184
# pid 8 score 8 22561892487547
# pid 4 score 8 23782981697568
# pid 3 score 7 14372992594229
# pid 0 score 8 24551892328649
# pid 4 score 7 12582181774147
# pid 0 score 9 33781837363168
# pid 4 score 7 13981825141188
# pid 7 score 7 12681859563157
# pid 8 score 8 21562981485386
# pid 2 score 7 13491869596238
# pid 0 score 8 23381829596128
# pid 1 score 9 33792987385268
# pid 10 score 8 23952981341187
# pid 8 score 9 34781897352169
# pid 7 score 3 63941892252182
# pid 1 score 9 31582992685386
# pid 11 score 8 21332981185496
# pid 2 score 8 21242981213116
# pid 11 score 8 21882926285176
# pid 11 score 8 24782949541169
# pid 11 score 9 33382992616428
# pid 11 score 9 34781826263169
# pid 9 score 9 33442992286438
# pid 5 score 9 33631881193158
# pid 0 score 7 13721881763168
# pid 2 score 8 24681845152159
# pid 2 score 9 32952992352122
# pid 1 score 9 32291881796387
# pid 3 score 8 22682987396157
# pid 5 score 9 34881895174179
# pid 11 score 9 31561892441276
# pid 10 score 9 31942981246486
