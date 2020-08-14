def valid(tom):
    tim = []
    for x in range(len(tom)):
        if not tim: tim.append(sorted(''.join(tom[x])))
        elif sorted(''.join(tom[x])) != tim[0]: return False
    pls = dict(zip(tim[0], [[] for x in range(len(tim[0]))]))
    for x in tom: 
        for y in x:
            for z in y:
                for w in y:
                    if w != z:
                        if w not in pls[z]: pls[z].append(w)
                        else: return False
    return True