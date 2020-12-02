import re

def part1(passwords, password_regex):
    count = 0
    for p in passwords:
        low, high, letter, password = password_regex.match(p).groups()
        low, high = int(low), int(high)
        letter_count = password.count(letter)
        if letter_count >= low and letter_count <= high:
            count += 1
    return count

def part2(passwords, password_regex):
    count = 0
    for p in passwords:
        low, high, letter, password = password_regex.match(p).groups()
        low, high = int(low)-1, int(high)-1
        if ((password[low] == letter) + (password[high] == letter)) == 1:
            count += 1
    return count

with open('inputs/day02.txt') as f:
    passwords = f.readlines()

password_regex = re.compile('(\d+)\-(\d+) ([a-z]): ([a-z]+)')

print(part1(passwords, password_regex))
print(part2(passwords, password_regex))

