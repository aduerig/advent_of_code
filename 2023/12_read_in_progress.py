

filled = {}
total = 0
with open('12_in_progress.txt') as f:
    for line in f.read().splitlines():
        if line.startswith('Total'):
            first, after = line.split(':')

            num = int(first.split()[-1])
            amt = int(after.strip())

            filled[num] = amt


for i in range(1, 1001):
    if i not in filled:
        print(f'Missing {i}')
print(sum(filled.values()))