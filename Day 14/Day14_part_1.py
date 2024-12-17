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

WIDTH = 101
HEIGHT = 103

def calc_path(pos, v):
    # return cord index 0 is i of grid (y axis)
    # return cord index 1 is j of grid (x axis)
    x, y = pos
    for i in range(100):
        new_x = x + v[0]
        new_y = y + v[1]

        if new_x < 0:
            diff = abs(new_x)
            new_x = WIDTH - diff
        elif new_x >= WIDTH:
            diff = new_x - WIDTH
            new_x = diff
        else:
            new_x = new_x
        
        if new_y < 0:
            diffy = abs(new_y)
            new_y = HEIGHT - diffy
        elif new_y >= HEIGHT:
            diffy = new_y - HEIGHT
            new_y = diffy
        else:
            new_y = new_y

        x, y = new_x, new_y
    return (y, x)

def quadrant_generator():
    tl_max =  ((HEIGHT-1)//2)-1, ((WIDTH-1)//2)-1
    tl_min = 0,0

    tr_max = ((HEIGHT-1)//2)-1, WIDTH-1
    tr_min = 0, (WIDTH-1)//2+1

    bl_max = HEIGHT-1, ((WIDTH-1)//2)-1
    bl_min = ((HEIGHT-1)//2)+1, 0

    br_max = HEIGHT-1, WIDTH-1
    br_min = ((HEIGHT-1)//2)+1, ((WIDTH-1)//2)+1
    # index 0 is i of grid (y axis)
    # index 1 is j of grid (x axis)
    return (tl_min, tl_max), (tr_min, tr_max), (bl_min, bl_max), (br_min, br_max)

def main(file):
    cords = []
    quadrant_dict = {}
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        pos, v = text.split(" ")
        pos = tuple(map(int, pos[2:].split(',')))
        v = tuple(map(int, v[2:].split(',')))
        final = calc_path(pos, v)
        cords.append(final)

    quadrants = quadrant_generator()
    for quadrant in quadrants:
        quadrant_dict[str(quadrant)] = []

    for cord in cords:
        y, x = cord
        for quadrant in quadrants:
            x_min, x_max = quadrant[0][1], quadrant[1][1]
            y_min, y_max = quadrant[0][0], quadrant[1][0]
            if x_min <= x <= x_max and y_min <= y <= y_max:
                quadrant_dict[str(quadrant)].append(cord)
                break
            else:
                continue    
    multiple = 1
    for region in quadrant_dict:
        multiple *= len(quadrant_dict[region])
    print(multiple)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    ans = main(input_file)
