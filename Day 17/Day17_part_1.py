import sys
import pyperclip as pc
import math
sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

def convert_to_pairs(lst):
    pairs = []
    for i in range(0, len(lst), 2):
        pairs.append((lst[i], lst[i+1]))
    return pairs

def combo_operand(operand, registers):
    match operand:
        case 0:
            return operand
        case 1:
            return operand
        case 2:
            return operand
        case 3:
            return operand
        case 4:
            return registers[0]
        case 5:
            return registers[1]
        case 6:
            return registers[2]
        
def main(file):
    br = False
    registers = []
    instructions = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        if not text:
            br = True
            continue

        if not br:
            num = int(text[11:])
            registers.append(num)
        else:
            lst = list(map(int, text[9:].split(",")))
            instructions = lst
            break

    instructions = convert_to_pairs(instructions)
    output = []
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        opcode = instruction[0]
        operand = instruction[1]
        combo = combo_operand(operand, registers)
        match opcode:
            case 0:
                numerator = registers[0]
                denominator = 2**combo
                div = math.trunc(numerator/denominator)
                registers[0] = div
                i += 1
            case 1:
                b = registers[1]
                xor = b ^ operand
                registers[1] = xor
                i += 1
            case 2:
                final = combo % 8
                registers[1] = final
                i += 1
            case 3:
                if registers[0] != 0:
                    i = operand
                else:
                    i += 1
            case 4:
                b = registers[1]
                c = registers[2]
                xor = b ^ c
                registers[1] = xor
                i += 1
            case 5:
                output.append(combo % 8)
                i += 1
            case 6:
                numerator = registers[0]
                denominator = 2**combo
                div = math.trunc(numerator/denominator)
                registers[1] = div
                i += 1
            case 7:
                numerator = registers[0]
                denominator = 2**combo
                div = math.trunc(numerator/denominator)
                registers[2] = div
                i += 1
    print(','.join(str(x) for x in output))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
