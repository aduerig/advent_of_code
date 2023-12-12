# https://adventofcode.com/2023
import sys
import pathlib
import random
import time

# import numpy as np
# from numba import njit

filepath = pathlib.Path(__file__)
sys.path.append(str(filepath.parent.parent))
from helpers import * 

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



x, y, z = ord('i') - ord('a'), ord('o') - ord('a'), ord('l') - ord('a') 



def first_req(password):
    for i in range(len(password) - 2):
        if password[i] + 1 == password[i+1] and password[i] + 2 == password[i+2]:
            return True
    return False


def illegal_char(character):
    return character == x or character == y or character == z


def second_req(password):
    for i in password:
        if illegal_char(i):
            return False
    return True

def third_req(password):
    last = None
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            if last is None:
                last = password[i]
            elif last != password[i]:
                return True
    return False

def is_valid(password):
    return first_req(password) and third_req(password)

def increment_letter(l):
    return (l + 1) % 26, (l + 1) // 26


def increment(s):
    index = len(s) - 1
    while True:
        new_char, should_carry = increment_letter(s[index])
        while illegal_char(new_char):
            new_char, should_carry = increment_letter(new_char)
        if index == 0:
            print(f'Got index 0 to {new_char}')
        s[index] = new_char
        if not should_carry:
            return
        index -= 1
        if index < 0:
            print('bad news')
    
def get_pass(password):
    start_time = time.time()
    iters = 0

    while not second_req(password):
        increment(password)
    
    while not is_valid(password):
        if random.random() < .0000001:
            print_green(f'Current password is: {readable(password)}, iters: {iters:,}, iters per second {iters / (time.time() - start_time):,.0f}, {first_req(password)=}, {second_req(password)=}, {third_req(password)=}')
        increment(password)
        iters += 1

def readable(password):
    return ''.join([chr(ord('a') + x) for x in password])

def val(s):
    return (ord(s) - ord('a'))

# hepxcrrr isn't right
with open(data_file) as f:
    for line in f.readlines():
        password = [val(x) for x in line.strip()]
        increment(password)
        get_pass(password)
        print(readable(password))