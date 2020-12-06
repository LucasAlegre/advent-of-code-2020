def read_groups(filename='inputs/day06.txt'):
    with open(filename) as f:
        groups = f.read().split('\n\n')
    groups = [g.split('\n') for g in groups]
    return groups

def count_questions_anyone(group):
    questions = set()
    for person in group:
        for q in person:
            questions.add(q)
    return len(questions)

def count_questions_everyone(group):
    questions = set(group[0])
    for person in group[1:]:
        person_questions = set(person)
        questions.intersection_update(person_questions)
    return len(questions)

def part1(groups):
    return sum(map(count_questions_anyone, groups))

def part2(groups):
    return sum(map(count_questions_everyone, groups))

groups = read_groups()
print(part1(groups))
print(part2(groups))