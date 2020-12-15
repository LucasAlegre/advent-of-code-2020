def run(numbers, iter):
    spoken = {n: i+1 for i, n in enumerate(numbers)}
    number = 0
    for t in range(len(numbers)+1, iter):
        last_number = number
        if number not in spoken.keys():
            number = 0
        else:
            number = t - spoken[number]
        spoken[last_number] = t
    print(number)

with open('inputs/day15.txt') as f:
    numbers = [int(x) for x in f.read().split(',')]

run(numbers, 2020)
run(numbers, 30000000)