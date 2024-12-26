import sys
import pyperclip as pc
from functools import cache, lru_cache
sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def keys_to_pins(keys):
    pins = []
    for key in keys:
        last_row = key[-1]
        key_pin = []

        for i in range(len(last_row)):
            if last_row[i] == "#":
                for j in range(len(key)-1, -1, -1):
                    if key[j][i] != "#":
                        key_pin.append(6-(j+1))
                        break
        pins.append(key_pin)
    return pins

def locks_to_pins(locks):
    pins = []
    for lock in locks:
        first_row = lock[0]
        lock_pin = []

        for i in range(len(first_row)):
            if first_row[i] == "#":
                for j in range(len(lock)):
                    if lock[j][i] != "#":
                        lock_pin.append(j-1)
                        break
        pins.append(lock_pin)
    return pins

def process(key_pin, lock_pin):
    for i in range(len(key_pin)):
        if key_pin[i] + lock_pin[i] > 5:
            return False
    return True

def main(file):
    inputs = []
    with open(file) as f:
        lines = f.read().strip().split("\n")
    prev = 0
    for i in range(len(lines)):
        if lines[i] == "":
            inputs.append(lines[prev:i])
            prev = i + 1
    inputs.append(lines[prev:])

    locks = []
    keys = []
    for input in inputs:
        if input[0] == "#####" and input[-1] == ".....":
            locks.append(input)
        elif input[0] == "....." and input[-1] == "#####":
            keys.append(input)

    key_pins = keys_to_pins(keys)
    lock_pins = locks_to_pins(locks)
    
    key_idx = [i for i in range(len(keys))]
    lock_idx = [i for i in range(len(locks))]

    pairs = []
    for key in key_idx:
        for lock in lock_idx:
            pairs.append((key, lock))

    correct_pairs = 0
    for pair in pairs:
        key, lock = pair
        key_pin = key_pins[key]
        lock_pin = lock_pins[lock]
        correct_pairs += process(key_pin, lock_pin)

    print(correct_pairs)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
