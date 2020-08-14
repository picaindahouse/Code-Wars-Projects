def josephus(tom,k):
    if not tom:
        return []
    tim, tam, n = list(enumerate(tom)) * 100, [], k - 1
    while tim and len(tam) != len(tom) - 1:
        tum = tim[n]
        tam.append(tum[1])
        [tim.remove(tim[0]) for x in list(range(n))] 
        [tim.remove(x) for x in tim if x == tum]
    tam.append(tim[0][1])
    return tam 


OR


def josephus_2 (tom, k):
    n , tam = 0, []
    while tom:
        n = (n + k - 1)%len(tom) 
        tam.append(tom.pop(n))
    return tam