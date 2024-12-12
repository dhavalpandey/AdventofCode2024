import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
from collections import deque
infinity = float("inf")

def printc(ans):
    print(ans)
    pc.copy(ans)

def calculate_perimeter(zone):
    zone_set = set(zone)
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for (i, j) in zone_set:
        for di, dj in directions:
            neighbour = (i + di, j + dj)
            if neighbour not in zone_set:
                perimeter += 1

    return perimeter

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
        perimeter = calculate_perimeter(zone)
        sum += area * perimeter
    printc(sum)
        
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)