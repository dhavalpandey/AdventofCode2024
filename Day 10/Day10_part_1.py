import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
infinity = float("inf")

def find_paths(grid, i, j):
    ans = 0
    visited = set()
    stack = [(i, j)]

    neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_i = len(grid)
    max_j = len(grid[0])

    # Dfs alg
    while len(stack) > 0:
        curi, curj = stack.pop()
        now = grid[curi][curj]

        if (curi, curj) in visited:
            continue
        visited.add((curi, curj))

        if now == 9:
            ans += 1
            continue

        for ni, nj in neighbours:
            new_i = curi + ni
            new_j = curj + nj
            if new_i >= 0 and new_i < max_i and new_j >= 0 and new_j < max_j:
                item = grid[new_i][new_j]

                if item != now + 1:
                    continue
                stack.append((new_i, new_j))
    return ans


def printc(ans):
    print(ans)
    pc.copy(ans)

def main(file):
    grid = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = list(line.strip())
        grid.append(text)
    
    grid = list(map(lambda x: list(map(int, x)), grid))
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    ans = 0
    for head in trailheads:
        sols = find_paths(grid, head[0], head[1])
        ans += sols
    return ans

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
    printc(ans)
