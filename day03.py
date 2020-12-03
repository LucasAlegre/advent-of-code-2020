import numpy as np

def count_trees(grid, slope_right, slope_down):
    width = len(grid[0])
    height = len(grid)
    pos_j = 0
    trees_count = 0
    for i in range(slope_down, height, slope_down):
        pos_j = (pos_j + slope_right) % width
        if grid[i][pos_j] == '#':
            trees_count += 1
    return trees_count

with open('inputs/day03.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

# Part 1
print(count_trees(grid, 3, 1))

# Part 2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
print(np.prod([count_trees(grid, s[0], s[1]) for s in slopes]))