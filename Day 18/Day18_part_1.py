import sys
import pyperclip as pc
import heapq

sys.setrecursionlimit(10**6)
infinity = float("inf")
original_print = print

def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)

print = printc

def main(file):
    grid = []
    cords = []
    count = 0
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        if not text:
            continue
        cord = list(map(int, text.split(',')))
        x, y = cord

        if count <= 1024:
            cords.append((x, y))
            count += 1
        else:
            continue

    max_x = max(x for x, y in cords) + 1
    max_y = max(y for x, y in cords) + 1

    grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

    for cord in cords:
        x, y = cord
        if 0 <= x < max_x and 0 <= y < max_y:
            grid[y][x] = 1

    start = (0, 0)
    end = (70, 70)

    def dijkstra(grid, start, end):
        rows, cols = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap, (0, start))
        visited = set()
        distances = {start: 0}
        came_from = {}
        
        while heap:
            current_dist, current = heapq.heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            
            if current == end:
                break
            
            x, y = current
            neighbors = []
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 0:
                    neighbors.append((nx, ny))
            
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                new_dist = current_dist + 1
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
                    came_from[neighbor] = current

        path = []
        current = end
        while current != start:
            path.append(current)
            current = came_from.get(current)
            if current is None:
                return None 
        path.append(start)
        path.reverse()
        return path
    
    path = dijkstra(grid, start, end)
    
    if path:
        print(len(path)-1)
    else:
        print(f"No path")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)