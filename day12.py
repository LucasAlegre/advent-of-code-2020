from collections import deque
from math import radians, sin, cos

class Ship:

    def __init__(self, instructions_file='inputs/day12.txt'):
        with open(instructions_file) as f:
            self.instructions = [line.strip() for line in f.readlines()]
    
    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)
    
    @property
    def facing(self):
        return self.directions[0]
    
    def run_instruction_part1(self, instruction):
        action, value = instruction[:1], int(instruction[1:])
        if action == 'N':
            self.y += value
        elif action == 'S':
            self.y -= value
        elif action == 'E':
            self.x += value
        elif action == 'W':
            self.x -= value
        elif action == 'L':
            self.directions.rotate(value//90)
        elif action == 'R':
            self.directions.rotate(-value//90)
        elif action == 'F':
            self.x += self.facing[0] * value 
            self.y += self.facing[1] * value

    def run_instruction_part2(self, instruction):
        action, value = instruction[:1], int(instruction[1:])
        if action == 'N':
            self.wy += value
        elif action == 'S':
            self.wy -= value
        elif action == 'E':
            self.wx += value
        elif action == 'W':
            self.wx -= value
        elif action == 'L':
            s, c = int(sin(radians(value))), int(cos(radians(value)))
            self.wx, self.wy = self.wx * c - self.wy * s, self.wx * s + self.wy * c
        elif action == 'R':
            s, c = int(sin(radians(value))), int(cos(radians(value)))
            self.wx, self.wy = self.wx * c + self.wy * s, -self.wx * s + self.wy * c
        elif action == 'F':
            self.x += self.wx * value 
            self.y += self.wy * value
    
    def run(self, part=1):
        self.x, self.y = 0, 0
        self.wx, self.wy = 10, 1
        self.directions = deque([(1,0), (0,-1), (-1,0), (0,1)])
        for instruction in self.instructions:
            if part == 1:
                self.run_instruction_part1(instruction)
            elif part == 2:
                self.run_instruction_part2(instruction)
        return self.manhattan_distance

ship = Ship()
print(ship.run(part=1))
print(ship.run(part=2))