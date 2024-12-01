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

    score = 0
    for num in left:
        occurances = right.count(num)
        multiply = num * occurances
        score += multiply

    print(score)


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