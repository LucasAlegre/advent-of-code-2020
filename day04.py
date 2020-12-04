import re

def read_passports(filename='inputs/day04.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    passports = []
    p = {}
    for line in lines:
        if line == '':
            passports.append(p)
            p = {}
        else:
            for item in line.split(' '):
                key, value = tuple(item.split(':'))
                p.update({key: value})
    passports.append(p)
    return passports

def has_required_fields(passport):
    required_fieds = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return required_fieds.issubset(passport.keys())

def valid_fields(passport):
    for key, value in passport.items():
        if key == 'byr':
            if not (int(value) >= 1920 and int(value) <= 2002):
                return False
        elif key == 'iyr':
            if not (int(value) >= 2010 and int(value) <= 2020):
                return False
        elif key == 'eyr':
            if not (int(value) >= 2020 and int(value) <= 2030):
                return False
        elif key == 'hgt':
            num, unit = value[:-2], value[-2:]
            if unit == 'cm':
                if not (int(num) >= 150 and int(num) <= 193):
                    return False
            elif unit == 'in':
                if not (int(num) >= 59 and int(num) <= 76):
                    return False
            else:
                return False
        elif key == 'hcl':
            if not re.match(r'^#([\da-f]){6}$', value):
                return False
        elif key == 'ecl':
            if value not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                return False
        elif key == 'pid':
            if not re.match(r'^[0-9]{9}$', value):
                return False
    return True

def part1(passports):
    return sum([has_required_fields(p) for p in passports])

def part2(passports):
    return sum([has_required_fields(p) and valid_fields(p) for p in passports])

passports = read_passports()
print(part1(passports))
print(part2(passports))