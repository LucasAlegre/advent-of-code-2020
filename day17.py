from itertools import product

def sum_vec(v1, v2):
    return tuple(map(sum, zip(v1, v2)))

def simulate(inp, dims):
    cubes = {(x,y) + tuple(0 for _ in range(dims-2)) for x in range(len(inp)) for y in range(len(inp[0])) if inp[x][y] == '#'}
    directions = list(product([0,1,-1], repeat=dims))[1:]

    for _ in range(6):
        count_neighbour = dict()
        for cube in cubes:
            for d in directions:
                count_neighbour[sum_vec(cube, d)] = count_neighbour.get(sum_vec(cube, d), 0) + 1
        
        cubes = {cube for cube in cubes if count_neighbour.get(cube) == 2 or count_neighbour.get(cube) == 3}
        cubes = cubes.union({cube for cube, count in count_neighbour.items() if count == 3})

    print(len(cubes))


with open('inputs/day17.txt') as f:
    inp = [line.strip() for line in f.readlines()]

simulate(inp, dims=3)
simulate(inp, dims=4)