import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
infinity = float("inf")

original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

def main(file):
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        print(text)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
