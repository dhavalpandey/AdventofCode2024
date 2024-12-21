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

CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

from collections import deque

def gen_path(points, grid, consider=None, start=None):
    start = points['S']
    end = points['E']
    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for cell in CELLS:
            neighbor = (current[0] + cell[0], current[1] + cell[1])
            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] != '#' and
                neighbor not in visited):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent.get(current)
        if current is None:
            return []
    path.append(start)
    path.reverse()
    return path

def main(file):
    grid = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        grid.append(list(text))

    points = {}
    for i in range(len(grid)):
        row = list(grid[i])
        for j in range(len(row)):
            if row[j] == "S" or row[j] == "E":
                points[row[j]] = (i, j)
                
    original = gen_path(points, grid)

    consider = []
    for i in range(1, len(grid)-1):
        row = list(grid[i])
        for j in range(1, len(row)-1):
            if grid[i][j] != "#":
                continue
            count = 0
            neighbour_in_path = False
            for cell in CELLS:
                neighbor = (i+cell[0], j+cell[1])
                if grid[neighbor[0]][neighbor[1]] == "." or grid[neighbor[0]][neighbor[1]] == "E":
                    if neighbor in original:
                        neighbour_in_path = True
                    count += 1
                if count >= 2 and neighbour_in_path:
                    consider.append((i, j))
                    break
                else: continue

    def find_first_and_last(subarray, big_array):
        sub_set = set(subarray)
        first_indices = {}
        last_indices = {}
        
        for index, element in enumerate(big_array):
            if element in sub_set:
                if element not in first_indices:
                    first_indices[element] = index
                last_indices[element] = index
        
        if not first_indices:
            return None, None
        
        first_element = min(first_indices, key=first_indices.get)
        last_element = max(last_indices, key=last_indices.get)
        
        return first_element, last_element
    
    count = 0
    for c in consider:
        path_n = []
        for cell in CELLS:
            if (c[0]+cell[0], c[1]+cell[1]) in original:
                path_n.append((c[0]+cell[0], c[1]+cell[1]))
        skip_from, skip_to = find_first_and_last(path_n, original)
        skip_from_index = original.index(skip_from)+1
        skip_to_index = original.index(skip_to)-1
        diff = skip_to_index - skip_from_index
        if diff >= 100:
            count += 1

    print(count+2)
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)