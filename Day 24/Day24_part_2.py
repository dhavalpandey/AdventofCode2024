import sys
import pyperclip as pc
from functools import cache, lru_cache
from collections import Counter, deque
sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def and_gate(i, j):
    if i == 1 and j == 1:
        return 1
    return 0

def or_gate(i, j):
    if i == 0 and j == 0:
        return 0
    if i == 1 or j == 1:
        return 1
    return 0

def xor_gate(i, j):
    if i != j:
        return 1
    return 0

def main(file):
    with open(file) as f:
        lines = f.readlines()
    initial = []
    gates = []
    reached = False
    for line in lines:
        if line == "\n":
            reached = True
            continue
        if not reached:
            initial.append(line.strip())
            continue
        else:
            gates.append(line.strip())

    dict = {}
    gates_dict = []

    for i in initial:
        term, val = i.split(':')
        dict[term] = int(val)
    
    for gate in gates:
        g = gate.strip()
        instruction = g[3:7]
        g = g.replace(instruction, ",")
        g = g.replace("->", ",")
        terms = g.split(",")
        terms = [term.strip() for term in terms]
        full = terms.copy()
        full.insert(0, instruction.strip())
        gates_dict.append(tuple(full))
    
    for gate in gates_dict:
        val1 = gate[1]
        val2 = gate[2]
        if val1 not in dict:
            dict[val1] = None
        if val2 not in dict:
            dict[val2] = None
    processed = {}
    later = deque([])
    for gate in gates_dict:
        operation = gate[0]
        val1 = dict[gate[1]]
        val2 = dict[gate[2]]
        if val1 == None or val2 == None:
            later.append(gate)
            continue
        if operation == "AND":
            output = and_gate(val1, val2)
        elif operation == "OR":
            output = or_gate(val1, val2)
        elif operation == "XOR":
            output = xor_gate(val1, val2)
        processed[gate[3]] = output
        dict[gate[3]] = output

    while later:
        gate = later.popleft()
        operation = gate[0]
        val1 = dict[gate[1]]
        val2 = dict[gate[2]]
        if val1 == None or val2 == None:
            later.append(gate)
            continue
        if operation == "AND":
            output = and_gate(val1, val2)
        elif operation == "OR":
            output = or_gate(val1, val2)
        elif operation == "XOR":
            output = xor_gate(val1, val2)
        processed[gate[3]] = output
        dict[gate[3]] = output
    in_order = sorted(set(dict))

    last = in_order[0][0]
    break_point = 0
    r = []
    for i in range(len(in_order)):
        curr = in_order[i][0]
        if i == len(in_order) - 1:
            r.append(in_order[break_point:])
            break
        if curr != last:
            last = curr
            r.append(in_order[break_point:i])
            break_point = i

    for wire in r:
        binary = []
        for w in wire:
            binary.append(dict[w])
        binary = ''.join(str(bit) for bit in binary)
        decimal = int(binary, 2)
        print(decimal)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)