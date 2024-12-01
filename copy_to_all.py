import sys
import pathlib

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import *


sub_directory = '2024' # change to None if not needed
for i in range(1, 26):
    if sub_directory:
        the_path = pathlib.Path(__file__).parent.joinpath(sub_directory)
        if not the_path.exists():
            print_red(f'ERROR: {the_path} does not exist')
            exit()
        prepath = str(the_path) + '/'

    cmds = [
        f'cp base_input.dat {prepath}{i}.dat',
        f'cp base_file.py {prepath}{i}.py',
    ]
    to_print = "\n".join(cmds)
    input(yellow(f'WARNING: about to execute:\n{to_print}\n'))
    [os.system(cmd) for cmd in cmds]