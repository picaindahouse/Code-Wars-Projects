from itertools import combinations
def choose_best_sum(t, k, ls):
    return max([x for x in [sum(x) for x in combinations (ls,k)] if x <=t]) if [x for x in [sum(x) for x in combinations (ls,k)] if x <=t] else None