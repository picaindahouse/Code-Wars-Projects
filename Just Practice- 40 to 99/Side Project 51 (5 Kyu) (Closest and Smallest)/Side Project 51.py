def weight (n):
    return sum([int(x) for x in str(n)])
    
def closest(strng):
    if len(strng) == 0:
        return []
    tom = [[weight(int(x)),i,int(x)] for i,x in enumerate(strng.split())]
    tum = [x[0] - y[0] for x in tom for y in tom if x[1] != y[1] and (x[0] - y[0]) >= 0]
    return min([[x,y] for x in tom for y in tom if y[0] - x[0] == min(tum) and x[1] != y[1]])