from math import factorial
def almost_everywhere_zero(n, k):
    if k == 1: return int(str(n)[0]) + 9 * (len(str(n)) - 1)
    if len(str(n)) == k: base = 0
    else: base = 9 ** k * factorial(len(str(n))-1) // (factorial(k) * factorial(len(str(n))-k-1))
    if int(str(n)[0]) > 1: additional = (int(str(n)[0])-1) * 9**(k-1) *  factorial(len(str(n))-1) // (factorial(k-1) * factorial(len(str(n))-(k-1)-1))
    else: additional = 0
    tom = 0
    for i,x in enumerate(str(n)):
        if i == 0 or tom == 0 and x == '0': pass
        elif tom == 0 and x != '0': tom = int(str(n)[i:])
    if tom == 0 or len(str(tom)) < k-1 : peak = 0
    else:  peak = 1 * almost_everywhere_zero(tom, k-1)
    return base + additional + peak