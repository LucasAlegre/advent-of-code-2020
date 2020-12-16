import numpy as np
import re

def read_input(filename='inputs/day16.txt'):
    with open(filename) as f:
        inp = f.read().split('\n\n')

    field_regex = re.compile(r'(.+): (\d+)\-(\d+) or (\d+)\-(\d+)')
    fields = dict()
    for line in inp[0].split('\n'):
        field, min0, max0, min1, max1 = field_regex.match(line).groups()
        fields[field] = (int(min0), int(max0), int(min1), int(max1))

    my_ticket = [int(x) for x in inp[1].split('\n')[1].split(',')]

    tickets = []
    for line in inp[2].split('\n')[1:]:
        tickets.append([int(x) for x in line.split(',')])

    return fields, my_ticket, tickets

def filter_valid(n, fields):
    for min0, max0, min1, max1 in fields.values():
        if (n >= min0 and n <= max0) or (n >= min1 and n <= max1):
            return False
    return True

def part1(fields, tickets):
    invalid = [x for ticket in tickets for x in filter(lambda x: filter_valid(x, fields), ticket)]
    return sum(invalid)

def filter_tickets(tickets, fields):
    filtered_tickets = []
    for ticket in tickets:
        if len(list(filter(lambda x: filter_valid(x, fields), ticket))) == 0:
            filtered_tickets.append(ticket)
    return filtered_tickets

def get_invalid_fields(n, fields):
    invalid_fields = []
    for field in fields.keys():
        min0, max0, min1, max1 = fields[field]
        if not ((n >= min0 and n <= max0) or (n >= min1 and n <= max1)):
            invalid_fields.append(field)
    return invalid_fields

def part2(tickets, fields, my_ticket):
    tickets = filter_tickets(tickets, fields)
    possible_pos = {i: set(field for field in fields.keys()) for i in range(len(my_ticket))}

    for ticket in tickets:
        for i, n in enumerate(ticket):
            for field in get_invalid_fields(n, fields):
                possible_pos[i].remove(field)
    field_pos = {}
    while len(field_pos) != len(fields):
        for i, f in possible_pos.items():
            if len(f) == 1:
                remove_f = f.pop()
                field_pos[remove_f] = i
                del possible_pos[i]
                break
        for f in possible_pos.values():
            f.remove(remove_f)

    return np.prod([my_ticket[i] for f, i in field_pos.items() if f.startswith('departure')])


fields, my_ticket, tickets = read_input()
print(part1(fields, tickets))
print(part2(tickets, fields, my_ticket))