import sys

def main(file):
    solution = ""
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        pass
    
    print(solution)


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