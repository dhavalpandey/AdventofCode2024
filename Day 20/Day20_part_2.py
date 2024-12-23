import sys
import pyperclip as pc
from tqdm import tqdm

sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print

def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)

print = printc

CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main(file):
    with open(file) as fin:
        grid = [list(line) for line in fin.read().strip().split("\n")]
    
    N = len(grid)
    
    def in_grid(i, j):
        return 0 <= i < N and 0 <= j < N
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "S":
                si, sj = i, j
            elif grid[i][j] == "E":
                ei, ej = i, j
    
    path = [(si, sj)]
    while path[-1] != (ei, ej):
        i, j = path[-1]
        for di, dj in CELLS:
            ii, jj = i + di, j + dj
            if not in_grid(ii, jj):
                continue
            if len(path) > 1 and (ii, jj) == path[-2]:
                continue
            if grid[ii][jj] == "#":
                continue
            path.append((ii, jj))
            break
    
    og = len(path) - 1
    times = {}
    for t, coord in enumerate(path):
        times[coord] = og - t
    
    max_len = 20
    saved = {}
    for t, coord in enumerate(tqdm(path, ncols=80)):
        i, j = coord
        for ii in range(i - max_len, i + max_len + 1):
            for jj in range(j - max_len, j + max_len + 1):
                time_used = abs(ii - i) + abs(jj - j)
                if not in_grid(ii, jj) or time_used > max_len or grid[ii][jj] == "#":
                    continue
                rem_t = times.get((ii, jj), 0)
                saved[(i, j, ii, jj)] = og - (t + rem_t + time_used)
    
    ans = 0
    for v in saved.values():
        if v >= 100:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)