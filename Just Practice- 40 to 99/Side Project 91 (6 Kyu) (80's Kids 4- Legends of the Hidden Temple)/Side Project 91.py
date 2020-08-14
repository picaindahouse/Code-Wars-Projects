def row (n, r):
    if r == int(n/2) + 1: return ' ' * (n-1) + 'X\n'
    else:
        if r > int(n/2) + 1:  r = abs(r - n -1)
        return (' ' * ((r-1)*2)) + 'X' + (' ' * (n*2 - 2 -1 - (r-1)*2*2)) + 'X\n'
def mark_spot(n):
    if type(n) != int or n<0 or n %2 == 0: return '?'
    return ''.join([row(n,x) for x in range(1, n+1)])