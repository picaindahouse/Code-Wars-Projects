from itertools import permutations
def gta(limit, *args): 
    tom,tim,tam = [*args],[],[]
    kyu, n = max([len(str(x)) for x in tom]), len(tom)
    for x in range(kyu):
        for y in range(n):
            try: 
                haiz = str(tom[y])[x]
                if haiz not in tam: 
                    tam.append(haiz)
                    tim.append(int(haiz))
            except IndexError: pass
    why = tim[:limit]
    return sum([sum([sum(x) for x in permutations(why,y)]) for y in range(1, limit+1)])