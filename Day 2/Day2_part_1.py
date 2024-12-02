def main(file):
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)