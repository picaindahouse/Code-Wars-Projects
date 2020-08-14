def first_n_smallest(tam, n):
    tom = sorted(tam)[:n]
    return [tom.pop(tom.index(x)) for x in tam if x in tom] 