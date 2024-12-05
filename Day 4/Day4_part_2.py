def solve(grid):
    found = 0
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            if grid[row][col] == "A":
                tl = grid[row-1][col-1]
                tr = grid[row-1][col+1]
                bl = grid[row+1][col-1]
                br = grid[row+1][col+1]
                cells = [tl, tr, bl, br]

                countM = cells.count("M")
                countS = cells.count("S")
                if countM == 2 and countS == 2:
                    if tl != br and tr != bl:
                        found += 1
    print(found)


def main(file):
    grid = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip().split("\n")
        row = list(text[0])
        grid.append(row)
    
    solve(grid)


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)