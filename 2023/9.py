# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

seqs = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            seqs.append(list(reversed(list(map(int, line.split())))))


total = 0
for b, seq in enumerate(seqs):
    stored = [seq]
    while any([x != 0 for x in stored[-1]]):
        new = []
        last = stored[-1]
        for index in range(1, len(last)):
            new.append(last[index] - last[index - 1])
        stored.append(new)

    for index in reversed(range(len(stored) - 1)):
        seq = stored[index]
        next_seq = stored[index + 1]
        seq.append(seq[-1] + next_seq[-1])
    
    total += stored[0][-1]



    


print(total)