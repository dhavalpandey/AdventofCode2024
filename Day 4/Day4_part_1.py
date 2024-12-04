def count_xmas(grid, word="XMAS"):
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word_len = len(word)
    
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if all(
                    0 <= i + dx * k < rows and
                    0 <= j + dy * k < cols and
                    grid[i + dx * k][j + dy * k] == word[k]
                    for k in range(word_len)
                ):
                    count += 1
    return count

def main(file):
    grid = []
    with open(file) as f:
        for line in f:
            grid.append(line.strip())
    print(count_xmas(grid))

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)