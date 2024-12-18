import sys
import pyperclip as pc
import re
sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

def main(file):
    program = []
    with open(file) as f:
        data = f.read()
    a, b, c, *program = list(map(int, re.findall(r"\d+", data)))

    def computer(a: int, b: int = 0, c: int = 0):
        def combo(val):
            if val <= 3: return val
            reg_map = {4: a, 5: b, 6: c}
            return reg_map[val]
        
        output = []
        ip = 0
        while ip < len(program):
            opcode = program[ip]
            operand = program[ip + 1]
            match opcode:
                case 0:
                    a = a >> combo(operand)
                case 1:
                    b = b ^ operand
                case 2:
                    b = combo(operand) % 8
                case 3:
                    if a != 0:
                        ip = operand
                        continue
                case 4:
                    b = b ^ c
                case 5:
                    output.append(combo(operand) % 8)
                case 6:
                    b = a >> combo(operand)
                case 7:
                    c = a >> combo(operand)
            ip += 2
        return output

    candidates = [0]
    for l in range(len(program)):
        next_candidates = []
        for val in candidates:
            for i in range(8):
                target = (val << 3) + i
                if computer(target) == program[-l-1:]:
                    next_candidates.append(target)
        candidates = next_candidates

    print(candidates[0])
    
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)