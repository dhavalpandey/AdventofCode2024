import sys
sys.setrecursionlimit(10000)

def solve(grid, start_pos):
    R = len(grid)
    C = len(grid[0])
    p1 = 0
    p2 = 0
    sr, sc = start_pos

    for o_r in range(R):
        for o_c in range(C):
            r, c = sr, sc
            d = 0 
            SEEN = set()
            SEEN_RC = set()
            while True:
                if (r, c, d) in SEEN:
                    p2 += 1
                    break
                SEEN.add((r, c, d))
                SEEN_RC.add((r, c))
                dr, dc = [(-1,0), (0,1), (1,0), (0,-1)][d]
                rr = r + dr
                cc = c + dc
                if not (0 <= rr < R and 0 <= cc < C):
                    if grid[o_r][o_c]=='#':
                        p1 = len(SEEN_RC)
                    break
                if grid[rr][cc]=='#' or (rr == o_r and cc == o_c):
                    d = (d + 1) % 4
                else:
                    r = rr
                    c = cc
    print(p2)

def main(file):
    grid = []
    start_pos = (0, 0)
    with open(file) as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        text = list(line.strip())
        if '^' in text:
            start_pos = (idx, text.index('^'))
        grid.append(text)
    solve(grid, start_pos)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)