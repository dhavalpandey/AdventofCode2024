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

def gen_target(grid, target, curr_idx, seq=""):
    if target == "":
        return ""
    
    next = target[0]
    next_idx = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == str(next):
                next_idx = (i, j)
                break
    i_change = next_idx[0] - curr_idx[0]
    j_change = next_idx[1] - curr_idx[1]

    translation = ""
    if i_change > 0:
        translation += 'v' * abs(i_change)
    elif i_change < 0:
        translation += '^' * abs(i_change)
    
    if j_change > 0:
        translation += '>' * abs(j_change)
    elif j_change < 0:
        translation += '<' * abs(j_change)
    
    translation += 'A'
    seq += translation
    return translation + gen_target(grid, target[1:], next_idx, seq)
    
def main(file):
    grid = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip('\n')
        n = list(text.strip())
        if text[0] == " ":
            n.insert(0, '.')
        grid.append(n)

    start_idx = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'A':
                start_idx = (i, j)
                break
    codes = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        codes.append(text)
    
    sum = 0
    for target in codes:
        target_seq = str(gen_target(grid, target, start_idx))

        admin_keypad = ['.^A', '<v>']
        admin_seq = str(gen_target(admin_keypad, target_seq, (0, 2)))
        master_seq = gen_target(admin_keypad, admin_seq, (0, 2))

        shortest_seq = len(master_seq)
        numeric_part = int(''.join(filter(str.isdigit, target)))
        multiple = shortest_seq * numeric_part
        sum += multiple
    print(sum)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
