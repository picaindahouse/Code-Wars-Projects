def ulam_sequence(u0, u1, n):
    boom, tom, t = [0] * max(u0,u1,n) * 2, [], 0 
    boom[u0], boom[u1] = 1, 1
    for x in range(n):
        while boom[t] != 1: t += 1
        if tom and t + tom[-1] >= len(boom): boom.extend([0] * (t+tom[-1]+1 - len(boom)))
        for w in tom: boom[t + w] += 1
        tom.append(t)
        t += 1
    return tom