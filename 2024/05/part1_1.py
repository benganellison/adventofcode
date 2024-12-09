from collections import defaultdict, deque

def topological_sort(pairs):
    graph = defaultdict(list)
    in_degree = {}
    nodes = set()

    # Build the graph and in-degree count
    for left, right in pairs:
        graph[left].append(right)
        if right in in_degree:
            in_degree[right] += 1
        else:
            in_degree[right] = 1
        nodes.update([left, right])

    # Find all nodes with no incoming edges
    queue = deque([node for node in nodes if node not in in_degree])
    sorted_list = []

    print(in_degree)
    print(nodes)

    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list

def collect_and_sort_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    pairs = []
    lefts = set()
    rights = set()
    for line in lines:
        if '|' in line:
            left, right = map(int, line.strip().split('|'))
            pairs.append((left, right))
            lefts.add(left)
            rights.add(right)

    print(lefts==rights)

    sorted_numbers = topological_sort(pairs)
    print(sorted_numbers)

    with open(output_file, 'w') as file:
        for number in sorted_numbers:
            file.write(f"{number},")

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'sorted_output.txt'
    collect_and_sort_numbers(input_file, output_file)
