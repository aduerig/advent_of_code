with open('19.data') as f:
    data_hex = f.readline().strip()
    data = []
    for i in data_hex:
        for j in lmao[i]:
            data.append(j)
    data = list(map(lambda x: int(x), data))