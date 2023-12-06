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


to_add = (template[0], template[-1])

holder = {}

for a,b in zip(template, template[1:]):
    if a + b not in holder:
        holder[a+b] = 0
    holder[a + b] += 1


print(iters)
for _ in range(iters):
    new_holder = {}
    for k, v in holder.items():
        if k in mapping:
            new_doubles = [k[0] + mapping[k], mapping[k] + k[1]]
            
            for new_double in new_doubles:
                if new_double not in new_holder:
                    new_holder[new_double] = 0
                new_holder[new_double] += v
    holder = new_holder

count = {}
for k, v in holder.items():
    for letter in k:
        if letter not in count:
            count[letter] = 0
        count[letter] += v

for i in to_add:
    count[i] += 1

for k, v in count.items():
    count[k] = v // 2


for k, v in count.items():
    print(k, v)

lol = sorted(list(count.values()))

print(lol[-1] - lol[0])


# i guessed 7155869758393
# I guessed 7155869758392

# want to g 7155869758393



# (3) zetai advent2021$ python 14pt2.py
# S 2214
# H 1696
# P 1543
# K 3166
# F 2542
# O 798
# B 1372
# V 633
# C 1353
# N 1067
# 3166
# 633
# 2533

# (3) zetai advent2021$ python 14.py 
# S 2765
# H 2116
# P 1910
# K 3461
# F 2833
# O 977
# B 1741
# V 749
# C 1666
# N 1239
# 2712



# iters 2
# (3) zetai advent2021$ python 14pt2.py
# S 10
# H 9
# P 6
# C 5
# K 7
# F 11
# V 4
# B 8
# O 1
# N 3
# 10
# (3) zetai advent2021$ python 14.py   
# S 12
# H 10
# P 7
# C 6
# K 7
# F 13
# V 6
# B 11
# O 1
# N 4
# 12


# iters 1
# (3) zetai advent2021$ python 14.py
# S 4
# P 4
# C 2
# F 3
# V 5
# B 6
# H 8
# K 4
# O 1
# N 2
# 7
# (3) zetai advent2021$ python 14pt2.py
# S 4
# P 3
# C 2
# F 2
# V 3
# B 4
# H 7
# K 4
# O 1
# N 2
# 6




# iters 0
# SCVHKHVSHPVCNBKBPVHV

# (3) zetai advent2021$ python 14.py   
# S 2
# C 2
# V 5
# H 4
# K 2
# P 2
# N 1
# B 2
# 4
# (3) zetai advent2021$ python 14pt2.py 
# S 2
# C 2
# V 3
# H 3
# K 2
# P 1
# N 1
# B 2