def uniq(seq): 
    tom = []
    [tom.append(x) for x in seq if not tom or x != tom[-1]]
    return tom