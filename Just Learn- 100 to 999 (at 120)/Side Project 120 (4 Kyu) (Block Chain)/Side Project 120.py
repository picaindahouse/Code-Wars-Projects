from math import sqrt
from decimal import Decimal
def solve (n):
    for x in range(1,1000000000000):
        base = 1 if x == 1 else top + x
        top = 9 if x == 1 else x * (int(x * '9') - int('1' + ('0' * (x-1)))) + 1 + top + x -1
        tim = int((((top - base)/x + 1) * (top + base))/2)
        if n-tim == 0: return 9
        elif n - tim < 0: break
        n -= tim
    yo = x * base - base ** 2 - 2 * x * n
    a,b,c = 1,x,yo
    u = int((-b + sqrt(b**2 - 4*a*c))//(2*a))
    while (u-base)%x != 0: u-=1
    z = n - int((((Decimal((u - base )/x)+1) * (u+base))/2))
    if z == 0: z = u
    h = 1
    while h!=0:
        b,t = int('1' + '0' * (h-1)), int('9' * h)
        if z - h*(t-b+1) >0: z -= h*(t-b+1)
        else: break
        h += 1
    e = -1
    while z%h != 0:
        z += 1
        e -= 1
    z = z/h - 1 + int('1'+ '0' * (h-1))
    return (int(str(int(z))[e]))