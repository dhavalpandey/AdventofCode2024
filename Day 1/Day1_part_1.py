import sys

def main(file):
    left, right = [], []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip().split("   ")
        left_text = int(text[0])
        right_text = int(text[1])

        left.append(left_text)
        right.append(right_text)

    left = sorted(left)
    right = sorted(right)
    
    total_distance = 0
    for i in range(len(left)):
        left_num = left[i]
        right_num = right[i]
        distance = abs(right_num - left_num)
        total_distance += distance

    print(total_distance)

if __name__ == "__main__":
    mode = sys.argv[1]
    inputer_file = ""
    if mode == "test":
        input_file = "test.txt"
    elif mode == "input" or mode == "i":
        input_file = "input.txt"
    else:
        input_file = "test.txt"
    
    main(input_file)