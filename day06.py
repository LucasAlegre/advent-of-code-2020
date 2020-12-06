def read_groups(filename='inputs/day06.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    groups = []
    group = []
    for line in lines:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)
    return groups

def count_questions_anyone(group):
    questions = set()
    for person in group:
        for q in person:
            questions.add(q)
    return len(questions)

def count_questions_everyone(group):
    questions = set(list(group[0]))
    for person in group[1:]:
        person_questions = set(list(person))
        questions.intersection_update(person_questions)
    return len(questions)

def part1(groups):
    return sum(count_questions_anyone(group) for group in groups)

def part2(groups):
    return sum(count_questions_everyone(group) for group in groups)

groups = read_groups()
print(part1(groups))
print(part2(groups))