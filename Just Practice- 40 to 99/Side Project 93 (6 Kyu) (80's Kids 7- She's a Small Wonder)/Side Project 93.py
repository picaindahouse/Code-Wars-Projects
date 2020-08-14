class Robot:
    def __init__(self):
        tom = []
        [tom.append(x)  for x in 'Thank you for teaching me I already know the word i do not understand the input'.lower().split()]
        self.tom = tom
        pass
    def learn_word(self, word):
        if not word or len([x for x in word if x.lower() in 'abcdefghijklmnopqrstuvwxyz']) < len(word):  return 'I do not understand the input'
        elif word.lower() not in self.tom: 
            self.tom.append(word.lower())
            return 'Thank you for teaching me {}'.format(word)
        else: return 'I already know the word {}'.format(word)