def is_mas_sequence(chars):
    return chars == ['M', 'A', 'S'] or chars == ['S', 'A', 'M']

def count_xmas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Diagonal from top-left to bottom-right
            diag1 = [grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]
            # Diagonal from top-right to bottom-left
            diag2 = [grid[i-1][j+1], grid[i][j], grid[i+1][j-1]]

            if is_mas_sequence(diag1) and is_mas_sequence(diag2):
                count += 1
    return count

def main(file):
    grid = [line.strip() for line in open(file)]
    print(count_xmas(grid))

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)