import sys
from functools import lru_cache
import pyperclip as pc
sys.setrecursionlimit(10**6)
infinity = float("inf")

def printc(ans):
    print(ans)
    pc.copy(ans)

def main(file):
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        return text


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
    printc(ans)
