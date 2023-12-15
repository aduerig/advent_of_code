# https://adventofcode.com/2023
import pathlib
import sys

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


def hash_thing(a):
    v = 0
    a = a.strip()
    for char in a:
        v += ord(char)
        v = (v * 17) % 256
    return v


boxes = [[] for _ in range(256)]
with open(data_file) as f:
    for stuff in f.readline().split(','):
        if '-' in stuff:
            label = stuff.replace('-', '')
            h = hash_thing(label)
            the_box = boxes[h]
            print(f'Hashing minus {h}, {label=}')
            
            to_delete = None
            for index, (label_in, _focal) in enumerate(the_box):
                print(f'{label=}, {label_in=}')
                if label_in == label:
                    to_delete = index
                    break
            if to_delete != None:
                print(f'deleting {label}')
                del the_box[to_delete]
        else:
            label, lens = stuff.split('=')
            label = label.strip()
            h = hash_thing(label)
            the_box = boxes[h]
            print(f'Hashing equals {h}, {label=}')

            for index, (label_in, _focal) in enumerate(the_box):
                if label_in == label:
                    the_box[index][1] = lens
                    break
            else:
                the_box.append([label, lens])



total = 0
for index, box in enumerate(boxes, start=1):
    if box:
        print(f'{index} {box}')
    for index2, (_label, focal) in enumerate(box, start=1):
        total += index2 * index * int(focal)

print(total)