import numpy as np
from itertools import product

def count_adjacent_occupied(seats, i, j, directions):
    x, y = [], []
    for d in directions:
        i2, j2 = d[0]+i, d[1]+j
        if i2 >= 0 and i2 < seats.shape[0] and j2 >= 0 and j2 < seats.shape[1]:
            x.append(i2)
            y.append(j2)
    return (seats[tuple([x,y])] == '#').sum()

def count_direction_occupied(seats, i, j, directions):
    x, y = [], []
    for d in directions:
        i2, j2 = d[0]+i, d[1]+j
        while i2 >= 0 and i2 < seats.shape[0] and j2 >= 0 and j2 < seats.shape[1] and seats[i2,j2] == '.':
            i2, j2 = d[0]+i2, d[1]+j2
        if i2 >= 0 and i2 < seats.shape[0] and j2 >= 0 and j2 < seats.shape[1]:
            x.append(i2)
            y.append(j2)
    return (seats[tuple([x,y])] == '#').sum()

def round_part1(seats):
    new_seats = seats.copy()
    directions = list(product([0,1,-1], repeat=2))[1:]
    count = 0
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            num_occupied = count_adjacent_occupied(seats, i, j, directions)
            if seats[i,j] == 'L' and num_occupied == 0:
                new_seats[i,j] = '#'
                count += 1
            elif seats[i,j] == '#' and num_occupied >= 4:
                new_seats[i,j] = 'L'
                count += 1
    return new_seats, count

def round_part2(seats):
    new_seats = seats.copy()
    directions = list(product([0,1,-1], repeat=2))[1:]
    count = 0
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            num_occupied = count_direction_occupied(seats, i, j, directions)
            if seats[i,j] == 'L' and num_occupied == 0:
                new_seats[i,j] = '#'
                count += 1
            elif seats[i,j] == '#' and num_occupied >= 5:
                new_seats[i,j] = 'L'
                count += 1
    return new_seats, count

def simulate(seats, round_func):
    while True:
        seats, count = round_func(seats)
        if count == 0:
            return (seats=='#').sum()

with open('inputs/day11.txt') as f:
    seats = np.array([list(line.strip()) for line in f.readlines()])

print(simulate(seats, round_part1))
print(simulate(seats, round_part2))