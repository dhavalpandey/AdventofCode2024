import sys
import pyperclip as pc
from functools import cache, lru_cache
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print

def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)

print = printc

CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def mix(x, y):
    return x ^ y

def prune(x):
    return x % 16777216

@cache
def prices(x):
    ans = [x]
    for _ in range(2000):
        x = prune(mix(x, 64 * x))
        x = prune(mix(x, x // 32))
        x = prune(mix(x, x * 2048))
        ans.append(x)
    return ans

def changes(P):
    return [P[i + 1] - P[i] for i in range(len(P) - 1)]

def get_score(P, C):
    ANS = {}
    for i in range(len(C) - 3):
        pattern = (C[i], C[i + 1], C[i + 2], C[i + 3])
        if pattern not in ANS:
            ANS[pattern] = P[i + 4]
    return ANS

def main(file):
    nums = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        if text:
            nums.append(int(text))

    SCORE = defaultdict(int)

    for num in nums:
        P = prices(num)
        P = [x % 10 for x in P]
        C = changes(P)
        S = get_score(P, C)
        for k, v in S.items():
            SCORE[k] += v

    if not SCORE:
        print(0)

    max_bananas = max(SCORE.values())
    best_sequence = [seq for seq, bananas in SCORE.items() if bananas == max_bananas]

    print(max_bananas)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)