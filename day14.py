import re
from itertools import product

def part1(mem, mask, value, address):
    for i, b in enumerate(reversed(mask)):
        if b == "1":
            value = value | (2 ** i)
        elif b == "0":
            value = (value | (2 ** i)) - 2 ** i
    mem[address] = value

def part2(mem, mask, value, address):
    address = str(bin(address))[2:]
    address = "".join(["0" * (36 - len(address))]) + address
    new_address = ""
    for i in range(len(address)):
        if mask[i] == "1":
            new_address += "1"
        elif mask[i] == "0":
            new_address += address[i]
        elif mask[i] == "X":
            new_address += "{}"
    num_floating = mask.count("X")
    for p in product(["0", "1"], repeat=num_floating):
        a = int(new_address.format(*p), 2)
        mem[a] = value

def run(code, func):
    mem = dict()
    mem_regex = re.compile(r"mem\[(\d+)\] = (\d+)")
    for inst in code:
        if inst[:4] == "mask":
            mask = inst[7:]
        else:
            address, value = mem_regex.match(inst).groups()
            address, value = int(address), int(value)
            func(mem, mask, value, address)
    print(sum(x for x in mem.values()))

with open("inputs/day14.txt") as f:
    code = [line.strip() for line in f.readlines()]

run(code, func=part1)
run(code, func=part2)
