def nico(key, message):
    n_key = [str(i) for y in key for i,x in enumerate(sorted(key),1) if x == y]
    tom = [(i%len(key),x) if i%len(key) > 0 else (len(key),x) for i,x in enumerate(message,1)]
    tim, why = [[x] for x in n_key], []
    for x in tom:
        tim[x[0]-1].append(x[1])         
    top = max([len(x) for x in tim])
    [x.append(' ') for x in tim if len(x) < top]
    for x in [[y for y in enumerate(x) if y[0]!=0] for x in sorted(tim, key = lambda t: int(t[0]))]:
        for i,y in x:
            if len(why) < i:
                why.append(y)
            else:
                why[i-1] = why[i-1] + y
    return ''.join(why)