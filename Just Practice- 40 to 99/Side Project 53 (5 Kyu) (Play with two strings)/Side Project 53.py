# Method 1
def one_side(a,b):
    return ''.join([x if (b.lower()).count(x.lower()) % 2 == 0  else x.swapcase() for x in a])
def work_on_strings(a,b):
    return one_side(a,b) + one_side(b,a)
    
# Method 2
def swap (x, n):
    tries = 0
    while tries != n:
        x = x.swapcase()
        tries += 1
    return x

def one_side (a,b):
    tom = [i for i,x in enumerate(a) for y in b if x.lower() == y.lower()]
    tum = [(x, tom.count(x)) for x in tom]
    tam = []
    [tam.append(x) for x in tum if tam.count(x) == 0]
    why = []
    for i,x in enumerate(a):
        if x.lower() not in b.lower():
            why.append(x)
        else:
            for r,y in tam:
                if r == i:
                    why.append(swap(x,y))
    return ''.join(why)

def work_on_strings(a,b):
    return one_side(a,b) + one_side(b,a)
