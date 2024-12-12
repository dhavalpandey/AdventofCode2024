import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
from collections import deque
infinity = float("inf")

def printc(ans):
    print(ans)
    pc.copy(ans)

def calculate_sides(zone):
    side_count = 0
    region = set(zone)
    edges = {}
    for r, c in region:
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if (nr, nc) in region: continue
            er = (r + nr) / 2
            ec = (c + nc) / 2
            edges[(er, ec)] = (er-r, ec-c)
    seen = set()
    for edge, direction in edges.items():
        if edge in seen: continue
        seen.add(edge)
        side_count += 1
        er, ec = edge
        if er % 1 == 0:
            for dr in [-1, 1]:
                cr = er + dr
                while edges.get((cr, ec)) == direction:
                    seen.add((cr, ec))
                    cr += dr
        else:
            for dc in [-1, 1]:
                cc = ec + dc
                while edges.get((er, cc)) == direction:
                    seen.add((er, cc))
                    cc += dc
    return side_count

def get_cords(char, grid):
    char_cords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                char_cords.append((i, j))
    return char_cords

seen = set()
def gen_zone_sequence(cord, grid):
    i, j = cord
    letter = grid[i][j]
    seen.add(cord)

    cells = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    zone = [cord]

    # BFS
    max_i = len(grid)
    max_j = len(grid[0])
    queue = deque([cord])

    while queue:
        curi, curj = queue.popleft()
        now = grid[curi][curj]
        if now == letter:
            seen.add((curi, curj))
            for ni, nj in cells:
                new_i = curi + ni
                new_j = curj + nj

                if new_i >= 0 and new_i < max_i and new_j >= 0 and new_j < max_j and (new_i, new_j) not in seen and (new_i, new_j) not in zone:
                    item = grid[new_i][new_j]
                    if item == letter:
                        zone.append((new_i, new_j))
                        queue.append((new_i, new_j))
    return zone

def main(file):
    grid = []
    unique = set()
    dict = {}
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        grid.append(text)
        for char in text:
            unique.add(char)

    lst = list(unique)
    for char in lst:
        dict[char] = get_cords(char, grid)

    sequences = []
    for char in lst:
        cords = dict[char]
        for cord in cords:
            if cord not in seen:
                seq = gen_zone_sequence(cord, grid)
                sequences.append(seq)
            else:
                continue
    sum = 0
    for zone in sequences:
        area = len(zone)
        sides = calculate_sides(zone)
        sum += area * sides
    printc(sum)
        
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)