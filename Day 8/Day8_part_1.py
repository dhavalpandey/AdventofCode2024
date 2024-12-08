def generate_antidotes(grid, cords):
    anti_dote_cords = []
    max_x = len(grid[0])-1
    lowest_y = (len(grid)-1)*-1
    def generate_pairs(cords):
        pairs = []
        for i in range(len(cords)):
            for j in range(i+1, len(cords)):
                pairs.append((cords[i], cords[j]))
        return pairs
    
    pairs = generate_pairs(cords)
    for pair in pairs:
        cord1 = pair[0]
        cord2 = pair[1]

        transformatation_from_cord1 = (2*(cord2[0] - cord1[0]), 2*(cord2[1] - cord1[1]))
        transformatation_from_cord2 = (-1*(transformatation_from_cord1[0]), -1*(transformatation_from_cord1[1]))
        new1 = (cord1[0] + transformatation_from_cord1[0], cord1[1] + transformatation_from_cord1[1])
        new2 = (cord2[0] + transformatation_from_cord2[0], cord2[1] + transformatation_from_cord2[1])
        if not new1[0] > max_x and not new1[0] < 0 and not new1[1] > 0 and not new1[1] < lowest_y:
            anti_dote_cords.append(new1)
        
        if not new2[0] > max_x and not new2[0] < 0 and not new2[1] > 0 and not new2[1] < lowest_y:
            anti_dote_cords.append(new2)
    return anti_dote_cords

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
    seen = []
    for signal in unique_signals:
        seen += generate_antidotes(grid, cords[signal])
        
    print(len(list(set(seen))))


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)