with open('6.data') as f:
    start_list = list(map(lambda x: int(x), f.readline().strip().split(',')))
    
curr = [0] * 9

for i in start_list:
    curr[i] += 1

for i in range(256):
    temp = curr[0]
    for i in range(8):
        curr[i] = curr[i + 1]
    curr[6] += temp
    curr[8] = temp

print(sum(curr))