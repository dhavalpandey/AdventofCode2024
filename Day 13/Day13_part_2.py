import sys
import pyperclip as pc
sys.setrecursionlimit(10**6)
infinity = float("inf")

original_print = print
def printc(*args, **kwargs):
    output = ' '.join(str(arg) for arg in args)
    original_print(output, **kwargs)
    pc.copy(output)
print = printc

def greedy(a, b, prize):
    # a cost = 3, b cost = 1 - optimise cost
    # (ax)K + (bx)M = targetX
    # (ay)K + (by)M = targetY

    # K = (targetX - (bx)M) / ax
    # ((targetX - (bx)M) / ax)ay + (by)M = targetY
    target = prize.split(",")
    targetX = int(target[0][2:]) + 10000000000000
    targetY = int(target[1][2:]) + 10000000000000

    ax = int(a.split(",")[0][2:])
    ay = int(a.split(",")[1][2:])
    bx = int(b.split(",")[0][2:])
    by = int(b.split(",")[1][2:])

    M = (targetY*ax - targetX*ay) / (ax*by - ay*bx)
    K = (targetX - (bx*M)) / ax

    if M.is_integer() and K.is_integer():
        sum = int(3*K + M)
        return sum

def main(file):
    games = []
    dict = []
    with open(file) as f:
        temp = f.readlines()
        lines = []
        for j in range(len(temp)):
            el = temp[j]
            if el != "\n":
                lines.append(el)                
        # add 3 lines to same game
        for i in range(0, len(lines), 3):
            games.append(lines[i:i+3])

    for game in games:
        a = game[0].strip()[9:].replace(" ", "")
        b = game[1].strip()[9:].replace(" ", "")
        prize = game[2].strip()[7:].replace(" ", "")        
        dict.append((a, b, prize))

    total_cost = 0
    prizes_won = 0
    for game in dict:
        a, b, prize = game
        cost = greedy(a, b, prize)
        if cost is not None:
            total_cost += cost
            prizes_won += 1
    print(total_cost)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
