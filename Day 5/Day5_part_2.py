from collections import defaultdict, deque

def check_is_valid(update, dict):
        for i in range(len(update)):
            current_element = update[i]
            if dict.get(current_element) is None:
                if i != len(update) - 1:
                    return False
                else: 
                    continue
            before = dict[current_element]
            behind = update[:i]

            for num in behind:
                if num in before:
                    return False
                else:
                    continue
        return True                    

 
def solve(update, constraints):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    unique_elements = set(update)

    for elem in unique_elements:
        in_degree[elem] = 0

    for elem in unique_elements:
        forbidden_elements = constraints.get(elem, [])
        for forbidden in forbidden_elements:
            if forbidden in unique_elements:
                graph[elem].append(forbidden)
                in_degree[forbidden] += 1

    queue = deque([elem for elem in unique_elements if in_degree[elem] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == len(unique_elements):
        return result
    else:
        return [] 

def main(file):
    dict = {}
    all_elements = []

    updates = []
    ended_section1 = False
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip().split("\n")
        if text == ['']:
            ended_section1 = True
        if not ended_section1:
            before, after = list(map(int, text[0].split("|")))
            all_elements.append(before)
            all_elements.append(after)
            if before not in dict:
                dict[before] = [after]
            else:
                dict[before].append(after)
        elif ended_section1 and text != ['']:
            update = list(map(int, text[0].split(',')))
            updates.append(update)

    sum = 0
    for update in updates:
        if not check_is_valid(update, dict):
            solved = solve(update, dict)
            mid_idx = len(solved) // 2
            to_add = solved[mid_idx]
            sum+=to_add
    print(sum)


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    input_file = "test.txt" if mode == "test" else "input.txt"
    main(input_file)