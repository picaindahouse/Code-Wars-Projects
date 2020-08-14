def fib (n):
    if n == 0 or n == 1: return n
    else: return (fib(n - 1) + fib (n - 2))
def pad(n):
    if n == 0: return 1
    elif n == 1 or n == 2: return 0
    else: return pad(n-2) + pad(n-3)
def jac (n):
    if n == 0 or n == 1: return n
    else: return jac(n-1) + 2 * (jac(n-2))
def pel (n):
    if n == 0 or n == 1: return n
    elif n > 1:  return 2 * (pel(n-1)) + pel(n-2)
def tri (n):
    if n == 0 or n == 1: return 0
    elif n == 2: return 1
    else: return tri(n-1) + tri(n-2) + tri(n-3)
def tet (n):
    if n == 0 or n == 1 or n == 2: return 0
    elif n == 3: return 1
    else:  return tet(n-1) + tet(n-2) + tet(n-3) + tet(n-4)
def mixbonacci(pattern, length):
    if not pattern: return []
    pattern, tum,tim = pattern * length, [], []
    for x in pattern:
        if len(tum) != length:
            tum.append(x + '(' + str(tim.count(x)) + ')')
            tim.append(x)
    return [eval(x) for x  in tum]
