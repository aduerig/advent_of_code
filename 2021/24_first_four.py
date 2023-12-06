


def try_it(aller, a, b, c, d, e):
    res = ((((a + 6) * 26 + b + 11) * 26 + c + 5) * 26 + d + 6) * 26 + e + 8
    # print(aller, res)
    if res <= 26 * 7:
        return True
    return False

largest = 99999
smallest = 10000

# linear back search
for index, i in enumerate(range(largest, smallest, -1)):
    strified = str(i)
    if '0' in strified:
        continue
    
    if try_it(i, int(strified[0]), int(strified[1]), int(strified[2]), int(strified[3]), int(strified[4])):
        print('success', i)



# - (((((x + 6) * 26 + y + 11) * 26 + z + 5) * 26 + a + 6) * 26 + 8)



# old 24 concise 

# import random


# def consise(w):

#     z = w.pop() + 6
#     z = (z * 26) + w.pop() + 11
#     z = (z * 26) + w.pop() + 5
#     z = (z * 26) + w.pop() + 6
#     z = (z * 26) + w.pop() + 8


#     tmp = w.pop()
#     ztmp = (z % 26) - 1
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 14

#     z = (z * 26) + w.pop() + 9

#     tmp = w.pop()
#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 4

#     tmp = w.pop()
#     ztmp = (z % 26) - 8
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 7

#     z = (z * 26) + w.pop() + 13

#     tmp = w.pop()
#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 11

#     tmp = w.pop()
#     ztmp = (z % 26) - 13
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 11

#     tmp = w.pop()
#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 6

#     tmp = w.pop()
#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != tmp:
#         z = (z * 26) + tmp + 1

#     return z


# aval = list(map(str, range(1, 10)))


# # random search
# for index, i in enumerate(range(10000000000)):
#     the_num = random.choices(aval, k=14)
#     my_z = consise(list(map(int, the_num)))
    
#     if my_z == 0:
#         print(i, '========= VALID ==========')

#     if my_z < 100:
#         print(my_z, ''.join(reversed(the_num)))
#     if index % 1000000 == 0 and index != 0:
#         print('checked:', index)




# def consise_dumb(w): (sucks)
#     z = w[0] + 6
#     z = (z * 26) + w[1] + 11
#     z = (z * 26) + w[2] + 5
#     z = (z * 26) + w[3] + 6
#     z = (z * 26) + w[4] + 8

#     ztmp = (z % 26) - 1
#     z //= 26
#     if ztmp != w[5]:
#         print('wowee 5')
#         return 9999999

#     z = (z * 26) + w[6] + 9

#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != w[7]:
#         print('wowee 7')
#         return 9999999

#     ztmp = (z % 26) - 8
#     z //= 26
#     if ztmp != w[8]:
#         print('wowee 8')
#         return 9999999

#     z = (z * 26) + w[9] + 13

#     ztmp = (z % 26) - 16
#     z //= 26
#     if ztmp != w[10]:
#         print('wowee 10')
#         return 9999999

#     ztmp = (z % 26) - 13
#     z //= 26
#     if ztmp != w[11]:
#         print('wowee 11')
#         return 9999999

#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != w[12]:
#         print('wowee 12')
#         return 9999999

#     ztmp = (z % 26) - 6
#     z //= 26
#     if ztmp != w[13]:
#         print('wowee 13')
#         return 9999999

#     return z

