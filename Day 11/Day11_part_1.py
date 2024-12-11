import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
infinity = float("inf")

def printc(ans):
    print(ans)
    pc.copy(ans)

def gen_seq(text):
    nums = list(map(int, text.split(" ")))
    arr = []
    for num in nums:
        if num == 0:
            arr.append(1)
        elif len(str(num))%2 == 0:
            txt = str(num)
            left = int(txt[:len(txt)//2])
            right = int(txt[len(txt)//2:])
            arr.append(left)
            arr.append(right)
        else:
            new = 2024 * num
            arr.append(new)
    return arr

def main(file):
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
    blinks_max = 25
    curr = 0
    arr = [text]
    while curr < blinks_max:
        r = " ".join(map(str, gen_seq(arr[-1])))
        arr.append(r)
        curr += 1
    
    return_arr = len(arr[-1].split(" "))
    print(return_arr)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
