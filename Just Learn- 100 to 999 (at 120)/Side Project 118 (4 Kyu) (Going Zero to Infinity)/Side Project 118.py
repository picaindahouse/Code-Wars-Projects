from math import factorial
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
def going (n):
    if n <= 50: return truncate((1/factorial(n)) * sum([factorial(x) for x in range(1,n+1)]),6)
    return truncate(sum([factorial(x) for x in range(max(1,n-6),n+1)])/factorial(n),6)