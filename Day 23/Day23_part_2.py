import sys
import pyperclip as pc
from functools import cache, lru_cache
from itertools import combinations
sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def gen_sets(all):
    dict = {}
    for couple in all:
        key = couple[0]
        val = couple[1]
        if key in dict:
            dict[key].add(val)
        else:
            dict[key] = set([val])
    return dict

def cleanse(d):
    fin = {}
    for key in d:
        initial = d[key]
        t = set(initial)
        for key2 in d:
            if key2 != key:
                temp_vals = d[key2]
                if key in temp_vals:
                    t.add(key2)
        fin[key] = t
    return fin

def are_connected(d, group):
    for i in range(0, len(group)):
        curr = group[i]
        vals = d[curr]
        for j in range(0, len(group)):
            if j == i: continue
            if group[j] not in vals:
                return False
    return True

def get_largest(d):
    largest = 2
    r = []
    for key in d:
        vals = d[key]
        for i in range(2,len(vals)+1):
            max_len = i+1
            if max_len < largest: continue
            combos = list(map(list, list(combinations(vals, i))))
            for combo in combos:
                if are_connected(d, combo):
                    if max_len > largest:
                        nested_list = [sorted(combo)]
                        largest = max_len
                        nested_list.append(key)
                        new = sorted([item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])])
                        r = new
                    else: continue
    return r

def main(file):
    all = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = tuple(line.strip().split('-'))
        all.append(text)
    d = gen_sets(all)
    d = cleanse(d)
    seq = get_largest(d)
    for el in seq:
        print(el, end=",")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
