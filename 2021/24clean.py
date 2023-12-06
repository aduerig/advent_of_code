def consise_choose_em(w):
    full_num = w[:5]
    z = w[0] * 456976 + w[1] * 17576 + w[2] * 676 + w[3] * 26 + w[4] + 2938736
    full_num.append((z % 26) - 1)
    z //= 26
    z = (z * 26) + w[5] + 9
    full_num += [w[5], (z % 26) - 16]
    z //= 26
    full_num.append((z % 26) - 8)
    z //= 26
    z = (z * 26) + w[6] + 13
    full_num += [w[6], (z % 26) - 16]
    z //= 26
    full_num.append((z % 26) - 13)
    z //= 26
    full_num.append((z % 26) - 6)
    z //= 26
    full_num.append((z % 26) - 6)
    z //= 26

    if z == 0 and len(full_num) == 14 and all(map(lambda x: x > 0, full_num)):
        return full_num

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            if ans := consise_choose_em([a, b, c, d, e, f, g]):
                                print(''.join(map(str, ans)))



# def consise_choose_em(w):
#     full_num = w[:5]
#     z = w[0] * 456976 + w[1] * 17576 + w[2] * 676 + w[3] * 26 + w[4] + 2938736
#     full_num.append((z % 26) - 1)
#     z //= 26
#     z = (z * 26) + w[5] + 9
#     full_num += [w[5], (z % 26) - 16]
#     z //= 26
#     full_num.append((z % 26) - 8)
#     z //= 26
#     z = (z * 26) + w[6] + 13
#     full_num += [w[6], (z % 26) - 16]
#     z //= 26
#     full_num.append((z % 26) - 13)
#     z //= 26
#     full_num.append((z % 26) - 6)
#     z //= 26
#     full_num.append((z % 26) - 6)
#     z //= 26

#     if z == 0 and len(full_num) == 14 and all(map(lambda x: x > 0, full_num)):
#         return full_num

# for a in range(1, 10):
#     for b in range(1, 10):
#         for c in range(1, 10):
#             for d in range(1, 10):
#                 for e in range(1, 10):
#                     for f in range(1, 10):
#                         for g in range(1, 10):
#                             if ans := consise_choose_em([a, b, c, d, e, f, g]):
#                                 print(''.join(map(str, ans)))
#                                 exit()
