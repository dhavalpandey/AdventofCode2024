import sys
import pyperclip as pc
from functools import cache
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
    dict = lines[0].strip().split(', ')
    words = []
    for i in range(1, len(lines)):
        wrd = lines[i].strip()
        if wrd != "":
            words.append(wrd)

    max_len = int(max(len(d) for d in dict))
    @cache
    def process(word):
        if word == "": return 1
        count = 0
        for i in range(min(len(word), max_len) + 1):
            if word[:i] in dict:
                count += process(word[i:])
        return count
    
    ways = 0         
    for word in words:
        ways += process(word)
    print(ways)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
