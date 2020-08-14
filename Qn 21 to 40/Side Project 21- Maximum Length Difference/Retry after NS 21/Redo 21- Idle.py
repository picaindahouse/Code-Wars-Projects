def mxdiflg(a1, a2):
    return -1 if not a1 or not a2 else max([max([len(x) for x in a1]) - min([len(x) for x in a2]), max([len(x) for x in a2]) - min([len(x) for x in a1])])