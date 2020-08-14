# Most Efficient:
def power_sumDigTerm(n):
    return sorted([x**y for x in range(109) for y in range(14) if sum([int(r) for r in str(x**y)]) == x and x**y > 80])

# What I had come up with first:

from itertools import combinations_with_replacement

def power (n):
    if n in [sum([int(x) for x in str(n)]) ** y for y in [3,4,5,6,7,8,9,10,13]]:
        return n
    else: return None

def power_sumDigTerm(n):
    print(n)
    if n == 1: return 81
    elif n > 35: t = 11
    elif n > 15: t = 10
    else: t = 5
    numbers= [0,1,2,3,4,5,6,7,8,9]
    tom = [sum(x) ** y for x in combinations_with_replacement(numbers,t) for y in [3,4,5,6,7,8,9,10,13]]
    return sorted([x for x in {x for x in tom} if x> 511 and power(x) == x])[n-2]