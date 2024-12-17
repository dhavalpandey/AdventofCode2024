import sys
import heapq
import pyperclip as pc
original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up, right, down, left

def main(file):
    ans = 0
    D = open(file).read().strip()

    G = D.split('\n')
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]

    for r in range(R):
        for c in range(C):
            if G[r][c] == 'S':
                sr, sc = r, c
            if G[r][c] == 'E':
                er, ec = r, c

    Q = []
    SEEN = set()
    heapq.heappush(Q, (0, sr, sc, 1))  # (score, row, col, direction)
    DIST = {}
    best = None

    while Q:
        d, r, c, dir = heapq.heappop(Q)
        if (r, c, dir) not in DIST:
            DIST[(r, c, dir)] = d
        if r == er and c == ec and best is None:
            best = d
            break  # Found the best score
        if (r, c, dir) in SEEN:
            continue
        SEEN.add((r, c, dir))
        
        # Move Forward
        dr, dc = DIRS[dir]
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#':
            heapq.heappush(Q, (d + 1, rr, cc, dir))
        
        # Turn Clockwise
        heapq.heappush(Q, (d + 1000, r, c, (dir + 1) % 4))
        
        # Turn Counterclockwise
        heapq.heappush(Q, (d + 1000, r, c, (dir + 3) % 4))

    print(best)

if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
    main(infile)