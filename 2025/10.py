# https://adventofcode.com/2023
import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}



machines = []
with open(data_file) as f:
    for line in f.readlines():

        line = line.strip()
        other, jolts = line.split('{')
        jolts = list(map(int, jolts.strip().strip('}').split(',')))

        indic, other = other.split(']')
        indic = list(indic.strip().strip('['))

        all_buttons = []
        for b in other.strip().split():
            b = b.strip('()')
            whole_button = list(map(int, b.split(',')))
            all_buttons.append(whole_button)

        whole_machine = (indic, all_buttons, jolts)
        machines.append(whole_machine)


for indic, all_buttons, jolts in machines:
    print(f'indic: {indic}, all_buttons: {all_buttons}, jolts: {jolts}')