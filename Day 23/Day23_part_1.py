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

def are_connected(d, pair):
    el1 = pair[0]
    el2 = pair[1]
    if el2 in d[el1] and el1 in d[el2]:
        return True
    return False

def get_triplets(d):
    triplets = set()
    for key in d:
        vals = d[key]
        pairs = list(combinations(vals, 2))
        for pair in pairs:
            if are_connected(d, pair):
                triplets.add(tuple(sorted((key, pair[0], pair[1]))))
    return list(triplets)

def main(file):
    all = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = tuple(line.strip().split('-'))
        all.append(text)
    d = gen_sets(all)
    d = cleanse(d)
    triplets = get_triplets(d)
    count = 0
    for tri in triplets:
        for el in tri:
            if el.startswith('t'): 
                count += 1
                break
    print(count)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
