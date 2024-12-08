from fractions import Fraction
def generate_antidotes(grid, cords):
    def generate_pairs(cords):
        pairs = []
        for i in range(len(cords)):
            for j in range(i+1, len(cords)):
                pairs.append((cords[i], cords[j]))
        return pairs
    
    anti_dote_cords = set()
    max_x = len(grid[0])-1
    lowest_y = (len(grid)-1)*-1
    pairs = generate_pairs(cords)
    for pair in pairs:
        cord1 = pair[0]
        cord2 = pair[1]
        x_change = cord2[0] - cord1[0]
        y_change = cord2[1] - cord1[1]
        frac = Fraction(x_change, y_change)
        transformation_from_cord2 = (frac.numerator, frac.denominator)
        transformation_from_cord1 = (-frac.numerator, -frac.denominator)
        
        curr_x = cord1[0]
        curr_y = cord1[1]

        while curr_x >= 0 and curr_x <= max_x and curr_y >= lowest_y and curr_y <= 0:
            new1 = (curr_x + transformation_from_cord1[0], curr_y + transformation_from_cord1[1])
            curr_x = new1[0]
            curr_y = new1[1]
            if curr_x >= 0 and curr_x <= max_x and curr_y >= lowest_y and curr_y <= 0:
                anti_dote_cords.add(new1)

        curr_x1 = cord2[0]
        curr_y1 = cord2[1]
        while curr_x1 >= 0 and curr_x1 <= max_x and curr_y1 >= lowest_y and curr_y1 <= 0:
            new2 = (curr_x1 + transformation_from_cord2[0], curr_y1 + transformation_from_cord2[1])
            curr_x1 = new2[0]
            curr_y1 = new2[1]

            if curr_x1 >= 0 and curr_x1 <= max_x and curr_y1 >= lowest_y and curr_y1 <= 0:
                anti_dote_cords.add(new2)

    return list(anti_dote_cords)

def main(file):
    grid = []
    unique_signals = {}
    cords = {}
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        text = list(lines[i].strip().split("\n")[0])
        grid.append(text)
        for char in text:
            if char != "." and unique_signals.get(char) is not None:
                unique_signals[char] += 1
                cords[char].append((int(text.index(char)), -i))
            elif char != ".":
                unique_signals[char] = 1
                cords[char] = [(int(text.index(char)), -i)]
    sum = []
    for signal in unique_signals:
        sum += generate_antidotes(grid, cords[signal])
    print(len(set(sum)))

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)