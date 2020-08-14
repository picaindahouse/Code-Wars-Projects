# With the use of // :
import math
def nth_catalan_number(n):
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    
# If not:
import math
tom = []
def nth_catalan_number(n):
    global tom
    if n <= 1:
        return 1
    elif n in [x[0] for x in tom]:
        return [x[1] for x in tom if x[0] == n][0]
    else:
        b = 0
        for x in range(n):
            b += nth_catalan_number(x) * nth_catalan_number(n-x-1)
        tom.append([n,b])
        return b
