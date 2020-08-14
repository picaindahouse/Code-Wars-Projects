def eureka (n):
    return sum([int(x) ** i for i,x in enumerate(str(n),1)])
def sum_dig_pow(a, b):
    return [x for x in range(a, b + 1) if x ==  eureka(x)]