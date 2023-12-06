iters = 40

data = []
mapping = {}

with open('14.data') as f:
    template = list(f.readline().strip())
    f.readline()
    for i in f.readlines():
        if i.strip():
            l, r = i.strip().split('->')
            mapping[l.strip()] = r.strip()




for _ in range(iters):
    index = 0
    new = []
    while index < len(template):
        new.append(template[index])
        for k, v in mapping.items():
            if index + len(k) <= len(template):
                breaker = False
                for i in range(len(k)):
                    if template[index + i] != k[i]:
                        breaker = True
                        break
                if not breaker:
                    new.append(v)        
        index += 1
    template = new

count = {}
for i in template:
    if i not in count:
        count[i] = 0
    count[i] += 1

for k, v in count.items():
    print(k, v)

lol = sorted(list(count.values()))

print(lol[-1] - lol[0])