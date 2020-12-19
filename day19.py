class State(object):
    def __init__(self, label, rules, dot_idx, start_idx, end_idx, idx, made_from, producer):
        self.label = label
        self.rules = rules
        self.dot_idx = dot_idx
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.idx = idx
        self.made_from = made_from
        self.producer = producer

    def next(self):
        """Returns the tag after the dot"""
        return self.rules[self.dot_idx]

    def complete(self):
        return len(self.rules) == self.dot_idx

    def __eq__(self, other):
        return (self.label == other.label and
                self.rules == other.rules and
                self.dot_idx == other.dot_idx and
                self.start_idx == other.start_idx and
                self.end_idx == other.end_idx)

    def __str__(self):
        rule_string = ''
        for i, rule in enumerate(self.rules):
            if i == self.dot_idx:
                rule_string += '\\bullet '
            rule_string += rule + ' '
        if self.dot_idx == len(self.rules):
            rule_string += '\\bullet'
        return 'S%d %s -> %s [%d, %d] %s %s' % (self.idx, self.label, rule_string, self.start_idx, self.end_idx, self.made_from, self.producer)

class Earley:
    def __init__(self, words, grammar, terminals):
        self.chart = [[] for _ in range(len(words) + 1)]
        self.current_id = 0
        self.words = words
        self.grammar = grammar
        self.terminals = terminals

    def get_new_id(self):
        self.current_id += 1
        return self.current_id - 1

    def is_terminal(self, tag):
        return tag in self.terminals

    def is_complete(self, state):
        return len(state.rules) == state.dot_idx

    def enqueue(self, state, chart_entry):
        if state not in self.chart[chart_entry]:
            self.chart[chart_entry].append(state)
        else:
            self.current_id -= 1

    def predictor(self, state):
        for production in self.grammar[state.next()]:
            self.enqueue(State(state.next(), production, 0, state.end_idx, state.end_idx, self.get_new_id(), [], 'predictor'), state.end_idx)

    def scanner(self, state):
        if self.words[state.end_idx] in self.grammar[state.next()]:
            self.enqueue(State(state.next(), [self.words[state.end_idx]], 1, state.end_idx, state.end_idx + 1, self.get_new_id(), [], 'scanner'), state.end_idx + 1)

    def completer(self, state):
        for s in self.chart[state.start_idx]:
            if not s.complete() and s.next() == state.label and s.end_idx == state.start_idx and s.label != 'gamma':
                self.enqueue(State(s.label, s.rules, s.dot_idx + 1, s.start_idx, state.end_idx, self.get_new_id(), s.made_from + [state.idx], 'completer'), state.end_idx)

    def parse(self):
        self.enqueue(State('gamma', ['0'], 0, 0, 0, self.get_new_id(), [], 'dummy start state'), 0)
        
        for i in range(len(self.words) + 1):
            for state in self.chart[i]:
                if not state.complete() and not self.is_terminal(state.next()):
                    self.predictor(state)
                elif i != len(self.words) and not state.complete() and self.is_terminal(state.next()):
                    self.scanner(state)
                elif state.complete():
                    self.completer(state)

        if self.chart[len(self.words)]:
            for s in self.chart[len(self.words)]:
                if s.label == '0' and s.complete():
                    return True
        return False

    def __str__(self):
        res = ''
        for i, chart in enumerate(self.chart):
            res += '\nChart[%d]\n' % i
            for state in chart:
                res += str(state) + '\n'
        return res

def build_grammar(rules):
    grammar = dict()
    terminals = []
    for line in rules.split('\n'):
        state, prod = line.split(': ')
        grammar[state] = []
        for p in prod.split(' | '):
            grammar[state].append([x for x in p.split()])
    for s, p in grammar.items():
        if p[0][0][0] == '"':
            grammar[s] = [p[0][0].replace('"','')]
            terminals.append(s)
    return grammar, terminals


with open('inputs/day19.txt') as f:
    rules, words = f.read().split('\n\n')
    words = words.split('\n')

grammar, terminals = build_grammar(rules)
print(sum(Earley([c for c in word], grammar, terminals).parse() for word in words))

grammar['8'] = [['42'], ['42', '8']]
grammar['11'] = [['42', '31'], ['42', '11', '31']]
print(sum(Earley([c for c in word], grammar, terminals).parse() for word in words))