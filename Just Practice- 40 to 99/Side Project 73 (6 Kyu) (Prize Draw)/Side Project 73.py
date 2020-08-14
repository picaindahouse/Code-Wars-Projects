def som (name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return sum([i for x in name.lower() for i,y in enumerate(alphabet,1) if x == y]) + len(name)
def rank (names, weight, n):
    if not names: return 'No participants'
    elif n > len(names.split(',')): return 'Not enough participants'
    return sorted(sorted([[x * y,z] for i,x in enumerate([som(x) for x in names.split(',')]) for r,y in enumerate(weight) for h,z in enumerate(names.split(',')) if i == r == h]),reverse=True, key= lambda t: t[0])[n-1][1]