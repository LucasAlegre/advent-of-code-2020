import re

class MyInt:
    def __init__(self, val):
        self._val = val
    def __truediv__(self, other):
        return MyInt(self._val + other._val)
    def __mul__(self, other):
        return MyInt(self._val * other._val)
    def __sub__(self, other):
        return MyInt(self._val * other._val)

def solve(exp, part):
    exp = re.sub(r'(\d+)', r'MyInt(\1)', exp)
    exp = re.sub(r'\+', r'/', exp)
    if part == 2:
        exp = re.sub(r'\*', r'-', exp)
    return eval(exp)._val

with open('inputs/day18.txt') as f:
    exps = [line.strip() for line in f.readlines()]

print(sum(solve(exp, part=1) for exp in exps))
print(sum(solve(exp, part=2) for exp in exps))