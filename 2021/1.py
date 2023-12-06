stuff = []
with open('1.data') as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            stuff.append(int(x))


last = float('inf')
total = 0
for i in range(len(stuff) - 2):
    x = sum(stuff[i:i+3])

    if x > last:
        total += 1
    last = x

print(total)