def get_adapters(filename='inputs/day10.txt'):
    with open(filename) as f:
        adapters = sorted([int(line.strip()) for line in f.readlines()])
    adapters.insert(0, 0)
    adapters.append(adapters[-1]+3)
    return adapters

def part1(adapters):
    one_joint, three_joint = 0, 0 
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:
            one_joint += 1
        elif adapters[i+1] - adapters[i] == 3:
            three_joint += 1
    return one_joint * three_joint

def count_ways(adapters, count, i):
    if i == len(adapters) - 1:
        return 1
    if count[i] != 0:
        return count[i]
    for j in range(i+1, i+4):
        if j < len(adapters) and adapters[j] - adapters[i] <= 3:
            count[i] += count_ways(adapters, count, j)
    return count[i]

def part2(adapters):
    count = [0 for _ in range(len(adapters))]
    return count_ways(adapters, count, 0)

adapters = get_adapters()
print(part1(adapters))
print(part2(adapters))