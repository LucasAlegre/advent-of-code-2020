def get_seat_id(boardpass):
    for key, value in {'B': '1', 'F': '0', 'R': '1', 'L': '0'}.items():
        boardpass = boardpass.replace(key, value)
    row, column = int(boardpass[:-3], 2), int(boardpass[-3:], 2)
    return row*8 + column

def part1(boardpasses):
    return max(get_seat_id(boardpass) for boardpass in boardpasses)

def part2(boardpasses):
    seat_ids = sorted([get_seat_id(boardpass) for boardpass in boardpasses])
    for i in range(1, len(seat_ids)-1):
        if seat_ids[i] != seat_ids[i+1]-1:
            return seat_ids[i]+1

with open('inputs/day05.txt') as f:
    boardpasses = [line.strip() for line in f.readlines()]

print(part1(boardpasses))
print(part2(boardpasses))
