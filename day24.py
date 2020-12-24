def sum_coord(c1, c2):
    return tuple(map(sum,zip(c1,c2)))

def parse_line(line):
    parse = []
    coord = ''
    for c in line:
        coord += c
        if c == 'e' or c == 'w':
            parse.append(coord)
            coord = ''
    return parse

with open('inputs/day24.txt') as f:
    lines = [parse_line(line.strip()) for line in f.readlines()]

black_tiles = set()
directions = {'ne': (0,-1,1), 'e': (1,-1,0), 'se': (1,0,-1), 'sw': (0,1,-1), 'w': (-1,1,0), 'nw': (-1,0,1)}

# Part 1
for line in lines:
    coord = (0,0,0)
    for direction in line:
        coord = sum_coord(coord, directions[direction])
    if coord in black_tiles:
        black_tiles.remove(coord)
    else:
        black_tiles.add(coord)
print(len(black_tiles))

# Part 2
for _ in range(100):
    white_tiles = dict()
    flip_to_white = []
    for black_tile in black_tiles:
        count = 0
        for dir in directions.values():
            coord = sum_coord(black_tile, dir)
            if coord in black_tiles:
                count += 1
            else:
                white_tiles[coord] = white_tiles.get(coord, 0) + 1
        if count == 0 or count > 2:
            flip_to_white.append(black_tile)
    for white_tile, count in white_tiles.items():
        if count == 2:
            black_tiles.add(white_tile)
    for tile in flip_to_white:
        black_tiles.remove(tile)
print(len(black_tiles))