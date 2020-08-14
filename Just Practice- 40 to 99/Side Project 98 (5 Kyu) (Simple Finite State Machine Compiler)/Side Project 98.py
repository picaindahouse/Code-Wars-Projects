class FSM(object):
    def __init__(self, instructions):
        self.instruct = instructions.split('\n')
    def run_fsm(self, start, sequence):
        state = [i for i,x in enumerate(self.instruct) if start == x.split(';')[0]][0]
        tom = [self.instruct[state].split(';')[0]]
        while len(tom) != len(sequence) + 1:
            if sequence[len(tom) - 1] == 0: 
                tom.append(self.instruct[state].split(';')[1].split(',')[0].strip())
                state = [i for i,x in enumerate(self.instruct) if x.split(';')[0] == self.instruct[state].split(';')[1].split(',')[0].strip()][0]
            else: 
                tom.append(self.instruct[state].split(';')[1].split(',')[1].strip())
                state = [i for i,x in enumerate(self.instruct) if x.split(';')[0] == self.instruct[state].split(';')[1].split(',')[1].strip()][0]  
        return(tom[-1],int(self.instruct[state].split(';')[-1]),tom)