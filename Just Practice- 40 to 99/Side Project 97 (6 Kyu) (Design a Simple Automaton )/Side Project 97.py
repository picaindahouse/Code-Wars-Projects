class Automaton(object):
    def __init__(self):
        self.states = []
    def read_commands(self, commands):
        tom = 1
        for x in commands:
            if tom == 1: tom += 1 if int(x) == 1 else 0
            elif tom == 2: tom += 1 if int(x) == 0 else 0
            else: tom -= 1
        return tom == 2