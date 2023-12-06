data = []

with open('24.data') as f:
    for line in f.readlines():
        if line.strip():
            splitted = line.split()

            if len(splitted) == 2:
                data.append((splitted[0].strip(), splitted[1].strip(), None))
            else:
                data.append((splitted[0].strip(), splitted[1].strip(), splitted[2].strip()))

def consise(w):

    z = w[0] + 6
    z = (z * 26) + w[1] + 11
    z = (z * 26) + w[2] + 5
    z = (z * 26) + w[3] + 6
    z = (z * 26) + w[4] + 8


    tmp = w[5]
    ztmp = (z % 26) - 1
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 14

    z = (z * 26) + w[6] + 9

    tmp = w[7]
    ztmp = (z % 26) - 16
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 4

    tmp = w[8]
    ztmp = (z % 26) - 8
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 7

    z = (z * 26) + w[9] + 13

    tmp = w[10]
    ztmp = (z % 26) - 16
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 11

    tmp = w[11]
    ztmp = (z % 26) - 13
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 11

    tmp = w[12]
    ztmp = (z % 26) - 6
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 6

    tmp = w[13]
    ztmp = (z % 26) - 6
    z //= 26
    if ztmp != tmp:
        z = (z * 26) + tmp + 1

    return z




def get_val(v):
    if v == None:
        return None
    global the_vars
    to_ret = None
    if v in set(['w', 'x', 'y', 'z']):
        to_ret = the_vars[v]
    else:
        to_ret = int(v)
    return to_ret

def add(v1, v2):
    return get_val(v1) + get_val(v2)

def mul(v1, v2):
    return get_val(v1) * get_val(v2)

def div(v1, v2):
    v2 = get_val(v2)
    if v2 == 0:
        print('div breakage', v1, v2)
        exit()
    return get_val(v1) // v2

def mod(v1, v2):
    v1 = get_val(v1)
    v2 = get_val(v2)
    if v1 < 0 or v2 <= 0:
        print('mod breakage', v1, v2)
        exit()
    return v1 % v2

def eql(v1, v2):
    return int(get_val(v1) == get_val(v2))

def inp(v1, v2):
    global inputs; global inputs_index;
    inputs_index += 1
    return inputs[inputs_index - 1]

mapper = {
    "add": add,
    "inp": inp,
    "mul": mul,
    "div": div,
    "mod": mod,
    "eql": eql,
}


def exe(data, in_inputs):
    if in_inputs == None:
        in_inputs = list(map(int, list(input("sequence: "))))
    global inputs; global inputs_index; global the_vars;
    the_vars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    inputs_index = 0
    inputs = in_inputs


    what_input = -1
    to_check_digit = 12
    z_vals = []

    # calcs = {
    #     0: in_inputs[0] + 6,
    #     1: (in_inputs[0] + 6) * 26 + in_inputs[1] + 11,
    #     2: ((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5,
    #     3: (((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6,
    #     4: ((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8,
    #     5: ((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14,
    #     6: (((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9,
    #     7: (((((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9) // 26) * 26 + in_inputs[7] + 4,
    #     8: (((((((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9) // 26) * 26 + in_inputs[7] + 4) // 26) * 26 + in_inputs[8] + 7,
    #     9: ((((((((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9) // 26) * 26 + in_inputs[7] + 4) // 26) * 26 + in_inputs[8] + 7) * 26 + in_inputs[9] + 13,
    #     10: ((((((((((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9) // 26) * 26 + in_inputs[7] + 4) // 26) * 26 + in_inputs[8] + 7) * 26 + in_inputs[9] + 13) // 26) * 26 + in_inputs[10] + 11,
    #     11: ((((((((((((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9) // 26) * 26 + in_inputs[7] + 4) // 26) * 26 + in_inputs[8] + 7) * 26 + in_inputs[9] + 13) // 26) * 26 + in_inputs[10] + 11) // 26) * 26 + in_inputs[11] + 11,
    #     12: ((((((((((((((((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + in_inputs[4] + 8) // 26) * 26 + in_inputs[5] + 14) * 26 + in_inputs[6] + 9) // 26) * 26 + in_inputs[7] + 4) // 26) * 26 + in_inputs[8] + 7) * 26 + in_inputs[9] + 13) // 26) * 26 + in_inputs[10] + 11) // 26) * 26 + in_inputs[11] + 11) // 26) * 26 + in_inputs[12] + 6,
    #     13: 0,
    # }

    for i, (op, v1, v2) in enumerate(data):
        # if op == 'inp':
        #     if what_input >= 0:
        #         z_vals.append(the_vars['z'])
        #     if z_vals and z_vals[-1] != calcs[len(z_vals) - 1]:
        #         print('MISMATCH ON', what_input, 'number is', in_inputs[what_input])
        #         print('the number', ''.join(map(str, in_inputs)))
        #         print('my algo', ', '.join(map(str, [x[1] for x in sorted(calcs.items())])))
        #         print('z vals: ' + ', '.join(map(str, z_vals)))
        #         global wrong_guys;
        #         if what_input not in wrong_guys:
        #             wrong_guys[what_input] = 0
        #         wrong_guys[what_input] += 1
        #         # if what_input == 5:
        #             # exit()
        #         print('======= WRONGO', wrong_guys)
        #         return
        #     # if what_input == to_check_digit:
        #     #     print('my algo', ', '.join(map(str, [x[1] for x in sorted(calcs.items())])))
        #     #     print('z vals: ' + ', '.join(map(str, z_vals)))
        #     #     exit()
        #     what_input += 1

        the_vars[v1] = mapper[op](v1, v2)


        # if what_input == to_check_digit:
            # old_v1 = the_vars[v1]
            # the_vars[v1] = mapper[op](v1, v2)
            # print(v1, '=', v1, op, v2, ':', the_vars[v1], '=', old_v1, op, get_val(v2))
        # print('data line', i, ':', op, v1, v2, the_vars)

{
    5: 2859, 
    7: 2830,
    8: 7120, 
    10: 7518, 
    11: 8421, 
    12: 4175, 
}


import random
largest = 99999999999999
smallest= 10000000000000

aval = list(map(str, range(1, 10)))
global the_vars

global wrong_guys
wrong_guys = {}



# random search with set indicies
# to_fill = set([5, 7, 8, 10, 11, 12, 13])
# for index, i in enumerate(range(10000000000)):
#     rand_nums = random.choices(aval, k=7)
#     num_to_try = ['1'] * 14
#     for index_from_choices, index_to_fill in enumerate(to_fill):
#         num_to_try[index_to_fill] = rand_nums[index_from_choices]

#     # print(num_to_try)

#     exe(data, list(map(int, num_to_try)))
#     if the_vars['z'] == 0:
#         print(i, '========= VALID ==========')

#     if the_vars['z'] < 2000:
#         print(the_vars['z'], ''.join(num_to_try))
#     if index % 100000 == 0:
#         print('checked:', index)



# random search vs. my concise
# for index, i in enumerate(range(10000000000)):
#     the_num = random.choices(aval, k=14)
#     exe(data, list(map(int, the_num)))
#     my_z = consise(list(map(int, the_num)))
#     if my_z != the_vars['z']:
#         print(index, 'mine:', my_z, 'real', the_vars['z'])
#         exit()
    
#     if the_vars['z'] == 0:
#         print(i, '========= VALID ==========')

#     if the_vars['z'] < 2000:
#         print(the_vars['z'], ''.join(the_num))
#     if index % 100000 == 0 and index != 0:
#         print('checked:', index)



# checked: 800000 95678866114271 {'w': 1, 'x': 1, 'y': 2, 'z': 185734954}
# checked: 1000000 73874455341633 {'w': 3, 'x': 0, 'y': 0, 'z': 6195896}
# checked: 1100000 11921834441519 {'w': 9, 'x': 1, 'y': 10, 'z': 3419426}
# checked: 1700000 36347476236969 {'w': 9, 'x': 1, 'y': 10, 'z': 114848822}




# 355 76746235152346
# 358 79344845163942
# 306 59451848475353
# 332 69632949541495
# 407 96553168496254
# 357 78695267341395
# 408 97613425185515
# 355 76381892644382
# 305 58829456285527
# 223 24282981528661
# 195 12764785141866
# 304 57272992585811



try_these = [
    64462981483139,
    14522826285924,
    34591292852249,
    12999181763287,
    84991892741198
]
for the_num in try_these:
    exe(data, list(map(int, str(the_num))))
    print(the_num, the_vars['z'])
    if the_vars['z'] == 0:
        print(i, 'VALID')



# tracking = []




# linear back search
# for index, i in enumerate(range(largest, smallest, -1)):
#     strified = str(i)
#     if index % 10000 == 0:
#         dist_to_go = largest - smallest
#         print('{:.7f}%'.format((index / largest) * 100))
#     if '0' in strified:
#         continue
#     exe(data, list(map(int, strified)))
#     if the_vars['z'] == 0:
#         print(i, 'VALID')
