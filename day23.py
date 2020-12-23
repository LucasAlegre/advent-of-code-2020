from collections import deque

def move(cups):
    picked = []
    for _ in range(3):
        picked.append(cups[1]); del cups[1]
    select = cups[0] - 1
    while select in picked:
        select -= 1
    if select not in cups:
        select = max(cups)
    select_index = cups.index(select)
    while picked:
        cups.insert(select_index+1, picked.pop())
    cups.rotate(-1)

def part1(cups, moves=100):
    cups = deque(cups)
    for _ in range(moves):
        move(cups)

    while cups[0] != 1:
        cups.rotate(-1)
    cups.popleft()
    print(''.join(str(x) for x in cups))


def part2(cups, moves=10000000):
    max_label = len(cups)
    min_label = 1
    inp_cups = cups
    cups = [None for _ in range(len(cups)+1)]
    cups[0] = inp_cups[0]
    for cup, next_cup in zip(inp_cups, inp_cups[1:]):
        cups[cup] = next_cup
    cups[inp_cups[-1]] = cups[0]

    for _ in range(moves):
        first_removed = cups[cups[0]]
        next = first_removed
        removed = []
        for _ in range(3):
            removed.append(next)
            next = cups[next]
        cups[cups[0]] = next

        select = cups[0]
        while True:
            select -= 1
            if select < min_label:
                select = max_label
            if select not in removed:
                break
        
        cups[removed[-1]] = cups[select]
        cups[select] = first_removed
        cups[0] = cups[cups[0]]
    
    print(cups[1] * cups[cups[1]])


with open('inputs/day23.txt') as f:
    cups = [int(x) for x in f.read().strip()]

part1(cups.copy())
part2(cups + [i for i in range(10, 1000000+1)])