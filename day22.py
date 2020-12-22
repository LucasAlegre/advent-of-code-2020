def read_decks(filename='inputs/day22.txt'):
    with open(filename) as f:
        deck1, deck2 = f.read().split('\n\n')
    deck1 = [int(x) for x in deck1.split('\n')[1:]]
    deck2 = [int(x) for x in deck2.split('\n')[1:]]
    return deck1, deck2

def score(deck):
    return sum((i+1)*x for i,x in enumerate(reversed(deck)))

def play_part1(deck1, deck2):
    while len(deck1) != 0 and len(deck2) != 0:
        c1, c2 = deck1.pop(0), deck2.pop(0)
        if c1 > c2:
            deck1.extend([c1, c2])
        else:
            deck2.extend([c2, c1])
    if len(deck1) != 0:
        return score(deck1)
    else:
        return score(deck2)

def decks_config(deck1, deck2):
    return (tuple(deck1), tuple(deck2))

def game(deck1, deck2, win_cofigs):
    game_config = decks_config(deck1, deck2)
    if game_config in win_cofigs:
        return win_cofigs[game_config]
    
    seen_rounds = set()
    while len(deck1) != 0 and len(deck2) != 0:
        config = decks_config(deck1, deck2)
        if config in seen_rounds:
            win_cofigs[config] = (1, score(deck1))
            return win_cofigs[config]
        else:
            seen_rounds.add(config)

        c1, c2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= c1 and len(deck2) >= c2:
            winner, win_score = game(deck1[:c1], deck2[:c2], win_cofigs)
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            deck1.extend([c1, c2])
        else:
            deck2.extend([c2, c1])

    if len(deck1) != 0:
        win_cofigs[game_config] = (1, score(deck1))
    else:
        win_cofigs[game_config] = (2, score(deck2))
    return win_cofigs[game_config]

def play_part2(deck1, deck2):
    win_configs = dict()
    winner, win_score = game(deck1, deck2, win_configs)
    return win_score

deck1, deck2 = read_decks()
win_score = play_part1(deck1.copy(), deck2.copy())
print(win_score)

win_score = play_part2(deck1.copy(), deck2.copy())
print(win_score)