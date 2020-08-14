def dig_pow(n, p):
    tom = (sum([int(x) ** i for i,x in enumerate(str(n),p)]))/n
    return int(tom) if tom%1 == 0 else -1