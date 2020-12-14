def read_input(filename="inputs/day13.txt"):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    depart = int(lines[0])
    bus_ids = [x for x in lines[1].split(",")]
    return depart, bus_ids

def bus_first_depart(bus, depart):
    time = (depart // bus) * bus
    if time != 0:
        time += bus
    return time

def part1(depart, bus_ids):
    bus_ids = [int(x) for x in bus_ids if x.isnumeric()]
    timestamps = [bus_first_depart(bus, depart) for bus in bus_ids]
    min_time = min(timestamps)
    first_bus = bus_ids[timestamps.index(min_time)]
    return first_bus * (min_time - depart)

def part2(bus_ids):
    bus = [int(x) for x in bus_ids if x.isnumeric()]
    offset = [i for i in range(len(bus_ids)) if bus_ids[i].isnumeric()]
    t, step = 0, 1
    for (bus, offset) in zip(bus, offset):
        while (t + offset) % bus:
            t += step
        step *= bus
    return t

depart, bus_ids = read_input()
print(part1(depart, bus_ids))
print(part2(bus_ids))
