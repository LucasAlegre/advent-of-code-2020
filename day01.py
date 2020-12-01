from itertools import combinations

def part1(entries):
    low, big = [], []
    for e in entries:
        if e < 1010:
            low.append(e)
        else:
            big.append(e)
        
    for b in big:
        for l in low:
            if b + l == 2020:
                return b*l

def part2(entries):
    for a, b, c in combinations(entries, 3):
        if a + b + c == 2020:
            return a * b * c

with open('inputs/day01.txt') as f:
    entries = [int(e.strip()) for e in f.readlines()]

print(part1(entries))
print(part2(entries))

