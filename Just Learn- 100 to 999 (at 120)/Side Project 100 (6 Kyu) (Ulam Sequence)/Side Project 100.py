from itertools import combinations
def ulam_sequence(u0, u1, n):
    tom = [u0,u1]
    while len(tom) != n:
        yo = [sum(x) for x in combinations(tom,2)]
        for x in sorted(yo):
            if yo.count(x) == 1 and x not in tom:
                tom.append(x)
                break
    return(tom)