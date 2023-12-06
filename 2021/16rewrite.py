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

class packet:
    def __init__(self, ver, rand_type, b):
        self.ver = ver
        self.rand_type = rand_type
        self.op = None
        self.children = []
        self.bytes_left = None
        self.packets_left = None
        self.bytes_taken = b
        self.literal_binary = None

    def solve(self):
        if self.rand_type == 4:
            # print('solve, literal', self.op)
            return self.op
        # print('solving', self.op, self.children)
        # return self.op(list(map(lambda x: x.solve(), self.children)))
        tmp = self.op(list(map(lambda x: x.solve(), self.children)))
        print(tmp, self.op, self.children)
        return tmp

    def __repr__(self):
        ok = ''
        if self.bytes_left is not None:
            ok = f' | bytes_left: {self.bytes_left}'
        elif self.packets_left is not None:
            ok = f' | packets_left: {self.packets_left}'
        literal = ''
        if type(self.op) == int:
            literal = 'binary: {} decimal: '.format(''.join(map(str, self.literal_binary)))
        return f'(version: {self.ver} | bytes: {self.bytes_taken} | {literal}{self.op} | sub_nodes: {len(self.children)}{ok})'


init_copy = list(data)

total = 0
total_bytes_read = 0
stack = []
first = True
while stack or first:
    first = False
    new_packet = packet(binary_to_dec(data[0:3]), binary_to_dec(data[3:6]), 6)
    total += new_packet.ver
    data = data[6:]
    if new_packet.rand_type == 4:
        continue_reading = True
        all_use = []
        while data and continue_reading:
            curr = data[:5]
            if curr[0] == 0:
                continue_reading = False
            all_use += curr[1:5]
            data = data[5:]
            new_packet.bytes_taken += 5
        new_packet.op = binary_to_dec(all_use)
        new_packet.literal_binary = all_use
    else:
        new_packet.op = ops[new_packet.rand_type]
        length_type_id = data[0]
        data = data[1:]
        if length_type_id == 0:
            new_packet.bytes_left = binary_to_dec(data[:15])
            data = data[15:]
            new_packet.bytes_taken += 16
        if length_type_id == 1:
            new_packet.packets_left = binary_to_dec(data[:11])
            data = data[11:]
            new_packet.bytes_taken += 12

    print('new_packet identified', new_packet)
    total_bytes_read += new_packet.bytes_taken
    print(f'{total_bytes_read} / {len(init_copy)} read. Version total is:', total)


    if not stack:
        stack.append(new_packet)
        print('FULL STACK:', ' -> '.join(map(lambda x: str(x), stack)))
        continue


    assigned = False
    while not assigned:
        last = stack[-1]

        if last.packets_left is not None:
            if last.packets_left == 0:
                stack.pop()
                continue
            last.packets_left -= 1
        
        elif last.bytes_left is not None:
            if last.bytes_left == 0:
                stack.pop()
                continue          
            # last.bytes_left -= bytes_read      

        last.children.append(new_packet)

        if new_packet.bytes_left or new_packet.packets_left:
            stack.append(new_packet)

        assigned = True

    # decrease byte lengths
    for i in stack:
        if i.bytes_left is not None and i != new_packet:
            i.bytes_left -= new_packet.bytes_taken
            if i.bytes_left < 0:
                print(f'negative bytes left on {i}. new_packet {new_packet}')
                exit()


    while stack and ((stack[-1].bytes_left is not None and stack[-1].bytes_left == 0) or (stack[-1].packets_left is not None and stack[-1].packets_left == 0)):
        # if stack[-1].packets_left is not None and stack[-1].packets_left == 0:
        final_popped = stack.pop()

    print('FULL STACK:', ' -> '.join(map(lambda x: str(x), stack)))


print('\n====== SOLVING =====')
print('final answer:', final_popped.solve())

# not 947



# index = len(stack) - 1
# if stack and stack[-1][0] == 0:
#     stack[-1][1] -= 1

# while index > -1:
#     if stack[-1][1] == 0:
#         lets_go_brandon(stack)

#     elif stack[index][0] == 1:
#         stack[index][1] -= bytes_read
#         if stack[index][1] <= 0:
#             lets_go_brandon(stack)
#     index -= 1



    # def lets_go_brandon(stack):
    #     global all_nums
    #     print('detected expiry', stack)
    #     print(all_nums)
    #     stack.pop()
    #     the_stuff = all_nums.pop()
    #     if len(all_nums) > 0:
    #         all_nums[-1].append(the_stuff)
    #     else:
    #         all_nums = list(the_stuff)


    # self.bytes_left = None
    # self.packets_left = None