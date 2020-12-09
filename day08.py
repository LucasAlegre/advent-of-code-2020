class GameBoy:
    def __init__(self, input='inputs/day08.txt'):
        with open(input) as f:
            self.code = [line.strip() for line in f.readlines()]
        self.reset()

    def reset(self):
        self.pc = 0
        self.acc = 0
    
    def run_instruction(self, instruction):
        op, arg = instruction.split(' ')
        arg = int(arg)
        if op == 'nop':
            self.pc += 1
        elif op == 'acc':
            self.acc += arg
            self.pc += 1
        elif op == 'jmp':
            self.pc += arg
    
    def is_loop(self):
        self.reset()
        run_inst = set([self.pc])
        while self.pc < len(self.code):
            self.run_instruction(self.code[self.pc])
            if self.pc in run_inst:
                return self.acc
            run_inst.add(self.pc)
        return False
    
    def find_loop_instructions(self):
        self.reset()
        run_inst = {self.pc: 1}
        while True:
            self.run_instruction(self.code[self.pc])
            if self.pc in run_inst and run_inst[self.pc] == 2:
                return [i for i in run_inst.keys() if run_inst[i] == 2]
            if self.pc not in run_inst:
                run_inst[self.pc] = 1
            else:
                run_inst[self.pc] += 1
    
    def fix_program(self):
        candidate_inst = [i for i in self.find_loop_instructions() if self.code[i][:3] != 'acc']
        self.original_code = self.code.copy()
        for i in candidate_inst:
            self.code = self.original_code.copy()
            op, arg = self.code[i].split(' ')
            if op == 'nop':
                self.code[i] = 'jmp ' + str(arg)
            elif op == 'jmp':
                self.code[i] = 'nop ' + str(arg)

            if self.is_loop() is False:
                return self.acc

gameBoy = GameBoy()
# Part 1
print(gameBoy.is_loop())
# Part 2
print(gameBoy.fix_program())