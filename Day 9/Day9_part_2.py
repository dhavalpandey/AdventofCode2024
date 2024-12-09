from collections import deque

def gen_seq(layouts, freespaces):
    string = ""
    curr_id = 0
    for i in range(len(layouts)):
        repeats = layouts[i]
        string += str(curr_id) * repeats
        curr_id += 1
        if i < len(freespaces):
            string += "." * freespaces[i]
    return string

def fix(sequence):
    A = deque([])
    SPACE = deque([])
    FINAL = []
    pos = 0
    file_id = 0

    for c in sequence:
        if c != '.':
            A.append((pos, 1, int(c)))
            FINAL.append(int(c))
        else:
            SPACE.append((pos, 1))
            FINAL.append(None)
        pos += 1

    # Sort A in decreasing order of file_id to move higher IDs first
    sorted_A = sorted(A, key=lambda x: -x[2])

    for (file_pos, sz, file_id) in sorted_A:
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < file_pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[file_pos + i] == file_id, f'Expected {file_id} at position {file_pos + i}, found {FINAL[file_pos + i]}'
                    FINAL[file_pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break

    compacted_seq = "".join([str(c) if c is not None else '.' for c in FINAL])
    return compacted_seq

def calc(sequence):
    total = 0
    for idx, c in enumerate(sequence):
        if c != ".":
            total += idx * int(c)
    return total

def main(file):
    layouts = []
    freespaces = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        if not text:
            continue

        numbers = list(map(int, list(text)))
        for i in range(0, len(numbers)-1, 2):
            layouts.append(numbers[i])
            freespaces.append(numbers[i+1])
        if len(numbers) % 2 != 0:
            layouts.append(numbers[-1])
    
    initial_sequence = gen_seq(layouts, freespaces)    
    compacted_sequence = fix(initial_sequence)
    checksum = calc(compacted_sequence)
    print(checksum)

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)