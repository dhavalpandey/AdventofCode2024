def main(file):
    with open(file) as f:
        lines = f.readlines()
        grid = []
        for line in lines:
            grid.append(str(line.strip()))

        count = 0
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if i+3<len(grid[j]) and grid[j][i] == "X" and grid[j][i+1] == "M" and grid[j][i+2] == "A" and grid[j][i+3] == "S":
                    count += 1
                if i-3>0 and grid[j][i-3] == "X" and grid[j][i-2] == "M" and grid[j][i-1] == "A" and grid[j][i] == "S":
                    count += 1
                if j+3 < len(grid) and grid[j][i] == "X" and grid[j+1][i] == "M" and grid[j+2][i] == "A" and grid[j+3][i] == "S":
                    count += 1
                if j+3 < len(grid) and i+3<len(grid[j]) and grid[j][i] == "X" and grid[j+1][i+1] == "M" and grid[j+2][i+2] == "A" and grid[j+3][i+3] == "S":
                    count += 1
        print(count)

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main('test.txt')