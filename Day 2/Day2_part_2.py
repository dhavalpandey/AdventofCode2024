import sys

def check_is_safe(arr):
    is_safe = True
    increasing = False
    if arr[1] - arr[0] > 0:
        increasing = True
    for i in range(len(arr)-1):
        curr = arr[i]
        next = arr[i+1]
        diff = abs(next - curr)
        if increasing:
            if next - curr < 0:
                is_safe = False
                break
        else:
            if next - curr > 0:
                is_safe = False
                break
        if diff > 3 or diff == 0:
            is_safe = False
            break

    return is_safe


def main(file):
    safe_count = 0
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip().split(" ")
        arr = [int(str) for str in text]
        is_safe = check_is_safe(arr)

        if not is_safe:
            for i in range(len(arr)):
                temp_arr = arr.copy()
                temp_arr.pop(i)
                if check_is_safe(temp_arr):
                    is_safe = True
                    break
        
        if is_safe:
            safe_count += 1

    print(safe_count)

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