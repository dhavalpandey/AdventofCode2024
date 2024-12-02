def is_safe(arr):
    if len(arr) < 2:
        return True
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)
    if not (increasing or decreasing):
        return False
    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False
    return True

def can_be_made_safe(arr):
    if is_safe(arr):
        return True
    for i in range(len(arr)):
        temp = arr[:i] + arr[i+1:]
        if is_safe(temp):
            return True
    return False

def main(file):
    safe_count = 0
    with open(file) as f:
        for line in f:
            arr = [int(x) for x in line.strip().split()]
            if can_be_made_safe(arr):
                safe_count += 1
    print(safe_count)

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)