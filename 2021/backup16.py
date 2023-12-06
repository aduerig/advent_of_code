lmao = {'0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

with open('16.data') as f:
    data_hex = f.readline().strip()
    data = []
    for i in data_hex:
        for j in lmao[i]:
            data.append(j)
    data = list(map(lambda x: int(x), data))


def mult(arr):
    total = None
    for i in arr:
        if total is None:
            total = i
        else:
            total *= i
    return total

def gt(lol):
    if lol[0] > lol[1]:
        return 1
    return 0

def lt(lol):
    if lol[0] < lol[1]:
        return 1
    return 0

def eq(lol):
    if lol[0] == lol[1]:
        return 1
    return 0


ops = {
    0: sum,
    1: mult,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq,
}


print('input hex', data_hex)
print('input binary', ''.join(map(lambda x: str(x), data)))


def print_ints(arr):
    print(''.join(map(lambda x: str(x), arr)))

def binary_to_dec(bin_arr):
    total = 0
    for index, i in enumerate(reversed(bin_arr)):
        total += i * pow(2, index)
    return total

init_copy = list(data)

set_length = []
total = 0
total_bytes_read = 0
all_nums = []
first = True
while set_length or first:
    first = False
    sub_packet_length = None
    sub_packet_num = None
    total += binary_to_dec(data[0:3])
    type = data[3:6]
    bytes_read = 6
    print('new iter', set_length, 'version', data[0:3], 'type: ', type)
    data = data[6:]
    if binary_to_dec(type) == 4:
        keep = True
        all_use = []
        while data and keep:
            curr = data[:5]
            if curr[0] == 0:
                keep = False
            all_use += curr[1:5]
            data = data[5:]
            bytes_read += 5
        operation = 4
        print('literal packet', binary_to_dec(all_use))
        if not all_nums:
            exit()
        all_nums[-1].append(binary_to_dec(all_use))
    else:
        length_type_id = data[0]
        operation = binary_to_dec(type)
        data = data[1:]
        bytes_read += 1
        all_nums.append([ops[operation]])
        print('sub packet, op is', ops[operation])
        if length_type_id == 0:
            sub_packet_length = binary_to_dec(data[:15])
            print('given bits of next sub packet', sub_packet_length)
            if len(data) < sub_packet_length:
                print('huh ^')
                exit()
            data = data[15:]
            bytes_read += 15
        if length_type_id == 1:
            sub_packet_num = binary_to_dec(data[:11])
            print('given number sub packets', sub_packet_num)
            data = data[11:]
            bytes_read += 11

    def solve(arr):
        op = arr[0]
        print('solving', arr)
        return op(arr[1:])

    def lets_go_brandon(set_length):
        print('detected expiry', set_length)
        print(all_nums)
        set_length.pop()
        the_stuff = all_nums.pop()
        lol = solve(the_stuff)
        if len(all_nums) > 0:
            all_nums[-1].append(lol)
        else:
            print('done', lol)

    print('before calc')
    print(set_length)
    print(all_nums)
    print('bytes to go', len(init_copy) - total_bytes_read)    
    index = len(set_length) -1
    if set_length and set_length[-1][0] == 0:
        set_length[-1][1] -= 1
    
    while index > -1:
        if set_length[-1][1] == 0:
            lets_go_brandon(set_length)

        elif set_length[index][0] == 1:
            set_length[index][1] -= bytes_read
            if set_length[index][1] <= 0:
                lets_go_brandon(set_length)
        index -= 1


    if sub_packet_num is not None and sub_packet_num != 0:
        set_length.append([0, sub_packet_num])
    if sub_packet_length is not None and sub_packet_length != 0:
        set_length.append([1, sub_packet_length])
    total_bytes_read += bytes_read

    print('after calc')
    print(set_length)
    print(all_nums)


print(total)

# not 947