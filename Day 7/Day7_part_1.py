from functools import reduce
from operator import mul
from itertools import product
import re

def evaluate_left_to_right(expression):
    tokens = re.findall(r'\d+|\+|\*', expression)
    total = int(tokens[0])
    index = 1
    while index < len(tokens):
        operator = tokens[index]
        next_number = int(tokens[index + 1])
        if operator == '+':
            total += next_number
        elif operator == '*':
            total *= next_number
        index += 2
    return total

def generate_expressions(numbers):
    operators = ['+', '*']
    for ops in product(operators, repeat=len(numbers)-1):
        expr = ''.join(str(n)+op for n, op in zip(numbers, ops)) + str(numbers[-1])
        yield expr

def is_valid(test_value, numbers):
    nums = list(map(int, numbers.split(" ")))
    if sum(nums) == test_value:
        return True
    if reduce(mul, nums) == test_value:
        return True
    for expr in generate_expressions(nums):
        calculated = evaluate_left_to_right(str(expr))
        if calculated == test_value:
            return True
    return False

def main(file):
    sum = 0
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip().split(":")
        text[1] = text[1].strip()
        line_valid = is_valid(int(text[0]), text[1])

        if line_valid:
            sum+=int(text[0])
    print(sum)


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)