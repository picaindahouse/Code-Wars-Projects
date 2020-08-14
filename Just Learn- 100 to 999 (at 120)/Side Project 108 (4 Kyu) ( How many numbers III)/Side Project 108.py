from itertools import combinations_with_replacement
def find_all(sum_dig, digs):
    tom = [x for x in combinations_with_replacement(range(1,10),digs) if sum(x) == sum_dig]
    sim = [int(''.join([str(z) for z in sorted(y)])) for y in tom]
    return [len(sim), min(sim),max(sim)] if sim else []