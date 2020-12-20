import numpy as np

def read_tiles(filename='inputs/day20.txt'):
    with open(filename) as f:
        inp = f.read().split('\n\n')
    tiles = dict()
    for tile in inp:
        tile = tile.split('\n')
        id = int(tile[0][5:9])
        tile = [[c for c in row] for row in tile[1:]]
        tile = (np.array(tile) == '#').astype(int)
        tiles[id] = tile
    return tiles

def get_rot_and_flip_variations(img):
    return [np.rot90(img, k=n) for n in range(4)] + [np.rot90(np.fliplr(img), k=n) for n in range(4)]

def top_row(img):
    return img[0,:]
def left_column(img):
    return img[:,0]
def right_column(img):
    return img[:,-1]
def bottom_row(img):
    return img[-1,:]

def to_int(v):
    return int(''.join(str(x) for x in v), 2)

def get_border_tiles(tiles, borders, count_appearances):
    matches = dict()
    for id, b in borders.items():
        matches[id] = [count_appearances[x] for x in b]
    return [id for id in tiles.keys() if matches[id].count(1) == 4]

def build_image(tiles, borders, first_tile, count_appearances):
    len_side = int(np.sqrt(len(tiles)))
    pos = np.zeros((len_side, len_side), dtype=int)
    pos[0,0] = first_tile
    for variation in get_rot_and_flip_variations(tiles[first_tile]):
        if count_appearances[to_int(top_row(variation))] == 1 and count_appearances[to_int(left_column(variation))] == 1:
            tiles[first_tile] = variation

    tiles_to_put = [id for id in tiles.keys() if id != first_tile]
    for i in range(len_side):
        for j in range(len_side):
            if i == 0 and j == 0:
                continue
            elif j == 0:
                match_tile = tiles[pos[i-1, j]]
                match_border = to_int(bottom_row(match_tile))
            else:
                match_tile = tiles[pos[i, j-1]]
                match_border = to_int(right_column(match_tile))

            for t in tiles_to_put:
                if match_border in borders[t]:
                    tile = t
                    tiles_to_put.remove(tile)
                    pos[i,j] = tile
                    break

            for variation in get_rot_and_flip_variations(tiles[tile]):
                if (j == 0 and (top_row(variation) == bottom_row(match_tile)).all()) or \
                   (j != 0 and (left_column(variation) == right_column(tiles[pos[i, j-1]])).all()):
                        tiles[tile] = variation
                        break
    image_rows = []
    for row in pos:
        image = tiles[row[0]][1:-1, 1:-1]
        for id in row[1:]:
            image = np.hstack((image, tiles[id][1:-1, 1:-1]))
        image_rows.append(image)
    image = np.vstack(image_rows)
    return image

def get_water_roughness(image):
    sea_monster = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
    monster_count = 0
    for i in range(image.shape[0] - sea_monster.shape[0]):
        for j in range(image.shape[1] - sea_monster.shape[1]):
            if (image[i:i+sea_monster.shape[0],j:j+sea_monster.shape[1]] * sea_monster == sea_monster).all():
                monster_count += 1
    return image.sum() - monster_count * sea_monster.sum()


tiles = read_tiles()
borders = dict()
for id, tile in tiles.items():
    borders[id] = []
    borders[id].append(to_int(top_row(tile)))
    borders[id].append(to_int(right_column(tile)))
    borders[id].append(to_int(bottom_row(tile)))
    borders[id].append(to_int(left_column(tile)))
    borders[id].append(to_int(reversed(top_row(tile))))
    borders[id].append(to_int(reversed(right_column(tile))))
    borders[id].append(to_int(reversed(bottom_row(tile))))
    borders[id].append(to_int(reversed(left_column(tile))))
count_appearances = dict()
for id, b in borders.items():
    for x in b:
        count_appearances[x] = count_appearances.get(x, 0) + 1

# Part 1
border_tiles = get_border_tiles(tiles, borders, count_appearances)
print(np.prod(border_tiles))

# Part 2
image = build_image(tiles, borders, border_tiles[0], count_appearances)
print(min(get_water_roughness(var) for var in get_rot_and_flip_variations(image)))