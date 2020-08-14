from itertools import permutations
def next_bigger(r):
    if r == int(''.join(sorted(str(r),reverse = True))): return -1
    w = 2
    for x in range(len(str(r))-1):
        n = str(r)[-w:]
        w += 1
        tim, tom = [], list(permutations([x for x in n]))
        [tim.append(int(''.join(x))) for x in tom if int(''.join(x)) not in tim]
        blum = sorted(tim)
        try: 
            digit = str(r)[:-w+1] + str(blum[blum.index(int(n)) + 1])
            return int(digit)
        except IndexError: pass