import re

def main(file):
    total = 0
    state = True
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
    with open(file) as f:
        for line in f:
            for match in pattern.finditer(line):
                instr = match.group()
                if instr == 'do()':
                    state = True
                elif instr == "don't()":
                    state = False
                else:
                    a, b = match.groups()
                    if a and b and state:
                        total += int(a) * int(b)
    print(total)

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)