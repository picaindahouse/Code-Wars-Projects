CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def convert_10 (number, base):
    sam,tim = [x for x in number],0
    for i,x in enumerate(reversed(sam)): tim += CHARS.index(x)* (base**i)
    return tim

def is_polydivisible(n, b):
    tom = []
    for i,x in enumerate(n,1):
        tom.append(x)
        tim = ''.join(tom)
        if convert_10(tim,b) % i == 0: pass
        else: return False
    return True

def get_polydivisible(n, b):
    yo, cool, tom = ['0'], 0, [0]
    while len(yo) < n:
        cool += 1
        tom[0] = cool
        if cool > b-1:
            cool = 0
            for y in range(len(tom)):
                if tom[y] > b-1:
                    tom[y] = 0
                    if len(tom) == y + 1:  tom.append(1)
                    else: tom[y + 1] = tom[y+1]+1
        z = ''.join([CHARS[e] for e in reversed(tom)])
        if is_polydivisible(z, b):  yo.append(z)
    return yo[-1]