import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
infinity = float("inf")

from functools import lru_cache

def printc(ans):
    print(ans)
    pc.copy(ans)

@lru_cache(maxsize=None)
def count_stones(num, blinks_left):
    if blinks_left == 0:
        return 1 
    
    if num == 0:
        return count_stones(1, blinks_left - 1)
    
    num_str = str(num)
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        left = int(num_str[:mid])
        right = int(num_str[mid:])
        return count_stones(left, blinks_left - 1) + count_stones(right, blinks_left - 1)
    else:
        new_num = num * 2024
        return count_stones(new_num, blinks_left - 1)

def main(file):
    with open(file) as f:
        lines = f.readlines()
    
    blinks_max = 75 
    stone_counts = {}
    
    for line in lines:
        text = line.strip()
        if not text:
            continue
        nums = list(map(int, text.split()))
        for num in nums:
            stone_counts[num] = stone_counts.get(num, 0) + 1
    
    total_stones = 0
    for num, count in stone_counts.items():
        total_stones += count * count_stones(num, blinks_max)
    
    printc(total_stones)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)