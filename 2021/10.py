data = []

with open('10.data') as f:
    for x in f.readlines():
        new_level = x.strip()
        data.append(new_level)

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}



opens = set(['(', '[', '{', '<'])
to_close = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}



incomplete = []
for seq in data:
    stack = []
    no = False
    for index, char in enumerate(seq):
        if char in opens:
            stack.append(to_close[char])
        else:
            if len(stack) == 0 or stack[-1] != char:
                no = True
                break
            stack.pop()
    if not no:
        incomplete.append(seq)



scores = []
for seq in incomplete:
    stack = []
    for index, char in enumerate(seq):
        if char in opens:
            stack.append(to_close[char])
        else:
            stack.pop()
    
    print(seq)
    total = 0 
    while stack:
        award = stack.pop()
        total *= 5
        total += points[award]
    scores.append(total)

    print(total, seq)

scores.sort()
print(scores)
print(scores[len(scores) // 2])
