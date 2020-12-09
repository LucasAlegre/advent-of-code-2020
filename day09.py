from itertools import combinations

def set_pair_sums(numbers):
    return set([a+b for a,b in combinations(numbers,2) if a!=b])

def part1(numbers):
    for i in range(25, len(numbers)):
        if numbers[i] not in set_pair_sums(numbers[i-25:i]):
            return numbers[i]

def part2(numbers, invalid):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if sum(numbers[i:j]) == invalid:
                return min(numbers[i:j]) + max(numbers[i:j])

with open('inputs/day09.txt') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

# Part 1
invalid = part1(numbers)
print(invalid)

# Part 2
print(part2(numbers, invalid))
