import sys
sys.setrecursionlimit(10000)

def solve(grid, curr, direction, cords_set=set()):
    cords_set.add(curr)
    if direction == "^" and curr[0] - 1 >= 0:
        if grid[curr[0] - 1][curr[1]] == "#":
            direction = ">"
        else:
            curr = (curr[0] - 1, curr[1])
    elif direction == "v" and curr[0] + 1 < len(grid):   
        if grid[curr[0] + 1][curr[1]] == "#":
            direction = "<"
        else:
            curr = (curr[0] + 1, curr[1])
    elif direction == ">" and curr[1] + 1 < len(grid[curr[0]]):   
        if grid[curr[0]][curr[1] + 1] == "#":
            direction = "v"
        else:
            curr = (curr[0], curr[1] + 1)
    elif direction == "<" and curr[1] - 1 >= 0:  
        if grid[curr[0]][curr[1] - 1] == "#":
            direction = "^"
        else:
            curr = (curr[0], curr[1] - 1) 
    else:
        print(len(list(cords_set)))
        return False
    solve(grid, curr, direction, cords_set)
            

def main(file):
    grid = []
    start_pos = (0, 0)
    with open(file) as f:
        lines = f.readlines()
    for line in lines:        
        text = list(line.strip().split("\n")[0])
        # find the position of element in text 
        if "^" in text:
            start_pos = (len(grid), text.index("^"))
        elif "v" in text:   
            start_pos = (len(grid), text.index("v"))
        elif ">" in text:   
            start_pos = (len(grid), text.index(">"))
        elif "<" in text:   
            start_pos = (len(grid), text.index("<"))
        grid.append(text)
    
    solve(grid, start_pos, grid[start_pos[0]][start_pos[1]])
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)