import re

def build_graph_part1(filename='inputs/day07.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    bags = re.compile(r'(\d [a-z]+ [a-z]+)')
    bag = re.compile(r'^([a-z]+ [a-z]+)')
    graph = {}
    for line in lines:
        dest = bag.findall(line)[0]
        if dest not in graph:
            graph[dest] = []
        for b in bags.findall(line):
            w, source = int(b[0]), b[2:]
            if source not in graph:
                graph[source] = []
            graph[source].append(dest)
    return graph

def build_graph_part2(filename='inputs/day07.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    bags = re.compile(r'(\d [a-z]+ [a-z]+)')
    bag = re.compile(r'^([a-z]+ [a-z]+)')
    graph = {}
    for line in lines:
        source = bag.findall(line)[0]
        if source not in graph:
            graph[source] = []
        for b in bags.findall(line):
            w, dest = int(b[0]), b[2:]
            if dest not in graph:
                graph[dest] = []
            graph[source].append((w, dest))
    return graph

def count_reachable_bags(graph, source='shiny gold'):
    visited = set()
    queue = [source]
    while queue:
        node = queue.pop()
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
    return len(visited) - 1

def count_bags_inside(graph, bag_count={}, source='shiny gold'):
    c = 0
    for n in graph[source]:
        w, d = n
        if d in bag_count:
            c += w + w * bag_count[d]
        else:
            c += w + w * count_bags_inside(graph, bag_count, source=d)
    bag_count[source] = c
    return bag_count[source]

# Part 1
graph = build_graph_part1()
print(count_reachable_bags(graph))

# Part 2
graph = build_graph_part2()
print(count_bags_inside(graph))