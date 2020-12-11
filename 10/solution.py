from itertools import combinations
from collections import defaultdict


def findAdapters(data):
    i = 0
    plus1 = 0
    plus3 = 0
    for i in range(len(data)-1):
        if (data[i+1]-data[i]) == 1:
            plus1 += 1
        elif (data[i+1]-data[i]) == 3:
            plus3 += 1
        else:
            print(
                f"data[{i+1}]-data[{i}] = {data[i+1]}-{data[i]} = {data[i+1]-data[i]}")

    print(f"plus1 * plus3 = {plus1} * {plus3} = {plus1 * plus3}")
    return plus1 * plus3


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def createGraph_alt2(data, mindist, maxdist):
    graph = defaultdict(list)
    for i in range(len(data)-1):
        for j in range(i+mindist, min([i+maxdist, len(data)])):
            if data[j]-data[i] <= 3:
                graph[data[i]].append(data[j])
    return graph


def createGraph_alt1(data):
    graph = defaultdict(list)
    for value in combinations(data, 2):
        #print(*value)
        if value[1]-value[0] <= 3:
            graph[value[0]].append(value[1])
    return graph


def findArrangement(data):
    #graph = createGraph_alt2(data,1,3)
    graph = dict(createGraph_alt1(data))
    print(f"graph has len {len(graph)=}")
    print(graph)
    return len(find_all_paths(graph, 0, max(data)))


def main():

    data = list(map(int, open('input', 'r').readlines()))
    data.append(max(data)+3)
    data.append(0)
    data = sorted(data)
    adapters = findAdapters(data)
    arrangements = findArrangement(data)

    return [adapters, arrangements]


if __name__ == "__main__":
    answers = main()
    print(f"Answer to question1: {answers[0]}")
    print(f"Answer to question2: {answers[1]}")
