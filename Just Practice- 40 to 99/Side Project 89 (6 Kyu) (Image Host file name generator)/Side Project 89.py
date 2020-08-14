import random
def generateName():
    alphabet,tom = 'abcdefghijklmnopqrstuvwxyz', []
    [tom.append(random.choice(alphabet)) for x in range(6)]
    name = ''.join(tom)
    return name