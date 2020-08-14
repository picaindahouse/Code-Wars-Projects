def indi (t):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [i for i,x in enumerate(alphabet,1) if x in t][0]
def points (w):
    return sum([indi(y) for y in w])    
def solve(s):
    tom = (''.join([' ' if x in 'aeiou' else x for x in s])).split()
    return max([points(x) for x in tom])
    
    
    
# OR:


def new_points (h):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return sum([i for i,x in enumerate(alphabet,1) for y in h if y == x])
def solve(s):
    tom = (''.join([' ' if x in 'aeiou' else x for x in s])).split()
    return max([points(x) for x in tom])