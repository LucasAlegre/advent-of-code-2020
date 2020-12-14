from functools import reduce

def read_input(filename="inputs/day13.txt"):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    depart = int(lines[0])
    bus_ids = [x for x in lines[1].split(",")]
    return depart, bus_ids

def bus_first_depart(bus, depart):
    time = (depart // bus) * bus + bus
    return time

def part1(depart, bus_ids):
    bus_ids = [int(x) for x in bus_ids if x.isnumeric()]
    timestamps = [bus_first_depart(bus, depart) for bus in bus_ids]
    min_time = min(timestamps)
    first_bus = bus_ids[timestamps.index(min_time)]
    return first_bus * (min_time - depart)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def part2(bus_ids):
    n = [int(x) for x in bus_ids if x.isnumeric()]
    a = [int(bus)*10 - i for i, bus in enumerate(bus_ids) if bus.isnumeric()]
    return chinese_remainder(n, a)

depart, bus_ids = read_input()
print(part1(depart, bus_ids))
print(part2(bus_ids))
