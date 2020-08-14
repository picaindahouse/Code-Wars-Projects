false = lambda t: lambda f: f
true  = lambda t: lambda f: t
a= lambda t: lambda f: f
d= lambda t: lambda f: f
n = lambda t: lambda f: t if t == d else lambda g: g
o = lambda t: t if t != false else lambda f: lambda g: f
t = lambda t: lambda f: t 
r = lambda t: t