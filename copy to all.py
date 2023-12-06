from helpers import *

for i in range(1, 26):
    input(yellow(f'WARNING: overwriting from {i} to 25'))
    os.system('cp base_input.dat ' + str(i) + '.dat')
    os.system('cp base_file.py ' + str(i) + '.py')