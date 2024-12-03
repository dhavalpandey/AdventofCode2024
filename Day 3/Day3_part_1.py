import re

def main(file):
    sum = 0
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        for match in matches:
            a, b = map(int, match[4:-1].split(","))
            sum += a * b
        
    print(sum)


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)