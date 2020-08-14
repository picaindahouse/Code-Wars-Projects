# With inheritance:
class remember(dict):
    def __init__ (self, function):
        self.function = function
        self.plum = {}
    def __call__(self, *args):
        if len(args) == 1: args = [x for x in args][0]
        if (args) in list(self.plum.keys()): return self.plum[(args)]
        self.plum[(args)] = self.function(*args) if type(args) != int else self.function(args)
        super().__init__(self.plum)
        return self.plum[(args)]
    def __getitem__ (self, n):
        if len(str(n)) == 1: return self.plum[n]
        return self.plum[(n)]

# Without inheritance:
class remember:
    def __init__ (self, function):
        self.function = function
        self.plum = {}
    def __call__(self, *args):
        if len(args) == 1: args = [x for x in args][0]
        if (args) in list(self.plum.keys()): return self.plum[(args)]
        self.plum[(args)] = self.function(*args) if type(args) != int else self.function(args)
        return self.plum[(args)]
    def __getitem__ (self, n):
        if len(str(n)) == 1: return self.plum[n]
        return self.plum[(n)]
    def __iter__ (self):
        self.n = -1
        return self 
    def __next__ (self):
        self.n += 1
        if self.n > len(self.plum) -1: raise StopIteration
        return list(self.plum.keys())[self.n]
        
# The class being decorated:
@remember
class B(object):
    def __init__(self, x=1, y=2):
        self.x, self.y = x, y
    def f(self):
        return self.x, self.y