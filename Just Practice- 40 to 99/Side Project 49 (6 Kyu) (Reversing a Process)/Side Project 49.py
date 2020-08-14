# To reverse:
def revr (y,tom):
    Help = [x for x in range(26) if (tom * x - y)%26 == 0] 
    if len(Help) > 1:
        return '_'
    else:
        return [x for x in range(26) if (tom * x - y)%26 == 0][0] if [x for x in range(26) if (tom * x - y)%26 == 0] else '_'
    
def decode(r):
    tom = int(''.join([x for x in r if x.isdigit()]))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    tim = ''.join([x for x in r if not x.isdigit()])
    cool = [revr(i,tom) for y in tim for i,x in enumerate(alphabet) if x == y]
    return ''.join([y for x in cool for i,y in enumerate(alphabet)  if i == x]) if cool.count('_') == 0 else 'Impossible to decode'

# The reverse of the reverse (Basically the original)
def code (text, number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    tom = [(i * number)%26 for x in text for i,y in enumerate(alphabet) if x == y]
    return str(number) + ''.join([y for x in tom for i,y in enumerate(alphabet) if i ==x])