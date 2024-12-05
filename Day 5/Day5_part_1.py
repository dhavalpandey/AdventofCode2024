def check_is_valid(update, dict):
        for i in range(len(update)):
            current_element = update[i]
            if dict.get(current_element) is None:
                if i != len(update) - 1:
                    return False
                else: 
                    continue
            before = dict[current_element]
            behind = update[:i]

            for num in behind:
                if num in before:
                    return False
                else:
                    continue
        return True                    


def main(file):
    dict = {}
    all_elements = []

    updates = []
    ended_section1 = False
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip().split("\n")
        if text == ['']:
            ended_section1 = True
        if not ended_section1:
            before, after = list(map(int, text[0].split("|")))
            all_elements.append(before)
            all_elements.append(after)
            if before not in dict:
                dict[before] = [after]
            else:
                dict[before].append(after)
        elif ended_section1 and text != ['']:
            update = list(map(int, text[0].split(',')))
            updates.append(update)
    
    sum = 0
    for update in updates:
        if check_is_valid(update, dict) == True:
            mid_idx = len(update) // 2
            to_add = update[mid_idx]
            sum+=to_add
    print(sum)


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)