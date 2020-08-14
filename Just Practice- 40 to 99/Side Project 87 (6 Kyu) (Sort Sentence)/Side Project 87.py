def pseudo_sort(st): 
    tom, tim,tam = [], [], []
    [tom.append(x) if x[0] == x[0].upper() else tim.append(x) for x in ''.join([x for x in st if x not in '.:;?!,']).split()]
    [tam.append(x) for x in sorted(tim)], [tam.append(x) for x in sorted(tom, reverse =True)]
    return ' '.join(tam)